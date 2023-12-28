# importing necessary files
# from db_layer import DBManager
# # from bl_layer import TicketManager, MatchManager, FanManager, RefundManager, StadiumManager, TransactionManager
# import bl_layer as bl
# from integ_layer import DataIntegration

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
    tickets_data = [
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
        (20, 1, 5, 666),
        (21, 0, 9, 777),
        (22, 1, 10, 888),
        (23, 0, 11, 999),
        (24, 1, 12, 111),
        (25, 0, 13, 222),
        (26, 1, 14, 333),
        (27, 0, 15, 444),
        (28, 1, 16, 555),
        (29, 0, 17, 666),
        (30, 1, 18, 777),
        (31, 0, 19, 888),
        (32, 1, 20, 999),
        (33, 0, 21, 111),
        (34, 1, 22, 222),
        (35, 0, 23, 333),
        (36, 1, 24, 444),
        (37, 0, 25, 555),
        (38, 1, 26, 666),
        (39, 0, 27, 777),
        (40, 1, 28, 888),
        (41, 0, 29, 999),
        (42, 1, 30, 111)
    ]
    cur.executemany('''
        INSERT INTO tickets (id, status, match, seat)
        VALUES (?, ?, ?, ?)
    ''', tickets_data)
# createtickets()
# cur.execute('''
# alter table tickets add column 
# ''')

def create_matches():
    cur.execute('''
        CREATE TABLE matches
        (MATCH_ID INT PRIMARY KEY NOT NULL,
        SCHEDULE DATETIME,
        STADIUM_ID INT
        );
    ''')
    cur.execute('''
        INSERT INTO matches (match_id, schedule, stadium_id)
        values (1, '2023-12-28 12:30:00', 1)
    ''')
    matches_data = [
        (2, '2023-12-29 15:45:00', 2),
        (3, '2023-12-30 18:00:00', 3),
        (4, '2023-12-31 20:15:00', 4),
        (5, '2024-01-01 14:00:00', 5),
        (6, '2024-01-02 16:30:00', 6),
        (7, '2024-01-03 19:45:00', 7),
        (8, '2024-01-04 21:00:00', 8),
        (9, '2024-01-05 12:00:00', 9),
        (10, '2024-01-06 14:30:00', 10),
        (11, '2024-01-07 16:45:00', 11),
        (12, '2024-01-08 18:30:00', 12),
        (13, '2024-01-09 20:15:00', 13),
        (14, '2024-01-10 12:00:00', 14),
        (15, '2024-01-11 14:30:00', 15),
        (16, '2024-01-12 17:00:00', 16),
        (17, '2024-01-13 19:45:00', 17),
        (18, '2024-01-14 21:30:00', 18),
        (19, '2024-01-15 12:30:00', 19),
        (20, '2024-01-16 15:00:00', 20)
    ]

    cur.executemany('''
        INSERT INTO matches (match_id, schedule, stadium_id)
        VALUES (?, ?, ?)
    ''', matches_data)
# create_matches()

def datetime_converter(result):
    datetime_str = result
    datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    return datetime_obj

