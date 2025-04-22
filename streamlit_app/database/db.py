# streamlit_app/database/db.py

import sqlite3
from pathlib import Path

# put the DB file next to your code, not in the CWD,
# so both pages see the same file
DB_PATH = Path(__file__).parent.parent / "app_data.db"

def _connect():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

# || ───– USER SIGN‑IN TABLE  ───– ||

def create_signin_table():
  conn = _connect()
  c = conn.cursor()
  c.execute("""
  CREATE TABLE IF NOT EXISTS signins (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    name           TEXT NOT NULL,
    email          TEXT NOT NULL,
    username       TEXT NOT NULL,
    password       TEXT NOT NULL,
    login_time     TEXT NOT NULL
  );
  """)
  conn.commit()
  conn.close()

def get_all_signins():
    conn = _connect()
    c = conn.cursor()
    c.execute("""
        SELECT name, email, username, password, login_time
        FROM signins
        ORDER BY login_time DESC
    """)
    rows = c.fetchall()
    conn.close()
    return rows

def insert_signin(name, email, username, password, login_time):
  conn = _connect()
  c = conn.cursor()
  c.execute("""
    INSERT INTO signins
      (name, email, username, password, login_time)
    VALUES (?, ?, ?, ?, ?)
  """, (name, email, username, password, login_time))
  conn.commit()
  conn.close()
# Connect sign in data to dashboard
# def get_all_signins():
#     conn = _connect()
#     c = conn.cursor()
#     c.execute("SELECT name, email, username, login_time FROM signins ORDER BY login_time DESC")
#     rows = c.fetchall()
#     conn.close()
#     return rows


# || ───– SURVEY RESPONSES TABLE  ───– ||

def create_response_table():
  conn = _connect()
  c = conn.cursor()
  c.execute("""
  CREATE TABLE IF NOT EXISTS responses (
    id                    INTEGER PRIMARY KEY AUTOINCREMENT,
    name                  TEXT,
    car_name              TEXT,
    car_model             TEXT,
    current_model_year    INTEGER,
    purchase_year         INTEGER,
    likert_rating         TEXT,
    dream_vehicle         TEXT,
    future_purchase_year  INTEGER,
    preferred_color       TEXT,
    vehicle_type          TEXT,
    powerplant            TEXT
  );
  """)
  conn.commit()
  conn.close()

def insert_response(data: dict):
  conn = _connect()
  c = conn.cursor()
  c.execute("""
    INSERT INTO responses (
      name, car_name, car_model, current_model_year,
      purchase_year, likert_rating, dream_vehicle,
      future_purchase_year, preferred_color,
      vehicle_type, powerplant
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  """, (
    data["name"],
    data["car_name"],
    data["car_model"],
    data["current_model_year"],
    data["purchase_year"],
    data["likert_rating"],
    data["dream_vehicle"],
    data["future_purchase_year"],
    data["preferred_color"],
    data["vehicle_type"],
    data["powerplant"],
  ))
  conn.commit()
  conn.close()

