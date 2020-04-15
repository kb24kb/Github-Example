from tkinter import *
from tkinter import messagebox as ms
fixed_user_id = 0
import sqlite3
# noinspection DuplicatedCode

def Main_Menu():

    root = Tk()
    root.title("Stock Management System")
    root.configure(background="sky blue")
    # Centered
    w = 400
    h = 650
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    menu = Menu(root)
    root.config(menu=menu)

    about_usmenu = Menu(menu)
    menu.add_cascade(label='About Us', menu=about_usmenu)
    about_usmenu.add_command(label='About Us', command=abt_us)
    about_usmenu.add_command(label='Contact Us', command=c_u)
    about_usmenu.add_separator()
    about_usmenu.add_command(label='Report an Issue', command=report)
    about_usmenu.add_command(label='Rate Us', command=rate)

    accountmenu = Menu(menu)
    menu.add_cascade(label='Account', menu=accountmenu)
    accountmenu.add_command(label='Profile', command=update_us)
    accountmenu.add_command(label='Change Password', command=cng_password)
    accountmenu.add_command(label='Logout', command=lambda: logout(root))

    Label(root, text='Welcome', bg='sky blue', font=('', 35, "bold"), pady=10).pack(padx=10, pady=10)
    Button(root, text='Portfolio', font=('', 15), pady=10, width=20, bg='light sky blue',
           activebackground='deep sky blue' ,command=Porfolio).pack(padx=10, pady=10)
    Button(root, text='WatchList', font=('', 15), pady=10, width=20, bg='light sky blue',
           activebackground='deep sky blue',command=watchlist).pack(padx=10, pady=10)
    Button(root, text='Buy/Sell', font=('', 15), pady=10, width=20, bg='light sky blue',
           activebackground='deep sky blue',command=Buy_page).pack(padx=10, pady=10)
    Button(root, text='Stock Percentage weight', font=('', 15), pady=10, width=20, bg='light sky blue',
           activebackground='deep sky blue', command=analytics).pack(padx=10, pady=10)
    Button(root, text='Current Stocks Analytics', font=('', 15), pady=10, width=20, bg='light sky blue',
           activebackground='deep sky blue', command=Profit_analytics).pack(padx=10, pady=10)
    Button(root, text='Sold Stocks Analytics', font=('', 15), pady=10, width=20, bg='light sky blue',
           activebackground='deep sky blue', command=S_Profit_analytics).pack(padx=10, pady=10)
    Button(root, text='Exit', font=('', 15), pady=10, width=20, bg='light sky blue', activebackground='deep sky blue',
           command=root.destroy).pack(padx=10, pady=10)

    root.mainloop()

def logout(a):
    a.destroy()
    Login_Page()