def create_fans():
    cur.execute('''
        CREATE TABLE fans
        (FAN_ID INT PRIMARY KEY NOT NULL,
        NAME TEXT,
        EMAIL TEXT,
        PHONE VARCHAR(12)
        );
    ''')
    fans_data = [
    (1, "Subhan Ali", "subhanali1212w@gmail.com", "03084072295"),
    (2, "John Doe", "john.doe@example.com", "1234567890"),
    (3, "Jane Doe", "jane.doe@example.com", "9876543210"),
    (4, "Alice Smith", "alice.smith@example.com", "555-1234"),
    (5, "Bob Johnson", "bob.johnson@example.com", "555-5678"),
    (6, "Emily Brown", "emily.brown@example.com", "555-9876"),
    (7, "Alex Wilson", "alex.wilson@example.com", "333-1111"),
    (8, "Grace Turner", "grace.turner@example.com", "444-5678"),
    (9, "Ryan Miller", "ryan.miller@example.com", "777-8888"),
    (10, "Sophia Davis", "sophia.davis@example.com", "999-0000"),
    (11, "Mia Garcia", "mia.garcia@example.com", "111-2222"),
    (12, "Liam White", "liam.white@example.com", "444-3333"),
    (13, "Olivia Martinez", "olivia.martinez@example.com", "777-6666"),
    (14, "Ethan Hall", "ethan.hall@example.com", "888-4444"),
    (15, "Ava Taylor", "ava.taylor@example.com", "333-9999"),
    (16, "Noah Harris", "noah.harris@example.com", "555-5555"),
    (17, "Isabella Clark", "isabella.clark@example.com", "666-1111"),
    (18, "James Turner", "james.turner@example.com", "999-8888"),
    (19, "Emma Moore", "emma.moore@example.com", "222-4444"),
    (20, "William Allen", "william.allen@example.com", "888-9999")
    # Add more data as needed
    ]
    cur.executemany('''
    insert into fans (fan_id, name, email, phone)
                    values(?, ?, ?, ?)
    ''', fans_data)
# create_fans()

def create_stadiums():
    cur.execute('''
        CREATE TABLE stadiums
        (STADIUM_ID INT PRIMARY KEY NOT NULL,
        NAME TEXT,
        CAPACITY INT    );
    ''')
    stadium_data = [
    (1, 'Stadium A', 50000),
    (2, 'Stadium B', 60000),
    (3, 'Stadium C', 70000),
    (4, 'Stadium D', 80000),
    (5, 'Stadium E', 90000),
    (6, 'Stadium F', 100000),
    (7, 'Stadium G', 110000),
    (8, 'Stadium H', 120000),
    (9, 'Stadium I', 130000),
    (10, 'Stadium J', 140000),
    (11, 'Stadium K', 150000),
    (12, 'Stadium L', 160000),
    (13, 'Stadium M', 170000),
    (14, 'Stadium N', 180000),
    (15, 'Stadium O', 190000),
    (16, 'Stadium P', 200000),
    (17, 'Stadium Q', 210000),
    (18, 'Stadium R', 220000),
    (19, 'Stadium S', 230000),
    (20, 'Stadium T', 240000),
    ]
    cur.executemany('''
    INSERT INTO stadiums (STADIUM_ID, NAME, CAPACITY) 
    VALUES (?, ?, ?)
    ''', stadium_data)
# create_stadiums()


