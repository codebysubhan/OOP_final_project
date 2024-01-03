from tkinter import *
from tkinter import ttk
import db_layer


root = Tk()
root.title("Tickets")

# main topic
topic = Label(root, text="PSL Ticket Management System", font=('Helvetica', 18))
topic.grid(row=0, column=0, padx=10, sticky=W)











# creating frames

# frame one
f_one = LabelFrame(root, text="FRAME 1", borderwidth=8, padx=5, pady=5, height=100)
f_one.grid(padx=5, pady=5, row=1, column=0, sticky=W+E)

# frame two
f_two = LabelFrame(root, text="SCREEN / FRAME 2", borderwidth=8, padx=5, pady=5, height=100)
f_two.grid(row=1, column=1, sticky=W)

# frame three
f_three = LabelFrame(root, text="FRAME 3" ,borderwidth=8, height=100)
f_three.grid(padx=5, pady=5, row=2, column=0, columnspan=2, sticky=W+E)

# frame four
f_four = LabelFrame(root, text="FRAME 4",borderwidth=8, height=100)
f_four.grid(padx=5, pady=5, row=3, column=0, sticky=W)

# frame five
f_five = LabelFrame(root, text="FRAME 5", borderwidth=8, height=100)
f_five.grid(padx=5, pady=5, row=3, column=1, sticky=W+E)




# frame = screen / frame 2
screen_frame = Text(f_two, height=10, width=65)
screen_frame.grid(row=0, column=0)
screen_frame.insert("1.0", "No text to display at the moment...")






def buy_ticket():
    out_str = ''
    inst = db_layer.main()
    if t0.get() == '':
        out_str = 'Please enter input in data fields before proceeding!!!'
    else:
        inst.buyTicketInDB(int(t0.get()))
        out_str = "Ticket Buy Success!!!"
    t0.delete(0, END)
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)

def get_available_tickets():
    out_str = ''
    inst = db_layer.main()
    if t_more.get() == '':
        out_str = 'Please enter input in data fields before proceeding!!!'
    else:
        out_str = inst.getAvailableTicketsFromDB(int(t_more.get()))
    t_more.delete(0, END)
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)



# frame = frame 1
l0 = Label(f_one, text="Buy Ticket", font=("sans-serif", 12))
l0.grid(row=0, column=0, sticky=W)
# button 0
b0 = Button(f_one, text="Proceed", padx=2, pady=4, command=buy_ticket)
b0.grid(row=0, column=1, sticky=E)
# Create a horizontal separator
s0 = ttk.Separator(f_one, orient='horizontal')
s0.grid(row=2, column=0, sticky=E+W, columnspan=2, padx=10, pady=10)
# text field 0
t0 = Entry(f_one, width=10, borderwidth=2)
t0.grid(row=1, column=1, sticky=E)
# sub label0
l0_0 = Label(f_one, text="Enter Fan ID: ", font=("sans-serif", 12))
l0_0.grid(row=1, column=0, sticky=W)
# ----------------------------
l1 = Label(f_one, text="Get Available Tickets", font=("sans-serif", 12))
l1.grid(row=3, column=0, sticky=W)
# sub label0
l1_0 = Label(f_one, text="Enter Match ID: ", font=("sans-serif", 12))
l1_0.grid(row=4, column=0, sticky=W)
# text field more
t_more = Entry(f_one, width=10, borderwidth=2)
t_more.grid(row=4, column=1, sticky=E)
# button 1
b1 = Button(f_one, text="Proceed", padx=2, pady=4, command=get_available_tickets)
b1.grid(row=5, column=0, sticky=W)






def reg_new_fan():
    out_str = ''
    inst = db_layer.main()
    chk = [t1.get(), t2.get(), t3.get()]
    for i in chk:
        if i == '':
            out_str = 'Please provide input in data fields!!!\n'
            break
    if out_str == '':
        out_str = inst.registerFanInDB(t1.get(), t2.get(), t3.get())
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)







