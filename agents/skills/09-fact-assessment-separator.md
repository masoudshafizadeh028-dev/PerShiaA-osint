# Fact and assessment separator

Restructures draft notes into two sections: what the sourcing supports, and what the analyst concludes from it. The model sorts the material. It does not grade the assessment.

**You need:** your draft notes, and your confidence language convention if your team uses one.

## Prompt

```
Variables:
[notes] = the draft working notes
[confidence_language] = the team's confidence convention
                       (default: none, use plain wording)

Restructure the notes below into two separate sections. Sort the
material. Do not evaluate it.

Confidence convention: [confidence_language]

NOTES:
[notes]

Return:

SECTION 1: WHAT THE SOURCING SUPPORTS
Each item with the source it rests on and the exact wording that
supports it. Include only what a named source states.

SECTION 2: ANALYST ASSESSMENT
Each judgement, inference, or conclusion drawn from Section 1, with the
Section 1 items it depends on.

SECTION 3: UNSOURCED
Statements in the notes with no source attached and no clear basis in
Section 1. List them without comment.

Do not grade the assessments. Do not add confidence levels the notes do
not already carry. Do not move an item from Section 2 to Section 1
because it reads as certain.
```
