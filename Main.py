import mysql.connector
from tkinter import *
from tkinter import messagebox

conn = mysql.connector.connect(host="localhost", user="admin", password="admin", database="mydatabase")
cursor = conn.cursor()


def add_users_function(): #Reven

    cursor = conn.cursor()

    fname = first_name.get()
    lname = last_name.get()
    user_name = user.get()
    user_password = passw.get()
    birthdate = birth.get()
    cellno = cpno.get()
    address = add.get()
    e_add = email_add.get()
    u_type = utype.get(utype.curselection())

    sql = "INSERT INTO user_information (user_fname, user_lname, user_name, user_password, birthdate, address, cell_number, email_address, user_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (fname, lname, user_name, user_password, birthdate, address, cellno, e_add, u_type)

    cursor.execute(sql, values)

    conn.commit()

    cursor.close()
    conn.close()

    messagebox.showinfo(title="Successful", message="Successfully Registered")

    register.withdraw()


def login_authentication_function():
    global window2

    username = lusername.get()
    password = lpassword.get()

    query = "SELECT * FROM user_information WHERE user_name = %s AND user_password = %s"
    cursor.execute(query, (username, password))
    user_data = cursor.fetchone()

    if user_data:
        user_type = user_data[9]
        if user_type == "Admin":
            if messagebox.showinfo("Login Successful", "Welcome, Admin"):
                window1 = Tk()
                window1.geometry("500x500")
                window1.config(background="#160060")

                welcome = Label(window1, text="Welcome, Administrator", font=("Times New Roman", 30), relief=RAISED)
                welcome.place(x=50, y=80)

                displayusers = Button(window1, text="Display All Users", font=("Times New Roman", 20), width=18, command=display_users_function)
                displayusers.place(x=100, y=170)

                editusers = Button(window1, text="Edit User Information", font=("Times New Roman", 20), width=18, command=edit_user_function)
                editusers.place(x=100, y=240)

                displaybooks = Button(window1, text="Display All Books", font=("Times New Roman", 20), width=18, command=display_books_function)
                displaybooks.place(x=100, y=310)

                login.destroy()
                window.destroy()

        elif user_type == "Staff":
            if messagebox.showinfo("Login Successful", "Welcome, Employee " + username):
                window2 = Tk()

                window2.geometry("500x500")
                window2.config(background="#160060")

                welcome = Label(window2, text="Welcome, " + username, font=("Times New Roman", 30), fg="white",
                                bg="#160060", width=18)
                welcome.place(x=40, y=80)

                registerbooks = Button(window2, text="Register Books", font=("Times New Roman", 20), command=register_books_function)
                registerbooks.place(x=135, y=200)

                displaybooks = Button(window2, text="Display All Books", font=("Times New Roman", 20), command=display_books_function)
                displaybooks.place(x=120, y=290)

                login.destroy()
                window.destroy()

        else:
            if messagebox.showinfo("Login Successful", "Welcome, User"):
                window3 = Tk()

                window3.geometry("500x500")
                window3.config(background="#160060")

                welcome = Label(window3, text="Welcome, ", font=("Times New Roman", 30), fg="white", bg="#160060",
                                width=18)
                welcome.place(x=50, y=80)

                browsebooks = Button(window3, text="Browse Books", font=("Times New Roman", 20), command=browse_books_function)
                browsebooks.place(x=150, y=180)

                borrowedbooks = Button(window3, text="Display Borrowed Books", font=("Times New Roman", 20))
                borrowedbooks.place(x=90, y=260)

                login.destroy()
                window.destroy()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def registration_function(): #Reven
    global register, first_name, last_name, birth, cpno, add, email_add, user, passw, utype

    register = Toplevel()
    register.geometry("600x600")
    register.title("Book Rental Application Registration Form")
    register.config(background="#160060")

    title = Label(register, text="Registration Form", font=("Times New Roman", 30), relief=RAISED)
    title.place(x=140, y=20)

    fname = Label(register, text="First Name:", font=("Times New Roman", 15), fg="white", bg="#160060")
    fname.place(x=40, y=120)
    lname = Label(register, text="Last Name:", font=("Times New Roman", 15), fg="white", bg="#160060")
    lname.place(x=300, y=120)
    bday = Label(register, text="Birth Date:", font=("Times New Roman", 15), fg="white", bg="#160060")
    bday.place(x=40, y=190)
    cp = Label(register, text="Cellphone Number:", font=("Times New Roman", 15), fg="white", bg="#160060")
    cp.place(x=300, y=190)
    addr = Label(register, text="Address:", font=("Times New Roman", 15), fg="white", bg="#160060")
    addr.place(x=40, y=250)
    eadd = Label(register, text="Email Address:", font=("Times New Roman", 15), fg="white", bg="#160060")
    eadd.place(x=40, y=310)
    user = Label(register, text="Username:", font=("Times New Roman", 15), fg="white", bg="#160060")
    user.place(x=40, y=380)
    passw = Label(register, text="Password:", font=("Times New Roman", 15), fg="white", bg="#160060")
    passw.place(x=40, y=460)
    utp = Label(register, text="User Type:", font=("Times New Roman", 15), fg="white", bg="#160060")
    utp.place(x=350, y=380)

    first_name = Entry(register, font=("Times New Roman", 15), fg="black", bg="white")
    first_name.place(x=40, y=150)

    last_name = Entry(register, font=("Times New Roman", 15), fg="black", bg="white")
    last_name.place(x=300, y=150)

    birth = Entry(register, font=("Times New Roman", 15), fg="black", bg="white")
    birth.place(x=40, y=220)

    cpno = Entry(register, font=("Times New Roman", 15), fg="black", bg="white")
    cpno.place(x=300, y=220)

    add = Entry(register, font=("Times New Roman", 15), fg="black", bg="white", width=44)
    add.place(x=40, y=280)

    email_add = Entry(register, font=("Times New Roman", 15), fg="black", bg="white", width=44)
    email_add.place(x=40, y=340)

    user = Entry(register, font=("Times New Roman", 20), fg="black", bg="white", )
    user.place(x=40, y=410)

    passw = Entry(register, font=("Times New Roman", 20), fg="black", bg="white", show="*")
    passw.place(x=40, y=490)

    utype = Listbox(register, font=("Times New Roman", 15))
    utype.place(x=350, y=410)
    utype.config(height=utype.size(), width=10)

    utype.insert(1, "Staff")
    utype.insert(2, "User")

    signinbutton = Button(register, text="Register", font=("Times New Roman", 10), width=10, command=add_users_function)
    signinbutton.place(x=40, y=540)


