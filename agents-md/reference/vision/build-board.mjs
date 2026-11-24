// Builds the review board from a round file. Usage:
//   node build-board.mjs <round.json> <out-dir>
// round.json: { "project", "runNote", "draft", "cards": [{ id, title, body, tests, why }] }
// Writes <out-dir>/board.html and review.css. Rerun with the same out-dir for each round.
import { copyFileSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { Script } from "node:vm";

const [roundPath, outDir] = process.argv.slice(2);
if (!roundPath || !outDir) throw new Error("usage: node build-board.mjs <round.json> <out-dir>");

const round = JSON.parse(readFileSync(roundPath, "utf8"));
for (const key of ["project", "draft"]) {
  if (typeof round[key] !== "string") throw new Error(`round.json needs a string "${key}"`);
}
if (!Array.isArray(round.cards)) throw new Error('round.json needs a "cards" array');
for (const card of round.cards) {
  for (const key of ["id", "title", "body", "tests", "why"]) {
    if (typeof card[key] !== "string") throw new Error(`card ${card.id ?? "?"} needs a string "${key}"`);
  }
}

const assets = join(dirname(fileURLToPath(import.meta.url)), "assets");
const html = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;");
const js = (v) => JSON.stringify(v).replace(/</g, "\\u003c");

const template = readFileSync(join(assets, "review-template.html"), "utf8");
const slots = {
  PROJECT: html(round.project),
  RUN_NOTE: html(round.runNote ?? ""),
  DRAFT_JSON: js(round.draft),
  CARDS: js(round.cards),
};
const found = [...template.matchAll(/\{\{(\w+)\}\}/g)].map((m) => m[1]);
const missing = Object.keys(slots).filter((name) => !found.includes(name));
const unknown = found.filter((name) => !(name in slots));
if (missing.length || unknown.length) {
  throw new Error(`template slots are off: missing ${missing.join(", ") || "none"}, unknown ${unknown.join(", ") || "none"}`);
}
const page = template.replace(/\{\{(\w+)\}\}/g, (_, name) => slots[name]);
for (const [, body] of page.matchAll(/<script>([\s\S]*?)<\/script>/g)) new Script(body);

mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, "board.html"), page);
copyFileSync(join(assets, "review.css"), join(outDir, "review.css"));
console.log(join(outDir, "board.html"));
