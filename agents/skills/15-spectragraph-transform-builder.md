# SpectraGraph Transform Builder

Develops modular OSINT data-gathering transforms for the SpectraGraph architecture, enabling AI agents to query external APIs (like GitHub, Shodan, VirusTotal) and normalize the results into Neo4j graph nodes and edges.

**You need:** the target API documentation, the entity types to be generated, and the API key vault reference.

## Prompt

```
Variables:
[osint_source] = The external data source (e.g., "GitHub API", "VirusTotal", "Shodan")
[input_entity] = The starting node type (e.g., "Email", "IP Address", "Username")
[output_entities] = The resulting node types to be connected (e.g., "Repository", "Malware Hash", "Domain")

You are an expert OSINT Developer specializing in Python, Celery, and Graph Databases (Neo4j). Your task is to write a production-ready "Transform" for the SpectraGraph framework.

Source: [osint_source]
Input: [input_entity]
Output: [output_entities]

Return three sections:

1. PREPROCESS & VALIDATION
   Write a Python method to validate the `[input_entity]`. For example, if it's an IP address, use `ipaddress` module to ensure it's valid before querying.

2. SCAN & VAULT AUTHENTICATION
   Write the asynchronous `scan(self, target: str, api_key: str)` method. Show how to handle rate limits, timeouts, and pass the API key securely in the headers.

3. NORMALIZE & GRAPH MAPPING
   Write the `normalize(self, raw_json)` method. Map the JSON response into SpectraGraph's Pydantic types (e.g., `Node` and `Edge` models). Clearly define the relationship (e.g., `[input_entity] -[:COMMITTED_TO]-> [output_entity]`).
```