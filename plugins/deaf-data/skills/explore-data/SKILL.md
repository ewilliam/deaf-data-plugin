---
name: explore-data
description: Explore Deaf Data Lab aggregate employment, education and other supported measures by population, place and survey period, including follow-up questions and exports.
---

# Explore Deaf Data Lab

Read [answer and conversation conventions](references/conventions.md) before answering.
Use the connected Deaf Data Lab MCP tools; no local data or runtime is needed.

1. For first use, start with “What can I learn about deaf employment in my state?” Call
   discover_data with kind=releases. Explain actual available coverage briefly; ask for the
   state if unknown and bundle any other necessary meaning questions. Connection success does
   not establish available data. If discovery fails, report the failure and actionable nextStep.
2. Discover measures for an eligible release using discover_data with kind=measures and release.
   Read describe_measure for the selected measure and resolve_geography for the place. Follow
   nextCursor when needed to establish coverage or newest period; never assume the first page
   or active release is the best match. Candidate labels are unapproved, even in authorized previews.
3. Check exact capability shapes: dimension catalogs do not prove arbitrary intersections exist.
   Populate all canonical query fields explicitly using metadata and established user choices.
4. Call query_statistics with {query}. Same-period population comparisons use supported
   calculations here; historical comparisons use compare_periods with two explicit snapshots.
5. Check status/isError, metadataGaps and completeness. Follow query cursors with identical
   selections before claiming completeness. Explain returned values using the shared conventions.
6. For sharing, use export_analysis with {analysis: {kind: query, query}, format: csv or json}.
   The canonical query comes from reproduction; do not include pagination in the export selection.

Example response shape (fill only from actual tool results):
“Among [defined population] in [place], [estimate and unit, uncertainty and confidence level]
were employed during [survey window]. [Material limitation]. Source: [returned citation/link].”
Follow with recoverable canonical details. A suppressed result instead says “The service withheld
this estimate: [returned reason]”; never insert an estimated number.
