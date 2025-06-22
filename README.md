# Ad Fraud Detection Demo

## Overview

This project demonstrates scalable and explainable methods to detect and visualize ad click fraud and ad spam.

It includes:
- **Bot & anomaly detection:** Python and SQL-based approaches to flag high-risk users, suspicious IPs, and bursty click activity.
- **Automated pipeline:** Production-ready DAG using Apache Airflow.
- **Visualization:** Maps and dashboards showing where fraud happens, and actionable reporting for stakeholders.
- **Geolocation:** Real-world mapping using GeoLite2 Country database.

## Getting Started

1. Install requirements:

2. Run the notebook:
Open and run `notebook/main_analysis.ipynb`.

3. Airflow pipeline:
Put `dags/fraud_detection_DAG.py` in your Airflow `dags/` folder and run `airflow standalone`.

## Example Results

- Detected high-volume bots and proxy IPs
- Fraud “hotspots” mapped by country
- Automated reporting and visualization

## Contact

*Created by Satwik Jinna. For demo/educational use.*
