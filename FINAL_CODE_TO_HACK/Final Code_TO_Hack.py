import json
from tkinter import *
import random
import mysql.connector
from tkinter import messagebox

profile_username = ""
profile_email = ""
login_Count = 0
user_answer = []
indexes = []
ques = 0


def MAIN_WINDOW():
    root = Tk()

    def contact_show():
        root.write = Label(text="Phone number->8103999780\nEmail->codetohack@gmail.com", bg="white", fg="blue",
                           font="Helvetica 16 bold").place(x=1200, y=60)

    # /////////////////////////////////////////Registration Module Starts//////////////////////////////////////////////

    def registering_user():
        mydb = mysql.connector.connect(host="localhost", user="root", password="21720101", database="registration")

        reg = Tk()
        reg.geometry('900x700+300+100')
        reg.title("Registration Form")
        reg.config(background="#4E8975")
        label_0 = Label(reg, text="Registration form", bg="#4E8975", width=30, font=("bold", 30))
        label_0.place(x=250, y=60)

        label_1 = Label(reg, text="USERNAME ", width=20, bg="#4E8975", font=("bold", 18))
        label_1.place(x=380, y=150)

        entry_1 = Entry(reg,font = "Helvetica 16 bold",justify="center" )
        entry_1.place(x=580, y=150)

        label_2 = Label(reg, text="EMAIL ", width=20, bg="#4E8975", font=("bold", 18))
        label_2.place(x=380, y=200)

        entry_2 = Entry(reg,font = "Helvetica 16 bold",justify="center")
        entry_2.place(x=580, y=200)

        label_3 = Label(reg, text="PASSWORD ", width=20, bg="#4E8975", font=("bold", 18))
        label_3.place(x=380, y=250)

        entry_3 = Entry(reg,font = "Helvetica 16 bold",justify="center",show="*")
        entry_3.place(x=580, y=250)

        def data_inserting():
            username = entry_1.get()
            email = entry_2.get()
            password = entry_3.get()
            sqlinsert = "Insert into persons(username,email,password) values (%s,%s,%s)"
            mycursor = mydb.cursor()
            mycursor.execute("select email from persons")
            myresult = mycursor.fetchall()
            if username == "" or email == "" or password == "":
                print("enter valid entry")
                messagebox.showerror("ERROR", "enter valid entry")
                reg.destroy()
                registering_user()
            elif email:
                for mail in myresult:
                    if mail[0] == email:
                        messagebox.showerror("ERROR", "Email id already registered")
                        reg.destroy()
                        registering_user()
                        break
                else:
                    people = [(username, email, password)]
                    mycursor.executemany(sqlinsert, people)
                    messagebox.showinfo("SUCCESS", "Registered Successfull")
                    mydb.commit()
                    reg.destroy()

        Button(reg, text='Submit', width=30, bg='green', fg='white', command=data_inserting).place(x=440, y=350)

    # ////////////////////////////////////Registraion Module End///////////////////////////////////////////////////////////

    # ***************************************LOGIN MODULE******************************************************************

    def loginmodule():
        global login_Count
        login_Count += 1
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="21720101",
                                       database="registration")
        lgin = Tk()
        lgin.geometry("300x300+700+200")

        lgin.title("Login Page")

        lgin.config(background="Lemon chiffon2")
        # Definging the first row
        lbl1 = Label(lgin, text="USERNAME -", bg="Lemon chiffon2", fg="black",font=("bold",10))
        lbl1.place(x=50, y=20)

        username = Entry(lgin, width=35,font = "Helvetica 16 bold",justify="center")
        username.place(x=150, y=20, width=100)

        lbl2 = Label(lgin, text="PASSWORD -", bg="Lemon chiffon2", fg="black",font=("bold",10))
        lbl2.place(x=50, y=80)

        pwd = Entry(lgin, width=35,font = "Helvetica 16 bold",justify="center",show="*")
        pwd.place(x=150, y=80, width=100)

        def check_login():
            usr = username.get()
            psrd = pwd.get()
            mycursor = mydb.cursor()
            mycursor.execute("select username, password , email from persons")
            myresult = mycursor.fetchall()
            if usr == "" or psrd == "":
                print("enter valid entry")
                messagebox.showerror("ERROR", "enter valid entry")
                lgin.destroy()
                loginmodule()
            else:
                for i in myresult:
                    if i[0] == usr and i[1] == psrd:
                        messagebox.showinfo("SUCCESS", "Login Successfull")
                        global profile_username
                        global profile_email
                        profile_username = i[0]
                        profile_email = i[2]
                        lgin.destroy()
                        if login_Count == 1:
                            root.destroy()
                        language_selection()
                        break
                else:
                    messagebox.showerror("Error", "No account with this id and password")
                    lgin.destroy()
                    loginmodule()

        submitbtn = Button(lgin, text="Login", bg='green', fg="white", command=check_login)
        submitbtn.place(x=150, y=135, width=55)

    def show_profile():

        profile = Toplevel()
        profile.title("Student Profile")
        profile.geometry("1500x1500")
        photo = PhotoImage(file="pictures\PicsArt_11-04-10.46.17.png")
        profile.config(background="#827B60")

        Label(profile, text="USERNAME :-", fg="black", background="#827B60", font="zebrazil 20 bold").place(x=600,
                                                                                                            y=400)
        Label(profile, text=(profile_username), font="zebrazil 20 bold", fg="red", bg="white").place(x=900, y=400)

        Label(profile, text="EMAIL :-", fg="black", font="zebrazil 20 bold", background="#827B60").place(x=600,
                                                                                                         y=470)

        Label(profile, text=(profile_email), font="zebrazil 20 bold", fg="red", bg="white").place(x=900, y=470)

        Label(profile, text="STUDENT PROFILE", fg="black", background="#827B60", font="zebrazil 30 bold").place(
            x=660, y=310)

        pic_label = Label(profile, image=photo, background="#827B60").place(x=733, y=150)

        profile.mainloop()

    # -----------------------------------LOGIN Module ENDS-------------------------------------------------------------

    # ==================================LANGUAGE SELECTION AND QUIZE===================================================

    # convert the dictionary in lists of questions and answers_choice
    def language_selection():
        LS = Tk()
        LS.title("Language selection")
        LS.geometry("1500x1500")
        LS.config(background="#CCFFFF")
        p = PhotoImage(file="pictures/logohomecrop.png")
        Label(image=p, background="#CCFFFF").pack(anchor="nw", side=TOP)
        pic3 = PhotoImage(file="pictures/Screenshot (233).png")
        pic2 = PhotoImage(file="pictures/Screenshot (231).png")
        pic1 = PhotoImage(file="pictures/Screenshot (232).png")
        pic4= PhotoImage(file="pictures/C++LOGO-removebg-preview.png")
        label = Label(text="Test YourSelf", background="#CCFFFF", fg="black", font="arial 30").place(
            x=150,
            y=240)
        Label(text="Skills Available For Practice", background="#CCFFFF", fg="black", font="arial 30").place(
            x=880,
            y=240)
        pic5= PhotoImage(file="pictures/pylogo-removebg-preview.png")

        def C_quize():
            LS.destroy()
            with open('./cquiz.json', encoding="utf8") as f:
                data = json.load(f)

            # convert the dictionary in lists of questions and answers_choice
            questions = [v for v in data[0].values()]
            answers_choice = [v for v in data[1].values()]

            answers = [1, 0, 1, 2, 1, 3, 1, 2, 3, 0]

            def EXIT_AND_HOME():
                CQ.destroy()
                global user_answer
                global indexes
                global ques
                user_answer.clear()
                indexes.clear()
                ques = 0
                language_selection()

            def gen():
                global indexes
                while (len(indexes) < 10):
                    x = random.randint(0, 9)
                    if x in indexes:
                        continue
                    else:
                        indexes.append(x)

            def showresult(score):
                lblQuestion.destroy()
                r1.destroy()
                r2.destroy()
                r3.destroy()
                r4.destroy()
                labelimage = Label(
                    CQ,
                    background="#ffffff",
                    border=0,
                )
                labelimage.pack(pady=(50, 30))
                labelresulttext = Label(
                    CQ,
                    font=("Consolas", 20),
                    background="#ffffff",
                )
                labelresulttext.pack()
                var = IntVar()
                if score >= 40:
                    l = Label(text="Final Score", font="zebrazil 20 bold").pack()
                    b = Label(text=(score), font="zebrazil 20 bold", fg="red", bg="white").pack()
                    img = PhotoImage(file="pictures/great.png")
                    labelimage.configure(image=img)
                    labelimage.image = img
                    labelresulttext.configure(text="You Are Excellent !!", fg="green")
                elif (score >= 20 and score < 40):

                    l = Label(text="Final Score", font="zebrazil 20 bold", bg="#ffffff").pack()
                    b = Label(text=(score), font="zebrazil 20 bold", fg="red", bg="#ffffff").pack()
                    img = PhotoImage(file="pictures/ok.png")
                    labelimage.configure(image=img)
                    labelimage.image = img
                    labelresulttext.configure(text="You Can Be Better !!", fg="green")
                else:
                    l = Label(text="Final Score", font="zebrazil 20 bold", bg="#ffffff").pack()
                    b = Label(text=(score), font="zebrazil 20 bold", fg="red", bg="#ffffff").pack()
                    img = PhotoImage(file="pictures/bad.png")
                    labelimage.configure(image=img)
                    labelimage.image = img
                    labelresulttext.configure(text="You Should Work Hard !!", fg="green")

            def calc():
                global indexes, user_answer
                x = 0
                score = 0
                for i in indexes:
                    if user_answer[x] == answers[i]:
                        # messagebox.showinfo("Result","Correct!")
                        score = score + 5

                    x += 1
                print(score)
                showresult(score)

            ques = 1

            def selected():
                global radiovar, user_answer
                global lblQuestion, r1, r2, r3, r4
                global ques
                x = radiovar.get()
                user_answer.append(x)
                radiovar.set(-1)
                if ques < 10:
                    lblQuestion.config(text=questions[indexes[ques]])
                    r1['text'] = answers_choice[indexes[ques]][0]
                    r2['text'] = answers_choice[indexes[ques]][1]
                    r3['text'] = answers_choice[indexes[ques]][2]
                    r4['text'] = answers_choice[indexes[ques]][3]
                    ques += 1
                else:
                    # print(indexes)
                    # print(user_answer)
                    # these two lines were just developement code
                    # we don't need them
                    calc()

            def startquiz():
                global lblQuestion, r1, r2, r3, r4
                lblQuestion = Label(
                    CQ,
                    text=questions[indexes[0]],
                    font=("Consolas", 20),
                    width=500,
                    justify="center",
                    wraplength=600,
                    background="#ffffff",
                )
                lblQuestion.pack(pady=(100, 30))

                global radiovar
                radiovar = IntVar()
                radiovar.set(-1)

                r1 = Radiobutton(
                    CQ,
                    text=answers_choice[indexes[0]][0],
                    font=("Times", 18),
                    value=0,
                    variable=radiovar,
                    command=selected,
                    background="#ffffff",
                )
                r1.pack(pady=5)

                r2 = Radiobutton(
                    CQ,
                    text=answers_choice[indexes[0]][1],
                    font=("Times", 18),
                    value=1,
                    variable=radiovar,
                    command=selected,
                    background="#ffffff",
                )
                r2.pack(pady=5)

                r3 = Radiobutton(
                    CQ,
                    text=answers_choice[indexes[0]][2],
                    font=("Times", 18),
                    value=2,
                    variable=radiovar,
                    command=selected,
                    background="#ffffff",
                )
                r3.pack(pady=5)

                r4 = Radiobutton(
                    CQ,
                    text=answers_choice[indexes[0]][3],
                    font=("Times", 18),
                    value=3,
                    variable=radiovar,
                    command=selected,
                    background="#ffffff",
                )
                r4.pack(pady=5)
                b2 = Button(CQ, text="EXIT", bg="white", fg="blue", font="Helvetica 16 bold",
                            command=CQ.destroy).place(x=1410, y=20)

                # stat = Label(text="Click to Answer!", bd=1, relief=SUNKEN, anchor=W).pack(side=BOTTOM, fill=X)

            def startIspressed():
                labelimage.destroy()
                labeltext.destroy()
                lblInstruction.destroy()
                lblRules.destroy()
                btnStart.destroy()
                gen()
                startquiz()

            CQ = Tk()
            CQ.title("Quizstart")
            CQ.geometry("1500x1500")
            CQ.config(background="#ffffff")
            # root.resizable(0,0)

            img1 = PhotoImage(file="pictures/qu2-removebg-preview.png")

            labelimage = Label(
                CQ,
                image=img1,
                background="#ffffff",
            )
            labelimage.pack(pady=(40, 0))

            labeltext = Label(
                CQ,
                text="code_to_hack",
                font=("Comic sans MS", 24, "bold"),
                background="#ffffff",
            )
            labeltext.pack(pady=(0, 50))

            img2 = PhotoImage(file="pictures/start_button-removebg-preview.png")

            btnStart = Button(
                CQ,
                image=img2,
                relief=FLAT,
                border=0,
                command=startIspressed,
                background="#ffffff",
            )
            btnStart.pack()

            lblInstruction = Label(
                CQ,
                text="Read The Rules And\nClick Start Once You Are ready",
                background="#ffffff",
                font=("Consolas", 20),
                justify="center",
            )
            lblInstruction.pack(pady=(100, 100))

            lblRules = Label(
                CQ,
                text="This quiz contains 10 questions\nOnce you select a radio button that will be a final "
                     "choice\nEach "
                     "right question carries 5 marks",
                width=100,
                font=("Times", 20),
                background="#000000",
                foreground="#FACA2F",
            )
            lblRules.pack(fill=X, side=BOTTOM)
            Button(CQ, text="LANG_SELECTION", bg="white", fg="blue", font="Helvetica 16 bold",
                   command=EXIT_AND_HOME).place(
                x=1150, y=20)
            CQ.mainloop()

        # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& C++ QUIZE &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        def CPP_quize():
            LS.destroy()
            with open('c++quiz.json', encoding="utf8") as f:
                data = json.load(f)

            # convert the dictionary in lists of questions and answers_choice
            questions = [v for v in data[0].values()]
            answers_choice = [v for v in data[1].values()]

            answers = [0, 2, 3, 3, 1, 3, 1, 2, 2, 0]

            def EXIT_AND_HOME():
                CQ.destroy()
                global user_answer
                global indexes
                global ques
                indexes.clear()
                user_answer.clear()
                ques = 0
                language_selection()

            def gen():
                global indexes
                while (len(indexes) < 10):
                    x = random.randint(0, 9)
                    if x in indexes:
                        continue
                    else:
                        indexes.append(x)

            def showresult(score):
                lblQuestion.destroy()
                r1.destroy()
                r2.destroy()
                r3.destroy()
                r4.destroy()
                labelimage = Label(
                    CQ,
                    background="#ffffff",
                    border=0,
                )
                labelimage.pack(pady=(50, 30))
                labelresulttext = Label(
                    CQ,
                    font=("Consolas", 20),
                    background="#ffffff",
                )
                labelresulttext.pack()
                var = IntVar()
                if score >= 40:
                    l = Label(text="Final Score", font="zebrazil 20 bold").pack()
                    b = Label(text=(score), font="zebrazil 20 bold", fg="red", bg="white").pack()
                    img = PhotoImage(file="pictures/great.png")
                    labelimage.configure(image=img)
                    labelimage.image = img
                    labelresulttext.configure(text="You Are Excellent !!", fg="green")
                elif (score >= 20 and score < 40):

                    l = Label(text="Final Score", font="zebrazil 20 bold", bg="#ffffff").pack()
                    b = Label(text=(score), font="zebrazil 20 bold", fg="red", bg="#ffffff").pack()
                    img = PhotoImage(file="pictures/ok.png")
                    labelimage.configure(image=img)
                    labelimage.image = img
                    labelresulttext.configure(text="You Can Be Better !!", fg="green")
                else:
                    l = Label(text="Final Score", font="zebrazil 20 bold", bg="#ffffff").pack()
                    b = Label(text=(score), font="zebrazil 20 bold", fg="red", bg="#ffffff").pack()
                    img = PhotoImage(file="pictures/bad.png")
                    labelimage.configure(image=img)
                    labelimage.image = img
                    labelresulttext.configure(text="You Should Work Hard !!", fg="green")

            def calc():
                global indexes, user_answer
                x = 0
                score = 0
                for i in indexes:
                    if user_answer[x] == answers[i]:
                        # messagebox.showinfo("Result","Correct!")
                        score = score + 5

                    x += 1
                print(score)
                showresult(score)

            ques = 1

            def selected():
                global radiovar, user_answer
                global lblQuestion, r1, r2, r3, r4
                global ques
                x = radiovar.get()
                user_answer.append(x)
                radiovar.set(-1)
                if ques < 10:
                    lblQuestion.config(text=questions[indexes[ques]])
                    r1['text'] = answers_choice[indexes[ques]][0]
                    r2['text'] = answers_choice[indexes[ques]][1]
                    r3['text'] = answers_choice[indexes[ques]][2]
                    r4['text'] = answers_choice[indexes[ques]][3]
                    ques += 1
                else:
                    # print(indexes)
                    # print(user_answer)
                    # these two lines were just developement code
                    # we don't need them
                    calc()

            def startquiz():
                global lblQuestion, r1, r2, r3, r4
                lblQuestion = Label(
                    CQ,
                    text=questions[indexes[0]],
                    font=("Consolas", 20),
                    width=500,
                    justify="center",
                    wraplength=600,
                    background="#ffffff",
                )
                lblQuestion.pack(pady=(100, 30))

                global radiovar
                radiovar = IntVar()
                radiovar.set(-1)

                r1 = Radiobutton(
                    CQ,
                    text=answers_choice[indexes[0]][0],
                    font=("Times", 18),
                    value=0,
                    variable=radiovar,
                    command=selected,
                    background="#ffffff",
                )
                r1.pack(pady=5)

                r2 = Radiobutton(
                    CQ,
                    text=answers_choice[indexes[0]][1],
                    font=("Times", 18),
                    value=1,
                    variable=radiovar,
                    command=selected,
                    background="#ffffff",
                )
                r2.pack(pady=5)

                r3 = Radiobutton(
                    CQ,
                    text=answers_choice[indexes[0]][2],
                    font=("Times", 18),
                    value=2,
                    variable=radiovar,
                    command=selected,
                    background="#ffffff",
                )
                r3.pack(pady=5)

                r4 = Radiobutton(
                    CQ,
                    text=answers_choice[indexes[0]][3],
                    font=("Times", 18),
                    value=3,
                    variable=radiovar,
                    command=selected,
                    background="#ffffff",
                )
                r4.pack(pady=5)
                b2 = Button(CQ, text="EXIT", bg="white", fg="blue", font="Helvetica 16 bold",
                            command=CQ.destroy).place(x=1420, y=20)

                # stat = Label(text="Click to Answer!", bd=1, relief=SUNKEN, anchor=W).pack(side=BOTTOM, fill=X)

            def startIspressed():
                labelimage.destroy()
                labeltext.destroy()
                lblInstruction.destroy()
                lblRules.destroy()
                btnStart.destroy()
                gen()
                startquiz()

            CQ = Tk()
            CQ.title("Quizstart")
            CQ.geometry("1500x1500")
            CQ.config(background="#ffffff")
            # root.resizable(0,0)

            img1 = PhotoImage(file="pictures/qu2-removebg-preview.png")

            labelimage = Label(
                CQ,
                image=img1,
                background="#ffffff",
            )
            labelimage.pack(pady=(40, 0))

            labeltext = Label(
                CQ,
                text="code_to_hack",
                font=("Comic sans MS", 24, "bold"),
                background="#ffffff",
            )
            labeltext.pack(pady=(0, 50))

            img2 = PhotoImage(file="pictures/start_button-removebg-preview.png")

            btnStart = Button(
                CQ,
                image=img2,
                relief=FLAT,
                border=0,
                command=startIspressed,
                background="#ffffff",
            )
            btnStart.pack()

            lblInstruction = Label(
                CQ,
                text="Read The Rules And\nClick Start Once You Are ready",
                background="#ffffff",
                font=("Consolas", 20),
                justify="center",
            )
            lblInstruction.pack(pady=(100, 100))

            lblRules = Label(
                CQ,
                text="This quiz contains 10 questions\nOnce you select a radio button that will be a final "
                     "choice\nEach right question carries 5 marks",
                width=100,
                font=("Times", 20),
                background="#000000",
                foreground="#FACA2F",
            )
            lblRules.pack(fill=X, side=BOTTOM)
            Button(CQ, text="LANG_SELECTION", bg="white", fg="blue", font="Helvetica 16 bold",
                   command=EXIT_AND_HOME).place(
                x=1150, y=20)
            CQ.mainloop()

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PYTHON QUIZE ----------------------------------------------------------
        def python_quize():
            LS.destroy()
            with open('python.json', encoding="utf8") as f:
                data = json.load(f)

            # convert the dictionary in lists of questions and answers_choice
            questions = [v for v in data[0].values()]
            answers_choice = [v for v in data[1].values()]

            answers = [2, 1, 0, 1, 3, 2, 1, 2, 3, 3]

            def EXIT_AND_HOME():
                CQ.destroy()
                global user_answer
                global indexes
                global ques
                user_answer.clear()
                indexes.clear()
                ques = 0
                language_selection()

            def gen():
                global indexes
                while (len(indexes) < 10):
                    x = random.randint(0, 9)
                    if x in indexes:
                        continue
                    else:
                        indexes.append(x)

            def showresult(score):
                lblQuestion.destroy()
                r1.destroy()
                r2.destroy()
                r3.destroy()
                r4.destroy()
                labelimage = Label(
                    CQ,
                    background="#ffffff",
                    border=0,
                )
                labelimage.pack(pady=(50, 30))
                labelresulttext = Label(
                    CQ,
                    font=("Consolas", 20),
                    background="#ffffff",
                )
                labelresulttext.pack()
                var = IntVar()
                if score >= 40:
                    l = Label(text="Final Score", font="zebrazil 20 bold").pack()
                    b = Label(text=(score), font="zebrazil 20 bold", fg="red", bg="white").pack()
                    img = PhotoImage(file="pictures/great.png")
                    labelimage.configure(image=img)
                    labelimage.image = img
                    labelresulttext.configure(text="You Are Excellent !!", fg="green")
                elif (score >= 20 and score < 40):

                    l = Label(text="Final Score", font="zebrazil 20 bold", bg="#ffffff").pack()
                    b = Label(text=(score), font="zebrazil 20 bold", fg="red", bg="#ffffff").pack()
                    img = PhotoImage(file="pictures/ok.png")
                    labelimage.configure(image=img)
                    labelimage.image = img
                    labelresulttext.configure(text="You Can Be Better !!", fg="green")
                else:
                    l = Label(text="Final Score", font="zebrazil 20 bold", bg="#ffffff").pack()
                    b = Label(text=(score), font="zebrazil 20 bold", fg="red", bg="#ffffff").pack()
                    img = PhotoImage(file="pictures/bad.png")
                    labelimage.configure(image=img)
                    labelimage.image = img
                    labelresulttext.configure(text="You Should Work Hard !!", fg="green")

            def calc():
                global indexes, user_answer
                x = 0
                score = 0
                for i in indexes:
                    if user_answer[x] == answers[i]:
                        # messagebox.showinfo("Result","Correct!")
                        score = score + 5

                    x += 1
                print(score)
                showresult(score)

            ques = 1

            def selected():
                global radiovar, user_answer
                global lblQuestion, r1, r2, r3, r4
                global ques
                x = radiovar.get()
                user_answer.append(x)
                radiovar.set(-1)
                if ques < 10:
                    lblQuestion.config(text=questions[indexes[ques]])
                    r1['text'] = answers_choice[indexes[ques]][0]
                    r2['text'] = answers_choice[indexes[ques]][1]
                    r3['text'] = answers_choice[indexes[ques]][2]
                    r4['text'] = answers_choice[indexes[ques]][3]
                    ques += 1
                else:
                    # print(indexes)
                    # print(user_answer)
                    # these two lines were just developement code
                    # we don't need them
                    calc()

            def startquiz():
                global lblQuestion, r1, r2, r3, r4
                lblQuestion = Label(
                    CQ,
                    text=questions[indexes[0]],
                    font=("Consolas", 20),
                    width=500,
                    justify="center",
                    wraplength=600,
                    background="#ffffff",
                )
                lblQuestion.pack(pady=(100, 30))

                global radiovar
                radiovar = IntVar()
                radiovar.set(-1)

                r1 = Radiobutton(
                    CQ,
                    text=answers_choice[indexes[0]][0],
                    font=("Times", 18),
                    value=0,
                    variable=radiovar,
                    command=selected,
                    background="#ffffff",
                )
                r1.pack(pady=5)

                r2 = Radiobutton(
                    CQ,
                    text=answers_choice[indexes[0]][1],
                    font=("Times", 18),
                    value=1,
                    variable=radiovar,
                    command=selected,
                    background="#ffffff",
                )
                r2.pack(pady=5)

                r3 = Radiobutton(
                    CQ,
                    text=answers_choice[indexes[0]][2],
                    font=("Times", 18),
                    value=2,
                    variable=radiovar,
                    command=selected,
                    background="#ffffff",
                )
                r3.pack(pady=5)

                r4 = Radiobutton(
                    CQ,
                    text=answers_choice[indexes[0]][3],
                    font=("Times", 18),
                    value=3,
                    variable=radiovar,
                    command=selected,
                    background="#ffffff",
                )
                r4.pack(pady=5)
                b2 = Button(CQ, text="EXIT", bg="white", fg="blue", font="Helvetica 16 bold",
                            command=CQ.destroy).place(x=1420, y=20)

                # stat = Label(text="Click to Answer!", bd=1, relief=SUNKEN, anchor=W).pack(side=BOTTOM, fill=X)

            def startIspressed():
                labelimage.destroy()
                labeltext.destroy()
                lblInstruction.destroy()
                lblRules.destroy()
                btnStart.destroy()
                gen()
                startquiz()

            CQ = Tk()
            CQ.title("Quizstart")
            CQ.geometry("1500x1500")
            CQ.minsize(900, 500)
            CQ.config(background="#ffffff")
            # root.resizable(0,0)

            img1 = PhotoImage(file="pictures/qu2-removebg-preview.png")

            labelimage = Label(
                CQ,
                image=img1,
                background="#ffffff",
            )
            labelimage.pack(pady=(40, 0))

            labeltext = Label(
                CQ,
                text="code_to_hack",
                font=("Comic sans MS", 24, "bold"),
                background="#ffffff",
            )
            labeltext.pack(pady=(0, 50))

            img2 = PhotoImage(file="pictures/start_button-removebg-preview.png")

            btnStart = Button(
                CQ,
                image=img2,
                relief=FLAT,
                border=0,
                command=startIspressed,
                background="#ffffff",
            )
            btnStart.pack()

            lblInstruction = Label(
                CQ,
                text="Read The Rules And\nClick Start Once You Are ready",
                background="#ffffff",
                font=("Consolas", 20),
                justify="center",
            )
            lblInstruction.pack(pady=(100, 100))

            lblRules = Label(
                CQ,
                text="This quiz contains 10 questions\nOnce you select a radio button that will be a final "
                     "choice\nEach "
                     "right question carries 5 marks",
                width=100,
                font=("Times", 20),
                background="#000000",
                foreground="#FACA2F",
            )
            lblRules.pack(fill=X, side=BOTTOM)
            Button(CQ, text="LANG_SELECTION", bg="white", fg="blue", font="Helvetica 16 bold",
                   command=EXIT_AND_HOME).place(
                x=1150, y=20)
            CQ.mainloop()

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PYTHON QUIZE END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def logout_module():
            LS.destroy()
            loginmodule()

        def HOME_window():
            LS.destroy()
            MAIN_WINDOW()



        def C_Excercise_practicle():
            LS.destroy()
            EX= Tk()
            def Que_2():
                EX.destroy()
                q1 = Tk()
                q1.title("Code_to_Hack")
                q1.geometry("1500x1500")
                label = Label(q1,
                              text="Que2)Insert a new line after 'Hello World', by using a special character: \n \nint "
                                   "main() { "
                                   "\ncout << 'Hello World! ';\ncout << 'I am learning C++';\nreturn "
                                   "0;\n}",
                              font="zebrazil 30 bold",
                              justify="center").pack(pady=200)
                userinput = Entry(q1, width=2,font = "Helvetica 20 bold",justify="center")
                userinput.place(x=935, y=340, width=100, height=50)

                ans = "<<endl"

                def ans_btn():
                    usr = userinput.get()
                    if ans == usr:
                        messagebox.showinfo("Result", "Correct Answer")
                    else:
                        messagebox.showerror("Result", "Wrong Answer")

                def show_ans():
                    Label(q1, text=(ans), bg="white", fg="blue",
                          font="Helvetica 16 bold").place(x=950, y=350)

                button3 = Button(q1, text="submit answer", bg="dark green", fg="white", padx=10, pady=10,
                                 command=ans_btn).place(x=450, y=550)
                Button(q1, text="SHOW_ANS", bg="dark green", fg="white", padx=10, pady=10,
                      command=show_ans).place(x=730, y=550)

                def Que_3():
                    q1.destroy()
                    q3 = Tk()
                    q3.title("Code_to_Hack")
                    q3.geometry("1500x1500")
                    label = Label(q3, text="Que 3)  ____   This is a Single line Comment\n", font="zebrazil 30 bold",
                                  justify="center").pack(pady=(200, 50))
                    userinput = Entry(q3, width=4,font = "Helvetica 20 bold",justify="center")
                    userinput.place(x=480, y=200, width=120, height=50)

                    ans = "//"

                    def ans_btn():
                        usr = userinput.get()
                        if ans == usr:
                            messagebox.showinfo("Result", "Correct Answer")
                        else:
                            messagebox.showerror("Result", "Wrong Answer")

                    def show_ans():
                        Label(q3, text=(ans), bg="white", fg="blue",
                              font="Helvetica 16 bold").place(x=500, y=210)
                    button3 = Button(q3, text="submit answer", bg="dark green", fg="white", padx=10, pady=10,
                                     command=ans_btn).place(x=450, y=550)
                    Button(q3, text="SHOW_ANS", bg="dark green", fg="white", padx=10, pady=10,
                           command=show_ans).place(x=730, y=550)

                    def Que_4():
                        q3.destroy()
                        q4 = Tk()
                        q4.title("Code_to_Hack")
                        q4.geometry("1500x1500")
                        label = Label(q4, text="Que 4) When a function call itself again and again, it is called \n",
                                      font="zebrazil 30 bold",
                                      justify="center").pack(pady=(200, 50))
                        userinput = Entry(q4, width=35,font = "Helvetica 20 bold",justify="center")
                        userinput.place(x=1320, y=200, width=180, height=50)

                        ans = "recursion"

                        def ans_btn():
                            usr = userinput.get()
                            if ans == usr:
                                messagebox.showinfo("Result", "Correct Answer")
                            else:
                                messagebox.showerror("Result", "Wrong Answer")

                        def show_ans():
                            Label(q4, text=(ans), bg="white", fg="blue",
                                  font="Helvetica 16 bold").place(x=1330, y=210)
                        button3 = Button(q4, text="submit answer", bg="dark green", fg="white", padx=10, pady=10,
                                         command=ans_btn).place(x=450, y=550)
                        Button(q4, text="SHOW_ANS", bg="dark green", fg="white", padx=10, pady=10,
                               command=show_ans).place(x=730, y=550)

                        def Que_5():
                            q4.destroy()
                            q5 = Tk()

                            def EXIT_LS():
                                q5.destroy()
                                language_selection()
                            q5.title("Code_to_Hack")
                            q5.geometry("1500x1500")
                            label = Label(q5, text="Que 5) A preprocessor directive begins with a symbol   ",
                                          font="zebrazil 30 bold",
                                          justify="center").pack(pady=(200, 50))
                            userinput = Entry(q5, width=35,font = "Helvetica 20 bold",justify="center")
                            userinput.place(x=1250, y=200, width=200, height=50)

                            ans = "#include"

                            def ans_btn():
                                usr = userinput.get()
                                if ans == usr:
                                    messagebox.showinfo("Result", "Correct Answer")
                                else:
                                    messagebox.showerror("Result", "Wrong Answer")

                            def show_ans():
                                Label(q5, text=(ans), bg="white", fg="blue",
                                      font="Helvetica 16 bold").place(x=1280, y=210)
                            button3 = Button(q5, text="submit answer", bg="dark green", fg="white", padx=10, pady=10,
                                             command=ans_btn).place(x=450, y=550)

                            Button(q5, text="LANG_SELECTION", bg="white", fg="blue", font="Helvetica 16 bold",
                                   command=EXIT_LS).place(
                                x=1150, y=20)
                            b2 = Button(q5, text="EXIT", bg="white", fg="blue", font="Helvetica 16 bold",
                                        command=q5.destroy).place(x=1410, y=20)
                            Button(q5, text="SHOW_ANS", bg="dark green", fg="white", padx=10, pady=10,
                                   command=show_ans).place(x=730, y=550)

                        Button(q4, text="NEXT", bg="dark green", fg="white", padx=10, pady=10,
                               command=Que_5).place(x=650, y=550)

                    Button(q3, text="NEXT", bg="dark green", fg="white", padx=10, pady=10,
                           command=Que_4).place(x=650, y=550)

                Button(q1, text="NEXT", bg="dark green", fg="white", padx=10, pady=10,
                       command=Que_3).place(x=650, y=550)

            EX.title("Code_to_Hack")

            EX.geometry("1500x1500")

            label = Label(EX, text="Que1)Insert the missing part of the code below to output 'Hello World'.\n \nint "
                                   "main() { "
                                   "\n_ _____ << Hello World!;\nreturn 0\n }", font="zebrazil 30 bold",
                          justify="center").pack(pady=200)
            userin = Entry(EX,font = "Helvetica 20 bold",justify="center")
            userin.place(x=470, y=340, width=200, height=50)

            q1ans = "cout"

            def que1ans():

                usr = userin.get()
                if q1ans == usr:
                    messagebox.showinfo("Result", "Correct Answer")
                else:
                    messagebox.showerror("Result", "Wrong Answer")

            def show_ans():
                Label(EX, text=(q1ans), bg="white", fg="blue",
                      font="Helvetica 16 bold").place(x=480, y=355)

            Button(EX, text="submit answer", bg="dark green", fg="white", padx=10, pady=10,
                   command=que1ans).place(x=450, y=550)
            Button(EX, text="NEXT", bg="dark green", fg="white", padx=10, pady=10,
                   command=Que_2).place(x=650, y=550)
            Button(EX, text="SHOW_ANS", bg="dark green", fg="white", padx=10, pady=10,
                   command=show_ans).place(x=730, y=550)
            EX.mainloop()

        def python_Excercise():
            LS.destroy()
            EX = Tk()
            def Que_2():
                EX.destroy()
                q1 = Tk()
                q1.title("Code_to_Hack")
                q1.geometry("1500x1500")
                label = Label(q1,
                              text="Que2) Create a variable named carname which is assigned the value Volvo to it.\n\n= 'Volvo'",
                              font="zebrazil 30 bold",
                              justify="center").pack(pady=200)
                userinput = Entry(q1, width=2, font="Helvetica 20 bold", justify="center")
                userinput.place(x=450, y=290, width=200, height=50)

                ans2 = "carname"

                def ans_btn():
                    usr = userinput.get()
                    if ans2 == usr:
                        messagebox.showinfo("Result", "Correct Answer")
                    else:
                        messagebox.showerror("Result", "Wrong Answer")

                button3 = Button(q1, text="submit answer", bg="dark green", fg="white", padx=10, pady=10,
                                 command=ans_btn).place(x=450, y=550)

                def Que_3():
                    q1.destroy()
                    q3 = Tk()
                    q3.title("Code_to_Hack")
                    q3.geometry("1500x1500")
                    label = Label(q3, text="Que 3)             This is a Single line Comment\n",
                                  font="zebrazil 30 bold",
                                  justify="center").pack(pady=(200, 50))
                    userinput = Entry(q3, width=4, font="Helvetica 20 bold", justify="center")
                    userinput.place(x=480, y=200, width=120, height=50)

                    ans3 = "#"

                    def ans_btn():
                        usr = userinput.get()
                        if ans3 == usr:
                            messagebox.showinfo("Result", "Correct Answer")
                        else:
                            messagebox.showerror("Result", "Wrong Answer")

                    button3 = Button(q3, text="submit answer", bg="dark green", fg="white", padx=10, pady=10,
                                     command=ans_btn).place(x=450, y=550)

                    def Que_4():
                        q3.destroy()
                        q4 = Tk()
                        q4.title("Code_to_Hack")
                        q4.geometry("1500x1500")
                        label = Label(q4,
                                      text="Que 4) Display the sum of 5 + 10, using two variables: x and y.\nx= 5\ny=10\nprint(x    y)",
                                      font="zebrazil 30 bold",
                                      justify="center").pack(pady=(200, 50))
                        userinput = Entry(q4, width=35, font="Helvetica 20 bold", justify="center")
                        userinput.place(x=770, y=350, width=40, height=40)

                        ans4 = "+"

                        def ans_btn():
                            usr = userinput.get()
                            if ans4 == usr:
                                messagebox.showinfo("Result", "Correct Answer")
                            else:
                                messagebox.showerror("Result", "Wrong Answer")

                        button3 = Button(q4, text="submit answer", bg="dark green", fg="white", padx=10, pady=10,
                                         command=ans_btn).place(x=450, y=550)

                        def Que_5():
                            q4.destroy()
                            q5 = Tk()

                            def EXIT_LS():
                                q5.destroy()
                                language_selection()

                            q5.title("Code_to_Hack")
                            q5.geometry("1500x1500")
                            label = Label(q5,
                                          text="Que 5) Insert the correct keyword to make the variable x belong to the global scope.\ndef myfunc():\n        x\nx = 'fantastic'",
                                          font="zebrazil 30 bold",
                                          justify="center").pack(pady=(200, 50))
                            userinput = Entry(q5, width=35, font="Helvetica 20 bold", justify="center")
                            userinput.place(x=560, y=300, width=200, height=50)

                            ans5 = "global"

                            def ans_btn():
                                usr = userinput.get()
                                if ans5 == usr:
                                    messagebox.showinfo("Result", "Correct Answer")
                                else:
                                    messagebox.showerror("Result", "Wrong Answer")

                            button3 = Button(q5, text="submit answer", bg="dark green", fg="white", padx=10, pady=10,
                                             command=ans_btn).place(x=450, y=550)
                            Button(q5, text="LANG_SELECTION", bg="white", fg="blue", font="Helvetica 16 bold",
                                   command=EXIT_LS).place(
                                x=1150, y=20)
                            b2 = Button(q5, text="EXIT", bg="white", fg="blue", font="Helvetica 16 bold",
                                        command=q5.destroy).place(x=1410, y=20)

                            def show_ans():
                                Label(q5, text=(ans5), bg="white", fg="blue",
                                      font="Helvetica 20 bold").place(x=570, y=310)

                            Button(q5, text="SHOW_ANS", bg="dark green", fg="white", padx=10, pady=10,
                                   command=show_ans).place(x=740, y=550)

                        Button(q4, text="NEXT", bg="dark green", fg="white", padx=10, pady=10,
                               command=Que_5).place(x=650, y=550)

                        def show_ans():
                            Label(q4, text=(ans4), bg="white", fg="blue",
                                  font="Helvetica 20 bold").place(x=780, y=353)

                        Button(q4, text="SHOW_ANS", bg="dark green", fg="white", padx=10, pady=10,
                               command=show_ans).place(x=740, y=550)

                    Button(q3, text="NEXT", bg="dark green", fg="white", padx=10, pady=10,
                           command=Que_4).place(x=650, y=550)

                    def show_ans():
                        Label(q3, text=(ans3), bg="white", fg="blue",
                              font="Helvetica 20 bold").place(x=490, y=210)

                    Button(q3, text="SHOW_ANS", bg="dark green", fg="white", padx=10, pady=10,
                           command=show_ans).place(x=740, y=550)

                Button(q1, text="NEXT", bg="dark green", fg="white", padx=10, pady=10,
                       command=Que_3).place(x=650, y=550)

                def show_ans():
                    Label(q1, text=(ans2), bg="white", fg="blue",
                          font="Helvetica 20 bold").place(x=470, y=300)

                Button(q1, text="SHOW_ANS", bg="dark green", fg="white", padx=10, pady=10,
                       command=show_ans).place(x=740, y=550)

            EX.title("Code_to_Hack")

            EX.geometry("1500x1500")

            label = Label(EX,
                          text="Que1) Insert the missing part of the code below to output 'Hello World'.\n \n__   ('Hello "
                               "World') ",
                          font="zebrazil 30 bold",
                          justify="center").pack(pady=200)
            userin = Entry(EX, font="Helvetica 20 bold", justify="center")
            userin.place(x=430, y=300, width=200, height=50)

            q1ans = "print"

            def que1ans():

                usr = userin.get()

                if q1ans == usr:
                    messagebox.showinfo("Result", "Correct Answer")
                else:
                    messagebox.showerror("Result", "Wrong Answer")

            def show_ans():
                Label(EX, text=(q1ans), bg="white", fg="blue",
                      font="Helvetica 20 bold").place(x=450, y=310)

            Button(EX, text="submit answer", bg="dark green", fg="white", padx=10, pady=10,
                   command=que1ans).place(x=450, y=550)
            Button(EX, text="NEXT", bg="dark green", fg="white", padx=10, pady=10,
                   command=Que_2).place(x=650, y=550)
            Button(EX, text="SHOW_ANS", bg="dark green", fg="white", padx=10, pady=10,
                   command=show_ans).place(x=740, y=550)

            EX.mainloop()



        Button(LS, text="LOGOUT", bg="white", fg="red", font="Helvetica 16 bold",
               command=logout_module).place(x=1250, y=30)
        Button(LS, image=pic1, padx=50, pady=10, command=C_quize).place(x=150, y=370)
        Button(LS, image=pic2, padx=50, pady=10, command=CPP_quize).place(x=150, y=470)
        Button(LS, image=pic3, padx=50, pady=10, command=python_quize).place(x=150, y=570)
        Button(LS, text="Profile", bg="white", fg="blue", font="Helvetica 16 bold", command=show_profile).place(
            x=1150, y=30)
        Button(LS, text="HOME", bg="white", fg="blue", font="Helvetica 16 bold", command=HOME_window).place(
            x=1050, y=30)
        Button(LS, image=pic4, padx=4, pady=5, command=C_Excercise_practicle).place(x=930, y=370,width=100,height=100)
        Button(LS, image=pic5, padx=14, pady=13,command=python_Excercise).place(x=930, y=500, width=100,
                                                                                      height=100)
        LS.mainloop()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ LANGUAGE SELECTION AND QUIZE ENDS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    root.geometry("1520x1510")

    root.title("Homepage")
    root.config(background="light blue")
    button1 = Button(root, text="CONTACT US", bg="white", fg="blue", font="Helvetica 16 bold",
                     command=contact_show).place(
        x=1350, y=20)
    button2 = Button(root, text="GET STARTED", bg="dark green", fg="white", padx=10, pady=10,
                     command=registering_user).place(
        x=350, y=650)
    button3 = Button(root, text="I ALREADY HAVE AN ACCOUNT", bg="dark green", fg="white", padx=10, pady=10,
                     command=loginmodule).place(x=550, y=650)

    photo = PhotoImage(file="pictures/imghome.png")

    pic_label = Label(root, image=photo, padx=70, pady=20, background="light blue").place(x=1000, y=200)

    root.label = Label(root, text="Learning a Language\n is Fun", fg="navy", font="zebrazil 50 bold",
                       background="light blue",
                       padx=70, pady=20).place(x=100, y=400)
    root.mainloop()


MAIN_WINDOW()
