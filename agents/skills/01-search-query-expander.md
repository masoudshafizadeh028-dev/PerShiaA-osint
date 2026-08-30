# Search query expander

Generates alternate search terms, spelling variants, transliterations, and platform-specific query syntax for a subject.

**You need:** the subject name or topic, and the platforms or engines you intend to search.

## Prompt

```
Variables:
[subject] = the person, organisation, or topic
[platforms] = the engines or platforms to be searched (default: Google, Bing, Yandex)
[known_variants] = spellings already tried (default: none)

You are supporting an open source intelligence search. Expand the
following subject into a search query set.

Subject: [subject]
Platforms: [platforms]
Already tried: [known_variants]

Return four sections:

1. NAME AND TERM VARIANTS
   Spelling variants, common misspellings, abbreviations, initialisms,
   former names, and informal forms.

2. QUERY STRINGS
   Ten query strings using operators supported by [platforms]. Include
   exact-phrase, exclusion, and site-restricted variants. Label the
   operator syntax used in each.

3. ADJACENT ANGLES
   Five queries that approach the subject indirectly, for example
   through associated entities, filings, addresses, or events.

4. GAPS
   State what you would need in order to expand this further. Do not
   guess at missing detail.

Do not assert facts about [subject]. Produce search terms only.
```