# frame = frame 3
l2 = Label(f_three, text="Register New Fan", font=("sans-serif", 12))
l2.grid(row=0, column=0, sticky=W, columnspan=2)
# button 2
b2 = Button(f_three, text="Proceed", padx=2, pady=4, command=reg_new_fan)
b2.grid(row=1, column=6, sticky=E)
# sub label
l2_0 = Label(f_three, text="Name: ", font=("sans-serif", 12))
l2_0.grid(row=1, column=0, sticky=W)
# text field 1
t1 = Entry(f_three, width=10, borderwidth=2)
t1.grid(row=1, column=1, sticky=W)
# sub label
l2_1 = Label(f_three, text="Email: ", font=("sans-serif", 12))
l2_1.grid(row=1, column=2, sticky=W)
# text field 2
t2 = Entry(f_three, width=10, borderwidth=2)
t2.grid(row=1, column=3, sticky=W)
# sub label
l2_2 = Label(f_three, text="Phone: ", font=("sans-serif", 12))
l2_2.grid(row=1, column=4, sticky=W)
# text field 3
t3 = Entry(f_three, width=10, borderwidth=2)
t3.grid(row=1, column=5, sticky=W)









def ticket_valid():
    out_str = ''
    inst = db_layer.main()
    if t4.get() == '':
        out_str = 'Please provide input in data fields!!!'
    else:
        out_str = inst.checkTicketValidityInDB(int(t4.get()))
    t4.delete(0, END)
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)

def get_fan_details():
    out_str = ''
    inst = db_layer.main()
    if t5.get() == '':
        out_str = 'Please provide input in data fields!!!'
    else:
        out_str = inst.getFanDetailsFromDB(int(t5.get()))
    t5.delete(0, END)
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)

def get_match_details():
    out_str = ''
    inst = db_layer.main()
    if t6.get() == '':
        out_str = 'Please provide input in data fields!!!'
    else:
        out_str = inst.getMatchDetailsFromDB(int(t6.get()))
    t6.delete(0, END)
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)

def get_match_schedules():
    inst = db_layer.main()
    out_str = inst.getMatchScheduleFromDB()
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)

# frame = frame 4
l3 = Label(f_four, text="Check Ticket Validity", font=("sans-serif", 12))
l3.grid(row=0, column=0, sticky=W, columnspan=2)
# sub label
l3_0 = Label(f_four, text="Enter Ticket ID: ", font=("sans-serif", 12))
l3_0.grid(row=1, column=0, sticky=W)
# text field 4
t4 = Entry(f_four, width=10, borderwidth=2)
t4.grid(row=1, column=1, sticky=W)
# button 3
b3 = Button(f_four, text="Proceed", padx=2, pady=4, command=ticket_valid)
b3.grid(row=2, column=0, sticky=W)
# Create a horizontal separator
s1 = ttk.Separator(f_four, orient='horizontal')
s1.grid(row=3, column=0, sticky=E+W, columnspan=5, padx=10, pady=10)
# ---------------------------
l4 = Label(f_four, text="Get Fan Details", font=("sans-serif", 12))
l4.grid(row=4, column=0, sticky=W, columnspan=2)
# sub label
l4_0 = Label(f_four, text="Enter Fan ID: ", font=("sans-serif", 12))
l4_0.grid(row=5, column=0, sticky=W)
# text field 5
t5 = Entry(f_four, width=10, borderwidth=2)
t5.grid(row=5, column=1, sticky=W)
# button 4
b4 = Button(f_four, text="Proceed", padx=2, pady=4, command=get_fan_details)
b4.grid(row=6, column=0, sticky=W)
# ------------------------- up ----------------------------
l5 = Label(f_four, text="Get Match Details", font=("sans-serif", 12))
l5.grid(row=0, column=3, sticky=W, columnspan=2)
# sub label
l5_0 = Label(f_four, text="Enter Match ID: ", font=("sans-serif", 12))
l5_0.grid(row=1, column=3, sticky=W)
# text field 6
t6 = Entry(f_four, width=10, borderwidth=2)
t6.grid(row=1, column=4, sticky=W)
# button 5
b5 = Button(f_four, text="Proceed", padx=2, pady=4, command=get_match_details)
b5.grid(row=2, column=3, sticky=W)
# Create a vertical separator
s2 = ttk.Separator(f_four, orient='vertical')
s2.grid(row=0, column=2, sticky=N+S,rowspan=7 ,padx=10, pady=10)
# --------------------------
l6 = Label(f_four, text="Get Match Schedules", font=("sans-serif", 12))
l6.grid(row=4, column=3, sticky=W, columnspan=2)
# button 6
b6 = Button(f_four, text="Proceed", padx=2, pady=4, command=get_match_schedules)
b6.grid(row=5, column=3, sticky=W+E)







