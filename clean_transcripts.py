# clean_transcripts.py
# This file contains plain task instructions for Claude Code to follow when executed inside Claude Code.

"""
Task for Claude Code:

You have access to the folder 'txt-files' that contains 103 RMBC II transcript files.
Your goal is to clean each transcript and write a new version in the 'cleaned' folder.

Cleaning rules:
1. Preserve all teaching content, definitions, examples, and steps.
2. Remove only redundant phrasing, irrelevant tangents, and filler language.
3. Do not summarize or shorten in a way that loses instructional meaning.
4. Maintain logical flow and professional instructional tone.
5. Write in Markdown using:
   - # for main topics
   - ## for subtopics
   - full sentences and paragraphs
6. Each cleaned transcript should be around or below 4000 words.

Processing steps:
1. Read each .txt file in the 'txt-files' directory.
2. For each one, clean the transcript according to the above rules.
3. Save the result as '<original_name>.cleaned.md' inside the 'cleaned' directory.
4. Skip any file that already has a cleaned version.
5. Process up to 10 files at a time, then stop and report which ones were completed.

Do not use any external API, SDK, or internet calls.
Use only the Claude Code environment to perform text transformation locally.
"""

print("Instructions loaded. Claude Code, please execute the above task.")
