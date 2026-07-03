# Experimental Methodology

## Device
Google Pixel 6a

## Temperature Definition
Battery temperature is internal thermistor value reported by Android system API.

## Measurement Tool
- Android system battery stats
- optional AccuBattery equivalent app

## Sampling Method
- interval: 5 minutes
- steady-state assumed after 10 minutes stabilization

## Environmental Conditions
- ambient temperature recorded separately
- airflow condition must be categorized (none / fan / AC)

## Experimental Scenarios
1. Idle usage
2. Charging (7.5W–20W range)
3. Fan-assisted cooling vs no cooling

## Data Validation Rules
- discard unstable readings during rapid change (>1°C/min)
- average over 3 samples if necessary
