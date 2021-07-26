from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
import pymysql



class ConnectorDatabase:

    def __init__(self, root):
        self.root = root
        self.root.title("STUDENT MANAGNMENT SYSTEM")
        self.root.geometry("1260x700+0+0")
        self.root.resizable(False, False)
        self.root.iconbitmap("Images/Logo2.ico")




        MainFrame = Frame(self.root, bd=10, width=1245, height=670, relief=GROOVE, bg="cyan2")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=1245, height=100, relief=GROOVE,bg="light cyan")
        TitleFrame.grid(row=0, column=0)
        TopFrame3 = Frame(MainFrame, bd=5, width=1245, height=670, relief=GROOVE,bg="salmon")
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=1245, height=670, padx=2, bg="maroon1", relief=GROOVE)
        LeftFrame.pack(side=LEFT,fill = X)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=510, height=670, padx=10, pady=9, bg="Lightcyan2", relief=GROOVE)
        LeftFrame1.pack(side=LEFT)

        RightFrame1 = Frame(TopFrame3, bd=5, width=600, height=670, padx=2, bg="tomato", relief=GROOVE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=700, height=671, padx=2, pady=7, bg="Lightcyan2", relief=GROOVE)
        RightFrame1a.pack(side=RIGHT)

        # ----------------------------------Variables---------------------------------------

        StudentID = StringVar()
        Branch = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        EmailID = StringVar()
        Contact = StringVar()
        Gender = StringVar()
        DOBs = StringVar()
        Address = StringVar()

        # -------------------------------------------------------------------------

        def iExit():
            iExit = tkinter.messagebox.askyesno("STUDENT MANAGNMENT SYSTEM", "Confirm, you want to Exit")
            if iExit > 0:
                root.destroy()
                return

        def Clear():
            self.entStudentID.delete(0, END)
            Branch.set("Select Branch")
            self.entFirstname.delete(0, END)
            self.entLastname.delete(0, END)
            self.entEmailID.delete(0, END)
            self.entContact.delete(0, END)
            Gender.set("Select Gender")
            self.entDOBs.delete(0, END)
            self.entAddress.delete(0, END)
            self.entSearch.delete(0,END)

        def addData():
            if StudentID.get() == "" or Branch.get() == "" or Firstname.get() == "" or Lastname.get() == "" or EmailID.get() == "" or Contact.get() == "" or Gender.get() == "" or DOBs.get() == "" or Address.get == "":
                tkinter.messagebox.showerror("STUDENT MANAGNMENT SYSTEM", "Enter Correct Details, Fill all Details")
            else:
                sqlCon = pymysql.connect(host="Localhost", user="root", passwd="joy00004", database="studentdatabase")
                cur = sqlCon.cursor()
                cur.execute("insert into studentdb values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                    StudentID.get(),
                    Branch.get(),
                    Firstname.get(),
                    Lastname.get(),
                    EmailID.get(),
                    Contact.get(),
                    Gender.get(),
                    DOBs.get(),
                    Address.get(),
                ))
                sqlCon.commit()
                # DisplayData()
                sqlCon.close()
                tkinter.messagebox.showinfo("STUDENT MANAGNMENT SYSTEM", "Your Data has been stored sucessfully")

        def DisplayData():
            sqlCon = pymysql.connect(host="Localhost", user="root", passwd="joy00004", database="studentdatabase")
            cur = sqlCon.cursor()
            cur.execute("SELECT * FROM studentdatabase.studentdb")
            result = cur.fetchall()
            if len(result) != 0:
                self.student_records.delete(*self.student_records.get_children())
                for row in result:
                    self.student_records.insert("", END, values=row)
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("STUDENT MANAGNMENT SYSTEM", "Now, You can see whole Data of Students")

        def SearchData():
            searched = self.entSearch.get()
            sqlCon = pymysql.connect(host="Localhost", user="root", passwd="joy00004", database="studentdatabase")
            cur = sqlCon.cursor()
            cur.execute("SELECT * FROM studentdatabase.studentdb where rollno=%s",searched)
            result = cur.fetchall()

            if len(result) != 0:
                self.student_records.delete(*self.student_records.get_children())
                for row in result:
                    self.student_records.insert("", END, values=row)
                    tkinter.messagebox.showinfo("STUDENT MANAGNMENT SYSTEM", "Now, You can see data of " + searched)

            else:
                tkinter.messagebox.showerror("STUDENT MANAGNMENT SYSTEM", "Your Data is not found of "+searched)
            sqlCon.commit()
            sqlCon.close()




        def studentdatabaseinfo(ev):
            viewInfo = self.student_records.focus()
            learnerData = self.student_records.item(viewInfo)
            row = learnerData["values"]
            StudentID.set(row[0])
            Branch.set(row[1])
            Firstname.set(row[2])
            Lastname.set(row[3])
            EmailID.set(row[4])
            Contact.set(row[5])
            Gender.set(row[6])
            DOBs.set(row[7])
            Address.set(row[8])

        def Update():
            sqlCon = pymysql.connect(host="Localhost", user="root", passwd="joy00004", database="studentdatabase")
            cur = sqlCon.cursor()
            cur.execute(
                "update studentdb set  branch =%s, firstname =%s, lastname =%s, email=%s, contact=%s, gender=%s,dob=%s, address=%s where rollno=%s",
                (
                    Branch.get(),
                    Firstname.get(),
                    Lastname.get(),
                    EmailID.get(),
                    Contact.get(),
                    Gender.get(),
                    DOBs.get(),
                    Address.get(),
                    StudentID.get(),
                ))
            sqlCon.commit()
            # DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("STUDENT MANAGNMENT SYSTEM", "Your Data has been Updated sucessfully")

        def Delete():
            sqlCon = pymysql.connect(host="Localhost", user="root", passwd="joy00004", database="studentdatabase")
            cur = sqlCon.cursor()
            cur.execute("delete from studentdb where rollno=%s", StudentID.get())

            sqlCon.commit()
            # DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("STUDENT MANAGNMENT SYSTEM", "Your Data has been Deleted sucessfully")

        # --------------------------------Labels And Entry-----------------------------------------
        # self.logo = Image.open("Images/download.png")
        # self.resized = self.logo.resize((225,300), Image.ANTIALIAS)
        # self.new_logo = ImageTk.PhotoImage(self.resized)

        self.logo = ImageTk.PhotoImage(file="Images/Image1.png")
        self.logoClg = ImageTk.PhotoImage(file="Images/CollegeLogo.png")

        self.lbltitle = Label(TitleFrame, padx=10, compound=RIGHT, image=self.logoClg, bd=7, bg="light cyan", fg="purple4")
        self.lbltitle.grid(row=0, column=1, padx=10)

        self.lbltitle = Label(TitleFrame,padx=40,compound=LEFT,image=self.logo, font=("arial", 40, "bold"), text="STUDENT MANAGNMENT SYSTEM",bd=7,bg="light cyan",fg="purple4")
        self.lbltitle.grid(row=0, column=0)

        # ----------------------------------------------------------------------------------------------

        self.lblStudentID = Label(LeftFrame1, font=("arial", 8, "bold"), text="Roll No:", bd=7,bg="Lightcyan2")
        self.lblStudentID.grid(row=0, column=0, sticky=W, padx=2)
        self.entStudentID = Entry(LeftFrame1, font=("arial", 8, "bold"), bd=7, width=45, justify="left",
                                  textvariable=StudentID)
        self.entStudentID.grid(row=0, column=1, sticky=W, padx=2)

        self.lblBranch = Label(LeftFrame1, font=("arial", 8, "bold"), text="Branch:", bd=7, bg="Lightcyan2")
        self.lblBranch.grid(row=1, column=0, sticky=W, padx=2)
        self.entBranch = ttk.Combobox(LeftFrame1, font=("arial", 8, "bold"), width=44, state="readonly",
                                      textvariable=Branch)
        self.entBranch["values"] = ("Select Branch", "Computer", "Mechanical", "Civil", "Electronics and "
                                                                                        "telecommunication")
        self.entBranch.current(0)
        self.entBranch.grid(row=1, column=1, sticky=W, padx=2)

        self.lblFirstname = Label(LeftFrame1, font=("arial", 8, "bold"), text="First Name:", bd=7,bg="Lightcyan2")
        self.lblFirstname.grid(row=2, column=0, sticky=W, padx=2)
        self.entFirstname = Entry(LeftFrame1, font=("arial", 8, "bold"), bd=7, width=45, justify="left",
                                  textvariable=Firstname)
        self.entFirstname.grid(row=2, column=1, sticky=W, padx=2)

        self.lblLastname = Label(LeftFrame1, font=("arial", 8, "bold"), text="Last Name:", bd=7,bg="Lightcyan2")
        self.lblLastname.grid(row=3, column=0, sticky=W, padx=2)
        self.entLastname = Entry(LeftFrame1, font=("arial", 8, "bold"), bd=7, width=45, justify="left",
                                 textvariable=Lastname)
        self.entLastname.grid(row=3, column=1, sticky=W, padx=2)

        self.lblEmailID = Label(LeftFrame1, font=("arial", 8, "bold"), text="Email ID:", bd=7,bg="Lightcyan2")
        self.lblEmailID.grid(row=4, column=0, sticky=W, padx=2)
        self.entEmailID = Entry(LeftFrame1, font=("arial", 8, "bold"), bd=7, width=45, justify="left",
                                textvariable=EmailID)
        self.entEmailID.grid(row=4, column=1, sticky=W, padx=2)

        self.lblContact = Label(LeftFrame1, font=("arial", 8, "bold"), text="Contact No:", bd=7,bg="Lightcyan2")
        self.lblContact.grid(row=5, column=0, sticky=W, padx=2)
        self.entContact = Entry(LeftFrame1, font=("arial", 8, "bold"), bd=7, width=45, justify="left",
                                textvariable=Contact)
        self.entContact.grid(row=5, column=1, sticky=W, padx=2)

        self.lblGender = Label(LeftFrame1, font=("arial", 8, "bold"), text="Gender:", bd=7,bg="Lightcyan2")
        self.lblGender.grid(row=6, column=0, sticky=W, padx=2)
        self.entGender = ttk.Combobox(LeftFrame1, font=("arial", 8, "bold"), width=44, state="readonly",
                                      textvariable=Gender)
        self.entGender["values"] = ("Select Gender", "Male", "Female", "Other")
        self.entGender.current(0)
        self.entGender.grid(row=6, column=1, sticky=W, padx=2)

        self.lblDOBs = Label(LeftFrame1, font=("arial", 8, "bold"), text="Date Of Birth:", bd=7,bg="Lightcyan2")
        self.lblDOBs.grid(row=7, column=0, sticky=W, padx=2)
        self.entDOBs = Entry(LeftFrame1, font=("arial", 8, "bold"), bd=7, width=45, justify="left", textvariable=DOBs)
        self.entDOBs.grid(row=7, column=1, sticky=W, padx=2)

        self.lblAddress = Label(LeftFrame1, font=("arial", 8, "bold"), text="Address:", bd=7,bg="Lightcyan2")
        self.lblAddress.grid(row=8, column=0, sticky=W, padx=2)
        self.entAddress = Entry(LeftFrame1, font=("arial", 8, "bold"), bd=7, width=45, justify="left",
                                textvariable=Address)
        self.entAddress.grid(row=8, column=1, sticky=W, padx=2)

        # ---------------------------Separate Label for Search Entry----------------------------------------------

        self.entSearch = Entry(LeftFrame1,font=("arial", 8, "bold"), bd=7, width=30, justify="left")
        self.entSearch.grid(row=12, column=1, sticky=W, padx=45)

        # ---------------------------Preview Table Screen----------------------------------------------
        scroll_y = Scrollbar(RightFrame1a, orient=VERTICAL)

        self.student_records = ttk.Treeview(RightFrame1a, height=24,
                                            columns=("StudentID","Branch", "Firstname", "Lastname", "EmailID",
                                                     "Contact", "Gender", "DOBs", "Address"),
                                            yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_records.heading("StudentID", text="Roll No")
        self.student_records.heading("Branch", text="Branch")
        self.student_records.heading("Firstname", text="First Name")
        self.student_records.heading("Lastname", text="Last Name")
        self.student_records.heading("EmailID", text="Email ID")
        self.student_records.heading("Contact", text="Contact No")
        self.student_records.heading("Gender", text="Gender")
        self.student_records.heading("DOBs", text="Date Of Birth")
        self.student_records.heading("Address", text="Address")

        self.student_records["show"] = "headings"

        self.student_records.column("StudentID", width=50)
        self.student_records.column("Branch", width=90)
        self.student_records.column("Firstname", width=70)
        self.student_records.column("Lastname", width=70)
        self.student_records.column("EmailID", width=120)
        self.student_records.column("Contact", width=70)
        self.student_records.column("Gender", width=50)
        self.student_records.column("DOBs", width=80)
        self.student_records.column("Address", width=130)

        self.student_records.pack(fill=BOTH, expand=1)
        self.student_records.bind("<ButtonRelease-1>", studentdatabaseinfo)

        # ---------------------------Buttons----------------------------------------------

        self.btAddNew = Button(LeftFrame1, font=("arial", 11, "bold"), text="Add New", bd=10,bg="chartreuse2",fg="black",
                               width=10, height=1, command=addData).grid(row=9, column=0, padx=0, pady=10)

        self.btUpdate = Button(LeftFrame1, font=("arial", 11, "bold"), text="Update", bd=10,bg="chartreuse2",fg="black",
                               width=10, height=1, command=Update).grid(row=9, column=1, padx=0, pady=5)

        self.btDelete = Button(LeftFrame1, font=("arial", 11, "bold"), text="Delete", bd=10,bg="chartreuse2",fg="black",
                               width=10, height=1, command=Delete).grid(row=10, column=0, padx=0, pady=5)

        self.btClear = Button(LeftFrame1, font=("arial", 11, "bold"), text="Clear", bd=10,bg="chartreuse2",fg="black",
                              width=10, height=1, command=Clear).grid(row=10, column=1, padx=0, pady=5)

        self.btSearch = Button(LeftFrame1, font=("arial", 9, "bold"), text="Search:Roll No", bd=10,bg="RoyalBlue1",fg="LightYellow2",
                               width=12, height=1,command=SearchData).grid(row=12, column=0, padx=0, pady=5)

        self.btDisplay = Button(LeftFrame1, font=("arial", 11, "bold"), text="Show All", bd=10,bg="chartreuse2",fg="black",
                                width=10, height=1, command=DisplayData).grid(row=11, column=0, padx=0, pady=5)

        self.btExit = Button(LeftFrame1, font=("arial", 11, "bold"), text="Exit", bd=10,bg="red",fg="black",
                             width=10, height=1,command=iExit).grid(row=11, column=1, padx=0, pady=5)


if __name__ == "__main__":
    root = Tk()
    application = ConnectorDatabase(root)
    root.mainloop()




