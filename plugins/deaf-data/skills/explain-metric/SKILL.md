---
name: explain-metric
description: Explain a Deaf Data Lab measure's versioned population universe, numerator, denominator, exclusions, survey period and limitations using service metadata.
---

# Explain a metric

Read [answer and conversation conventions](../explore-data/references/conventions.md) for
clarification, latest-period selection, accessible answers, follow-ups, recovery and sharing.

1. Reuse the release and measure from the user's analysis. Otherwise discover_data identifies
   eligible releases and measures; clarify population, period or competing denominators only
   when their meanings differ. Obtain technical IDs from metadata, not from the user.
2. Call describe_measure with release and metric. Explain the applicable versioned definition,
   universe, numerator, denominator, exclusions, survey window, units and limitations in plain
   language. Use the returned populationDefinition rather than assuming a cultural identity.
3. Definitions and methodology resources are release-qualified. Retrieve changing definitions
   from the service; never substitute a current methodology for missing versioned metadata.
   Disclose metadataGaps. Dimension categories explain meanings; exact capabilities establish
   supported query shapes. A definition alone does not prove coverage or storage availability.
4. Cite available source links and keep release, definition and methodology identity recoverable.
   Suppression is not zero; absent coverage is not suppression. If asked for a finding, use
   query_statistics and preserve uncertainty beside estimates. If asked for sharing, provide
   a copy-ready explanation and citation; export_analysis exports an actual query/comparison,
   not a fabricated dataset derived from this explanation.

Example response shape: “[Measure] counts [numerator] among [denominator/universe], excluding
[returned exclusions], for [survey window]. It does not establish [material limitation from
metadata]. This is definition [version] for [release]. [Source citation].”