def login_function():
    global login, lusername, lpassword

    login = Toplevel()
    login.geometry("600x600")
    login.title("Book Rental Application Login Form")

    bground = PhotoImage(file='images\\bg3.png')
    background2 = Label(login, image=bground, bg="#160060")
    background2.pack()

    title = Label(login, text="Login Form", font=("Times New Roman", 30), relief=RAISED, width=15, height=1)
    title.place(x=123, y=30)

    name1 = Label(login, text="Username:", font=("Times New Roman", 20), fg="white", bg="#160060")
    name1.place(x=123, y=160)
    name2 = Label(login, text="Password:", font=("Times New Roman", 20), fg="white", bg="#160060")
    name2.place(x=123, y=280)

    lusername = Entry(login, font=("Times New Roman", 20), fg="black", bg="white", width=23)
    lusername.place(x=123, y=210)

    lpassword = Entry(login, font=("Times New Roman", 20), fg="black", bg="white", show="*", width=23)
    lpassword.place(x=123, y=330)

    loginButton = Button(login, text="Login", width=10, font=("Times New Roman", 10), command=login_authentication_function)
    loginButton.place(x=123, y=390)


def display_users_function():
    conn = mysql.connector.connect(host="localhost", user="admin", password="admin", database="mydatabase")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_information")
    items = cursor.fetchall()
    window3 = Tk()
    window3.title("User Information Window")
    window3.geometry("1300x500")
    window3.config(background="#160060")

    label1 = Label(window3, text="User Information", font=("Times New Roman", 20), bg="#160060", fg="white")
    label1.pack()

    frame = Frame(window3, bg="#160060")
    frame.pack(fill="both", expand=True)

    scrollbar = Scrollbar(frame, bg="#160060")
    scrollbar.pack(side="right", fill="y")

    canvas = Canvas(frame, yscrollcommand=scrollbar.set, bg="#160060")
    canvas.pack(fill="both", expand=True)

    scrollbar.config(command=canvas.yview)

    inner_frame = Frame(canvas, bg="#160060")
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas.bind("<Configure>", on_configure)

    Label(inner_frame, text="ID Number", font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=0, column=0, padx=5, pady=5)
    Label(inner_frame, text="First Name", font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=0, column=1, padx=5, pady=5)
    Label(inner_frame, text="Last Name", font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=0, column=2, padx=5, pady=5)
    Label(inner_frame, text="Username", font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=0, column=3, padx=5, pady=5)
    Label(inner_frame, text="Password", font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=0, column=4, padx=5, pady=5)
    Label(inner_frame, text="Birthdate", font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=0, column=5, padx=5, pady=5)
    Label(inner_frame, text="Address", font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=0, column=6, padx=5, pady=5)
    Label(inner_frame, text="Cellphone Number", font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=0, column=7, padx=5, pady=5)
    Label(inner_frame, text="Email Address", font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=0, column=8, padx=5, pady=5)
    Label(inner_frame, text="User Type", font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=0, column=9, padx=5, pady=5)

    for index, item in enumerate(items):
        item_detail1 = (f"{item[0]}")
        item_detail2 = (f"{item[1]}")
        item_detail3 = (f"{item[2]}")
        item_detail4 = (f"{item[3]}")
        item_detail5 = (f"{item[4]}")
        item_detail6 = (f"{item[5]}")
        item_detail7 = (f"{item[6]}")
        item_detail8 = (f"{item[7]}")
        item_detail9 = (f"{item[8]}")
        item_detail0 = (f"{item[9]}")

        Label(inner_frame, text=item_detail1, font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=index + 1, column=0, padx=5, pady=5)
        Label(inner_frame, text=item_detail2, font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=index + 1, column=1, padx=5, pady=5)
        Label(inner_frame, text=item_detail3, font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=index + 1, column=2, padx=5, pady=5)
        Label(inner_frame, text=item_detail4, font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=index + 1, column=3, padx=5, pady=5)
        Label(inner_frame, text=item_detail5, font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=index + 1, column=4, padx=5, pady=5)
        Label(inner_frame, text=item_detail6, font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=index + 1, column=5, padx=5, pady=5)
        Label(inner_frame, text=item_detail7, font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=index + 1, column=6, padx=5, pady=5)
        Label(inner_frame, text=item_detail8, font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=index + 1, column=7, padx=5, pady=5)
        Label(inner_frame, text=item_detail9, font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=index + 1, column=8, padx=5, pady=5)
        Label(inner_frame, text=item_detail0, font=("Times New Roman", 15), fg="white", bg="#160060").grid(row=index + 1, column=9, padx=5, pady=5)


