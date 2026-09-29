# Answer and conversation conventions

Clarify meaning, not implementation fields. Establish population, place, survey period, measure,
and denominator from the request and conversation. Bundle related necessary questions once.
Derive release, methodology and geography IDs and explicit canonical arguments from discovery.
Never ask users to supply internal IDs. Do not ask again for established selections.

For “latest,” inspect all relevant discovery pages and select the newest approved, queryable
release supporting the requested analysis, ordered by survey period, not deployment date or
activeRelease. Disclose its actual survey window. If products, periods or denominators would
materially change the interpretation, explain those choices and ask before querying. Authorization
is not a storage-health probe. Do not substitute an older release after a storage failure.

Lead with the finding and identify population, place and survey window. Put returned uncertainty
beside the estimate (including its confidence level); explain margin of error in plain language
when first needed. Retain units, universe, denominator, sample/reliability cautions, suppression,
approval status and material limitations. Never omit material uncertainty even when asked to.
Cite the returned citation and source links. Do not invent links, metadata or missing uncertainty.
Keep the full canonical query, release/definition/methodology versions, available source IDs and
query hash recoverable in a details block or accompanying artifact. Material caveats belong in
the main answer. An MCP resource URI is not a public citation URL.

Use descriptive table headers with units, explicit “Suppressed” and “Not available” labels, chart
text summaries and labels that do not depend on color. Do not infer identity beyond the service's
population definition. Explain that definition when it matters to interpretation.

| State                           | Explain and act                                                                                                                                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Suppressed row                  | The estimate is withheld under the returned reliability rule. Preserve the reason and nulls. Suppression is not zero; never reconstruct it.                                                                                    |
| Absent coverage                 | This exact combination was not materialized. Discover supported alternatives; explain what each changes and wait for selection before querying altered scope.                                                                  |
| Incompatible comparison         | The server cannot answer this comparison. State the returned reasons, including overlapping windows or changed boundaries. Do not infer significance.                                                                          |
| Temporary failure / unavailable | The service could not verify this request. Retry the same request when appropriate, respect Retry-After, and provide any returned request ID to support. Do not describe an outage as an empty catalog or invent alternatives. |
| Invalid / unsupported           | Use issues and nextStep to check discovered definitions and exact capability shapes. Distinguish a suggested alternative from an executable, validated query.                                                                  |
| Output limit                    | No complete export was produced. Offer an explicitly narrower scope; do not label a page or truncated preview complete.                                                                                                        |

For “What about Texas?”, preserve the preceding analysis and change only place. For “Compare that
with hearing adults,” retain period and other selections and use a supported same-period query
calculation. For “Use the previous period,” discover the preceding supported survey period in the
same product; clarify competing meanings or ambiguous earlier analyses. Revalidate coverage and
comparability; disclose meaningful changes. Keep continuity in the client conversation.

For sharing, provide a copy-ready paragraph with uncertainty, limitations and citation. Call
export_analysis for a complete CSV or JSON. Use supported client file handling to decode the
embedded bytes, check byteLength and SHA-256, confirm complete=true, and retain reproduction and
context alongside the file. Never present base64 or deafdata:// as a download link. If the client
cannot create attachments or verify the digest, say so and provide usable text plus canonical
reproduction without claiming file delivery. Do not create an application deep link: exact URL
round trips are not supported by this plugin.
