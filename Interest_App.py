from tkinter import *
from csv import DictWriter



import os
window = Tk()
window.title("Interest.APP")
window.geometry('1300x650')
window.configure()

################################################
## ACCOUNT CALCULATION

### DEFININING FUNCTION ####

###CALACULATION SECTION

def monthlyint(p,t):
     interest = (p*t*8)/36500
     return interest
def action():

    b1 = e1.get()
    b2 = e2.get()
    b3 = e3.get()
    b4 = e4.get()
    b5 = e5.get()
    b6 = e6.get()
    b7 = e7.get()
    b8 = e8.get()
    b9 = e9.get()
    b10 = e10.get()
    b11 = e11.get()
    b12 = e12.get()
    acc = account_no.get()
    balance1 = be10.get()
    rate = be11.get()
    balance2 = q1.get()
    balance3 = q2.get()
    balance4 = q3.get()
    times1 = t1.get()
    times2 = t2.get()
    times3 = t3.get()
    rates= rate2.get()









    interest1 = monthlyint(int(b1),360)
    interest2 = monthlyint(int(b2),330)
    interest3 = monthlyint(int(b3),300)
    interest4 = monthlyint(int(b4),270)
    interest5 = monthlyint(int(b5),240)
    interest6 = monthlyint(int(b6),210)
    interest7 = monthlyint(int(b7),180)
    interest8 = monthlyint(int(b8),150)
    interest9 = monthlyint(int(b9),120)
    interest10 = monthlyint(int(b10),90)
    interest11 = monthlyint(int(b11),60)
    interest12 = monthlyint(int(b12),30)
    TotalMonthlyInterest = interest1 + interest2 + interest3 + interest4 + interest5 + interest6+ interest7 + interest8 + interest9 + interest10 + interest11 + interest12
    saving = int(b1)+int(b2)+int(b3)+int(b4)+int(b5)+int(b6)+int(b7)+int(b8)+int(b9)+int(b10)+int(b11)+int(b12)


    if balance1 != "0":
        balance_interest = (int(balance1)*1*int(rate))/100
        total_got_interest = TotalMonthlyInterest+ balance_interest
        tax= (total_got_interest*5)/100
        total_getting_interest = total_got_interest-tax
        total_balance = int(balance1) + saving + int(total_getting_interest)
        obl16 = Label(frame6, text=saving, font=("times", 14, "bold", "italic"), bd=10).grid(column=1, row=0)
        obl16 = Label(frame6, text="वर्षमा कुल बचत:", font=("times", 14, "bold", "italic"), bd=10).grid(column=0, row=0)
        obl20 = Label(frame6, text="पाउन पर्ने व्याज:", font=("times", 14, "bold", "italic"), bd=10).grid(column=0,
                                                                                                          row=4)
        obl20 = Label(frame6, text=int(total_got_interest), font=("times", 14, "bold", "italic"), bd=10).grid(column=1,
                                                                                                              row=4)

        obl21 = Label(frame6, text="घटाइएको कर:", font=("times", 14, "bold", "italic"), bd=10).grid(column=0, row=5)
        obl21 = Label(frame6, text=int(tax), font=("times", 14, "bold", "italic"), bd=10).grid(column=1, row=5)
        obl22 = Label(frame6, text="पायको कुल ब्याज:", font=("times", 14, "bold", "italic"), bd=10).grid(column=0,
                                                                                                         row=6)
        obl22 = Label(frame6, text=int(total_getting_interest), font=("times", 14, "bold", "italic"), bd=10).grid(
            column=1, row=6)
        obl22 = Label(frame6, text="खातामा कुल ब्लान्स:", font=("times", 14, "bold", "italic"), bd=10).grid(column=0,
                                                                                                            row=7)
        obl22 = Label(frame6, text=int(total_balance), font=("times", 14, "bold", "italic"), bd=10).grid(column=1,
                                                                                                         row=7)


    else:
        list=[int(balance2), int(balance3), int(balance4)]
        interestofbalance= (int(balance2)*int(times1)*int(rates))/1200
        interestofbalance1 = (int(balance3)*int(times2)*int(rates))/1200
        interestofbalance2 = (int(balance4)*int(times3)*int(rates))/1200
        total_int_from_it = interestofbalance + interestofbalance1 + interestofbalance2
        total_got_interest = TotalMonthlyInterest + total_int_from_it
        tax = (total_got_interest * 5) / 100
        total_getting_interest = total_got_interest - tax
        if balance4 != "0":
            balance5 = int(balance4)
            total_balance = int(balance5) + saving + int(total_getting_interest)
        else:
            total_balance = int(balance3) + saving + int(total_getting_interest)

        obl16 = Label(frame6, text=saving, font=("times", 14, "bold", "italic"), bd=10).grid(column=1, row=0)
        obl16 = Label(frame6, text="वर्षमा कुल बचत:", font=("times", 14, "bold", "italic"), bd=10).grid(column=0, row=0)
        obl20 = Label(frame6, text="पाउन पर्ने व्याज:", font=("times", 14, "bold", "italic"), bd=10).grid(column=0,
                                                                                                          row=4)
        obl20 = Label(frame6, text=int(total_got_interest), font=("times", 14, "bold", "italic"), bd=10).grid(column=1, row=4)

        obl21 = Label(frame6, text="घटाइएको कर:", font=("times", 14, "bold", "italic"), bd=10).grid(column=0, row=5)
        obl21 = Label(frame6, text=int(tax), font=("times", 14, "bold", "italic"), bd=10).grid(column=1, row=5)
        obl22 = Label(frame6, text="पायको कुल ब्याज:", font=("times", 14, "bold", "italic"), bd=10).grid(column=0,
                                                                                                         row=6)
        obl22 = Label(frame6, text=int(total_getting_interest), font=("times", 14, "bold", "italic"), bd=10).grid(column=1, row=6)
        obl22 = Label(frame6, text="खातामा कुल ब्लान्स:", font=("times", 14, "bold", "italic"), bd=10).grid(column=0,
                                                                                                            row=7)
        obl22 = Label(frame6, text=int(total_balance), font=("times", 14, "bold", "italic"), bd=10).grid(column=1, row=7)

        # write to csv file code here
    with open('newfile.csv', 'a', newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['ACC_NO', 'Saving', 'pauna_parne_interest', 'Payako_interest', 'Tax', 'Balance'])
        if os.stat('newfile.csv').st_size == 0:  # if file is not empty than header write else not
            dict_writer.writeheader()
            dict_writer.writerow({
                'ACC_NO': acc,
                'Saving': saving,
                'pauna_parne_interest': int(total_got_interest),
                'Payako_interest': int(total_getting_interest),
                'Tax': int(tax),
                'Balance': int(total_balance),

            })


