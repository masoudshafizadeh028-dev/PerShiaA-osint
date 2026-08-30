# Entity and relationship extractor

Pulls people, organisations, locations, and the stated relationships between them out of a document into a structured list.

**You need:** the source text pasted in full, and the entity types you want captured.

## Prompt

```
Variables:
[text] = the source document
[entity_types] = types to capture (default: people, organisations,
                locations, dates, identifiers)

Extract entities and relationships from the text below. Work only from
the text. Add nothing from outside it.

Entity types: [entity_types]

TEXT:
[text]

Return two tables in plain text.

TABLE 1: ENTITIES
Columns: entity | type | how it appears in the text | first mention
Use the exact wording from the text in the third column.

TABLE 2: RELATIONSHIPS
Columns: entity A | relationship | entity B | supporting sentence
Only include relationships the text states or directly implies. Quote
the supporting sentence.

Then add:

UNRESOLVED
Names or references you could not attribute to a specific entity, for
example pronouns without a clear antecedent or partial names.

If the text does not support a relationship, leave it out rather than
inferring it.
```
