

from tkinter import *
from tkinter import ttk
import pymysql




class Myclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1500x800')
        title=Label(self.root,text="WELCOME TO STUDENTS INFORMATION",bd=3,bg='gray',fg='white',relief='raised',font=('cooper black',40))
        title.pack(fill='x')



        #creating variables
        self.rollNoVar=StringVar()
        self.fnameVar=StringVar()
        self.lnameVar=StringVar()
        self.cnameVar=StringVar()
        self.mobileVar=StringVar()
        self.emailVar=StringVar()
        self.feeVar=StringVar()
        self.qualificationVar=StringVar()


        #CREATING FORMFRAME
        formFrame=Frame(self.root,bg='beige')
        formFrame.place(x=10,y=80,width=500,height=700)

        #creating display frame
        displayFrame=Frame(self.root,bg='gray')
        displayFrame.place(x=520,y=80,width=970,height=700)

        ########working on formframe
        title1=Label(formFrame,text="Data ENTRY Here!!!",font=('book antique',15),bg="cyan",fg="red",bd=3,relief="raised")
        title1.grid(row=0,columnspan=2,padx=140,pady=10)

        #roll no
        rollb1=Label(formFrame,text="Enter Roll No:",font=("book antiqua",15),bg='skyblue',fg="Black")
        rollb1.grid(row=1,column=0,sticky='W')

        #creating inputbox
        rollEntry=Entry(formFrame,font=('book antiqua',15),text=self.rollNoVar)
        rollEntry.grid(row=1,column=1,sticky='w',pady=10)

        #first name
        f1=Label(formFrame,text="Enter first name:",font=("book antiqua",15),bg='skyblue',fg="Black")
        f1.grid(row=2,column=0,sticky='W')

        #creating inputbox
        f1Entry=Entry(formFrame,font=('book antiqua',15),text=self.fnameVar)
        f1Entry.grid(row=2,column=1,sticky='w',pady=10)


        

        
        #last name
        l1=Label(formFrame,text="Enter Last name:",font=("book antiqua",15),bg='skyblue',fg="Black")
        l1.grid(row=3,column=0,sticky='W')

        #creating inputbox
        l1Entry=Entry(formFrame,font=('book antiqua',15),text=self.lnameVar)
        l1Entry.grid(row=3,column=1,sticky='w',pady=10)


        #course
        course=Label(formFrame,text="Enter Course Name:",font=("book antiqua",15),bg='skyblue',fg="Black")
        course.grid(row=4,column=0,sticky='W')

        #creating inputbox
        feeEntry=Entry(formFrame,font=('book antiqua',15),text=self.cnameVar)
        feeEntry.grid(row=4,column=1,sticky='w',pady=10)

                
        #mobile number 
        mobile=Label(formFrame,text="Enter Number:",font=("book antiqua",15),bg='skyblue',fg="Black")
        mobile.grid(row=5,column=0,sticky='W')

        #creating inputbox
        mobileEntry=Entry(formFrame,font=('book antiqua',15),text=self.mobileVar)
        mobileEntry.grid(row=5,column=1,sticky='w',pady=10)

                
        #email
        email=Label(formFrame,text="Enter Email id:",font=("book antiqua",15),bg='skyblue',fg="Black")
        email.grid(row=6,column=0,sticky='W')

        #creating inputbox
        emailEntry=Entry(formFrame,font=('book antiqua',15),text=self.emailVar)
        emailEntry.grid(row=6,column=1,sticky='w',pady=10)

                
        #fee
        fee=Label(formFrame,text="Enter Fee Amount:",font=("book antiqua",15),bg='skyblue',fg="Black")
        fee.grid(row=7,column=0,sticky='W')

        #creating inputbox
        feeEntry=Entry(formFrame,font=('book antiqua',15),text=self.feeVar)
        feeEntry.grid(row=7,column=1,sticky='w',pady=10)
        
        #Qualification
        quali=Label(formFrame,text="Enter Qualification:",font=("book antiqua",15),bg='skyblue',fg="Black")
        quali.grid(row=8,column=0,sticky='W')

        #creating inputbox
        qualiEntry=Entry(formFrame,font=('book antiqua',15),text=self.qualificationVar)
        qualiEntry.grid(row=8,column=1,sticky='w',pady=10)


        ##working on interface

        ###btn frame
        btnFrame=Frame(formFrame,bg='PINK',bd=3,relief='raised')
        btnFrame.place(x=10,y=460,width=480,height=150)
        
        ### add button
        addBtn=Button(btnFrame,text="ADD",font=('book antiqua',15),bg='beige',fg='black',command=self.addData)
        addBtn.grid(row=0,column=0,padx=25,pady=50)
        
         ### UPDATE button
        updateBtn=Button(btnFrame,text="Update",font=('book antiqua',15),bg='beige',fg='black',command=self.updatingdata)
        updateBtn.grid(row=0,column=1,padx=25,pady=50)

         ### Delete button
        deleteBtn=Button(btnFrame,text="Delete",font=('book antiqua',15),bg='beige',fg='black',command=self.deleting)
        deleteBtn.grid(row=0,column=2,padx=25,pady=50)

         ### clear button
        clearBtn=Button(btnFrame,text="clear",font=('book antiqua',15),bg='beige',fg='black',command=self.clearData)
        clearBtn.grid(row=0,column=3,padx=10,pady=50)




        ### working on display form

        title3=Label(displayFrame,text="Data Display Here",font=('book antique',15),bg="cyan",fg="red",bd=3,relief="raised")
        title3.place(x=380,y=10)


        tableframe=Frame(displayFrame,bg='white',bd=3,relief="raised")
        tableframe.place(x=20,y=45,width='930' ,height='230')


        self.studentsinfo=ttk.Treeview(tableframe,columns=('rollno','fname','lname','cname','mobile','email','fee','qualification'))

        self.studentsinfo.heading('rollno',text='Roll No')
        self.studentsinfo.heading('fname',text='First Name')
        self.studentsinfo.heading('lname',text='Last Name')
        self.studentsinfo.heading('cname',text='Course Name')
        self.studentsinfo.heading('mobile',text='Contact Number')
        self.studentsinfo.heading('email',text='Email Id')
        self.studentsinfo.heading('fee',text='Fee')
        self.studentsinfo.heading('qualification',text='Qualification')

        self.studentsinfo.column('rollno',width=100,anchor="center")
        self.studentsinfo.column('fname',width=130,anchor="center")
        self.studentsinfo.column('lname',width=130,anchor="center")
        self.studentsinfo.column('cname',width=130,anchor="center")
        self.studentsinfo.column('mobile',width=100,anchor="center")
        self.studentsinfo.column('email',width=130,anchor="center")
        self.studentsinfo.column('fee',width=80,anchor="center")
        self.studentsinfo.column('qualification',width=130,anchor="center")
        


        
        self.studentsinfo['show']='headings'
        self.fetchdata()
        self.studentsinfo.pack()
        self.studentsinfo.bind('<ButtonRelease-1>',self.cursorRow)
        



        
    def addData(self):
        connection = pymysql.connect(host='localhost', user='root', password='root', database='guidb', charset='utf8')
        c=connection.cursor()
        
        c.execute('insert into studentsdata values (%s,%s,%s,%s,%s,%s,%s,%s)',
        (
            self.rollNoVar.get(),
            self.fnameVar.get(),
            self.lnameVar.get(),
            self.cnameVar.get(),
            self.mobileVar.get(),
            self.emailVar.get(),
            self.feeVar.get(),
            self.qualificationVar.get()
            )
             )
        
        connection.commit()
        self.clearData()
        self.fetchdata()
        connection.close()
        
    def clearData(self):
        
        self.rollNoVar.set(''),
        self.fnameVar.set(''),
        self.lnameVar.set(''),
        self.cnameVar.set(''),
        self.mobileVar.set(''),
        self.emailVar.set(''),
        self.feeVar.set(''),
        self.qualificationVar.set('')


    def fetchdata(self):
        connection = pymysql.connect(host='localhost', user='root', password='root', database='guidb', charset='utf8')
        c=connection.cursor()
        c.execute('select * from studentsdata')
        data=c.fetchall()
        self.studentsinfo.delete(*self.studentsinfo.get_children())
        for i in data:
            self.studentsinfo.insert('',END,value=i)
        connection.commit()
        connection.close()

    ## creating cursor

    def cursorRow(self,x):
        cursor_row=self.studentsinfo.focus()
        content=self.studentsinfo.item(cursor_row)
        row=content['values']
        
        self.rollNoVar.set(row[0]),
        self.fnameVar.set(row[1]),
        self.lnameVar.set(row[2]),
        self.cnameVar.set(row[3]),
        self.mobileVar.set(row[4]),
        self.emailVar.set(row[5]),
        self.feeVar.set(row[6]),
        self.qualificationVar.set(row[7])
        

    def updatingdata(self):
        connection = pymysql.connect(host='localhost', user='root', password='root', database='guidb', charset='utf8')
        c=connection.cursor()
        c.execute('update studentsdata set fname=%s,lname=%s,cname=%s,mobile=%s,email=%s,fee=%s,qualification=%s where rollNo=%s',
                  (self.fnameVar.get(),
                   self.lnameVar.get(),
                   self.cnameVar.get(),
                   self.mobileVar.get(),
                   self.emailVar.get(),
                   self.feeVar.get(),
                   self.qualificationVar.get(),
                   self.rollNoVar.get()
                      ))
        connection.commit()
        self.fetchdata()
        self.clearData()
        connection.close()


        #########delete
    def deleting(self):
        connection = pymysql.connect(host='localhost', user='root', password='root', database='guidb', charset='utf8')
        c=connection.cursor()
        c.execute('delete from studentsdata where rollNo=%s',self.rollNoVar.get())
        
        connection.commit()
        self.fetchdata()
        self.clearData()
        connection.close()
        
            
        


    
        
        
        
        

        
        
obj=Tk()
x=Myclass(obj)
