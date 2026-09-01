## Context

The project already defines a web application for Brazilian stock analysis, with data-processing logic separated from the presentation layer. The current scope requires a ranking based on recent six-month performance and a view that allows the user to inspect the results.

## Goals / Non-Goals

**Goals:**
- Generate a ranking from valid six-month performance data.
- Render the ranking in the web interface.
- Handle partial data and empty-result states without exposing broken output.

**Non-Goals:**
- Defining investment recommendations.
- Replacing the external data source contract during the planning phase.
- Introducing new architectural components beyond the current Flask + templates + processing structure.

## Decisions

- Keep the ranking logic and the presentation logic as separate responsibilities, consistent with the existing project structure. This preserves a clear distinction between data preparation and user-facing rendering.
- Use the project’s existing notion of a recent six-month performance window, while excluding assets that do not have enough valid data for the analysis. This prevents incomplete entries from distorting the ranking.
- Treat the empty-result case as a first-class user state, not as an error-only path. The interface should clearly explain that no ranking is available instead of rendering an incomplete or misleading list.
- Do not define new formulas or financial heuristics beyond the project’s current scope; the planning artifacts stay within the behavior already described for the application.

## Risks / Trade-offs

- [Partial data] → The ranking may be shorter than the full set of analyzed assets, but this is acceptable as long as the system keeps only valid data and communicates clearly when some assets are excluded.
- [No available results] → The app must present an explicit empty state instead of a blank or broken screen.
- [Scope drift] → The design deliberately avoids adding new investment guidance or unsupported API assumptions so the implementation remains aligned with the established requirement.

## Migration Plan

- No migration is required for this change; it is a feature addition within the current application structure.
- The implementation should be introduced in the existing processing and template flow without changing the project’s overall purpose or scope.

## Open Questions

- None at this planning stage. Selection and integration of the external financial data API are explicitly outside the scope of this change.