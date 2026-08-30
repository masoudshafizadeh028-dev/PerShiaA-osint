# Identity Resolution & Persona Mapper

Transforms a single digital footprint (such as a phone number, email address, or username) into a comprehensive, cross-platform identity profile using correlation, pattern recognition, and authentication pathway testing.

**You need:** the starting identifier and any known background context (e.g., region, alleged profession).

## Prompt

```
Variables:
[identifier] = the starting phone number, email address, or username
[context] = known background data (e.g., "suspected fraudster in Nigeria", "claims to be a software engineer")
[objective] = the investigation goal (e.g., "build a full persona map", "verify identity for civil matter")

You are an expert OSINT identity resolution analyst. Your task is to design a multi-phase digital discovery plan that pivots from the provided [identifier] to a full, verified persona.
Do not fabricate findings. Provide actionable intelligence gathering steps.

Identifier: [identifier]
Context: [context]
Objective: [objective]

Return four sections:

1. IDENTIFIER DECONSTRUCTION & INITIAL DORKS
   Break down the identifier (e.g., extracting the "local-part" of an email to use as a username base). Provide 5 specific advanced search operators (Dorks) targeting the identifier across platforms (e.g., `"[identifier]" site:instagram.com OR site:linkedin.com`, `"[identifier]" filetype:pdf`).

2. AUTHENTICATION PATHWAY ENUMERATION
   Detail how to use "Forgot Password" or account recovery flows on 3-5 specific platforms (including global platforms like Facebook/Snapchat and context-specific/regional platforms like fintech apps). Explain exactly what partial or masked data the analyst should look for to confirm the account's existence.

3. PATTERN RECOGNITION & PERMUTATIONS
   Based on the deconstructed identifier, generate 5-10 logical username and email permutations (e.g., reversing first and last name, adding birth years). Detail how the analyst should use email intelligence tools (e.g., Epieos) to validate these permutations to find hidden, secondary accounts.

4. VISUAL & SUPPLEMENTARY PIVOTS
   Provide instructions on checking messaging services (e.g., saving a phone number to contacts to view WhatsApp/Telegram avatars, statuses, and "last seen" data). Explain how to use reverse image search engines (Yandex, PimEyes, Google Lens) on any discovered profile pictures to pivot to new forums, websites, and unlinked social profiles.
```