def Login_Page():


    with sqlite3.connect('project.db') as db:
        c = db.cursor()

    class main:
        def __init__(self, master):
            self.master = master
            self.username = StringVar()
            self.password = StringVar()
            self.n_name = StringVar()
            self.n_city = StringVar()
            self.n_country = StringVar()
            self.n_email = StringVar()
            self.n_number = IntVar()
            self.n_username = StringVar()
            self.n_password = StringVar()
            self.widgets()

        def login(self):
            global fixed_user_id
            with sqlite3.connect('project.db') as db:
                c = db.cursor()
            find_user = ('SELECT * FROM user_details WHERE user_id = ? and password = ?')
            c.execute(find_user, [(self.username.get()), (self.password.get())])
            result = c.fetchall()
            if result:
                fixed_user_id = int(self.username.get())
                print(fixed_user_id)
                root1.destroy()
                Main_Menu()
            else:
                ms.showerror('Oops!', 'Incorrect credentials')

        def new_user(self):
            balance =1000000
            from random import randint
            with sqlite3.connect('project.db') as db:
                c = db.cursor()
            k = randint(100001,999999)
            find_user = ('SELECT * FROM user_details WHERE user_id = ?')
            c.execute(find_user, [k])
            while(c.fetchall()):
                k = randint(100001,999999)
                find_user = ('SELECT * FROM user_details WHERE user_id = ?')
                c.execute(find_user, [k])
            ms.showinfo('Success!', 'Account Created!\n Your Username is ' + str(k))
            self.log()

            insert = 'INSERT INTO user_details(name,email_id,city,country,phone_no,user_id,password,Balance) VALUES(?,?,?,?,?,?,?,?)'
            c.execute(insert, [(self.n_name.get()), (self.n_email.get()), (self.n_city.get()), (self.n_country.get()),
                               (self.n_number.get()), k, (self.n_password.get()), balance])
            db.commit()

        def log(self):
            self.username.set('')
            self.password.set('')
            self.crf.pack_forget()
            self.head['text'] = 'LOGIN'
            self.logf.pack()

        def cr(self):
            self.n_name.set('')
            self.n_email.set('')
            self.n_city.set('')
            self.n_country.set('')
            self.n_number.set('')
            self.n_username.set('')
            self.n_password.set('')
            self.logf.pack_forget()
            self.head['text'] = 'Create Account'
            self.crf.pack()

        def widgets(self):
            Label(self.master, text='', bg='sky blue', font=('', 7), pady=15, padx=5).pack()
            self.head = Label(self.master, text='LOGIN', bg='sky blue', font=('', 35))
            self.head.pack()
            self.logf = Frame(self.master, bg='sky blue', padx=10, pady=10)

            Label(self.logf, text='Username: ', bg='sky blue', font=('', 20), pady=5, padx=5).grid(sticky=W)
            Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
            Label(self.logf, text='Password: ', bg='sky blue', font=('', 20), pady=5, padx=5).grid(sticky=W)
            Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
            Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
            Button(self.logf, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2, column=1)

            self.logf.pack()

            self.crf = Frame(self.master, bg='sky blue', padx=10, pady=10)

            Label(self.crf, text='Name: ', bg='sky blue', font=('', 20), pady=5, padx=5).grid(sticky=W)
            Entry(self.crf, textvariable=self.n_name, bd=5, font=('', 15)).grid(row=0, column=1)
            Label(self.crf, text='Email: ', bg='sky blue', font=('', 20), pady=5, padx=5).grid(sticky=W)
            Entry(self.crf, textvariable=self.n_email, bd=5, font=('', 15)).grid(row=1, column=1)
            Label(self.crf, text='City: ', bg='sky blue', font=('', 20), pady=5, padx=5).grid(sticky=W)
            Entry(self.crf, textvariable=self.n_city, bd=5, font=('', 15)).grid(row=2, column=1)
            Label(self.crf, text='Country: ', bg='sky blue', font=('', 20), pady=5, padx=5).grid(sticky=W)
            Entry(self.crf, textvariable=self.n_country, bd=5, font=('', 15)).grid(row=3, column=1)
            Label(self.crf, text='Phone no.: ', bg='sky blue', font=('', 20), pady=5, padx=5).grid(sticky=W)
            Entry(self.crf, textvariable=self.n_number, bd=5, font=('', 15)).grid(row=4, column=1)

            Label(self.crf, text='Password: ', bg='sky blue', font=('', 20), pady=5, padx=5).grid(sticky=W)
            Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=5, column=1)
            Button(self.crf, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
            Button(self.crf, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=6,
                                                                                                             column=1)

    root1 = Tk()
    root1.title("Login Form")

    # centered
    w = 450
    h = 500
    ws = root1.winfo_screenwidth()
    hs = root1.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root1.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root1.configure(bg='sky blue')

    main(root1)
    root1.mainloop()

def watchlist():

    from tkinter import ttk

    root = Tk()
    root.title("Company_Details")

    # centered
    w = 750
    h = 500
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.configure(bg='sky blue')

    Label(root, text='Watchlist', bg='sky blue', font=('', 35, "bold"), pady=10).pack(padx=10, pady=10)

    watchlist_view = ttk.Treeview(root)
    watchlist_view['columns'] = (
    "Company_ID", "Name", "Highest Point", "Lowest Point", "Current Market Price", "% Change")
    watchlist_view.pack(pady=5)

    global c_name
    c_name = StringVar(root)

    def display():
        global fixed_user_id
        i = 0
        db = sqlite3.connect('project.db')
        cursor = db.execute('select * from watchlist WHERE user_id = ?', [fixed_user_id])
        watchlist_view.delete(*watchlist_view.get_children())
        for row in cursor:
            # row[0] --> user_id
            watchlist_view.insert('', 'end', text="" + str(i), values=(row[1], row[2], row[3], row[4], row[5], row[6]))
            i = i + 1
        db.commit()
        db.close()

    def Watchlist_Search():
        global fixed_user_id
        global c_name
        i = 0
        db = sqlite3.connect('project.db')
        print(c_name.get())
        cursor = db.execute('select * from company_details where name = ?', [c_name.get()])
        watchlist_view.delete(*watchlist_view.get_children())
        for row in cursor:
            watchlist_view.insert('', 'end', text="" + str(i), values=(row[0], row[1], row[4], row[5], row[2], row[6]))
            i = i + 1
        db.commit()
        db.close()

    watchlist_view.heading("#0", text="Index", anchor="w")
    watchlist_view.column("#0", anchor="center", width=40, stretch=NO)
    watchlist_view.heading("Company_ID", text="Company ID", anchor="w")
    watchlist_view.column("Company_ID", anchor="center", width=80)
    watchlist_view.heading("Name", text="Name", anchor="center")
    watchlist_view.column("Name", anchor="center", width=120)
    watchlist_view.heading("Highest Point", text="Highest Point", anchor="w")
    watchlist_view.column("Highest Point", anchor="center", width=100)
    watchlist_view.heading("Lowest Point", text="Lowest Point", anchor="w")
    watchlist_view.column("Lowest Point", anchor="center", width=100)
    watchlist_view.heading("Current Market Price", text="Current Market Price", anchor="w")
    watchlist_view.column("Current Market Price", anchor="center", width=130)
    watchlist_view.heading("% Change", text="Percent Change", anchor="w")
    watchlist_view.column("% Change", anchor="center", width=100)

    Label(root, text='Company Name', font=('', 15), bg='sky blue', pady=5, padx=20).pack(pady=5)
    Entry(root, textvariable=c_name, font=('', 15)).pack(pady=5)
    Button(root, text='Search', font=('', 15), pady=5, width=20, bg='light sky blue',
           activebackground='deep sky blue', command=Watchlist_Search).pack(side=LEFT, padx=10, pady=10)
    Button(root, text='Display', font=('', 15), pady=5, width=20, bg='light sky blue',
           activebackground='deep sky blue', command=display).pack(side=LEFT, padx=10, pady=10)
    Button(root, text='Main Menu', font=('', 15), pady=5, width=20, bg='light sky blue',
           activebackground='deep sky blue', command=root.destroy).pack(side=LEFT, padx=10, pady=10)
    root.mainloop()

def Buy_page():
    from tkinter import ttk

    import uuid

    root = Tk()
    w = 950
    h = 500
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.configure(bg='sky blue')

    root.title("Stock Management System")
    tabcontrol = ttk.Notebook(root)
    Stock = ttk.Frame(tabcontrol)
    labelFrame = ttk.LabelFrame(Stock, text="Buy Stock")
    labelFrame.grid(column=0, row=0, padx=8, pady=4, sticky="N")

    tabcontrol1 = ttk.Notebook(root)
    Stock1 = ttk.Frame(tabcontrol1)

    labelFrame1 = ttk.LabelFrame(Stock, text="Company List", borderwidth=3)
    labelFrame1.grid(row=0, column=1, padx=8, pady=4, sticky="N")

    Stock1.pack()
    i = 0

    def Get_data():
        global i
        i = 0
        tree.delete(*tree.get_children())
        db1 = sqlite3.connect('project.db')
        cursor = db1.execute('select * from company_details')
        for row in cursor:
            tree.insert('', 'end', text="" + str(i), values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            i = i + 1
        db1.commit()
        db1.close()

    def Insert_data():
        from random import randint
        global fixed_user_id
        companyNameEntry.configure(state=NORMAL)
        stockPriceEntry.configure(state=NORMAL)
        db1 = sqlite3.connect('project.db')
        c = db1.cursor()
        c.execute('select Balance from user_details where user_id = ? ', [fixed_user_id])
        balance_value = c.fetchone()
        Balance = float(''.join(map(str, balance_value)))
        c.execute('select quantity from company_details where company_id = ? ', [int(COMPANY_ID_VALUE.get())])
        z = c.fetchone()
        qty = int(''.join(map(str, z)))
        a = float(COMPANY_PRICE_VALUE.get())
        b = float(COMPANY_QUANTITY_VALUE.get())
        req_balance = a*b
        if qty >= int(COMPANY_QUANTITY_VALUE.get()):
            if Balance >= req_balance:
                Balance = Balance - req_balance
                transaction_id = str(uuid.uuid4())[0:8]
                c.execute(
                    'insert into buy_history(user_id, transaction_id, company_id, company_name, buy_price, quantity) values (?,?,?,?,?,?)',
                    [int(fixed_user_id), transaction_id, int(COMPANY_ID_VALUE.get()), COMPANY_NAME_VALUE.get(),
                     float(COMPANY_PRICE_VALUE.get()), int(COMPANY_QUANTITY_VALUE.get())])
                c.execute('update user_details set Balance = ? where user_id = ?',[Balance,fixed_user_id])
                c.execute('update company_details set quantity = ? where company_id = ?', [qty-int(COMPANY_QUANTITY_VALUE.get()), int(COMPANY_ID_VALUE.get())])
                random_points = randint(20, 200)
                random_profit = random_points * b
                c.execute('select company_id,buy_price,quantity,Profit from current_stocks where user_id = ? and company_id = ?',[fixed_user_id,int(COMPANY_ID_VALUE.get())])
                results = c.fetchall()
                if results:
                    print(results)
                    row = results
                    print(row[0][1])
                    d = float(results[0][1])
                    e = float(results[0][2])
                    f = float(results[0][3])
                    buy_price = ((a*b)+(d*float(e)))/(b+e)
                    print(buy_price)
                    c.execute('update current_stocks set quantity = ?,buy_price = ?,Profit = ? where company_id = ? and user_id = ?',[int(b+int(e)), buy_price, (f+float(random_profit)), int(COMPANY_ID_VALUE.get()), int(fixed_user_id)])
                    print("Updated Current stocks")
                else:
                    c.execute('insert into current_stocks(user_id, company_id, company_name, buy_price, CMP, quantity,Profit) values (?,?,?,?,?,?,?)', [int(fixed_user_id), int(COMPANY_ID_VALUE.get()), COMPANY_NAME_VALUE.get(), float(COMPANY_PRICE_VALUE.get()), float(COMPANY_PRICE_VALUE.get()),int(b), float(random_profit)])
                    print("Inserted into Current stock")
                print("Transaction Successful")

                companyIdEntry.delete(0, "end")
                companyNameEntry.delete(0, "end")
                stockPriceEntry.delete(0, "end")
                stockQuantityEntry.delete(0, "end")
                companyNameEntry.configure(state=DISABLED)
                stockPriceEntry.configure(state=DISABLED)
                stockQuantityEntry.configure(state=DISABLED)
            else:
                ms.showerror('Oops!', 'Your account balance is not sufficient')
        else:
            ms.showerror('Oops!', 'Number of stocks to be bought is more than the stocks allocated by the company in the market')
        db1.commit()
        db1.close()

    def Search_data():
        companyNameEntry.configure(state=NORMAL)
        stockPriceEntry.configure(state=NORMAL)
        stockPriceEntry.delete(0, "end")
        companyNameEntry.delete(0,"end")
        print(COMPANY_ID_VALUE.get())
        db1 = sqlite3.connect('project.db')
        c = db1.cursor()
        c.execute("select * from company_details where company_id = ? ",[int(COMPANY_ID_VALUE.get())])
        records = c.fetchall()
        print(records)
        if records:
            for record in records:
                companyNameEntry.insert(0, record[1])
                stockPriceEntry.insert(0, record[2])
            companyNameEntry.configure(state=DISABLED)
            stockPriceEntry.configure(state=DISABLED)
            stockQuantityEntry.configure(state=NORMAL)
        else:
            ms.showerror('Oops!', 'Company_ID Not Found.')
        db1.commit()
        db1.close()

    tree = ttk.Treeview(labelFrame1, columns=('Company_ID','Name','Current Market Price','quantity','Highest Point','Lowest Point','% Change'), height=20)
    tree.place(x=30, y=95)


    tree.heading('#0', text='Index')
    tree.column("#0", anchor="center", width=40, stretch=NO)
    tree.heading("Company_ID", text="Company ID", anchor="w")
    tree.column("Company_ID", anchor="center", width=80)
    tree.heading("Name", text="Name", anchor="center")
    tree.column("Name", anchor="center", width=120)
    tree.heading("quantity", text="quantity", anchor="w")
    tree.column("quantity", anchor="center", width=100)
    tree.heading("Highest Point", text="Highest Point", anchor="w")
    tree.column("Highest Point", anchor="center", width=100)
    tree.heading("Lowest Point", text="Lowest Point", anchor="w")
    tree.column("Lowest Point", anchor="center", width=100)
    tree.heading("Current Market Price", text="Current Market Price", anchor="w")
    tree.column("Current Market Price", anchor="center", width=130)
    tree.heading("% Change", text="Percent Change", anchor="w")
    tree.column("% Change", anchor="center", width=100)
    tree.grid(row=11, columnspan=7, sticky='nsew')
    tabcontrol1.pack(expand=0, fill="both")

    def des():
        root.destroy()

    global COMPANY_QUANTITY_VALUE
    global COMPANY_ID_VALUE
    global COMPANY_PRICE_VALUE
    global COMPANY_NAME_VALUE

    COMPANY_ID_VALUE = StringVar(labelFrame)
    COMPANY_NAME_VALUE = StringVar(labelFrame)
    COMPANY_PRICE_VALUE = StringVar(labelFrame)
    COMPANY_QUANTITY_VALUE = StringVar(labelFrame)

    companyId = ttk.Label(labelFrame, text="Company ID: ")
    companyIdEntry = ttk.Entry(labelFrame, textvariable=COMPANY_ID_VALUE)
    companyIdEntry.grid(column=0, row=1, sticky='W')
    companyName = ttk.Label(labelFrame, text="Company Name : ")
    companyNameEntry = ttk.Entry(labelFrame, textvariable=COMPANY_NAME_VALUE)
    stockPrice = ttk.Label(labelFrame, text="Stock Price : ")
    stockPriceEntry = ttk.Entry(labelFrame, textvariable=COMPANY_PRICE_VALUE)
    stockPriceEntry.grid(column=0, row=5, sticky='W')
    stockQuantity = ttk.Label(labelFrame, text="Quantity : ")
    stockQuantityEntry = ttk.Entry(labelFrame, textvariable=COMPANY_QUANTITY_VALUE)
    stockQuantityEntry.grid(column=0, row=7, sticky="W")
    SearchButton = ttk.Button(labelFrame, width=20, text='Search', command=Search_data)
    ShowButton = ttk.Button(labelFrame, width=20, text='Show', command=Get_data)
    BackButton = ttk.Button(labelFrame, width=20, text='Main Menu', command=des)

    companyNameEntry.configure(state=DISABLED)
    stockPriceEntry.configure(state=DISABLED)
    stockQuantityEntry.configure(state=DISABLED)
    style = ttk.Style()
    style.configure('TButton', background='#3498db')

    InsertButton = ttk.Button(labelFrame, text='Buy', width=20, command=Insert_data)
    InsertButton.grid(column=0, row=11, sticky='W', pady=4)
    BackButton.grid(column=0, row=13, sticky='W', pady=4)
    ShowButton.grid(column=0, row=9, sticky='W', pady=4)
    SearchButton.grid(column=0, row=8, sticky='W', pady=7)
    stockQuantity.grid(column=0, row=6, sticky="W")
    stockPrice.grid(column=0, row=4, sticky='W')
    companyNameEntry.grid(column=0, row=3, sticky='W')
    companyName.grid(column=0, row=2, sticky='W')
    companyId.grid(column=0, row=0, sticky='W')
    tabcontrol.add(Stock, text='Buy Stock')
    tabcontrol.pack(expand=1, fill="both")


    tab2 = ttk.Frame(tabcontrol)
    tabcontrol.add(tab2, text="Sell Stock")
    tabcontrol.pack(expand=1, fill="both")


    def S_Insert_data():
        global fixed_user_id
        s_company_name_Entry.configure(state=NORMAL)
        s_stock_price_Entry.configure(state=NORMAL)
        db1 = sqlite3.connect('project.db')
        c = db1.cursor()
        c.execute('select Balance from user_details where user_id = ? ', [fixed_user_id])
        balance_value = c.fetchone()
        Balance = float(''.join(map(str, balance_value)))
        c.execute('select quantity from current_stocks where company_id = ? and user_id = ?', [int(S_COMPANY_ID.get()), int(fixed_user_id)])
        z = c.fetchone()
        # if z == "None":
        print(z)
        qty = int(''.join(map(str, z)))
        if qty >= int(S_STOCK_QTY.get()):
            c.execute('select CMP from company_details where company_id = ?',[S_COMPANY_ID.get()])
            CMP = c.fetchone()
            price = float(''.join(map(str, CMP)))
            Balance += (price*int(S_STOCK_QTY.get()))
            transaction_id = str(uuid.uuid4())[0:8]

            c.execute(
                'insert into sell_history values (?,?,?,?,?,?,?)',
                [int(fixed_user_id), transaction_id, int(S_COMPANY_ID.get()), S_COMPANY_NAME.get(),
                 float(S_STOCK_PRICE.get()), int(S_STOCK_QTY.get()), float(price*int(S_STOCK_QTY.get()))])
            sub = qty -int(S_STOCK_QTY.get())
            print(sub)
            c.execute('update user_details set Balance = ? where user_id = ?', [Balance, fixed_user_id])

            c.execute('update company_details set quantity = ? where company_id = ?',
                      [qty + int(S_STOCK_QTY.get()), int(S_COMPANY_ID.get())])
            if (qty - int(S_STOCK_QTY.get())) == 0:
                c.execute('DELETE from current_stocks where user_id = ? and company_id = ?',[int(fixed_user_id), int(S_COMPANY_ID.get())])
            else:
                c.execute('update current_stocks set quantity = ? where company_id = ? and user_id = ?', [int(qty-int(S_STOCK_QTY.get())), int(S_COMPANY_ID.get()), int(fixed_user_id)])

            print("Transaction Successful")
            s_company_id_Entry.delete(0, "end")
            s_stock_price_Entry.delete(0, "end")
            s_company_name_Entry.delete(0, "end")
            s_stock_quantity_Entry.delete(0, "end")
            s_stock_price_Entry.configure(state=DISABLED)
            s_company_name_Entry.configure(state=DISABLED)
            s_stock_quantity_Entry.configure(state=DISABLED)


        else:
            ms.showerror('Oops!', 'Invalid quantity value')
        db1.commit()
        db1.close()
        s_stock_price_Entry.delete(0, "end")
        s_company_name_Entry.delete(0, "end")
        s_stock_quantity_Entry.delete(0, "end")
        s_company_name_Entry.configure(state=DISABLED)
        s_stock_price_Entry.configure(state=DISABLED)
        s_stock_quantity_Entry.configure(state=DISABLED)
        # else:
        #     ms.showerror("Error","Company ID does not match to any stocks you have purchased. ")
        #     s_stock_price_Entry.delete(0, "end")
        #     s_company_name_Entry.delete(0, "end")
        #     s_stock_quantity_Entry.delete(0, "end")
        #     s_company_name_Entry.configure(state=DISABLED)
        #     s_stock_price_Entry.configure(state=DISABLED)
        #     s_stock_quantity_Entry.configure(state=DISABLED)

    def S_Search_Data():
        s_company_name_Entry.configure(state=NORMAL)
        s_stock_price_Entry.configure(state=NORMAL)
        s_stock_quantity_Entry.configure(state=NORMAL)
        s_stock_price_Entry.delete(0, "end")
        s_company_name_Entry.delete(0, "end")
        db1 = sqlite3.connect('project.db')
        c = db1.cursor()
        c.execute("select * from company_details where company_id = ? ", [S_COMPANY_ID.get()])
        records = c.fetchall()
        if records:
            for record in records:
                s_company_name_Entry.insert(0, record[1])
                s_stock_price_Entry.insert(0, record[2])
            s_company_name_Entry.configure(state=DISABLED)
            s_stock_price_Entry.configure(state=DISABLED)
        else:
            ms.showerror('Oops!', 'Company_ID Not Found.')
        db1.commit()
        db1.close()

    k=0
    def S_Show():
        global k
        global fixed_user_id
        k = 0
        tree1.delete(*tree1.get_children())
        db1 = sqlite3.connect('project.db')
        cursor = db1.execute('select * from current_stocks where user_id = ?',[fixed_user_id])
        for row in cursor:
            tree1.insert('', 'end', text="" + str(k), values=(row[1], row[2], row[3], row[4], row[5], row[6]))
            k = k + 1
        db1.commit()
        db1.close()

    SellStockFrame = ttk.LabelFrame(tab2, text="Sell")
    SellStockFrame.grid(column=0, row=0, pady=4, padx=8, sticky='N')

    global S_COMPANY_ID
    global S_STOCK_QTY
    global S_STOCK_PRICE
    global S_COMPANY_NAME

    S_COMPANY_ID = StringVar(SellStockFrame)
    S_STOCK_QTY = StringVar(SellStockFrame)
    S_STOCK_PRICE = StringVar(SellStockFrame)
    S_COMPANY_NAME = StringVar(SellStockFrame)

    s_company_id = ttk.Label(SellStockFrame, text="Company Id :")
    s_company_id.grid(row=0, column=0, sticky='W')
    s_company_id_Entry = ttk.Entry(SellStockFrame, textvariable=S_COMPANY_ID)
    s_company_id_Entry.grid(column=0, row=1, sticky='W')
    s_company_name = ttk.Label(SellStockFrame, text="Company Name : ")
    s_company_name.grid(column=0, row=2, sticky='W')
    s_company_name_Entry = ttk.Entry(SellStockFrame, state=DISABLED, textvariable=S_COMPANY_NAME)
    s_company_name_Entry.grid(column=0, row=3, sticky='W')
    s_stock_price = ttk.Label(SellStockFrame, text="Price :")
    s_stock_price.grid(row=4, column=0, sticky='W')
    s_stock_price_Entry = ttk.Entry(SellStockFrame, state=DISABLED, textvariable=S_STOCK_PRICE)
    s_stock_price_Entry.grid(column=0, row=5, sticky='W')
    s_stock_quantity = ttk.Label(SellStockFrame, text="Quantity :")
    s_stock_quantity.grid(column=0, row=6, sticky='W')
    s_stock_quantity_Entry = ttk.Entry(SellStockFrame, textvariable=S_STOCK_QTY)
    s_stock_quantity_Entry.grid(column=0, row=7, sticky='w')

    s_stock_price_Entry.configure(state=DISABLED)
    s_company_name_Entry.configure(state=DISABLED)
    s_stock_quantity_Entry.configure(state=DISABLED)

    SearchButton2 = ttk.Button(SellStockFrame, text="Search", width=20, command=S_Search_Data)
    SearchButton2.grid(column=0, row=8, sticky='E', pady=7)
    ShowButton2 = ttk.Button(SellStockFrame, text="Show", width=20, command=S_Show)
    ShowButton2.grid(column=0, row=9, sticky='E', pady=7)
    InsertButton2 = ttk.Button(SellStockFrame, text="Sell", width=20, command=S_Insert_data)
    InsertButton2.grid(column=0, row=10, sticky='W', pady=7)
    BackButton2 = ttk.Button(SellStockFrame, text="Main Menu", width=20, command=des)
    BackButton2.grid(column=0, row=11, sticky='W', pady=7)

    tabcontrol2 = ttk.Notebook(root)
    Stock2 = ttk.Frame(tabcontrol2)

    labelFrame2 = ttk.LabelFrame(tab2, text="Stock List", borderwidth=3)

    labelFrame2.grid(row=0, column=1, padx=8, pady=4, sticky="N")

    Stock2.pack()

    tree1 = ttk.Treeview(labelFrame2, columns=('Company_ID', 'Name', 'Bought_Price', 'CMP', 'quantity', 'Profit'), height=20)

    tree1.heading('#0', text='Index')
    tree1.column("#0", anchor="center", width=40, stretch=NO)
    tree1.heading("Company_ID", text="Company ID", anchor="w")
    tree1.column("Company_ID", anchor="center", width=80)
    tree1.heading("Name", text="Name", anchor="center")
    tree1.column("Name", anchor="center", width=120)
    tree1.heading("Bought_Price", text="Bought Price", anchor="w")
    tree1.column("Bought_Price", anchor="center", width=100)
    tree1.heading("CMP", text="Current Market Price", anchor="w")
    tree1.column("CMP", anchor="center", width=130)
    tree1.heading("quantity", text="Quantity", anchor="w")
    tree1.column("quantity", anchor="center", width=100)
    tree1.heading("Profit", text="Profit", anchor="w")
    tree1.column("Profit", anchor="center", width=100)
    tree1.grid(row=11, columnspan=6, sticky='nsew')
    tabcontrol1.pack(expand=0, fill="both")
    root.mainloop()


def Porfolio():
    from tkinter import ttk
    root = Tk()
    root.title("Portfolio")

    # centered
    w = 700
    h = 500
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.configure(bg='sky blue')

    Label(root, text='Portfolio', bg='sky blue', font=('', 35, "bold"), pady=10).pack(padx=10, pady=10)
    watchlist_view = ttk.Treeview(root)
    watchlist_view['columns'] = ("Company_ID", "Name", "Current Market Price", "Buy_price", "quantity", "Profit")
    watchlist_view.pack()

    def display():
        global fixed_user_id
        i = 0
        db = sqlite3.connect('project.db')
        cursor = db.execute('select * from current_stocks where user_id = ?', [fixed_user_id])
        watchlist_view.delete(*watchlist_view.get_children())
        for row in cursor:
            watchlist_view.insert('', 'end', text="" + str(i), values=(row[1], row[2], row[3], row[4], row[5], row[6]))
            i = i + 1
        db.commit()
        db.close()

    watchlist_view.heading("#0", text="Index", anchor="w")
    watchlist_view.column("#0", anchor="center", width=40, stretch=NO)
    watchlist_view.heading("Company_ID", text="Company ID", anchor="center")
    watchlist_view.column("Company_ID", anchor="center", width=80)
    watchlist_view.heading("Name", text="Name", anchor="center")
    watchlist_view.column("Name", anchor="center", width=130)
    watchlist_view.heading("Buy_price", text="Bought Price", anchor="center")
    watchlist_view.column("Buy_price", anchor="center", width=100)
    watchlist_view.heading("Current Market Price", text="Current Market Price", anchor="center")
    watchlist_view.column("Current Market Price", anchor="center", width=130)
    watchlist_view.heading("quantity", text="Quantity", anchor="center")
    watchlist_view.column("quantity", anchor="center", width=80)
    watchlist_view.heading("Profit", text="Profit", anchor="center")
    watchlist_view.column("Profit", anchor="center", width=70)

    Button(root, text='Display', font=('', 15), pady=10, width=20, bg='light sky blue', activebackground='deep sky blue', command=display).pack(padx=10, pady=10)
    Button(root, text='Main Menu', font=('', 15), pady=10, width=20, bg='light sky blue',
           activebackground='deep sky blue', command=root.destroy).pack(padx=10, pady=10)
    root.mainloop()
def analytics():

    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
    from matplotlib.figure import Figure
    root = Tk()
    root.title("Stocks")
    # centered
    w = 700
    h = 500
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.configure(bg='sky blue')

    global fixed_user_id
    c_id = []
    c_name = []
    c_qty = []
    db1 = sqlite3.connect('project.db')
    c = db1.cursor()
    c.execute('select company_id,company_name,quantity from current_stocks where user_id = ? group by company_id',
              [fixed_user_id])
    rows = c.fetchall()
    for row in rows:
        c_id.append(row[0])
        c_name.append(row[1])
        c_qty.append(row[2])

    canvas1 = Canvas(root, width=0.1, height=0.1)
    canvas1.pack()

    figure2 = Figure(figsize=(6, 5), dpi=100)
    subplot2 = figure2.add_subplot(111)
    subplot2.pie(c_qty, labels=c_name, autopct='%0.2f%%', shadow=True, startangle=90)
    subplot2.axis('equal')
    pie2 = FigureCanvasTkAgg(figure2, root)
    toolbar = NavigationToolbar2Tk(pie2, root)
    pie2.get_tk_widget().pack()
    root.mainloop()

def Profit_analytics():

    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
    from matplotlib.figure import Figure
    root = Tk()
    root.title("Profit from Stocks")
    # centered
    w = 700
    h = 500
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.configure(bg='sky blue')

    global fixed_user_id
    c_id = []
    c_name = []
    profit = []
    db1 = sqlite3.connect('project.db')
    c = db1.cursor()
    c.execute('select company_id,company_name,Profit from current_stocks where user_id = ?',
              [fixed_user_id])
    rows = c.fetchall()
    for row in rows:
        c_id.append(row[0])
        c_name.append(row[1])
        profit.append(row[2])

    canvas1 = Canvas(root, width=0.1, height=0.1)
    canvas1.pack()

    figure2 = Figure(figsize=(6, 5), dpi=100)
    subplot2 = figure2.add_subplot(111)
    subplot2.pie(profit, labels=c_name, autopct='%0.2f%%', shadow=True, startangle=90)
    subplot2.axis('equal')
    pie2 = FigureCanvasTkAgg(figure2, root)
    toolbar = NavigationToolbar2Tk(pie2, root)
    pie2.get_tk_widget().pack()
    root.mainloop()


def S_Profit_analytics():

    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
    from matplotlib.figure import Figure
    root = Tk()
    root.title("Profit from Sold Stocks")
    # centered
    w = 700
    h = 500
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.configure(bg='sky blue')

    global fixed_user_id
    c_id = []
    c_name = []
    profit = []
    db1 = sqlite3.connect('project.db')
    c = db1.cursor()
    c.execute('select company_id,company_name,sum(Profit) from sell_history where user_id = ? group by company_id',
              [fixed_user_id])
    rows = c.fetchall()
    for row in rows:
        c_id.append(row[0])
        c_name.append(row[1])
        profit.append(row[2])
    canvas1 = Canvas(root, width=0.1, height=0.1)
    canvas1.pack()

    figure2 = Figure(figsize=(6, 5), dpi=100)
    subplot2 = figure2.add_subplot(111)
    subplot2.pie(profit, labels=c_name, autopct='%0.2f%%', shadow=True, startangle=90)
    subplot2.axis('equal')
    pie2 = FigureCanvasTkAgg(figure2, root)
    toolbar = NavigationToolbar2Tk(pie2, root)
    pie2.get_tk_widget().pack()
    root.mainloop()


def report():

    from tkinter import ttk
    from random import randint


    root = Tk()
    root.title("Report")
    root.configure(background="sky blue")
    # Centered
    w = 500
    h = 175
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    label1=ttk.Label(root,text='Enter your query: ',background='sky blue',font=('MS',20,'bold'))
    label1.pack()
    entry1=ttk.Entry(root, font=('', 16))
    entry1.pack(ipadx=80)

    def prob():
        global fixed_user_id
        connection = sqlite3.connect('project.db')
        cursor = connection.cursor()
        k = randint(10001, 99999)
        find_query = ('SELECT * FROM query WHERE query_id = ?')
        cursor.execute(find_query, [k])
        while (cursor.fetchall()):
            k = randint(10001, 99999)
            find_query = ('SELECT * FROM user_details WHERE user_id = ?')
            cursor.execute(find_query, [k])
        cursor.execute('Insert into query values(?,?,?)',(k,int(fixed_user_id),entry1.get()))
        connection.commit()
        connection.close()
        entry1.delete(0, "end")
        ms.showinfo("Notification","Your query has been recorded.")
        root.destroy()

    button1 = Button(root, text='Submit', bg='light sky blue', activebackground='deep sky blue', font=('', 13),
                     command=prob)
    button1.pack(pady=8,ipadx=25)

    root.mainloop()

def rate():


    root = Tk()
    root.title("Rate Us")
    root.configure(background="sky blue")
    # Centered
    w = 300
    h = 200
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    label1 = Label(root, text='Enter your query: ', background='sky blue', font=('MS', 20, 'bold'))
    label1.pack()
    w=Scale(root,from_=0,to=5,orient=HORIZONTAL,bg='sky blue')
    w.pack(ipadx=50)

    def table():
        global fixed_user_id
        connection = sqlite3.connect('project.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS review(user_id INTEGER, rating INTEGER)')
        cursor.execute('insert into review values(?,?)', (int(fixed_user_id), w.get()))
        connection.commit()
        connection.close()
        ms.showinfo("Notification","Your feed has been recorded.")
        root.destroy()
    button1=Button(root,text='submit',command=table,bg='light sky blue', activebackground='deep sky blue')
    button1.pack(ipadx=15,padx=10)
    root.mainloop()


def abt_us():
    root = Tk()
    root.title("About Us")
    root.configure(background="sky blue")
    # Centered
    w = 1300
    h = 350
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    label6 = Label(root, text="ABOUT US", font=('MS', 22, 'bold'), bg='sky blue')
    label6.pack()

    label7 = Label(root, text="1. Overview", font=('MS', 15, 'bold'), bg='sky blue')
    label7.pack(anchor=W)

    label1 = Label(root,
                   text="1.1 Stock Market Challenge is an online simulation trading game where you create and manage "
                        "your own portfolio and compete with other players in a risk-free environment.",
                   bg='sky blue', font=('', 10))
    label1.pack(anchor=W)
    label2 = Label(root,
                   text="1.2 Whether you're new to the stock markets or an experienced investor, this is a powerful "
                        "tool for building skill, evaluating and tuning your strategy, and gaining important "
                        "investing experience.",
                   bg='sky blue', font=('', 10))
    label2.pack(anchor=W)
    label3 = Label(root,
                   text="1.3 Stock Market Challenge is free and easy to use. Simply buy stocks to build your initial "
                        "portfolio. Continue to track the market and keep an shuffle your portfolio to grab "
                        "opportunities provided so as to maximize your gains.",
                   bg='sky blue', font=('', 10))
    label3.pack(anchor=W)
    label4 = Label(root,
                   text="1.4 Stock Market Challenge is free and easy to use. Simply buy stocks to build your initial "
                        "portfolio. Continue to track the market and keep an eye on your portfolio to grab "
                        "opportunities provided etc.",
                   bg='sky blue', font=('', 10))
    label4.pack(anchor=W)
    label5 = Label(root,
                   text="1.5 Access financial information on stocks to get better insight on its potential and "
                        "fundamentals.",
                   bg='sky blue', font=('', 10))
    label5.pack(anchor=W)

    label8 = Label(root, text="2. Rules", font=('MS', 15, 'bold'), bg='sky blue')
    label8.pack(anchor=W)
    label9 = Label(root,
                   text="The Stock Market Challenge is governed by game rules that you should be aware of to ensure "
                        "you fully understand the online trading process and to make the most from this experience.",
                   bg='sky blue', font=('', 10))
    label9.pack(anchor=W)
    label10 = Label(root,
                    text="2.1 REGISTRATION:Existing subscribers can use existing username, password.New "
                         "visitors/users need to register. Registration is FREE! ",
                    bg='sky blue', font=('', 10))
    label10.pack(anchor=W)
    label11 = Label(root, text="2.2 GAME DURATION:The game starts the very moment you register for the game. ",
                    bg='sky blue', font=('', 10))
    label11.pack(anchor=W)
    label12 = Label(root, text="2.3 OPENING BALANCE:Starting balance is Rs 10,00,000 in cash.", bg='sky blue',
                    font=('', 10))
    label12.pack(anchor=W)

    root.mainloop()

def cng_password():

    from tkinter import messagebox as ms

    root = Tk()
    root.title("Project_Name")
    root.configure(background="sky blue")
    # Centered
    w = 500
    h = 400
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    label1=Label(root,text='Enter Previous Password',bg='sky blue', font=('',17))
    label1.pack(pady=5)
    entry1=Entry(root, font=('',15), show='*')
    entry1.pack(pady=5)

    label2=Label(root,text='Enter New Password',bg='sky blue', font=('',17))
    label2.pack(pady=5)
    entry2=Entry(root, font=('',15), show='*')
    entry2.pack(pady=5)

    label3=Label(root,text='Enter Re-enter new Password',bg='sky blue', font=('',17))
    label3.pack(pady=5)
    entry3=Entry(root, font=('',15), show='*')
    entry3.pack(pady=5)

    def submission():
        global fixed_user_id
        connection = sqlite3.connect('project.db')
        cursor = connection.cursor()
        cursor.execute("SELECT password FROM user_details where user_id = ?", [int(fixed_user_id)])
        r = cursor.fetchone()
        a = entry1.get()
        b = entry2.get()
        c = entry3.get()
        if(b==c):
            if r[0] == a:
                if r[0]!=b:
                    cursor.execute("UPDATE user_details SET password = ? where user_id = ?",[c,int(fixed_user_id)])
                    print('Password Changed')
                else:
                    ms.showerror("Error","Entered the new password same as the current password")
            else:
                ms.showerror("Incorrect","Enter the correct password for the account.")
        else:
            ms.showerror("Error", "Enter the correct new password while verifying")
        connection.commit()
        connection.close()
    def des():
        root.destroy()
    button1=Button(root,text='Submit', bg='light sky blue', activebackground='deep sky blue', pady=5, font=('',13), command=submission)
    button1.pack(ipadx=100,pady=20)
    button2 = Button(root, text='Main Menu', bg='light sky blue', activebackground='deep sky blue', pady=5, font=('', 13),
                     command=des)
    button2.pack(ipadx=84, pady=10)
    root.mainloop()

def update_us():
    from tkinter import ttk

    from tkinter import messagebox as ms
    root = Tk()
    root.title("Profile")
    root.configure(background="sky blue")
    # Centered
    w = 500
    h = 500
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    v = StringVar(root, "1")
    label1 = Label(root, text='Update Your Account', bg='sky blue', font=('', 22,"bold"))
    label1.pack(pady=5)
    label1 = Label(root, text='Enter Password', bg='sky blue', font=('', 15))
    label1.pack(pady=5)
    entry1 = Entry(root, width=18, font=('', 15), show='*')
    entry1.pack(pady=5)
    def upd():
        global fixed_user_id
        db = sqlite3.connect('Project.db')
        c = db.cursor()
        c.execute("SELECT password FROM user_details where user_id = ?", [int(fixed_user_id)])
        r = c.fetchone()
        a = entry1.get()
        if a==r[0]:
            label1 = Label(root, text='Select the attribute to be updated', bg='sky blue', font=('', 15))
            label1.pack(pady=5)

            def clicked(a):
                global fixed_user_id
                root1 = Tk()
                root1.title("Profile")
                root1.configure(background="sky blue")
                # Centered
                w = 500
                h = 250
                ws = root1.winfo_screenwidth()
                hs = root1.winfo_screenheight()
                x = (ws / 2) - (w / 2)
                y = (hs / 2) - (h / 2)
                root1.geometry('%dx%d+%d+%d' % (w, h, x, y))
                label1 = Label(root1, text='Update Your Account', bg='sky blue', font=('', 22, "bold"))
                label1.pack(pady=5)
                if a == "1":
                    Label(root1, text='Enter Name', bg='sky blue', font=('', 22, "bold")).pack(pady=5)
                    entry2 = Entry(root1, font=('', 15))
                    entry2.pack()
                elif a == "2":
                    Label(root1, text='Enter Email ID ', bg='sky blue', font=('', 22, "bold")).pack(pady=5)
                    entry2 = Entry(root1, font=('', 15))
                    entry2.pack()
                elif a == "3":
                    Label(root1, text='Enter City ', bg='sky blue', font=('', 22, "bold")).pack(pady=5)
                    entry2 = Entry(root1, font=('', 15))
                    entry2.pack()
                elif a == "4":
                    Label(root1, text='Enter Country ', bg='sky blue', font=('', 22, "bold")).pack(pady=5)
                    entry2 = Entry(root1, font=('', 15))
                    entry2.pack()
                elif a == "5":
                    Label(root1, text='Enter Phone Number ', bg='sky blue', font=('', 22, "bold")).pack(pady=5)
                    entry2 = Entry(root1, font=('', 15))
                    entry2.pack()
                else:
                    print("Error1")
                Button(root1, text='Submit', bg='light sky blue', activebackground='deep sky blue', pady=5, font=('', 13), command=lambda: submit(entry2.get(), a, root1)).pack()
                root1.mainloop()
            def submit(m,n,o):
                global fixed_user_id
                if n == "1":
                    db1 = sqlite3.connect('Project.db')
                    c = db1.cursor()
                    c.execute("update user_details set name = ? where user_id = ?", [m,int(fixed_user_id)])
                    db1.commit()
                    db1.close()
                    print("Success!")
                    o.destroy()
                    ms.showinfo("Success","You name has been updated")
                elif n == "2":
                    db1 = sqlite3.connect('Project.db')
                    c = db1.cursor()
                    c.execute("update user_details set email_id = ? where user_id = ?", [m,int(fixed_user_id)])
                    db1.commit()
                    db1.close()
                    print("Success!")
                    o.destroy()
                    ms.showinfo("Success", "You Email iD has been updated")
                elif n == "3":
                    db1 = sqlite3.connect('Project.db')
                    c = db1.cursor()
                    c.execute("update user_details set city = ? where user_id = ?", [m, int(fixed_user_id)])
                    db1.commit()
                    db1.close()
                    print("Success!")
                    o.destroy()
                    ms.showinfo("Success", "You city has been updated")
                elif n == "4":
                    db1 = sqlite3.connect('Project.db')
                    c = db1.cursor()
                    c.execute("update user_details set country = ? where user_id = ?", [m, int(fixed_user_id)])
                    db1.commit()
                    db1.close()
                    print("Success!")
                    o.destroy()
                    ms.showinfo("Success", "You country has been updated")
                elif n == "5":
                    db1 = sqlite3.connect('Project.db')
                    c = db1.cursor()
                    c.execute("update user_details set phone_no = ? where user_id = ?", [int(m), int(fixed_user_id)])
                    db1.commit()
                    db1.close()
                    print("Success!")
                    o.destroy()
                    ms.showinfo("Success", "You Phone Number has been updated")
                else:
                    print("Error","Contact the admistrator")
            def desc():
                root.destroy()
            ttk.Radiobutton(root, text="Name        ", variable = v, value = 1, command=lambda: clicked(v.get())).pack(side = TOP, ipady = 5,anchor='center')
            ttk.Radiobutton(root, text="Email ID    ", variable = v, value = 2, command=lambda: clicked(v.get())).pack(side = TOP, ipady = 5,anchor='center')
            ttk.Radiobutton(root, text="City        ", variable=v, value=3, command=lambda: clicked(v.get())).pack(side=TOP, ipady=5,anchor='center')
            ttk.Radiobutton(root, text="Country     ", variable=v, value=4, command=lambda: clicked(v.get())).pack(side=TOP, ipady=5,anchor='center')
            ttk.Radiobutton(root, text="Phone Number", variable=v, value=5, command=lambda: clicked(v.get())).pack(side=TOP, ipady=5,anchor='center')
            style = ttk.Style(root)
            Button(root, text='Main Menu', bg='light sky blue', activebackground='deep sky blue', pady=5, font=('', 13),
                   command=desc).pack(ipadx=50, pady=20)
            style.configure("TRadiobutton", background="sky blue", font=("arial", 10, "bold"))
        else:
            ms.showerror("Incorrrect","Enter the correct password.")

    button1 = Button(root, text='Verify', bg='light sky blue', activebackground='deep sky blue', pady=5, font=('', 13), command=upd)
    button1.pack(ipadx=50, pady=20)
    root.mainloop()

def c_u():
    from tkinter import messagebox as ms

    root = Tk()
    root.title("Project_Name")
    root.configure(background="sky blue")
    w = 400
    h = 300
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    Label(root, text='Contact Us', background="sky blue", font=('', 20, "bold")).pack(pady=5)

    Label(root, text='Subject', background="sky blue", font=('', 15)).pack()
    h = Entry(root, font=('', 12))
    h.pack(pady=5)
    Label(root, text='Message', background="sky blue", font=('', 15)).pack(pady=5)
    j = Entry(root, font=('', 12))
    j.pack()

    def table():
        global fixed_user_id
        connection = sqlite3.connect('project.db')
        cursor = connection.cursor()
        cursor.execute('Insert into contact_us values(?,?,?)', (int(fixed_user_id), h.get(), j.get()))
        connection.commit()
        ms.showinfo("Success", "Your query has been recorded.")

    def desc():
        root.destroy()

    i = Button(root, text='Submit', bg='light sky blue', activebackground='deep sky blue', command=table, font=('', 14)).pack(pady=5)
    i = Button(root, text='Main Menu', bg='light sky blue', activebackground='deep sky blue', command=desc, font=('', 14)).pack(pady=5)

    root.mainloop()


Login_Page()


