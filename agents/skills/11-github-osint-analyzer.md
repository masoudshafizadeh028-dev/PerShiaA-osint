# GitHub OSINT Analyzer

Extracts intelligence from GitHub repositories, users, and organizations using targeted search operators, API calls, and code analysis techniques to uncover hidden connections, credentials, and structural patterns.

**You need:** the target's GitHub username, organization name, or relevant keywords/domains.

## Prompt

```
Variables:
[target] = the GitHub username, organization name, or specific project keyword
[objective] = what you are trying to find (e.g., "leaked credentials", "employee network", "infrastructure details", "historical email addresses")
[known_repos] = any specific repository URLs already identified (default: none)

You are an expert open source intelligence (OSINT) analyst specializing in GitHub and version control systems.
Analyze the target based on the provided objective and construct a concrete investigation plan and query set.

Target: [target]
Objective: [objective]
Known Repos: [known_repos]

Return four sections:

1. TARGET PROFILING COMMANDS
   List specific `curl` or `gh api` commands to extract the target's hidden metadata (e.g., creation date, exact email addresses from commit logs, organizational structure).
   Example: `curl -s "https://api.github.com/users/[target]/events" | jq -r '.[].payload.commits[].author.email'`

2. PRECISION SEARCH OPERATORS
   Provide 5-10 specific GitHub dorks tailored to the target and objective. Include:
   - File extension targeting (e.g., `extension:env "DATABASE_URL" org:[target]`)
   - Path-specific searching (e.g., `path:.github/workflows repo:[target]/core`)
   - Credential patterns (if objective aligns) (e.g., `"AKIA" org:[target]`)
   - Internal network references (e.g., `"internal" OR "10.0.0." org:[target]`)

3. AUTOMATED TOOLING RECOMMENDATIONS
   Recommend 2-3 specific command-line tools (e.g., TruffleHog, Gitleaks, Gitrob) configured specifically for this target. Provide the exact command string you would use to scan the target safely and effectively.

4. BEHAVIORAL AND METADATA ANGLES
   List 3 specific ways an analyst should manually review the target's commit history, fork network, or issue trackers to uncover insights related to the [objective]. Explain *what* to look for (e.g., "Review merged PRs in [repo] to identify the hierarchy of code reviewers and infer the engineering team's chain of command.")

Do not invent findings or fabricate API responses. Output actionable intelligence gathering steps.
```