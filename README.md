# Open Smartphone Battery Thermal Dataset (OSBTD)

## Overview
This project collects real-world smartphone battery temperature data under different workloads, charging conditions, and cooling environments.

## Target Devices
- Google Pixel series (focus: Pixel 6a)
- Other Android devices (optional extension)

## Collected Variables
- Timestamp
- Device model
- Battery temperature (°C)
- Ambient temperature (°C)
- Battery level (%)
- Charging power (W)
- Screen state (ON/OFF)
- CPU load estimation
- Network type (Wi-Fi / LTE / 5G)
- Cooling condition (none / fan / AC)
- Case usage (yes/no)

## Goals
- Build thermal prediction models
- Estimate cooling effectiveness
- Evaluate battery aging acceleration factors
- Compare device thermal efficiency

## License
MIT License

## Research Assumptions

This project assumes:

- Battery temperature is influenced by ambient temperature + internal heat generation
- Cooling efficiency is determined by thermal resistance, not linear temperature difference alone
- Charging state significantly increases thermal load compared to idle usage
- Smartphone thermal behavior is device-specific and must be empirically measured


## Modeling Philosophy

This project uses empirical and simplified models.

It is NOT a full physical simulation.

Approaches used:
- regression-based modeling
- simplified thermal resistance approximations
- observational data fitting


## Data Priority

1. Real measured data (highest priority)
2. Repeated measurements under same conditions
3. Derived estimates
4. Synthetic data (lowest priority)


## Minimal Reproduction Protocol

### Device
Google Pixel 6a

### Measurement tool
Battery temperature from system API / AccuBattery

### Conditions
- Ambient temperature: 22–28°C
- Screen brightness: fixed 50%
- No case / case must be specified

### Sampling interval
Every 5 minutes

### Minimum dataset
- 30 minutes idle
- 30 minutes charging
- fan ON/OFF comparison

### Success criteria
- Temperature variance < ±1.5°C under stable conditions

## Research Assumptions
## Modeling Philosophy
## Data Priority
## Measurement Uncertainty
## Battery Temperature Definition
## Time Scale Assumption
