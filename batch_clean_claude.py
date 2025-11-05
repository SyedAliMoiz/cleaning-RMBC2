# batch_clean_claude.py
from pathlib import Path
import time
import anthropic
client = anthropic.Anthropic()

SRC_DIR = Path("txt-files")
OUT_DIR = Path("cleaned")
MODEL = "claude-4-5-sonnet-latest"
MAX_OUTPUT_TOKENS = 8000      # ≈ 4000 words
FILES_PER_RUN = 10            # process 10 per batch

OUT_DIR.mkdir(parents=True, exist_ok=True)

def system_prompt():
    return """
Role, Transcript cleaning and refinement expert.
Goal, Convert raw transcript files into clear, readable text that keeps all factual and instructional details but removes repetition, filler, and irrelevant chatter.

Guidelines,
Each input is a transcript of RMBC II training content. Do not summarize or shorten by removing information that conveys meaning or process.
Keep every teaching point, definition, example, and detailed step.
Remove repeated phrases, side conversations, irrelevant tangents, and verbal tics.
Keep the speaker’s ideas complete and in logical order.
Maintain a professional instructional tone.
Do not add or invent content.

Formatting,
Use Markdown.
# for main topics
## for subtopics
Use full sentences and paragraphs, not outlines.

Trim only redundant or non-essential filler, not instructional material ever.
""".strip()

def clean_file(p: Path):
    text = p.read_text(encoding="utf-8", errors="ignore")
    user_prompt = f"""You are cleaning a transcript file, not summarizing it.
Keep every teaching and procedural detail but remove redundant or irrelevant parts.
Output a cleaned transcript up to about 4000 words.
Filename: {p.name}

Transcript:
{text}
"""
    resp = client.messages.create(
        model=MODEL,
        max_tokens=MAX_OUTPUT_TOKENS,
        system=system_prompt(),
        messages=[{"role": "user", "content": user_prompt}],
    )

    cleaned = resp.content[0].text
    out_path = OUT_DIR / f"{p.stem}.cleaned.md"
    out_path.write_text(cleaned, encoding="utf-8")
    print(f"Cleaned {p.name} → {out_path.name}")

def main():
    files = sorted([f for f in SRC_DIR.glob("*.txt") if f.is_file()])
    remaining = [f for f in files if not (OUT_DIR / f"{f.stem}.cleaned.md").exists()]
    batch = remaining[:FILES_PER_RUN]

    if not batch:
        print("All transcripts already cleaned.")
        return

    print(f"Processing {len(batch)} files...")
    for f in batch:
        clean_file(f)
        time.sleep(3)  # slight delay for safety
    print("Batch complete. Re-run to process next set.")

if __name__ == "__main__":
    main()


