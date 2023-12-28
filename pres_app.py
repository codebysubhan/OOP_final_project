import tkinter as tk
from tkinter import messagebox
from db_layer import DBManager
from tkinter import simpledialog
class TicketApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Ticket Management System")

        self.db_manager = DBManager("database.db")

        self.label = tk.Label(master, text="Ticket Management System", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.buy_ticket_button = tk.Button(master, text="Buy Ticket", command=self.buy_ticket)
        self.buy_ticket_button.pack(pady=5)

        self.check_ticket_button = tk.Button(master, text="Check Ticket Validity", command=self.check_ticket_validity)
        self.check_ticket_button.pack(pady=5)

        self.match_details_button = tk.Button(master, text="Get Match Details", command=self.get_match_details)
        self.match_details_button.pack(pady=5)

        self.match_schedule_button = tk.Button(master, text="Get Match Schedule", command=self.get_match_schedule)
        self.match_schedule_button.pack(pady=5)

        self.register_fan_button = tk.Button(master, text="Register Fan", command=self.register_fan)
        self.register_fan_button.pack(pady=5)

        self.fan_details_button = tk.Button(master, text="Get Fan Details", command=self.get_fan_details)
        self.fan_details_button.pack(pady=5)

        self.stadium_details_button = tk.Button(master, text="Get Stadium Details", command=self.get_stadium_details)
        self.stadium_details_button.pack(pady=5)

        self.stadium_capacity_button = tk.Button(master, text="Get Stadium Capacity", command=self.get_stadium_capacity)
        self.stadium_capacity_button.pack(pady=5)

        self.purchase_history_button = tk.Button(master, text="Get Fan Purchase History", command=self.get_fan_purchase_history)
        self.purchase_history_button.pack(pady=5)

        self.refund_button = tk.Button(master, text="Process Refund", command=self.process_refund)
        self.refund_button.pack(pady=5)

    def buy_ticket(self):
        fan_id = self.get_user_input("Enter Fan ID:")
        self.db_manager.buyTicketInDB(int(fan_id))
        messagebox.showinfo("Success", "Ticket purchased successfully!")

    def check_ticket_validity(self):
        ticket_id = self.get_user_input("Enter Ticket ID:")
        self.db_manager.checkTicketValidityInDB(int(ticket_id))

    def get_match_details(self):
        match_id = self.get_user_input("Enter Match ID:")
        self.db_manager.getMatchDetailsFromDB(int(match_id))

    def get_match_schedule(self):
        self.db_manager.getMatchScheduleFromDB()

    def register_fan(self):
        name = self.get_user_input("Enter Fan Name:")
        email = self.get_user_input("Enter Fan Email:")
        phone = self.get_user_input("Enter Fan Phone:")
        self.db_manager.registerFanInDB(name, email, phone)
        messagebox.showinfo("Success", "Fan registered successfully!")

    def get_fan_details(self):
        fan_id = self.get_user_input("Enter Fan ID:")
        self.db_manager.getFanDetailsFromDB(int(fan_id))

    def get_stadium_details(self):
        match_id = self.get_user_input("Enter Match ID:")
        self.db_manager.getStadiumDetailsFromDB(int(match_id))

    def get_stadium_capacity(self):
        stadium_id = self.get_user_input("Enter Stadium ID:")
        self.db_manager.getStadiumCapacityFromDB(int(stadium_id))

    def get_fan_purchase_history(self):
        fan_id = self.get_user_input("Enter Fan ID:")
        self.db_manager.getFanPurchaseHistoryFromDB(int(fan_id))

    def process_refund(self):
        ticket_id = self.get_user_input("Enter Ticket ID for Refund:")
        self.db_manager.processRefundInDB(int(ticket_id))
        messagebox.showinfo("Success", "Refund processed successfully!")

    def get_user_input(self, prompt):
        return simpledialog.askstring("Input", prompt)

def main():
    root = tk.Tk()
    app = TicketApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
