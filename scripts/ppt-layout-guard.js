#!/usr/bin/env node
"use strict";

/*
 * Adapted for Prompt Library from PPT-Design-DNA's ppt-layout-guard.js.
 * Original work Copyright 2026 dakjdakd, licensed under Apache-2.0.
 * This modified implementation performs conservative source-level checks.
 */

const fs = require("fs");
const path = require("path");

const args = process.argv.slice(2);
const input = args.find((arg) => !arg.startsWith("--"));
const reportIndex = args.indexOf("--report");
const reportPath = reportIndex >= 0 ? args[reportIndex + 1] : null;
const jsonOnly = args.includes("--json");

if (!input || (reportIndex >= 0 && !reportPath)) {
  console.error("Usage: node scripts/ppt-layout-guard.js <deck.html> [--json] [--report <path>]");
  process.exit(2);
}

const htmlPath = path.resolve(input);
let html;
try {
  html = fs.readFileSync(htmlPath, "utf8");
} catch (error) {
  console.error(`Cannot read ${htmlPath}: ${error.message}`);
  process.exit(2);
}

const issues = [];
const add = (code, slide, message) => issues.push({ severity: "P0", code, slide, message });
const attr = (source, name) => {
  const match = source.match(new RegExp(`${name}\\s*=\\s*["']([^"']*)["']`, "i"));
  return match ? match[1] : "";
};

const slides = [];
const slidePattern = /<(section|article|div)\b([^>]*)class=["'][^"']*\bslide\b[^"']*["'][^>]*>([\s\S]*?)<\/\1>/gi;
let slideMatch;
while ((slideMatch = slidePattern.exec(html))) {
  slides.push({
    page: attr(slideMatch[2], "data-page") || String(slides.length + 1).padStart(2, "0"),
    body: slideMatch[3],
  });
}

if (!slides.length) {
  add("no_slides_detected", "global", "No section/article/div with class=slide was detected.");
}

const hasBudget = /layout_box_budget/i.test(html);
for (const slide of slides) {
  const zones = [...slide.body.matchAll(/\bdata-zone\s*=\s*["']([^"']+)["']/gi)].map((match) => match[1]);
  const textBlocks = [...slide.body.matchAll(/<(h1|h2|h3|p)\b[^>]*>[\s\S]*?<\/\1>/gi)];

  if (textBlocks.length > 1 && !zones.length) {
    add("missing_data_zones", slide.page, "A multi-text slide has no data-zone markers.");
  }
  if ((textBlocks.length > 1 || zones.length > 1) && !hasBudget) {
    add("missing_layout_box_budget", slide.page, "A multi-element slide has no layout_box_budget source contract.");
  }
  if (zones.some((zone) => /card|body|footer/i.test(zone)) && !zones.some((zone) => /nav/i.test(zone))) {
    add("missing_nav_safe_zone", slide.page, "Content reaches lower-page roles without a declared navigation-safe zone.");
  }

  for (const heading of slide.body.matchAll(/<(h1|h2|h3)\b([^>]*)>([\s\S]*?)<\/\1>/gi)) {
    const rawText = heading[3];
    const text = rawText.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
    const style = attr(heading[2], "style");
    const lineHeightMatch = style.match(/line-height\s*:\s*(\d*\.?\d+)/i);
    const lineHeight = lineHeightMatch ? Number(lineHeightMatch[1]) : null;
    const isCjk = /[\u3400-\u9fff\u3040-\u30ff\uac00-\ud7af]/.test(text);
    const explicitLines = rawText.split(/<br\s*\/?>/i).map((line) => line.replace(/<[^>]+>/g, "").trim()).filter(Boolean);

    if (lineHeight !== null && lineHeight < 0.95) {
      add("unsafe_tight_line_height", slide.page, `Display line-height ${lineHeight} is below 0.95.`);
    }
    if (isCjk && lineHeight !== null && lineHeight < 1.02) {
      add("unsafe_cjk_display_line_height", slide.page, `CJK display line-height ${lineHeight} is below 1.02.`);
    }
    if (isCjk && explicitLines.length > 1 && [...explicitLines.at(-1)].length <= 2) {
      add("cjk_orphan_line", slide.page, `Display title ends with an orphan short line: ${explicitLines.at(-1)}`);
    }
  }
}

for (const match of html.matchAll(/([^{}]+)\{([^{}]+)\}/g)) {
  const selector = match[1].trim();
  const rules = match[2];
  const displaySelector = /title|headline|display|poster|mega|huge|cjk|zh/i.test(selector);
  const lineHeight = rules.match(/line-height\s*:\s*(\d*\.?\d+)/i);
  if (displaySelector && lineHeight && Number(lineHeight[1]) < 1.02) {
    add("unsafe_display_selector_line_height", "global", `${selector} uses line-height ${lineHeight[1]}.`);
  }
  if (displaySelector && /letter-spacing\s*:\s*-/i.test(rules)) {
    add("negative_display_letter_spacing", "global", `${selector} uses negative display letter-spacing.`);
  }
  if (displaySelector && /(word-break\s*:\s*break-all|overflow-wrap\s*:\s*anywhere)/i.test(rules)) {
    add("unsafe_display_word_break", "global", `${selector} uses unsafe automatic display wrapping.`);
  }
  if (/content|card|lead|caption|label|title|body|chart/i.test(selector) && /overflow\s*:\s*hidden/i.test(rules)) {
    add("text_overflow_hidden", "global", `${selector} may conceal a text-layout failure with overflow:hidden.`);
  }
}

const report = {
  status: issues.length ? "fail" : "pass",
  file: htmlPath,
  summary: { slides: slides.length, p0: issues.length },
  issues,
  checked_rules: [
    "slide discoverability",
    "data-zone presence",
    "layout_box_budget presence",
    "navigation-safe zone declaration",
    "display and CJK line-height",
    "CJK explicit orphan lines",
    "unsafe display wrapping and tracking",
    "text overflow hiding"
  ]
};

if (reportPath) {
  const resolvedReport = path.resolve(reportPath);
  fs.mkdirSync(path.dirname(resolvedReport), { recursive: true });
  fs.writeFileSync(resolvedReport, JSON.stringify(report, null, 2), "utf8");
}

if (jsonOnly) {
  console.log(JSON.stringify(report, null, 2));
} else if (report.status === "pass") {
  console.log(`PASS ${path.basename(htmlPath)}: ${slides.length} slide(s) checked.`);
} else {
  console.log(`FAIL ${path.basename(htmlPath)}: ${issues.length} P0 issue(s).`);
  for (const item of issues.slice(0, 20)) console.log(`[P0] slide ${item.slide} ${item.code}: ${item.message}`);
  if (reportPath) console.log(`Report: ${path.resolve(reportPath)}`);
}

process.exit(report.status === "pass" ? 0 : 1);
