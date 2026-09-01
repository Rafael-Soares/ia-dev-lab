## Purpose

Este capability define a apresentação do ranking de ações ao usuário, incluindo a forma como os resultados são exibidos quando existem dados válidos e como o sistema comunica a ausência de resultados sem erro não tratado.

## ADDED Requirements

### Requirement: Ranking results are displayed with key information

The system SHALL present the ranking results in the web interface with at least the position, ticker, and monthly average return expressed as a percentage for each asset when results are available.

#### Scenario: Results are shown with required fields

- **GIVEN** a ranking with at least one valid asset result
- **WHEN** the user opens the ranking view
- **THEN** the system SHALL display at least the position, ticker, and monthly average return expressed as a percentage for each result in the ranking

#### Scenario: Results respect ranking order

- **GIVEN** a ranking containing multiple valid assets ordered by performance
- **WHEN** the results are displayed to the user
- **THEN** the system SHALL preserve the ranking order in the presentation so the highest-performing asset appears first and the lowest appears last

### Requirement: Empty results show a clear message

The system SHALL present a clear user-facing message when no ranking results are available and SHALL not fail with an unhandled error.

#### Scenario: No results are available

- **GIVEN** an empty ranking result
- **WHEN** the user opens the ranking view
- **THEN** the system SHALL display a clear message indicating that no results are available

#### Scenario: Empty state does not produce an error

- **GIVEN** an empty ranking result
- **WHEN** the ranking view is rendered
- **THEN** the system SHALL handle the empty state gracefully and SHALL not result in an unhandled error

### Requirement: Partial ranking results remain usable in the interface

The system SHALL keep the ranking view usable when the ranking contains only the valid subset of the analyzed assets.

#### Scenario: Valid subset remains visible

- **GIVEN** a ranking result containing only the valid assets after other analyzed assets were excluded
- **WHEN** the ranking is displayed
- **THEN** the system SHALL display all available ranking results in their existing order without rendering an error or broken layout