import sqlite3 as sql_db


class DBManager:
    def __init__(self, filename:str, con=None, cur=None):
        if con is None:
            con = sql_db.connect(filename)
        if cur is None:
            cur = con.cursor()
        self.con = con
        self.cur = cur
        print('DBManager Initialized!!!')

    def purchase_ticket(self, match_id: int, enclosure: str, ):
        pass