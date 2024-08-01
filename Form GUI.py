from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
def getvals():
    Firstname = Fisrt_Nameentry.get()
    Lastname = Last_Nameentry.get()
    Title = Title_Combo.get()
    Gender = Gender_combo.get()
    City = Cityentry.get()
    Course = Course_combo.get()
    Contact_Num = Student_contact_numentry.get()
    Email_address = Emailentry.get()
    
    print("Title: ", Title, "First_name: ",Firstname,"Last_Name: ",Lastname, "City: ", City, "Course_Name: ", Course, "Contact_Num: ", Contact_Num,"Email: ",Email_address)                           
    
    
    

root.geometry("800x300")
root.title("Application Form")
User_Inf0 = Label(root,text = "User_Inforamation",font="Arial 13 bold")
User_Inf0.grid(row = 0,column= 1)
First_Name = Label(root,text = "Name")
First_Name.grid(row = 1,column = 5,padx = 10,pady = 5)
First_Namevalue = StringVar()
Fisrt_Nameentry = Entry(root, textvariable = First_Namevalue)
Fisrt_Nameentry.grid(row = 1,column = 6)

Last_Name = Label(root,text = "Last Name")
Last_Name.grid(row = 1, column = 3,padx = 10,pady = 5)
Last_Namevalue = StringVar()
Last_Nameentry = Entry(root, textvariable = Last_Namevalue)
Last_Nameentry.grid(row = 1,column = 4)


Title = Label(root,text = "Title")
Title.grid(row = 1, column = 1,padx = 10,pady = 5)
Titlevalue = StringVar()
#Titleentry = Entry(root, textvariable = Titlevalue)
Title_Combo= ttk.Combobox(root,values = ["Mrs","Miss","Mr","Mst"])
Title_Combo.grid(row = 1,column = 2)


Gender = Label(root,text = "Gender")
Gender.grid(row = 2, column = 3,padx = 10,pady = 5)
Gendervalue = StringVar()
Genderentry = Entry(root, textvariable = Gendervalue)
Gender_combo = ttk.Combobox(root,values = ["Male","Female"])
Gender_combo.grid(row = 2,column = 4)

Age = Label(root,text = "Age")
Age.grid(row = 2, column = 5,padx = 10,pady = 5)
Agevalue = IntVar()
Ageentry = Entry(root, textvariable = Agevalue)
#Age = ttk.Combobox(root,values = ["Male","Female"])
Ageentry.grid(row = 2,column = 6)

City = Label(root,text = "City")
City.grid(row = 2, column = 1,padx = 10,pady = 5)
Cityvalue = StringVar()
Cityentry = Entry(root, textvariable = Cityvalue)
Cityentry.grid(row = 2,column = 2)

IT_Course = Label(root,text = "IT Course Info", font="Arial 13 bold")
IT_Course.grid(row = 4, column= 1)



Course_Name = Label(root,text = "Course_Name")
Course_Name .grid(row = 5, column = 1,padx = 10,pady = 5)
Course_Namevalue = StringVar()
Course_Nameentry = Entry(root, textvariable =Course_Namevalue)
Course_combo = ttk.Combobox(root,values = ["Data Analyst","Developer", "Tester", "Data Science", "Machine learning"])
Course_combo.grid(row = 5,column = 2)

Contact_details = Label(root,text = "Stud_Contact_Details", font="Arial 13 bold")
Contact_details.grid(row = 6, column= 1)

Student_contact_num = Label(root,text = "Student_contact_num")
Student_contact_num.grid(row = 7, column = 1,padx = 10,pady = 5)
Student_contact_numvalue = StringVar()
Student_contact_numentry = Entry(root, textvariable =Student_contact_numvalue)
Student_contact_numentry.grid(row = 7,column = 2)

Email = Label(root,text = "Email")
Email.grid(row = 7, column = 3,padx = 10,pady = 5)
Emailvalue = StringVar()
Emailentry = Entry(root, textvariable =Email)
Emailentry.grid(row = 7,column = 4)


terms_var = IntVar()
terms_checkbox = Checkbutton(root, text="I accept the terms and conditions", variable=terms_var)
terms_checkbox.grid(row=8, column=3, sticky="w", padx=20, pady=10)
Button = Button(text = "Submit", command =getvals).grid(row=9,column =3)





root.mainloop()
