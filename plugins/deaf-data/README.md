# Deaf Data Lab

Explore aggregate statistics, understand definitions, compare supported populations and survey
periods, and share findings with uncertainty and reproducible context. No Bun, Python, local Census
data or access to the application repository is needed.

Version: 0.1.0. Published by William Albright under MIT.
Repository: https://github.com/ewilliam/deaf-data-plugin. Marketplace: `deaf-data-lab`.
MCP endpoint: https://deaf-data.vercel.app/mcp. Access: anonymous, approved public aggregates only.
Support: https://github.com/ewilliam/deaf-data-plugin/issues. Tested client versions and file delivery: Codex CLI 0.158.0 manifest/schema validation and Claude Code 2.1.274 isolated install/uninstall checks passed. Hosted MCP tools, resources and CSV/JSON export bytes were verified with the official SDK. Full client conversation, upgrade, attachment-delivery and Deaf-user comprehension evaluations remain pending; no claim of completed acceptance is made. Until your client delivers an actual attachment, use the documented usable-text and canonical-query fallback.

## Install

In Codex, add this catalog:

```sh
codex plugin marketplace add ewilliam/deaf-data-plugin
```

Open the Codex plugin directory, select the `deaf-data-lab` marketplace and install `deaf-data`.
Start a new chat after installation. In Claude Code:

```sh
claude plugin marketplace add ewilliam/deaf-data-plugin
claude plugin install deaf-data@deaf-data-lab
```

End installation with your first question:

> What can I learn about deaf employment in my state?

The assistant checks available releases and measures, briefly explains coverage, and asks for your
state if it is not already known. If discovery is unavailable, a successful connection does not
mean there is data to query. Follow the recovery message or contact support with the request ID.

Try “What does the denominator mean?”, “What about Texas?”, “Compare that with hearing adults,”
“Use the previous period,” or “Give me a copy-ready finding and a complete CSV.” The assistant
carries forward established selections and asks before changing the analysis to obtain coverage.
“Latest” means the newest approved, queryable survey period supporting your analysis, not a recent
website deployment. The answer names the actual survey window.

## Read and share results

Estimates describe the service's defined survey populations and universes. They are not individual
records. Answers retain uncertainty and limitations; suppression means withheld, not zero, and
missing coverage is different from suppression. Overlapping survey windows and changed geography
boundaries can prevent comparison. The service's returned reasons govern interpretation.

Exports are complete bounded CSV/JSON resources. Where your client supports attachments, the
assistant checks completeness, byte count and SHA-256 and retains query/provenance details beside
the file. Otherwise it provides usable text and canonical reproduction and explains the file
limitation. An embedded resource URI or base64 text is not a download. Exact application deep links
are not supported; use the canonical query or export to reproduce an analysis.

## Troubleshooting and versions

- No matching coverage: inspect available shapes; choose an alternative only after understanding
  its changed population, period, geography or denominator.
- Suppressed or incompatible: retain the returned reason. Repeating requests will not reveal a value.
- 403: check that the installed endpoint matches the canonical host; contact support.
- 429 or busy: respect Retry-After and retry the same request later.
- Unavailable data: retry the same selection; send support the request ID. Do not replace it with zero.
- Oversized export: choose a smaller scope explicitly. Never treat a preview as a complete file.

Refresh the marketplace using your client's plugin manager, upgrade `deaf-data`, then start a new
chat. Uninstall it through the same manager (Claude: `claude plugin uninstall deaf-data@deaf-data-lab`).
For rollback, obtain an earlier reviewed `vVERSION` tag from the public repository, register that
local checkout as a marketplace, and reinstall its version. The service preserves tool contracts;
breaking changes require a documented matching bundle version. Contact support for supported versions.
