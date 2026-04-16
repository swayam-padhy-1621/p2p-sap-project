import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS pr (id INTEGER PRIMARY KEY, item TEXT, qty INTEGER)')
c.execute('CREATE TABLE IF NOT EXISTS po (id INTEGER PRIMARY KEY, vendor TEXT)')

conn.commit()
conn.close()

print("Database created")