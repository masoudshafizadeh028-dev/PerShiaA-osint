# Timeline builder

Converts dated references scattered across multiple sources into a single chronological sequence, flagging gaps and conflicting dates.

**You need:** the source extracts with their origins labelled, and the time zone convention you want applied.

## Prompt

```
Variables:
[sources] = the source extracts, each labelled with its origin
[timezone] = the convention to normalise to (default: UTC)

Build a single chronology from the labelled extracts below.

Normalise all times to: [timezone]

SOURCES:
[sources]

Return three sections:

1. CHRONOLOGY
   Columns: date and time | event | source label | original wording of
   the time reference
   Order earliest to latest. Where a source gives a relative reference,
   for example "the following morning", record it as relative and say
   what it depends on.

2. CONFLICTS
   Points where sources place the same event at different times.
   Give both accounts and their source labels. Do not resolve the
   conflict.

3. GAPS AND VAGUE REFERENCES
   Periods with no coverage, and time references too imprecise to
   place, for example "recently" or "last year".

Do not convert a relative reference into an absolute time unless the
sources support the conversion. Do not add events from outside the
extracts.
```
