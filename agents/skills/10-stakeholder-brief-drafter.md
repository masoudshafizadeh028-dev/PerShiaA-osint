# Stakeholder brief drafter

Turns working notes into a short brief for a reader outside the intelligence function, stripping jargon while keeping the caveats intact.

**You need:** the notes, the audience, and the decision the brief supports.

## Prompt

```
Variables:
[notes] = the working notes or finished assessment
[audience] = who reads it (default: senior non-specialist)
[decision] = the decision the brief supports
[word_limit] = the length ceiling (default: 400 words)

Draft a brief from the notes below.

Audience: [audience]
Decision it supports: [decision]
Limit: [word_limit]

Structure:

BOTTOM LINE
The single most important point, in two sentences.

WHAT WE KNOW
The findings the sourcing supports.

WHAT WE DO NOT KNOW
The gaps, stated plainly.

WHAT THIS MEANS FOR [decision]
The implication, no more than three points.

Rules:
Remove technical vocabulary the audience would not use, and explain any
term that has to stay. Keep every caveat and confidence qualifier from
the notes intact. Do not strengthen a hedged statement. Do not add a
recommendation the notes do not contain. Do not introduce any fact
absent from the notes.
```
