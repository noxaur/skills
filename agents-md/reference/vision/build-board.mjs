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
for (const key of ["project", "draft", "cards"]) {
  if (round[key] === undefined) throw new Error(`round.json is missing "${key}"`);
}
for (const card of round.cards) {
  for (const key of ["id", "title", "body", "tests", "why"]) {
    if (typeof card[key] !== "string") throw new Error(`card ${card.id ?? "?"} needs a string "${key}"`);
  }
}

const assets = join(dirname(fileURLToPath(import.meta.url)), "assets");
const html = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;");
const js = (v) => JSON.stringify(v).replace(/</g, "\\u003c");

const page = readFileSync(join(assets, "review-template.html"), "utf8")
  .replaceAll("{{PROJECT}}", html(round.project))
  .replaceAll("{{RUN_NOTE}}", html(round.runNote ?? ""))
  .replace("{{DRAFT_JSON}}", () => js(round.draft))
  .replace("{{CARDS}}", () => js(round.cards));

if (page.includes("{{")) throw new Error("a slot was left unfilled");
for (const [, body] of page.matchAll(/<script>([\s\S]*?)<\/script>/g)) new Script(body);

mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, "board.html"), page);
copyFileSync(join(assets, "review.css"), join(outDir, "review.css"));
console.log(join(outDir, "board.html"));