def get_purchase_hist():
    out_str = ''
    inst = db_layer.main()
    if t7.get() == '':
        out_str = 'Please provide input in data fields!!!'
    else:
        out_str = inst.getFanPurchaseHistoryFromDB(int(t7.get()))
    t7.delete(0, END)
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)

def get_stadium_details():
    out_str = ''
    inst = db_layer.main()
    if t9.get() == '':
        out_str = 'Please provide input in data fields!!!'
    else:
        out_str = inst.getStadiumDetailsFromDB(int(t9.get()))
    t9.delete(0, END)
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)

def get_stadium_capacity():
    out_str = ''
    inst = db_layer.main()
    if t10.get() == '':
        out_str = 'Please provide input in data fields!!!'
    else:
        out_str = inst.getStadiumCapacityFromDB(int(t10.get()))
    t10.delete(0, END)
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)

def refund_process():
    out_str = ''
    inst = db_layer.main()
    if t8.get() == '':
        out_str = 'Please provide input in data fields!!!'
    else:
        out_str = inst.processRefundInDB(int(t8.get()))
    t8.delete(0, END)
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)







# frame = frame 5
l7 = Label(f_five, text="Purchase History", font=("sans-serif", 12))
l7.grid(row=0, column=0, sticky=W, columnspan=2)
# sub label
l7_0 = Label(f_five, text="Enter Fan ID: ", font=("sans-serif", 12))
l7_0.grid(row=1, column=0, sticky=W)
# text field 7
t7 = Entry(f_five, width=10, borderwidth=2)
t7.grid(row=1, column=1, sticky=W)
# button 7
b7 = Button(f_five, text="Proceed", padx=2, pady=4, command=get_purchase_hist)
b7.grid(row=2, column=0, sticky=W)
# Create a horizontal separator
s3 = ttk.Separator(f_five, orient='horizontal')
s3.grid(row=3, column=0, sticky=E+W, columnspan=5, padx=10, pady=10)
# ---------------------------
l8 = Label(f_five, text="Refund Process", font=("sans-serif", 12))
l8.grid(row=4, column=0, sticky=W, columnspan=2)
# sub label
l8_0 = Label(f_five, text="Enter Ticket ID: ", font=("sans-serif", 12))
l8_0.grid(row=5, column=0, sticky=W)
# text field 8
t8 = Entry(f_five, width=10, borderwidth=2)
t8.grid(row=5, column=1, sticky=W)
# button 8
b8 = Button(f_five, text="Proceed", padx=2, pady=4, command=refund_process)
b8.grid(row=6, column=0, sticky=W)
# ------------------------- up ----------------------------
l9 = Label(f_five, text="Stadium Details", font=("sans-serif", 12))
l9.grid(row=0, column=3, sticky=W, columnspan=2)
# sub label
l9_0 = Label(f_five, text="Enter Match ID: ", font=("sans-serif", 12))
l9_0.grid(row=1, column=3, sticky=W)
# text field 9
t9 = Entry(f_five, width=10, borderwidth=2)
t9.grid(row=1, column=4, sticky=W)
# button 9
b9 = Button(f_five, text="Proceed", padx=2, pady=4, command=get_stadium_details)
b9.grid(row=2, column=3, sticky=W)
# Create a vertical separator
s3 = ttk.Separator(f_five, orient='vertical')
s3.grid(row=0, column=2, sticky=N+S,rowspan=7 ,padx=10, pady=10)
# --------------------------
l10 = Label(f_five, text="Get Stadium Capacity", font=("sans-serif", 12))
l10.grid(row=4, column=3, sticky=W, columnspan=2)
# sub label
l10_0 = Label(f_five, text="Enter Stadium ID: ", font=("sans-serif", 12))
l10_0.grid(row=5, column=3, sticky=W)
# text field 10
t10 = Entry(f_five, width=10, borderwidth=2)
t10.grid(row=5, column=4, sticky=W)
# button 10
b10 = Button(f_five, text="Proceed", padx=2, pady=4, command=get_stadium_capacity)
b10.grid(row=6, column=3, sticky=W)












root.geometry("1100x600")
root.mainloop()
