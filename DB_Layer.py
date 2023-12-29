import sqlite3 as sql_db
import dbpopulate
import random
from datetime import datetime
class DBManager:
    def __init__(self, filename:str, con=None, cur=None):
        if con is None:
            con = sql_db.connect(filename)
        if cur is None:
            cur = con.cursor()
        self.con = con
        self.cur = cur
        print('DBManager Initialized!!!')

    def buyTicketInDB(self, fan_id:int):
        query = '''
            select * from tickets where status = 1
        '''
        self.cur.execute(query)
        data = self.cur.fetchone()
        if len(data) == 0:
            print('ERROR! All tickets are sold')
        else:
            purchase_data = [
                self.create_new_purchase_id(),
                fan_id,
                data[0],
                data[2],
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                1,
                random.choice([1200, 2500, 2000, 2700]),
                random.choice(['Credit Card', 'Cash', 'PayPal'])
            ]
            query = '''
                insert into purchase_log
                (purchase_id, fan_id, ticket_id, match_id, purchase_date, quantity, total_amount, payment_method)
                values (?, ?, ?, ?, ?, ?, ?, ?)
            '''
            self.cur.execute(query, purchase_data)
            query0 = '''
                update tickets
                set status = 0
                where id = ?
            '''
            self.cur.execute(query0, (data[0], ))
            self.con.commit()

    def getAvailableTicketsFromDB(self, match:int):
        # Logic to retrieve available tickets for a match from the database
        self.cur.execute(f'''
        select id from tickets where match = {match} and status = 1
        ''')
        tickets = self.cur.fetchall()
        print('Total available tickets are: ', len(tickets))
        out_str = f'Total available tickets are: {len(tickets)}\n{tickets}'
        return out_str

    def checkTicketValidityInDB(self, ticket_id:int):
        self.cur.execute(f'''
        select status from tickets where ID = {ticket_id}
        ''')
        data = self.cur.fetchall()
        try:
            if data[0][0] == 1:
                # print('Congratulations! ticket is valid!', data)
                return f'Congratulations! ticket is valid!'
            else:
                # print(': ticket is not valid!')
                return f': ticket is not valid!'
        except:
            # print('An error occurred!')
            return f'An error occurred!'

    def getMatchDetailsFromDB(self, match_id:int):
        self.cur.execute(f'''
        select match_id, schedule from matches where match_id = {match_id}
        ''')
        data = self.cur.fetchone()
        # print(data)
        id = data[0]
        timeofmatch = dbpopulate.datetime_converter(data[1])
        out_str = (f'Details for the match with id = {id} are below:\nSchedule\t---\t{timeofmatch}')
        return out_str

    def getMatchScheduleFromDB(self):
        self.cur.execute('''
        select match_id, schedule from matches
        ''')
        data = self.cur.fetchall()
        # print(data)
        out_str = ''
        for row in data:
            id = row[0]
            timeofmatch = dbpopulate.datetime_converter(row[1])
            out_str += f'Match id = {id}\tSchedule = {timeofmatch}\n'
        return out_str

    def create_new_fan_id(self):
        self.cur.execute('''
        select fan_id from fans
        ''')
        data = self.cur.fetchall()
        data = [i[0] for i in data]
        new_id = random.choice(list(set(range(1, 500)) - set(data)))
        return new_id
    
    def create_new_purchase_id(self):
        self.cur.execute('''
        select purchase_id from purchase_log
        ''')
        data = self.cur.fetchall()
        data = [i[0] for i in data]
        new_id = random.choice(list(set(range(1, 500)) - set(data)))
        return new_id

    def registerFanInDB(self, name:str, email:str, phone:str):
        self.cur.execute('''
            INSERT INTO fans (fan_id, name, email, phone)
            VALUES (?, ?, ?, ?)
        ''', (self.create_new_fan_id(), name, email, phone))
        self.con.commit()
        return f'Fan added success!!!'

    def getFanDetailsFromDB(self, fan_id:int):
        self.cur.execute(f'''
        select name, email, phone from fans where fan_id = {fan_id}
        ''')
        data = self.cur.fetchall()
        out_str = f'Fan id = {fan_id}\nName: {data[0][0]}\nEmail: {data[0][1]}\nPhone: {data[0][2]}'
        print(out_str)
        return out_str

    def getFanPurchaseHistoryFromDB(self, fan_id:int):
        query = '''
            select * from purchase_log where fan_id = ?
        '''
        self.cur.execute(query, (fan_id, ))
        data = self.cur.fetchall()
        out_str = 'ID\tF_ID\tTIC_ID\tMAT_ID\tPURCHASE_DATE\t\tQUAN\tTOTAL\tPAYMENT_METHOD\n'
        for row in data:
            out_str += '\t'.join(map(str, row))
            out_str += '\n'
        print(out_str)
        return out_str

    def processRefundInDB(self, ticket_id:int):
        query = '''
            update purchase_log
            set total_amount = - total_amount
            where ticket_id = ?
        '''
        self.cur.execute(query, (ticket_id, ))
        query0 = '''
            update tickets
            set status = 1
            where id = ?
        '''
        self.cur.execute(query0, (ticket_id, ))
        query1 = '''
            update purchase_log
            set PURCHASE_DATE = ?
            where ticket_id = ?
        '''
        self.cur.execute(query1, (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ticket_id, ))
        self.con.commit()
        return f'Refund successfull against ticket_id = {ticket_id}'

    def getStadiumDetailsFromDB(self, match_id:int):
        query = '''
        SELECT stadiums.stadium_id, stadiums.name, stadiums.capacity
        FROM matches
        JOIN stadiums ON matches.stadium_id = stadiums.stadium_id
        WHERE matches.match_id = ?
        '''
        self.cur.execute(query, (match_id,))
        result = self.cur.fetchone()
        out_str = f'MATCH_ID = {match_id}\nStadium Nmae: {result[1]}\nStadium Capacity: {result[2]}'
        print(out_str)
        return out_str

    def getStadiumCapacityFromDB(self, stadium_id:int):
        query = '''
        select capacity from stadiums where stadium_id = ?
        '''
        self.cur.execute(query, (stadium_id,))
        result = self.cur.fetchone()[0]
        out_str = f'Stadium Capacity for Stadium ID = {stadium_id} is:\t{result}'
        print(out_str)
        return out_str

def main():
    filename = "database.db"
    layer = DBManager(filename)
    return layer
#     # layer.getAvailableTicketsFromDB(5)
#     # layer.checkTicketValidityInDB(2)
#     # layer.getMatchDetailsFromDB(1)
#     # layer.getMatchScheduleFromDB()
#     # # layer.registerFanInDB("Abdullah", "abd@gmail.com", "03334568527")
#     return layer.getFanDetailsFromDB(1)
#     # layer.getStadiumDetailsFromDB(20)
#     # layer.getStadiumCapacityFromDB(15)
#     # # layer.buyTicketInDB(1)
#     # layer.getFanPurchaseHistoryFromDB(1)
#     # layer.processRefundInDB(1)
# if __name__ == "__main__":
#     main()
