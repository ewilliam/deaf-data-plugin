---
name: interpret-comparison
description: Interpret Deaf Data Lab comparisons between deaf and hearing populations or survey periods, preserving uncertainty, eligibility and exact selections.
---

# Interpret a comparison

Read [answer and conversation conventions](../explore-data/references/conventions.md), including
latest-period selection, follow-up continuity, recovery, accessible output and file sharing.

1. Use discover_data, describe_measure and resolve_geography to establish the requested populations,
   measure, denominator, places and periods. Reuse established choices. Clarify only meaningful
   ambiguity; derive explicit IDs and methodology from returned metadata.
2. For populations in the same period, use query_statistics and the exact supported calculation.
   Do not use compare_periods as a generic population comparator. Explain a difference in rates
   in percentage points; a relative change is percent change with an explicit baseline.
3. For historical change, use compare_periods with explicit before and after canonical snapshot
   queries and change=absolute, relative or disparity. Absolute/relative require empty source
   calculations; disparity requires both populations and empty calculations or difference.
   Do not silently drop an incompatible requested calculation. For earnings, obtain the supported
   commonDollarYear and explain the dollar basis before comparing.
4. Preserve both source contexts, returned change uncertainty, source availability and per-row
   reasons. Overlapping ACS windows are not independent observations. Never manufacture confidence
   intervals or claim statistical significance without returned evidence. “Not comparable” means
   this requested comparison cannot be answered, even if both source estimates exist.
5. State the finding, baseline and survey windows, uncertainty and all material warnings. Cite
   both sources and keep the complete comparison reproduction recoverable. For a shareable file,
   call export_analysis with analysis.kind=comparison and the comparison request, checking the
   complete embedded file and digest with supported client handling.

Example response shape: “The returned change between [before window] and [after window] is
[value, unit and returned uncertainty]. [Comparability limitation].” If ineligible: “The service
cannot estimate this change because [returned reason]. [Catalog-backed options, for user choice].”
Do not calculate a missing or suppressed change yourself.
