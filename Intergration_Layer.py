class DataIntegration:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def buyTicket(self, fan, match, seat):
        self.db_manager.buyTicketInDB(fan, match, seat)

    def viewAvailableTickets(self, match):
        return self.db_manager.getAvailableTicketsFromDB(match)

    def checkTicketValidity(self, ticket):
        return self.db_manager.checkTicketValidityInDB(ticket)

    def getMatchDetails(self, match_id):
        return self.db_manager.getMatchDetailsFromDB(match_id)

    def getMatchSchedule(self):
        return self.db_manager.getMatchScheduleFromDB()

    def registerFan(self, name, email, phone):
        return self.db_manager.registerFanInDB(name, email, phone)

    def getFanDetails(self, fan_id):
        return self.db_manager.getFanDetailsFromDB(fan_id)

    def purchaseHistory(self, fan_id):
        return self.db_manager.getFanPurchaseHistoryFromDB(fan_id)

    def processRefund(self, ticket_id):
        return self.db_manager.processRefundInDB(ticket_id)

    def getStadiumDetails(self, match):
        return self.db_manager.getStadiumDetailsFromDB(match)

    def getStadiumCapacity(self, stadium):
        return self.db_manager.getStadiumCapacityFromDB(stadium)
