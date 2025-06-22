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

## Key Results

- **Detected high-risk users:** Flagged 5+ user accounts with >1000 clicks/day using anomaly detection and Z-score methods.
- **Identified suspicious proxy IPs:** Found IP addresses associated with unusually high numbers of user accounts, suggesting bot farms or click fraud.
- **Automated pipeline:** Set up a daily Airflow DAG to run fraud checks and export results automatically.
- **Actionable insights for stakeholders:** Produced easy-to-read maps and reports to help business teams identify fraud trends by country.

## Contact

*Created by Satwik. For demo/educational use.*
