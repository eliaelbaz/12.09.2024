import sqlite3
import pandas as pd

csv_file = 'ecommerce_customer_behavior.csv'

df = pd.read_csv(csv_file)

conn = sqlite3.connect('ecomm.db')
df.to_sql('ecomm', conn, if_exists='replace', index=False)

conn.commit()
conn.close()

print("Database 'ecomm.db' created and CSV data imported successfully.")
