import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// Copy the pre-rendered front page into the output directory.
// Nothing is drawn or fetched here: the image is built ahead of time
// by draw.py and shipped in this repository as entry.png.
const outDir = process.env.MAKEFUN_OUTPUT_DIR?.trim() || "out";
mkdirSync(outDir, { recursive: true });
const here = dirname(fileURLToPath(import.meta.url));
copyFileSync(join(here, "entry.png"), join(outDir, "entry.png"));
