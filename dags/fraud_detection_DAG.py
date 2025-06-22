from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from scipy.stats import zscore

def fraud_detection_task():
    # Function to load the data
    def load_data(path='/Users/satwikcrj/ad_click_events.csv'):
        df = pd.read_csv(path)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df

    # Detect bot users (many clicks)
    def detect_bot_users(df, threshold=1000):
        user_click_counts = df['user_id'].value_counts()
        return user_click_counts[user_click_counts > threshold]

    # Detect proxy IPs (many users from same IP)
    def detect_proxy_ips(df, user_threshold=10):
        ip_user_counts = df.groupby('ip_address')['user_id'].nunique()
        return ip_user_counts[ip_user_counts > user_threshold]

    # Detect click bursts (many clicks in a minute)
    def detect_click_bursts(df, burst_threshold=5):
        df['minute'] = df['timestamp'].dt.floor('min')
        burst_counts = df.groupby(['user_id', 'minute']).size().reset_index(name='clicks')
        return burst_counts[burst_counts['clicks'] > burst_threshold]

    # Detect Z-score anomalies
    def detect_zscore_anomalies(df, z_thresh=4):
        user_click_counts = df['user_id'].value_counts().reset_index()
        user_click_counts.columns = ['user_id', 'num_clicks']
        user_click_counts['z_score'] = zscore(user_click_counts['num_clicks'])
        return user_click_counts[user_click_counts['z_score'] > z_thresh]

    # Load data
    df = load_data()

    # Detect fraud patterns
    bots = detect_bot_users(df)
    print("Detected Bot Users:")
    print(bots)
    bots.to_csv('/Users/satwikcrj/bots_detected.csv')

    proxies = detect_proxy_ips(df)
    print("\nDetected Proxy IPs:")
    print(proxies)
    proxies.to_csv('/Users/satwikcrj/proxies_detected.csv')

    bursts = detect_click_bursts(df)
    print("\nDetected Click Bursts:")
    print(bursts.head(10))
    bursts.to_csv('/Users/satwikcrj/bursts_detected.csv', index=False)

    anomalies = detect_zscore_anomalies(df)
    print("\nDetected Anomalous Users (Z-score):")
    print(anomalies)
    anomalies.to_csv('/Users/satwikcrj/anomalies_detected.csv', index=False)

# Airflow DAG definition
default_args = {
    'owner': 'satwikcrj',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    'fraud_detection_dag',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
) as dag:
    fraud_detection = PythonOperator(
        task_id='fraud_detection_task',
        python_callable=fraud_detection_task
    )
