import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

c.execute('''
          insert into products (name) 
          values 
          ('Apple'),
          ('Banana'),
          ('Cupcake'),
          ('Donut')
          ''')
c.execute('''
            insert into prices (price)
            values
            (100),
            (200),
            (300),
            (400)
            ''')

conn.commit()