# Framing and rhetoric breakdown

Identifies how a text is constructed to persuade: what it asserts, what it implies, what it omits, and which rhetorical devices carry the argument.

**You need:** the text. Works best with a comparison piece on the same event.

## Prompt

```
Variables:
[text] = the piece to analyse
[comparison_text] = a second piece covering the same event
                   (default: none)

Analyse how the text below is constructed. Describe the construction.
Do not judge the content.

TEXT:
[text]

COMPARISON TEXT (if supplied):
[comparison_text]

Return six sections:

1. ASSERTED
   What the text states outright.

2. IMPLIED
   What the text leads a reader towards without stating. Quote the
   wording that does the work.

3. ABSENT
   Context a reader would need that the text does not provide.

4. ATTRIBUTION
   How claims are sourced: named sources, unnamed sources, passive
   constructions that hide the actor, or no attribution at all.

5. DEVICES
   The rhetorical techniques carrying the argument, with the specific
   wording in each case.

6. DIVERGENCE
   Where the two texts differ in emphasis, sequence, or attribution.
   Only complete this section if a comparison text was supplied.

Describe what the text does. Do not state whether it is accurate or
misleading.
```
