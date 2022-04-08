import sqlite3
import pandas as pd

conn = sqlite3.connect('test.db')
c = conn.cursor()

c.execute('''
            select a.name, b.price
            from products a
            left join prices b on a.id = b.id
            ''')

df = pd.DataFrame(c.fetchall(), columns=['name', 'price'])
print(df)