# INFORMATION REGARDING COMPANY

title = Label(window, text='हातेमालो बचत तथा ऋण सहकारी सस्था लि.', font=("himalaya", 16, "bold"), fg="black",bg='#D1F5FF', anchor=W,
           justify=LEFT, ).place(x=500, y=9)
address = Label(window, text='ग.न.पा - ७ ,बागलुङ्ग.', font=("himalaya", 12, "bold"), fg="black", anchor=W,bg='#D1F5FF', justify=CENTER,
           bd=10).place(x=600, y=38)
Account = Label(window, text='ACCOUNT NO:', font=("himalaya", 10, "bold"),bg='#79BAEC',fg="black", anchor=W, justify=CENTER,
           bd=10,).place(x=500, y=100)
account_no= Entry(window, bd=5,)
account_no.place(x=625, y=104)
account_no.focus()

# MONTHLY INFORMATION OF ACCOUNT HOLDER
frame1 = LabelFrame(window, text="महिनाको हिसाबले वर्षको बचत प्रविष्ट गर्नुहोस्", font=("times", 14, "bold"), padx=10,pady=10, bd=5)
frame1.place(x=30, y=160)

# label section
l3 = Label(frame1, text="श्रावणको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0, row=3)
l4 = Label(frame1, text="भाद्रको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0, row=4)
l5 = Label(frame1, text="आश्विनको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0, row=5)
l6 = Label(frame1, text="कार्तिकको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0, row=6)
l7 = Label(frame1, text="मंसिरको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0, row=7)
l8 = Label(frame1, text="पौषको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0, row=8)
l9 = Label(frame1, text="माघको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0,row=9)
l10 = Label(frame1, text="फाल्गुणको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0, row=10)
l11 = Label(frame1, text="चैत्रको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0, row=11)
l12 = Label(frame1, text="बैशाखको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0, row=12)
l13 = Label(frame1, text="जेष्ठको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0, row=13)
l14 = Label(frame1, text="आषाढको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0, row=14)

# entery sectionमंसिर पौष  माघ  फाल्गुण चैत्र बैशाख

e1 = Entry(frame1, bd=5,)

e1.grid(column=1, row=3)
e2 = Entry(frame1, bd=5)
e2.grid(column=1, row=4)
e3 = Entry(frame1, bd=5)
e3.grid(column=1, row=5)
e4 = Entry(frame1, bd=5)
e4.grid(column=1, row=6)
e5 = Entry(frame1, bd=5)
e5.grid(column=1, row=7)
e6 = Entry(frame1, bd=5)
e6.grid(column=1, row=8)
e7 = Entry(frame1, bd=5)
e7.grid(column=1, row=9)
e8 = Entry(frame1, bd=5)
e8.grid(column=1, row=10)
e9 = Entry(frame1, bd=5)
e9.grid(column=1, row=11)
e10 = Entry(frame1, bd=5)
e10.grid(column=1, row=12)
e11 = Entry(frame1, bd=5)
e11.grid(column=1, row=13)
e12 = Entry(frame1, bd=5)
e12.grid(column=1, row=14)



#INFROMATION REGARDING BALANCE RETURN
#Balance return Query Section
frame4 = LabelFrame(window, text="Balance Return", font=("times", 14, "bold"), padx=10,pady=10, bd=5)
frame4.place(x=500, y=380)
lable1 = Label(frame4, text="First Balance: ").grid(column=1, row=1)
time= Label(frame4, text="Time: ").grid(column=1, row=2)
q1 = Entry(frame4, bd=2, )
q1.insert(0,"0")
q1.grid(column=2, row=1)
t1 = Entry(frame4, bd=2,)
t1.insert(0,"0")
t1.grid(column=2, row=2)
lable2 = Label(frame4, text="second Balance: ").grid(column=1, row=3)
time2= Label(frame4, text="Time: ").grid(column=1, row=4)
q2 = Entry(frame4, bd=2, )
q2.insert(0,"0")
q2.grid(column=2, row=3)
t2 = Entry(frame4, bd=2, )
t2.insert(0,"0")
t2.grid(column=2, row=4)
lable3 = Label(frame4, text="Third Balance: ").grid(column=1, row=5)
time3= Label(frame4, text="Time: ").grid(column=1, row=6)
q3 = Entry(frame4, bd=2, )
q3.insert(0,"0")
q3.grid(column=2, row=5)
t3 = Entry(frame4, bd=2, )
t3.insert(0,"0")
t3.grid(column=2, row=6)
rate2= Label(frame4, text="ब्याजदर :",font=("times", 10, "bold")).grid(column=1, row=7)
rate2 = Entry(frame4, bd=2, )
rate2.insert(0,"0")
rate2.grid(column=2, row=7)
btn = Button(frame4, text="प्रविष्ट गर्नुहोस्", bd=5, command=action).grid(column=2, row=17)


# INFORMATION FOR NO BALANCE RETURN
#If User Select no Option
frame3 = LabelFrame(window, text="Balance Section", font=("times", 14, "bold"), padx=10,pady=10, bd=5)
frame3.place(x=500, y=180)


bl14 = Label(frame3, text="खाताको कुल बचत:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0, row=14)
bl15 = Label(frame3, text="ब्याजदर :", font=("times", 10, "bold", "italic"), bd=10).grid(column=0, row=15)

be10 = Entry(frame3, bd=5)
be10.insert(0,"0")
be10.grid(column=1, row=14)
be11 = Entry(frame3, bd=5)
be11.insert(0,"0")
be11.grid(column=1, row=15)

btn = Button(frame3, text="प्रविष्ट गर्नुहोस्", bd=5, command=action).grid(column=1, row=17)

#INFORMATION FOR OUTPUT SECTION
#output section

def clear():

    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    be10.delete(0, END)
    be11.delete(0, END)
    q1.delete(0, END)
    q2.delete(0, END)
    q3.delete(0, END)
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    rate2.delete(0, END)


    account_no.delete(0,END)

frame6 = LabelFrame(window, text="आउटपुट सेक्सन ", font=("times", 14, "bold"), padx=10, pady=10, bd=1, )
frame6.place(x=900, y=200)
btn1 = Button(frame6, text="NEXT", bd=10, command=clear).grid(column=1, row=17)


window.mainloop()