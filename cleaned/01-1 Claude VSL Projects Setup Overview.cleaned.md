# Claude VSL Projects Setup Overview

This module covers setting up Claude projects for generating different VSL lengths. The process is straightforward and builds on the brief creation section.

## Prerequisites

Before setting up VSL projects, ensure you've completed the brief section. This is essential for effective VSL generation.

## VSL Project Types

You'll create Claude projects for four VSL length categories:

### 1. Long-Form VSLs
Traditional 15-50+ minute video sales letters

### 2. Medium-Form VSLs
6-18 minute VSLs

### 3. Three to Seven-Minute VSLs
Eight example transcripts ranging from just over 3 minutes to 7 minutes. These are almost always run as in-feed video ads on Meta.

**Note**: Adding time lengths to transcript titles (e.g., "3:30", "6:54") provides Claude with frame of reference when generating new VSLs of specific lengths.

### 4. Short VSLs
1-2 minute video ads. Short VSLs and 3-7 minute VSLs function essentially the same as video ads.

## Standard Project Instructions

Here's the instruction template for a 3-7 minute VSL project:

```
Your job is to generate video sales letters that are typically three to seven minutes long. The documents in your knowledge base include transcripts from several VSLs, which we can model while writing new VSLs.

Analyze the structure of the various VSL examples, synthesize that knowledge, and use that same knowledge along with your judgment to produce new VSLs.

Please note that most VSLs of this length run as in-feed video ads on Meta. They often do not reveal the product being sold and instead tease a new solution or breakthrough, with the call to action directing viewers to watch a video or read a report for more information. At other times, they may mention the product and how people can get a discount.

I'll typically specify the goal when asking you to write VSL scripts. When you write, I'll provide various inputs or an outline and game plan. You'll model the examples based on the information about the current VSL project.

One important note: Please don't rush or condense anything. Whenever you run out of space, prompt me and I'll tell you to continue.
```

The last instruction about not rushing is less relevant now since Claude has longer output capacity, but it's still useful to include.

## Setting Up a Claude Project

### Step-by-Step Process

1. **Create New Project**: Click "Create new project" in Claude
2. **Name the Project**: Example: "Claude 3-7 Minute VSL Generator"
3. **Add Project Description**: Copy and paste the instruction template into "What are you trying to achieve?"
4. **Add Knowledge Base**: Click the plus button to add content, or drag and drop PDF transcripts into the knowledge base area

That's the complete setup process.

## Long-Form VSL Knowledge Base Examples

The long-form VSL project includes diverse transcript examples:

- **Agora Financial**: Example from the brief training showing sophisticated financial copy
- **Beverly Hills MD Pinch Test**: Covered in VSL structure training
- **Backyard Liberty**: Classic survival letter from earlier direct response era
- **Emma Relief**: Strong example of white hat copy
- **Genius Wave**: Successful ClickBank manifestation offer
- **Mydalene**: Aggressive ClickBank weight loss offer with solid structure
- **Swipe Builder Example**: White hat copy with strong structure
- **BizOp Example**: Business opportunity VSL

### Note on ClickBank Examples

Some examples come from ClickBank, which can raise ethical questions about aggressive claims. However, the copy structure and techniques can be valuable even when the claims themselves are questionable. Key points:

- Good copywriting structure exists independently of claim accuracy
- LLMs can adapt aggressive copy to make less aggressive claims
- When given proper briefs, Claude will generate appropriate claims while maintaining structural quality
- You can always instruct Claude to tone down aggressiveness

## Synthesis vs Swipe-Specific Approach

### Evolution of the Process

**Original approach**: Swipe-specific sales letters
- Provide one winning sales letter as reference
- Supply all inputs (the brief)
- Ask Claude to rewrite the winning sales letter with new brief inputs
- Manually edit to differentiate from original
- Still works and has value

**New synthesis approach**: Composite structure generation
- Provide multiple example transcripts (8+ examples)
- Instruct Claude to "analyze structures, synthesize knowledge, and use that knowledge along with judgment"
- Creates composite copy drawing best elements from all examples
- Produces original structure rather than close swipe

### Advantages of Synthesis Approach

**Avoids proximity issues**: Copy won't be uncomfortably close to a single source

**Reduces legal concerns**: No disputes about copying specific sales letters

**Creates originality**: Combines best elements from multiple sources into new structures

**Flexibility**: Still allows swipe-specific approach when desired (e.g., adapting your own winning VSL to new category)

### When to Use Swipe-Specific Approach

- Adapting your own VSL to a different category
- You specifically want close structural matching
- You have explicit permission to model closely

## Experimentation Guidelines

Feel free to experiment with these setups (number of examples, types of transcripts, instruction variations). However, keep these points in mind:

**Incremental gains**: Most experiments yield small improvements rather than breakthroughs

**Diminishing returns**: Adding more examples beyond 8-10 may not significantly improve output

**Avoid productive procrastination**: Don't use endless tweaking as distraction from actual work

**Use proven processes first**: Test the provided setups before extensive customization

If you have time and genuine curiosity, experiment away. If you're trying to move the needle on results, use the proven processes first.

## Continuous Improvement

These processes have been refined during RMBC2 creation, with significant improvements discovered along the way (particularly with brief creation). You're receiving the most current, cutting-edge versions of these processes.

## Next Steps

After setting up your Claude projects for different VSL lengths, the next section covers actually generating copy using these projects. You'll see examples with the Unity eye serum, financial offers, blood sugar examples, and more.

Set up your projects, then move forward to copy generation.
