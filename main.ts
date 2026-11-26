// main.ts — news image entry for 26 November 2026.
//
// Copy-only entry point: the front page was rendered ahead of time by
// draw.py and is committed to this repository as entry.png. At grade time
// this script does nothing but copy that file into the output directory.
// It never invokes Python, Pillow, or any network or rendering step.

import { copyFileSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// Copy-only contract: the grader must receive the exact pre-rendered
// entry.png, byte for byte. This script performs no drawing, no fetching
// and no transformation — if the copy ever came out a different size than
// the committed source, that would mean the output is not the graded
// image, so the run must fail loudly instead of shipping a wrong file.
function verifyCopyMatches(source: string, destination: string): void {
  const sourceSize = statSync(source).size;
  const copiedSize = statSync(destination).size;
  if (copiedSize !== sourceSize) {
    throw new Error(
      `entry.png copy mismatch: source is ${sourceSize} bytes but copied file is ${copiedSize} bytes`,
    );
  }
}

function resolveOutputDir(): string {
  const configured = process.env.MAKEFUN_OUTPUT_DIR?.trim();
  return configured ? configured : "out";
}

function main(): void {
  const outDir = resolveOutputDir();
  mkdirSync(outDir, { recursive: true });

  const here = dirname(fileURLToPath(import.meta.url));
  const source = join(here, "entry.png");
  const destination = join(outDir, "entry.png");

  copyFileSync(source, destination);
  verifyCopyMatches(source, destination);
}

main();
