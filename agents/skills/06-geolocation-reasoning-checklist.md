# Geolocation reasoning checklist

Produces a structured list of features to examine in an image and the sequence to work through them. The model works from your written description, not the image, and it does not identify the location.

**You need:** your own description of what is visible, and any region you have already ruled in or out.

## Prompt

```
Variables:
[description] = the analyst's written description of the image
[ruled_in] = regions already considered likely (default: none)
[ruled_out] = regions already excluded (default: none)

You are supporting a geolocation task. You cannot see the image. Work
only from the description below and produce a structured examination
checklist. Do not name a location.

DESCRIPTION:
[description]

Ruled in: [ruled_in]
Ruled out: [ruled_out]

Return four sections:

1. EXAMINATION SEQUENCE
   The order to work through the visible features, most discriminating
   first. Explain why each feature ranks where it does.

2. FEATURES TO CHECK
   For each feature in the description, the specific detail to look for
   and what it would narrow down. Cover signage, script, vegetation,
   built environment, vehicles, road markings, utilities, terrain, sun
   position, and anything else the description supports.

3. MISSING OBSERVATIONS
   Features that would be most useful and are absent from the
   description. These are the things to go back to the image for.

4. CROSS-REFERENCE SOURCES
   The reference sources that would test each finding, for example
   street-level imagery, national road sign standards, vehicle
   registration formats, satellite imagery.

Do not propose a location, a country, or a coordinate. Produce the
checklist only.
```
