import sqlite3

DB_NAME = "tree_tracker_ai.db"

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS plantations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tree_name TEXT NOT NULL,
    location TEXT NOT NULL,
    count INTEGER NOT NULL,
    date TEXT NOT NULL,
    watering_per_week INTEGER NOT NULL,
    season TEXT NOT NULL,
    predicted_survival REAL NOT NULL,
    actual_survival REAL
)
""")

sample_data = [
    ("Neem", "School Campus", 10, "2025-07-10", 4, "Monsoon", 0, 88),
    ("Mango", "Village Farm", 15, "2025-07-20", 3, "Monsoon", 0, 82),
    ("Ashoka", "Road Side", 8, "2025-04-12", 5, "Summer", 0, 65),
    ("Jamun", "Park Area", 12, "2025-12-05", 2, "Winter", 0, 70),
    ("Bamboo", "Farm Area", 25, "2025-08-15", 4, "Monsoon", 0, 90),
    ("Gulmohar", "Highway Road", 20, "2025-05-05", 3, "Summer", 0, 60),
    ("Peepal", "College Campus", 5, "2025-01-15", 2, "Winter", 0, 72),
]

cur.executemany("""
INSERT INTO plantations
(tree_name, location, count, date, watering_per_week, season, predicted_survival, actual_survival)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", sample_data)

conn.commit()
conn.close()

print("Database created and sample data inserted.")
