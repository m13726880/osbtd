# Data Integrity Rules

## 1. No mixing of data types
Real, derived, and synthetic data must be clearly separated.

## 2. Always include source_type column
- real_measured
- derived_estimate
- synthetic_model

## 3. Do not overwrite raw logs
Raw data must be append-only.

## 4. Invalid data handling
Noisy or inconsistent data should be flagged, not deleted.

## Data Integrity Rules
## Invalid Data Handling
## No Overwrite Policy
## Sampling Interval Rule