def create_purchase_log():
    cur.execute('''
        CREATE TABLE purchase_log
        (
            PURCHASE_ID INT PRIMARY KEY,
            FAN_ID INT,
            TICKET_ID INT,
            MATCH_ID INT,
            PURCHASE_DATE DATETIME,
            QUANTITY INT,
            TOTAL_AMOUNT DECIMAL(10, 2),
            PAYMENT_METHOD VARCHAR(50),
            FOREIGN KEY (FAN_ID) REFERENCES fans(FAN_ID),
            FOREIGN KEY (TICKET_ID) REFERENCES tickets(ID),
            FOREIGN KEY (MATCH_ID) REFERENCES matches(MATCH_ID)
        );
    ''')
    purchase_data = [
        (1, 1, 1, 1, '2023-12-28 13:00:00', 2, 100.0, 'Credit Card'),
        (2, 2, 3, 2, '2023-12-29 16:00:00', 1, 50.0, 'Cash'),
        (3, 3, 5, 3, '2023-12-30 18:30:00', 4, 200.0, 'PayPal'),
        (4, 4, 7, 4, '2023-12-31 21:00:00', 3, 150.0, 'Credit Card'),
        (5, 5, 9, 5, '2024-01-01 15:30:00', 1, 50.0, 'Cash'),
        (6, 6, 11, 6, '2024-01-02 17:00:00', 2, 100.0, 'PayPal'),
        (7, 7, 13, 7, '2024-01-03 19:30:00', 4, 200.0, 'Credit Card'),
        (8, 8, 15, 8, '2024-01-04 21:45:00', 1, 50.0, 'Cash'),
        (9, 9, 17, 9, '2024-01-05 13:15:00', 3, 150.0, 'PayPal'),
        (10, 10, 19, 10, '2024-01-06 15:30:00', 2, 100.0, 'Credit Card'),
        (11, 11, 21, 11, '2024-01-07 18:00:00', 1, 50.0, 'Cash'),
        (12, 12, 23, 12, '2024-01-08 20:15:00', 3, 150.0, 'PayPal'),
        (13, 13, 25, 13, '2024-01-09 12:30:00', 2, 100.0, 'Credit Card'),
        (14, 14, 27, 14, '2024-01-10 14:45:00', 4, 200.0, 'Cash'),
        (15, 15, 29, 15, '2024-01-11 16:30:00', 1, 50.0, 'PayPal'),
        (16, 16, 31, 16, '2024-01-12 18:45:00', 3, 150.0, 'Credit Card'),
        (17, 17, 33, 17, '2024-01-13 21:00:00', 2, 100.0, 'Cash'),
        (18, 18, 35, 18, '2024-01-14 13:15:00', 1, 50.0, 'PayPal'),
        (19, 19, 37, 19, '2024-01-15 15:30:00', 4, 200.0, 'Credit Card'),
        (20, 20, 39, 20, '2024-01-16 17:45:00', 2, 100.0, 'Cash'),
        (21, 1, 41, 1, '2024-01-17 20:00:00', 3, 150.0, 'PayPal'),
        (22, 2, 43, 2, '2024-01-18 12:15:00', 1, 50.0, 'Credit Card'),
        (23, 3, 45, 3, '2024-01-19 14:30:00', 2, 100.0, 'Cash'),
        (24, 4, 47, 4, '2024-01-20 16:45:00', 4, 200.0, 'PayPal'),
        (25, 5, 49, 5, '2024-01-21 19:00:00', 1, 50.0, 'Credit Card'),
        (26, 6, 51, 6, '2024-01-22 21:15:00', 3, 150.0, 'Cash'),
        (27, 7, 53, 7, '2024-01-23 13:30:00', 2, 100.0, 'PayPal'),
        (28, 8, 55, 8, '2024-01-24 15:45:00', 1, 50.0, 'Credit Card'),
        (29, 9, 57, 9, '2024-01-25 18:00:00', 4, 200.0, 'Cash'),
        (30, 10, 59, 10, '2024-01-26 20:15:00', 2, 100.0, 'PayPal'),
        (31, 11, 61, 11, '2024-01-27 12:30:00', 3, 150.0, 'Credit Card'),
        (32, 12, 63, 12, '2024-01-28 14:45:00', 1, 50.0, 'Cash'),
        (33, 13, 65, 13, '2024-01-29 17:00:00', 2, 100.0, 'PayPal'),
        (34, 14, 67, 14, '2024-01-30 19:15:00', 4, 200.0, 'Credit Card'),
        (35, 15, 69, 15, '2024-01-31 21:30:00', 1, 50.0, 'Cash'),
        (36, 16, 71, 16, '2024-02-01 13:45:00', 3, 150.0, 'PayPal'),
        (37, 17, 73, 17, '2024-02-02 16:00:00', 2, 100.0, 'Credit Card'),
        (38, 18, 75, 18, '2024-02-03 18:15:00', 1, 50.0, 'Cash'),
        (39, 19, 77, 19, '2024-02-04 20:30:00', 4, 200.0, 'PayPal'),
        (40, 20, 79, 20, '2024-02-05 12:45:00', 2, 100.0, 'Credit Card'),
        (41, 1, 81, 1, '2024-02-06 15:00:00', 3, 150.0, 'Cash'),
        (42, 2, 83, 2, '2024-02-07 17:15:00', 1, 50.0, 'PayPal')
    ]

    cur.executemany('''
    INSERT INTO purchase_log 
    (PURCHASE_ID, FAN_ID, TICKET_ID, MATCH_ID, PURCHASE_DATE, QUANTITY, TOTAL_AMOUNT, PAYMENT_METHOD) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', purchase_data)
# create_purchase_log()


con.commit()


# closing database
cur.close()
con.close()