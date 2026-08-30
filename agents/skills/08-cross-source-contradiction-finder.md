# Cross-source contradiction finder

Compares two or more accounts of the same event and surfaces where they disagree on fact, sequence, or attribution.

**You need:** the accounts, clearly separated and labelled by source.

## Prompt

```
Variables:
[accounts] = two or more accounts of the same event, each labelled
[event] = the event in one line

Compare the labelled accounts below of the following event.

Event: [event]

ACCOUNTS:
[accounts]

Return five sections:

1. AGREED
   Points all accounts support.

2. CONTRADICTED
   Points where accounts directly conflict. Give each version with its
   source label and the wording it rests on.

3. UNIQUE TO ONE SOURCE
   Claims appearing in a single account only. Note which.

4. ATTRIBUTION DIFFERENCES
   Where accounts assign the same action to different actors, or where
   one names an actor and another does not.

5. SHARED SOURCING
   Signs the accounts draw on the same upstream source, for example
   identical phrasing or the same quoted figure. Repetition is not
   corroboration.

Do not decide which account is correct. Do not weight sources by
reputation.
```
