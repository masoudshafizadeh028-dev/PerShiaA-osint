# Query translator

Takes a query set and renders it in a target language, including local naming conventions and script variants.

**You need:** the query set, the target language, and the region if naming conventions vary within the language.

## Prompt

```
Variables:
[queries] = the query set to translate
[target_language] = the language to translate into
[region] = the country or region, where naming conventions vary
          (default: none specified)

Translate the following search queries for use in [target_language]
sources.

Queries: [queries]
Target language: [target_language]
Region: [region]

Return five sections:

1. TRANSLATED QUERIES
   Each query rendered in [target_language]. Keep search operators in
   the syntax the local engine expects.

2. NAME RENDERINGS
   Any personal or organisational names transliterated into the target
   script. Give every accepted transliteration, not one preferred form.

3. LOCAL TERMINOLOGY
   Where a direct translation would not match how the topic is
   discussed locally, give the term a native speaker would use instead.
   Note the difference.

4. FALSE FRIENDS
   Words in the translation that carry a different sense in
   [target_language] and would pull irrelevant results.

5. UNCERTAINTY
   Flag any translation you are unsure of and say why. Do not smooth
   over uncertainty.
```
