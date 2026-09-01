## Purpose

Este capability define a geração do ranking de ações brasileiras com base no desempenho recente dos ativos válidos, incluindo o tratamento de dados insuficientes, inválidos e da ausência total de ativos válidos.

## ADDED Requirements

### Requirement: Valid assets produce a six-month performance ranking

The system SHALL evaluate each valid asset using exactly seven monthly closing prices in chronological order, derive six consecutive monthly returns from those values, compute the arithmetic mean of those returns as the asset performance, and order the ranking from highest to lowest performance.

#### Scenario: Valid asset performance is calculated

- **GIVEN** an asset with exactly seven numeric monthly closing prices greater than zero and provided in chronological order
- **WHEN** the system calculates the asset performance for the last six months
- **THEN** the system SHALL compute six consecutive monthly returns using the formula `((current_price / previous_price) - 1) * 100` and SHALL calculate the asset performance as the arithmetic mean of those six returns

#### Scenario: Ranking is ordered from best to worst performance

- **GIVEN** multiple valid assets with calculated performance values
- **WHEN** the system builds the ranking
- **THEN** the system SHALL order the assets from the highest performance to the lowest performance

#### Scenario: Invalid or incomplete assets do not block valid assets

- **GIVEN** one or more assets that do not have exactly seven monthly closing prices, or whose prices contain non-numeric values or values less than or equal to zero
- **WHEN** the system builds the ranking together with valid assets
- **THEN** the system SHALL exclude the invalid or incomplete assets and SHALL continue ranking the valid assets

#### Scenario: No valid assets are available

- **GIVEN** all analyzed assets are invalid or incomplete
- **WHEN** the system attempts to build the ranking
- **THEN** the system SHALL produce an empty ranking result and SHALL not include any invalid asset