def register_books_function():
    global rbooks, btitle2, bauthor2, bpublished2, bstatus2

    rbooks = Tk()
    rbooks.geometry("600x600")
    rbooks.config(background="#160060")
    rbooks.title("Book Registration Window")

    title = Label(rbooks, text="Book Registration Form", font=("Times New Roman", 30), relief=RAISED, width=20)
    title.place(x=60, y=50)

    btitle1 = Label(rbooks, text="Book Title:", font=("Timese New Roman", 20), fg="white", bg="#160060")
    btitle1.place(x=60, y=150)
    btitle2 = Entry(rbooks, font=("Times New Roman", 20), width=25)
    btitle2.place(x=60, y=190)

    bauthor1 = Label(rbooks, text="Book Author:", font=("Times New Roman", 20), fg="white", bg="#160060")
    bauthor1.place(x=60, y=240)
    bauthor2 = Entry(rbooks, font=("Times New Roman", 20), width=25)
    bauthor2.place(x=60, y=280)

    bpublished1 = Label(rbooks, text="Book Published:", font=("Times New Roman", 20), fg="white", bg="#160060")
    bpublished1.place(x=60, y=330)
    bpublished2 = Entry(rbooks, font=("Times New Roman", 20), width=25)
    bpublished2.place(x=60, y=370)

    bstatus1 = Label(rbooks, text="Book Status:", font=("Times New Roman", 20), fg="white", bg="#160060")
    bstatus1.place(x=60, y=410)
    bstatus2 = Entry(rbooks, font=("Times New Roman", 20), width=25)
    bstatus2.place(x=60, y=450)

    submit = Button(rbooks, text="Register", font=("Times New Roman", 10), width=10, command=add_books_function)
    submit.place(x=60, y=500)


