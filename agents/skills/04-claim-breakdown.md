# Claim breakdown

Splits a piece of content into discrete factual claims so each one can be verified separately, rather than accepting or rejecting the piece as a whole.

**You need:** the text, and a note on whether you want implied claims included alongside stated ones.

## Prompt

```
Variables:
[text] = the content to break down
[include_implied] = whether to capture implied claims as well as
                   stated ones (default: yes)

Break the text below into discrete factual claims so each can be
verified separately.

Include implied claims: [include_implied]

TEXT:
[text]

For each claim, give:

CLAIM: the claim in one sentence, stated neutrally
TYPE: stated or implied
SOURCE IN TEXT: the sentence or passage it comes from
VERIFIABLE BY: the kind of record or source that would confirm or
               contradict it, for example a company filing, a court
               record, imagery, a named witness

Then add:

NOT A CLAIM
Passages that carry no factual assertion, for example opinion,
prediction, or rhetorical framing.

Do not assess whether any claim is true. Do not rank them by
plausibility. Separate them, describe them, and stop there.
```
