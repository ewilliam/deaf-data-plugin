# Deaf Data Lab

Explore aggregate statistics, understand definitions, compare supported populations and survey
periods, and share findings with uncertainty and reproducible context. No Bun, Python, local Census
data or access to the application repository is needed.

Version: 0.2.1. Published by William Albright under MIT.
Repository: https://github.com/ewilliam/deaf-data-plugin. Marketplace: `deaf-data-lab`.
MCP endpoint: https://deaf-data.vercel.app/mcp. Access: anonymous, approved public aggregates only.
Support: https://github.com/ewilliam/deaf-data-plugin/issues. Tested client versions and file delivery: Codex CLI 0.158.0 manifest/schema validation and Claude Code 2.1.274 isolated install/uninstall checks passed. Hosted MCP tools, resources and CSV/JSON export bytes were verified with the official SDK. Full client conversation, upgrade, attachment-delivery and Deaf-user comprehension evaluations remain pending; no claim of completed acceptance is made. Until your client delivers an actual attachment, use the documented usable-text and canonical-query fallback.

## Choose your client

All packages include the same three skills and shared interpretation reference. Packaging support
is distinct from completed live client acceptance; see the validation status above.

| Client                    | Installation                                  | Data connection                                                                                         |
| ------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Codex                     | GitHub marketplace below                      | Bundled remote MCP configuration                                                                        |
| Claude Code               | GitHub marketplace below                      | Bundled remote MCP configuration                                                                        |
| Claude web/Desktop/Cowork | Upload the `claude.zip` release asset         | Review/connect the bundled remote connector; if needed add the endpoint in Connectors                   |
| ChatGPT                   | Upload the `chatgpt-skills.zip` release asset | Register the MCP app separately and select it with the skills; see connected-package instructions below |

Download the versioned ZIPs from [Releases](https://github.com/ewilliam/deaf-data-plugin/releases).
Names include the version, for example `deaf-data-0.2.1-claude.zip`.
Do not upload GitHub's **Source code ZIP** or **Code → Download ZIP** as a plugin: those contain
a marketplace repository, with the actual plugin nested inside it.

## Codex and Claude Code

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

## Claude web, Desktop and Cowork

Open **Customize → Browse plugins** (or the Plugins directory in your client), choose the option
to upload a custom plugin, and select `deaf-data-0.2.1-claude.zip`. Install/enable it and
review its connector setup. The server is https://deaf-data.vercel.app/mcp and needs no authentication. If the
connector is not imported automatically, add that URL as a custom remote connector and enable
it alongside the plugin. Start a new conversation and check that all three skills and the data
connection are available. Account/workspace policies may restrict custom uploads or connectors.

## ChatGPT: skills and data together

Upload `deaf-data-0.2.1-chatgpt-skills.zip` using **Plugins → Add → Upload**. This is a
standalone skill package with the manifest and `skills/` at its root. It intentionally contains
no raw MCP configuration; a skills upload does not register the service.

In **Create MCP App**, register https://deaf-data.vercel.app/mcp as **Deaf Data Lab**, with no authentication.
Install that connection and the skill package and select both in a new Work chat. If developer
mode is required, enable it in **Settings → Security and login**. UI labels and access vary by
account. Confirm that the tools appear before asking for statistics.

For a single package that declares your registered connection, copy its technical ID from the
connection's browser URL (starts with `plugin_asdk_app`). A maintainer can then run:

```sh
python3 build-archives.py --output connected-release --chatgpt-app-id YOUR_REGISTERED_APP_ID
```

Upload the resulting `deaf-data-0.2.1-chatgpt-connected.zip`. The `.app.json` mapping binds
the three skills to that registered connection. The ID must belong to a connection available to
your account/workspace; it does not grant access. This account-specific archive is not included
in the generic public release. Do not substitute a fabricated ID. Upload acceptance and tool
availability still need verification in your ChatGPT account.

For public ChatGPT directory distribution, use the OpenAI submission portal's **With MCP**
path, submit https://deaf-data.vercel.app/mcp, and include the skills from the skills archive in the same draft.
Complete domain verification, listing and review requirements. A GitHub release is not directory
approval, and a registered personal app ID is not a substitute for submitting the endpoint.

## Reproduce upload packages

Maintainers can run `python3 build-archives.py --output release-assets` from this repository root.
Python's standard library creates deterministic ZIPs and `SHA256SUMS`; end users only download
and upload the assets. `portable.zip` additionally provides Agent Plugins 1.0 root manifests
for hosts supporting that format. Claude's legacy HTTP configuration is retained separately.

Packaging references: [OpenAI](https://developers.openai.com/plugins/build/plugins),
[OpenAI MCP and skills submission](https://developers.openai.com/plugins/guides/submit-claude-plugin),
[Claude plugins](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

## Read and share results

Estimates describe the service's defined survey populations and universes. They are not individual
records. Answers retain uncertainty and limitations; suppression means withheld, not zero, and
missing coverage is different from suppression. Overlapping survey windows and changed geography
boundaries can prevent comparison. The service's returned reasons govern interpretation.

Routine answers use plain Markdown with the finding, uncertainty, essential caveats and a source
link. They do not rely on HTML disclosure panels or append technical query dumps. Ask “Show the
methods and exact query” for sample details, versioned provenance and canonical reproduction.
Follow-up answers carry forward your selections without repeating unchanged technical details.

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
