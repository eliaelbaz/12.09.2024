import sqlite3
import pandas as pd

# טען את קובץ ה-CSV שהורדת
csv_file = 'ecommerce_customer_behavior.csv'  # כאן עליך לוודא שהשם נכון

# קרא את הקובץ עם pandas
df = pd.read_csv(csv_file)

# יצירת חיבור למסד הנתונים ושמירת הנתונים בטבלה בשם 'ecomm' בתוך מסד הנתונים ecomm.db
conn = sqlite3.connect('ecomm.db')  # שם מסד הנתונים הוא ecomm.db
df.to_sql('ecomm', conn, if_exists='replace', index=False)

# סגירת החיבור למסד הנתונים
conn.commit()
conn.close()

print("Database 'ecomm.db' created and CSV data imported successfully.")
