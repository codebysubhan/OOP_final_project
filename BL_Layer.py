class TicketManager:
    #__init__ accesses Integration layer
    def __init__(self, integration_layer):
        self.integration_layer = integration_layer()

    def buyTicket(self, fan, match, seat):
        self.integration_layer.buyTicket(fan, match, seat)

    def viewAvailableTickets(self, match):
        self.integration_layer.viewAvailableTickets(match)

    def checkTicketValidity(self, ticket):
        return self.integration_layer.checkTicketValidity(ticket)

class MatchManager:
    #__init__ accesses Integration layer
    def __init__(self, integration_layer):
        self.integration_layer = integration_layer()

    def getMatchDetails(self, match_id):
        return self.integration_layer.getMatchDetails(match_id)

    def getMatchSchedule(self):
        return self.integration_layer.getMatchSchedule()

class FanManager:
    #__init__ accesses Integration layer
    def __init__(self, integration_layer):
        self.integration_layer = integration_layer
    def registerFan(self, name, email, phone):
        return self.integration_layer.registerFan(name, email, phone)

    def getFanDetails(self, fan_id):
        return self.integration_layer.getFanDetails(fan_id)

    def purchaseHistory(self, fan_id):
        return self.integration_layer.purchaseHistory(fan_id)
    
class RefundManager:
    #__init__ accesses Integration layer
    def __init__(self, integration_layer):
        self.integration_layer = integration_layer

    def processRefund(self, ticket_id):
        return self.integration_layer.processRefund(ticket_id)

class StadiumManager:
    #__init__ accesses Integration layer
    def __inint__(self , integration_layer):
        self.integration_layer = integration_layer()

    def getStadiumDetails(self, match):
        return self.integration_layer.getStadiumDetails(match)

    def getStadiumCapacity(self, stadium):
        return self.integration_layer.getStadiumCapacity(stadium)

class TransactionManager:
    #__init__ accesses Integration layer
    def __inint__(self , integration_layer):
        self.integration_layer = integration_layer()

    def processPayment(self, ticket, payment_info):
        self.integration_layer.processPayment(ticket, payment_info)