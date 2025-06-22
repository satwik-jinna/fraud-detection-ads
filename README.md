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

## Visualizations

### Fraud Map (Demo Data)

![Fraud Map](![fraud_map](https://github.com/user-attachments/assets/b7782078-4ce5-4d2a-ac5e-4726a8d035e2)
)

*Note: This project uses sample/simulated data. In real-world deployments, the fraud map would show clear regional “hotspots.” For this demo, the map highlights detected fraud activity by country where present.*

### Top Flagged Users
|   user_id |   total_clicks | ip_address      | country   |
|----------:|---------------:|:----------------|:----------|
|      1583 |           2027 | 198.123.220.105 | US        |
|      2274 |           2024 | 189.248.189.178 | MX        |
|       183 |           2019 | 95.67.89.62     | UA        |
|      2856 |           2018 | 208.145.17.246  | US        |
|      4442 |           2015 | 5.97.109.163    | IT        |

*Table: Example of users flagged for high click activity (potential bots or click farms).*

## Contact

*Created by Satwik. For demo/educational use.*
