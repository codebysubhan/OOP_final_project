# importing necessary files
from db_layer import DBManager
# from bl_layer import TicketManager, MatchManager, FanManager, RefundManager, StadiumManager, TransactionManager
import bl_layer as bl
from integ_layer import DataIntegration

# importing necessary modules
import sqlite3 as sql_db
from datetime import datetime
# creating one-time database
filename = "database.db"
con = sql_db.connect(filename)
cur = con.cursor()

# populating database
def createtickets():
    cur.execute('''
        CREATE TABLE tickets
        (ID INT PRIMARY KEY NOT NULL,
        STATUS INT CHECK (STATUS IN(0, 1)),
        MATCH INT,
        SEAT INT
        );
    ''')
    cur.execute('''
        INSERT INTO tickets (id, status, match, seat)
        values (1, 0, 5, 367)
    ''')
    records_to_insert = [
        (2, 1, 6, 451),
        (3, 0, 5, 512),
        (4, 1, 6, 275),
        (5, 0, 7, 134),
        (6, 1, 8, 210),
        (7, 0, 7, 189),
        (8, 1, 5, 333),
        (9, 0, 6, 420),
        (10, 1, 8, 555),
        (11, 0, 7, 123),
        (12, 1, 5, 777),
        (13, 0, 6, 888),
        (14, 1, 8, 999),
        (15, 0, 7, 111),
        (16, 1, 5, 222),
        (17, 0, 6, 333),
        (18, 1, 8, 444),
        (19, 0, 7, 555),
        (20, 1, 5, 666)
    ]
    cur.executemany('''
        INSERT INTO tickets (id, status, match, seat)
        VALUES (?, ?, ?, ?)
    ''', records_to_insert)
# createtickets()
# cur.execute('''
# alter table tickets add column 
# ''')

def creatematches():
    cur.execute('''
        CREATE TABLE matches
        (MATCH_ID INT PRIMARY KEY NOT NULL,
        SCHEDULE DATETIME
        );
    ''')
    cur.execute('''
        INSERT INTO matches (match_id, schedule)
        values (1, '2023-12-28 12:30:00')
    ''')
    matches_data = [
        (2, '2023-12-29 15:45:00'),
        (3, '2023-12-30 18:00:00'),
        (4, '2023-12-31 20:15:00'),
        (5, '2024-01-01 14:00:00'),
        (6, '2024-01-02 16:30:00'),
        (7, '2024-01-03 19:45:00'),
        (8, '2024-01-04 21:00:00'),
        (9, '2024-01-05 12:00:00'),
        (10, '2024-01-06 14:30:00'),
        (11, '2024-01-07 16:45:00'),
        (12, '2024-01-08 18:30:00'),
        (13, '2024-01-09 20:15:00'),
        (14, '2024-01-10 12:00:00'),
        (15, '2024-01-11 14:30:00'),
        (16, '2024-01-12 17:00:00'),
        (17, '2024-01-13 19:45:00'),
        (18, '2024-01-14 21:30:00'),
        (19, '2024-01-15 12:30:00'),
        (20, '2024-01-16 15:00:00')
    ]
    cur.executemany('''
    insert into matches (match_id, schedule)
                    values(?, ?)
    ''', matches_data)
# creatematches()
def datetime_converter(result):
    datetime_str = result
    datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    return datetime_obj




con.commit()


# closing database
cur.close()
con.close()