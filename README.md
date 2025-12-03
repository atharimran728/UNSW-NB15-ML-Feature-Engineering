# Feature Engineering for UNSW-NB15

This project contains a minimal, clean feature-engineering pipeline built on the UNSW-NB15 training dataset.  
It converts raw network telemetry into ML-ready features suitable for intrusion detection, SOC analytics, and threat-classification experimentation.
This repository extends the **UNSW-NB15 ML Preprocessing Pipeline** by adding a dedicated feature-engineering stage.  


## What This Pipeline Does
- Loads UNSW-NB15 training-set CSV  
- One-hot encodes categorical fields (`proto`, `service`, `state`)  
- Removes metadata and non-predictive fields  
- Scales numerical features with `StandardScaler`  
- Produces a final feature matrix expanding 45 raw columns → 194 ML-ready features

## Why It Matters for SOC Work
Security teams rely on feature-rich data to detect abnormal behavior. This pipeline:
- Normalizes the dataset to remove noise and variance  
- Expands protocol/service/state data into high-signal indicators  
- Provides a clean input layer for building IDS/IPS ML models  
- Helps analysts experiment with feature importance, threat prediction, and anomaly scoring

In short, it transforms messy network telemetry into a usable foundation for ML-driven SOC automation.

## Run the Script
`python feature_engineering.py`

## Dataset
UNSW-NB15 training set.  
Source: UNSW Canberra Cyber Range Lab.
