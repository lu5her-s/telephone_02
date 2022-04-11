import sqlite3
import pandas as pd

conn = sqlite3.connect('02_telephone.db')

c = conn.cursor()

c.execute("""CREATE TABLE telephone
          ([id] INTEGER PRIMARY KEY AUTOINCREMENT,
          [name] TEXT,
          [place] TEXT,
          [rtaf_tel] TEXT,
          [rta_tel] TEXT,
          [note] TEXT)
          """)

# load data from csv file
#tel = pd.read_csv('02_telephone.csv', sep=',', header=0, encoding='utf-8')
tel = pd.read_csv('update.csv', sep=',', header=0, encoding='utf-8')

# write data to database
tel.to_sql('telephone', conn, if_exists='append', index=False)

# show data
# all = c.execute("SELECT * FROM tel").fetchall()
# print(all)


conn.close()