def add_books_function(): #Mathew
    conn = mysql.connector.connect(user='admin', password='admin', host='localhost', database='mydatabase')

    cursor = conn.cursor()

    btitle = btitle2.get()
    bauthor = bauthor2.get()
    bpublished = bpublished2.get()
    bstatus = bstatus2.get()

    sql = "INSERT INTO book_information(book_title, book_author, book_published, book_status) VALUES(%s, %s, %s, %s)"
    values = (btitle, bauthor, bpublished, bstatus)

    cursor.execute(sql, values)

    conn.commit()

    cursor.close()
    conn.close()

    if messagebox.showinfo(title="Successful", message="Book Successfully Registered"):
        rbooks.destroy()


def display_books_function():
    conn = mysql.connector.connect(host="localhost", user="admin", password="admin", database="mydatabase")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book_information")
    items = cursor.fetchall()
    cursor.close()
    conn.close()

    displaybooks = Tk()
    displaybooks.config(background="#160060")
    displaybooks.geometry("900x500")
    displaybooks.title("Book Information Window")

    Label(displaybooks, text="Book Information", font=("Times New Roman", 20), fg="white", bg="#160060").pack()

    frame = Frame(displaybooks, bg="#160060")
    frame.pack(padx=20, pady=20, fill=BOTH, expand=True)

    canvas = Canvas(frame, bg="#160060")
    scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    canvas.configure(yscrollcommand=scrollbar.set)

    inner_frame = Frame(canvas, bg="#160060")
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    headers = ["Book ID", "Book Title", "Book Author", "Book Published", "Book Status"]
    for col, header in enumerate(headers):
        Label(inner_frame, text=header, font=("Times New Roman", 15), fg="white", bg="#160060", bd=2).grid(row=0,
                                                                                                           column=col,
                                                                                                           padx=5,
                                                                                                           pady=5)

    for index, item in enumerate(items):
        for col, detail in enumerate(item):
            Label(inner_frame, text=detail, font=("Times New Roman", 15), fg="white", bg="#160060", bd=2).grid(
                row=index + 1, column=col, padx=5, pady=5)

    inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


def edit_user_function(): #Mathew
    global uedit, first_name, last_name, birth, cpno, add, email_add, idno, user, passw

    uedit = Tk()
    uedit.geometry("600x600")
    uedit.title("User Information Editor Window")

    uedit.config(background="#160060")

    title = Label(uedit, text="User Information Editor", font=("Times New Roman", 30), relief=RAISED)
    title.place(x=110, y=30)

    fname = Label(uedit, text="First Name:", font=("Times New Roman", 15), fg="white", bg="#160060")
    fname.place(x=40, y=120)
    lname = Label(uedit, text="Last Name:", font=("Times New Roman", 15), fg="white", bg="#160060")
    lname.place(x=300, y=120)
    bday = Label(uedit, text="Birth Date:", font=("Times New Roman", 15), fg="white", bg="#160060")
    bday.place(x=40, y=190)
    cp = Label(uedit, text="Cellphone Number:", font=("Times New Roman", 15), fg="white", bg="#160060")
    cp.place(x=300, y=190)
    addr = Label(uedit, text="Address:", font=("Times New Roman", 15), fg="white", bg="#160060")
    addr.place(x=40, y=250)
    eadd = Label(uedit, text="Email Address:", font=("Times New Roman", 15), fg="white", bg="#160060")
    eadd.place(x=40, y=310)
    uid = Label(uedit, text="ID Number:", font=("Times New Roman", 15), fg="white", bg="#160060")
    uid.place(x=300, y=310)
    user = Label(uedit, text="Username:", font=("Times New Roman", 15), fg="white", bg="#160060")
    user.place(x=40, y=380)
    passw = Label(uedit, text="Password:", font=("Times New Roman", 15), fg="white", bg="#160060")
    passw.place(x=40, y=460)

    first_name = Entry(uedit, font=("Times New Roman", 15), fg="black", bg="white")
    first_name.place(x=40, y=150)

    last_name = Entry(uedit, font=("Times New Roman", 15), fg="black", bg="white")
    last_name.place(x=300, y=150)

    birth = Entry(uedit, font=("Times New Roman", 15), fg="black", bg="white")
    birth.place(x=40, y=220)

    cpno = Entry(uedit, font=("Times New Roman", 15), fg="black", bg="white")
    cpno.place(x=300, y=220)

    add = Entry(uedit, font=("Times New Roman", 15), fg="black", bg="white", width=46)
    add.place(x=40, y=280)

    email_add = Entry(uedit, font=("Times New Roman", 15), fg="black", bg="white")
    email_add.place(x=40, y=340)

    idno = Entry(uedit, font=("Times New Roman", 15), fg="black", bg="white")
    idno.place(x=300, y=340)

    user = Entry(uedit, font=("Times New Roman", 20), fg="black", bg="white", width=33)
    user.place(x=40, y=410)

    passw = Entry(uedit, font=("Times New Roman", 20), fg="black", bg="white", show="*", width=33)
    passw.place(x=40, y=490)

    signinbutton = Button(uedit, text="Edit", font=("Times New Roman", 10), width=10, command=edit_function)
    signinbutton.place(x=40, y=540)

    displayuserinfo = Button(uedit, text="Display User Information", font=("Times New Roman", 10), command=display_users_function)
    displayuserinfo.place(x=140, y=540)


