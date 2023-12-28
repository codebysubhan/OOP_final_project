import sqlite3 as sql_db
import dbpopulate
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
                print('Congratulations! ticket is available!', data)
            else:
                print(': ticket is not available! already sold!')
        except:
            print('An error occurred!')

    def getMatchDetailsFromDB(self, match_id):
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

    def registerFanInDB(self, name, email, phone):
        # Logic to register a fan in the database
        pass

    def getFanDetailsFromDB(self, fan_id):
        # Logic to retrieve fan details based on fan_id
        pass

    def getFanPurchaseHistoryFromDB(self, fan_id):
        # Logic to retrieve fan's purchase history from the database
        pass

    def processRefundInDB(self, ticket_id):
        # Logic to process ticket refund in the database
        pass

    def getStadiumDetailsFromDB(self, match):
        # Logic to retrieve stadium details based on match
        pass

    def getStadiumCapacityFromDB(self, stadium):
        # Logic to retrieve stadium capacity based on stadium
        pass


def main():
    filename = "database.db"
    layer = DBManager(filename)
    layer.getAvailableTicketsFromDB(5)
    layer.checkTicketValidityInDB(2)
    layer.getMatchDetailsFromDB(1)
    layer.getMatchScheduleFromDB()

if __name__ == "__main__":
    main()
