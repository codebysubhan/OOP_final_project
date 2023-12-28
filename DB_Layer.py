class DBManager:
    def __init__(self, mycur):
        self.cur = mycur  # Initialize your database connection

    def buyTicketInDB(self, fan, match, seat):
        # Logic to perform ticket purchase operation in the database
        self.cur.execute("")

    def getAvailableTicketsFromDB(self, match):
        # Logic to retrieve available tickets for a match from the database
        pass

    def checkTicketValidityInDB(self, ticket):
        # Logic to check ticket validity in the database
        pass

    def getMatchDetailsFromDB(self, match_id):
        # Logic to retrieve match details based on match_id
        pass

    def getMatchScheduleFromDB(self):
        # Logic to retrieve match schedule from the database
        pass

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




# initializing database

def main():
    import sqlite3 as db
    con = db.connect('database.db')
    cur = con.cursor()

    # one time tasks
    cur.execute('CREATE table tickets ()')

    con.commit()
    cur.close()
    con.close()



if __name__ == "__main__":
    main()