def edit_function():
    conn = mysql.connector.connect(host="localhost", user="admin", password="admin", database="mydatabase")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_information")
    existing_data = cursor.fetchall()

    new_fname = first_name.get()
    new_lname = last_name.get()
    new_bday = birth.get()
    new_cp = cpno.get()
    new_add = add.get()
    new_eadd = email_add.get()
    new_id = idno.get()
    new_user = user.get()
    new_pass = passw.get()

    sql = "UPDATE user_information SET user_fname = %s, user_lname = %s, user_name = %s, user_password = %s, birthdate = %s, address = %s, cell_number = %s, email_address = %s WHERE user_idno = %s"
    new_values = (new_fname, new_lname, new_user, new_pass, new_bday, new_add, new_cp, new_eadd, new_id)

    cursor.execute(sql, new_values)

    conn.commit()
    conn.close()

    if messagebox.showinfo(title="Successful", message="Successfully Updated"):
        uedit.destroy()


def browse_books_function():
    conn = mysql.connector.connect(host="localhost", user="admin", password="admin", database="mydatabase")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book_information")
    items = cursor.fetchall()

    displaybooks = Tk()
    displaybooks.geometry("500x495")
    displaybooks.config(background="#160060")
    displaybooks.title("Book Browsing Window")

    label1 = Label(displaybooks, text="Available Books", font=("Times New Roman", 20), bg="#160060", fg="white")
    label1.pack()

    listbox = Listbox(displaybooks, font=("Times New Roman", 15), fg="white", bg="#160060", width=50)
    listbox.pack()

    for item in items:
        listbox.insert(END, f"Book Title: {item[1]}")

    listbox.config(height=15)

    button1 = Button(displaybooks, text="Borrow", font=("Times New Roman", 20), width=33)
    button1.pack()

    button2 = Button(displaybooks, text="Return", font=("Times New Roman", 20), width=33)
    button2.pack()


window = Tk()
window.geometry("600x600")
window.title("Book Rental Application")
icon = PhotoImage(file='images\\logo.png')
window.iconphoto(True, icon)

bg = PhotoImage(file='images\\bg.png')
background = Label(window, image=bg)
background.place(x=-2, y=-2)

label = Label(window, text="Welcome to\n Book Rental Application", font=("Times New Roman", 30), fg="white", bg="#160060")
label.place(x=80, y=190)

log = Button(window, text="Login", font=("Times New Roman", 25), width=7, command=login_function, relief=RAISED, border=5)
log.place(x=130, y=340)

reg = Button(window, text="Register", font=("Times New Roman", 25), width=8, command=registration_function, relief=RAISED, border=5)
reg.place(x=310, y=340)


window.mainloop()
