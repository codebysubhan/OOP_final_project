import sqlite3 as sql_db
import dbpopulate
import random
class DBManager:
    def __init__(self, filename:str, con=None, cur=None):
        if con is None:
            con = sql_db.connect(filename)
        if cur is None:
            cur = con.cursor()
        self.con = con
        self.cur = cur
        print('DBManager Initialized!!!')

    def buyTicketInDB(self, fan, match, seat):
        # Logic to perform ticket purchase operation in the database
        self.cur.execute("")

    def getAvailableTicketsFromDB(self, match:int):
        # Logic to retrieve available tickets for a match from the database
        self.cur.execute(f'''
        select id from tickets where match = {match} and status = 1
        ''')
        tickets = self.cur.fetchall()
        print('Total available tickets are: ', len(tickets))
        return tickets

    def checkTicketValidityInDB(self, ticket_id:int):
        self.cur.execute(f'''
        select status from tickets where ID = {ticket_id}
        ''')
        data = self.cur.fetchall()
        try:
            if data[0][0] == 1:
                print('Congratulations! ticket is valid!', data)
            else:
                print(': ticket is not valid!')
        except:
            print('An error occurred!')

    def getMatchDetailsFromDB(self, match_id:int):
        self.cur.execute(f'''
        select match_id, schedule from matches where match_id = {match_id}
        ''')
        data = self.cur.fetchone()
        print(data)
        id = data[0]
        timeofmatch = dbpopulate.datetime_converter(data[1])
        print(f'Details for the match with id = {id} are below:\nSchedule\t---\t{timeofmatch}')
        return data

    def getMatchScheduleFromDB(self):
        self.cur.execute('''
        select match_id, schedule from matches
        ''')
        data = self.cur.fetchall()
        # print(data)
        for row in data:
            id = row[0]
            timeofmatch = dbpopulate.datetime_converter(row[1])
            print(f'Match id = {id}\tSchedule = {timeofmatch}')

    def create_new_fan_id(self):
        self.cur.execute('''
        select fan_id from fans
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
        print('Fan added success!!!')

    def getFanDetailsFromDB(self, fan_id:int):
        self.cur.execute(f'''
        select name, email, phone from fans where fan_id = {fan_id}
        ''')
        data = self.cur.fetchall()
        out_str = f'Fan id = {fan_id}\nName: {data[0][0]}\nEmail: {data[0][1]}\nPhone: {data[0][2]}'
        print(out_str)
        return data[0]

    def getFanPurchaseHistoryFromDB(self, fan_id):
        # Logic to retrieve fan's purchase history from the database
        pass

    def processRefundInDB(self, ticket_id):
        # Logic to process ticket refund in the database
        pass

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

    def getStadiumCapacityFromDB(self, stadium_id:int):
        query = '''
        select capacity from stadiums where stadium_id = ?
        '''
        self.cur.execute(query, (stadium_id,))
        result = self.cur.fetchone()[0]
        out_str = f'Stadium Capacity for Stadium ID = {stadium_id} is:\t{result}'
        print(out_str)
        return result

def main():
    filename = "database.db"
    layer = DBManager(filename)
    layer.getAvailableTicketsFromDB(5)
    layer.checkTicketValidityInDB(2)
    layer.getMatchDetailsFromDB(1)
    layer.getMatchScheduleFromDB()
    # layer.registerFanInDB("Abdullah", "abd@gmail.com", "03334568527")
    layer.getFanDetailsFromDB(1)
    layer.getStadiumDetailsFromDB(20)
    layer.getStadiumCapacityFromDB(15)
if __name__ == "__main__":
    main()
