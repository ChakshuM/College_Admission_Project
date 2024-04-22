import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.simpledialog import askinteger
from tkinter import font
from Humber_AdmissionOOPS import Admission





"""
Developers' Name: Team4 Developer
Last Edited on : 14-April-2024

Class Description: This class represents the main application window of AdmitPro v1.00.0, designed for the Admission Department of Humber College.

It initializes the application window and sets up various tabs for different functionalities including form submission, viewing submitted details,
overall results, selected and rejected students, reasoning for rejections, and an about us section. It also handles login attempts, student 
information storage, and provides a copyright notice.

Method included in the class:
- welNote
- on_entry_click
- on_focus_out
- on_button_click
- starLogin
- getting
- enterStudentDetails
- entrStudentRecords
- marksExceptionHandling
- fetchMarksAndName
- view_grades_table
- createReport1
- createReport2
- createReport3
- createReport4
- help
- veiwAboutUs
"""


class TkinterApp:
    def __init__(self, master):
        
        # Initialize the Tkinter application with the provided master window
        self.master = master
        self.welNote()

         # Set up the main window title
        self.master.title("AdmitPro v1.00.0: Admission Department of Humber College")
        tabControl = ttk.Notebook(master) 

        # Create a tabbed interface for different functionalities
        self.tab1 = ttk.Frame(tabControl) 
        self.tab2 = ttk.Frame(tabControl)
        self.tab3 = ttk.Frame(tabControl) 
        self.tab4 = ttk.Frame(tabControl)
        self.tab5 = ttk.Frame(tabControl)
        self.tab6 = ttk.Frame(tabControl)
        self.tab7 = ttk.Frame(tabControl)

        # Add tabs with corresponding labels
        tabControl.add(self.tab1, text ='Form') 
        tabControl.add(self.tab2, text ='Submitted Details') 
        tabControl.add(self.tab3, text ='Overall Result') 
        tabControl.add(self.tab4, text ='Selected Students') 
        tabControl.add(self.tab5, text ='Rejected Students') 
        tabControl.add(self.tab7, text ='Rejection Reasoning') 
        tabControl.add(self.tab6, text ='About Us') 

        # Expand the tabbed interface to fill the available space
        tabControl.pack(expand = 1, fill ="both") 


        # Display copyright notice at the bottom of the window
        label1 = tk.Label(master, text="Copyright (c) 2024 Humber College. All rights reserved", font=("Helvetica", 8))
        label1.pack()

        # Initialize variables for login attempts, student information storage, etc.
        self.attempts = 2
        self.attemptsStudents = 2
        self.nextClick = 0
        self.student_names = []
        self.student_marks = []
        
        # Initialize the about us section
        self.veiwAboutUs()

         # Set font for the login interface
        univFont = font.Font(size=8,weight="bold")
        
        # Display the login screen
        self.starLogin()
        
        


       
    """
    Method Name: welNote

    Description:
    # Displays a welcome message upon launching the application.
    """
    def welNote(self):
        obj1 = Admission()
        print("1")
        messagebox.showinfo("Humber College", obj1.welcomeNote())

    
    """
    Method Name: on_entry_click

    Description:
    #If the current content of the username entry field matches the default user,
    #the method deletes the default text and changes the text color to black.
    """
    def on_entry_click(self, event):
        if self.usernameEntry.get() == self.default_user:
            self.usernameEntry.delete(0, tk.END)
            self.usernameEntry.config(fg='black')

    
    """
    Method Name: on_focus_out

    Description: #This method inserts the default user text and changes the text color to grey.
    """
    
    def on_focus_out(self, event):
        # Get the text from the username entry field
        if self.usernameEntry.get() == '':
            self.usernameEntry.insert(0, self.default_user)
            self.usernameEntry.config(fg='grey')
    
    """
    Method Name: on_button_click

    Description:
    #Retrieves the text from the username entry field, modifies it if necessary,
    #and creates a label to display the logged-in user information.
    """
    def on_button_click(self):
        text = self.usernameEntry.get()
        
        # Modify text if it matches the placeholder
        newFont = font.Font(size=10,weight="bold")
        if text == "e.g., Admin":
            text = "Admin"
        
        # Create a label to display the logged-in user information
        self.loggedInLabel = tk.Label(self.master, text="User: "+text, justify="right", font=newFont, fg="#00466a")
        
        # For debugging/logging purpose
        print("text = ",text)
        self.loggedInLabel.place(relx = 1.0,  rely = 0.04, anchor ='ne')

            
    """
    Method Name: starLogin

    Description:
    #Initializes and configures the login window. 
    #Sets up the login window with username and password entry fields, labels, and buttons for login.
    """
    def starLogin(self):
         # Set font for the heading label
        AboutNewLabelFont = font.Font(slant="italic",size=20,weight="bold")
        
        # Create the login window
        self.pwdWindow = tk.Tk()
        self.pwdWindow.geometry("440x160")
        self.pwdWindow.title("Humber Login")
        
          # Add a heading label for the login window
        loginHeading = tk.Label(self.pwdWindow, text="Sign In",font=AboutNewLabelFont)
        loginHeading.grid(row=1, column=1,columnspan=10, padx=10, pady=5)


         # Add labels for username and password entry fields
        usernameLabel = tk.Label(self.pwdWindow, text="Enter the Username:")
        usernameLabel.grid(row=3, column=1,columnspan=3, padx=10, pady=5)

        passwordLabel = tk.Label(self.pwdWindow, text="Enter the Password:")
        passwordLabel.grid(row=5, column=1,columnspan=3, padx=10, pady=5)
        
        # Create the username entry field with placeholder text and event bindings
        self.usernameEntry = tk.Entry(self.pwdWindow,  width = 30, borderwidth=5, fg='grey')
        self.default_user = "e.g., Admin"
        self.usernameEntry.insert(tk.END, self.default_user)
        self.usernameEntry.bind("<FocusIn>", self.on_entry_click)
        self.usernameEntry.bind("<FocusOut>", self.on_focus_out)

        self.usernameEntry.focus()
        # Create the password entry field with password masking
        self.passwordEntry = tk.Entry(self.pwdWindow,  width = 30, borderwidth=5, show="*")
        
        # Place username and password entry fields in the grid
        self.usernameEntry.grid(row=3, column=4, padx=10, pady=5)
        self.passwordEntry.grid(row=5, column=4, padx=10, pady=5)

        # Create buttons for exit, login, and help
        self.passwordButton = tk.Button(self.pwdWindow, text="Exit", command=exit, width=10)
        self.cancelButton = tk.Button(self.pwdWindow, text="Login", command=self.getting, width=10)
        self.helpButton = tk.Button(self.pwdWindow, text="Help", command=self.help, width=10)
        
        # Place buttons in the grid
        self.passwordButton.grid(row=7, column=2, padx=1, pady=1, columnspan=2)
        self.cancelButton.grid(row=7, column=4, padx=1, pady=1, columnspan=2)
        self.helpButton.grid(row=7, column=6, padx=1, pady=1, columnspan=2)
        

    """
    Method Name: getting
    Desctiption:
    #1.Checks if the entered password is correct. If correct, displays a success message,closes the login window, and proceeds to the next step.
    #2. If incorrect, decrements the attempt counter, displays an error message, and clears the password entry field. Terminates the program if the maximum number of attempts is reached.
    """
    def getting(self):
        obj1 = Admission() # Initialize an Admission object for password validation
        
        # Check if the password is correct
        if obj1.passwordValidation(self.passwordEntry.get()):
            # Display a success message if the password is correct
            messagebox.showinfo("Success", "You have given the correct password!")
            self.on_button_click()
            self.pwdWindow.destroy() # Close the login window
            self.enterStudentDetails() # Proceed to the next step i.e., enter student details
        else:
             # If the password is incorrect
            if self.attempts == 0:
                # If maximum attempts reached, terminate the program
                messagebox.showerror("Error: Incorrect Password Format", "Invalid input the program will terminate now")
                exit()
            else:
                messagebox.showerror("Error: Incorrect Password Format", "You are left with {} attempts".format(self.attempts))
                
                # Move focus to the next widget for user convenience
                self.pwdWindow.tk_focusNext()
                # Decrement the attempt counter
                self.attempts -= 1
                # Clear the password entry field
                self.passwordEntry.delete(0, tk.END)
                # Ensure the login window remains on top
                self.pwdWindow.attributes('-topmost',True)

    """
    Method Name: enterStudentDetails
    Description: This method is for entering student details
    """
    def enterStudentDetails(self):
            AboutNewLabelFont = font.Font(size=16,weight="bold")
            
            studentDeetailHeading = tk.Label(self.tab1, text="Enter Student Details", justify="center" ,font=AboutNewLabelFont)
            studentDeetailHeading.place(relx = 0.5, rely = 0.04, anchor ='center')
            
            studentLabelFont = font.Font(size=8,weight="bold")
            self.numberOfStudent = tk.Label(self.tab1, text="Enter the no. of the student: ", font=studentLabelFont)
            self.numberOfStudent.place(relx = 0.2, rely = 0.13, anchor ='e')


             # Create an entry field for entering the number of students
            self.numberOfStudentEntry = tk.Entry(self.tab1, width = 30, borderwidth=5)
            self.numberOfStudentEntry.place(relx = 0.5, rely = 0.13, anchor ='e')
            
            #  Create a button to proceed to entering student records
            self.studentNoButton = tk.Button(self.tab1, text="Proceed", command=self.entrStudentRecords, padx=5, pady=2)
            self.studentNoButton.place(relx = 0.6, rely = 0.13, anchor ='e')

    """ 
    Method Name: entrStudentRecords

    Description:
    This method serves the purpose of managing the entry of student records. 
    Initially, it validates the user input to ensure that the number of student 
    entries provided falls within the acceptable range of 1 to 50. 
    """
    def entrStudentRecords(self, itr=0):
                        

            if self.numberOfStudentEntry.get().isdigit() and 1 <= int(self.numberOfStudentEntry.get()) <= 50:
                self.studentNoButton.destroy()
                #self.numberOfStudentEntry
                #self.nextClick += 1
                print("self.numberOfStudentEntry.get() = ", self.numberOfStudentEntry.get())
                print("self.nextClick = ",self.nextClick)
                
                studentLabelFont = font.Font(size=8,weight="bold")

                self.StudentNameLabel = tk.Label(self.tab1, text="Enter the Name of the student: ", font=studentLabelFont)
                # self.StudentNameLabel.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
                self.StudentNameLabel.place(relx = 0.218, rely = 0.2, anchor ='e')

                self.StudentNameEntry = tk.Entry(self.tab1, width = 30, borderwidth=5)
                # self.StudentNameEntry.grid(row=4, column=3, padx=10, pady=5)
                self.StudentNameEntry.place(relx = 0.5, rely = 0.2, anchor ='e')

                self.MathsLabel = tk.Label(self.tab1, text="Maths Marks: ", font=studentLabelFont)
                # self.MathsLabel.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
                self.MathsLabel.place(relx = 0.108, rely = 0.27, anchor ='e')

                self.MathsEntry = tk.Entry(self.tab1, width = 30, borderwidth=5)
                self.MathsEntry.place(relx = 0.5, rely = 0.27, anchor ='e')

                
                self.ScienceLabel = tk.Label(self.tab1, text="Science Marks: ", font=studentLabelFont)
                self.ScienceLabel.place(relx = 0.116, rely = 0.34, anchor ='e')
                # self.ScienceLabel.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

                
                self.ScienceEntry = tk.Entry(self.tab1, width = 30, borderwidth=5)
                # self.ScienceEntry.grid(row=8, column=3, padx=10, pady=5)
                self.ScienceEntry.place(relx = 0.5, rely = 0.34, anchor ='e')

                
                self.LanguageLabel = tk.Label(self.tab1, text="Language Marks: ", font=studentLabelFont)
                self.LanguageLabel.place(relx = 0.130, rely = 0.41, anchor ='e')
                # self.LanguageLabel.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

                self.LanguageEntry = tk.Entry(self.tab1, width = 30, borderwidth=5)
                self.LanguageEntry.place(relx = 0.5, rely = 0.41, anchor ='e')
                # self.LanguageEntry.grid(row=10, column=3, padx=10, pady=5)
                
                

                self.DramaLabel = tk.Label(self.tab1, text="Drama Marks: ", font=studentLabelFont)
                self.DramaLabel.place(relx = 0.109, rely = 0.47, anchor ='e')
                # self.DramaLabel.grid(row=12, column=0, columnspan=2, padx=10, pady=5)

                self.DramaEntry = tk.Entry(self.tab1, width = 30, borderwidth=5)
                self.DramaEntry.place(relx = 0.5, rely = 0.47, anchor ='e')
                # self.DramaEntry.grid(row=12, column=3, padx=10, pady=5)

                
                self.MusicLabel = tk.Label(self.tab1, text="Music Marks: ", font=studentLabelFont)
                # self.MusicLabel.grid(row=14, column=0, columnspan=2, padx=10, pady=5)
                self.MusicLabel.place(relx = 0.108, rely = 0.54, anchor ='e')

                self.MusicEntry = tk.Entry(self.tab1, width = 30, borderwidth=5)
                # self.MusicEntry.grid(row=14, column=3, padx=10, pady=5)
                self.MusicEntry.place(relx = 0.5, rely = 0.54, anchor ='e')

                self.BiologyLabel = tk.Label(self.tab1, text="Biology Marks: ", font=studentLabelFont)
                # self.BiologyLabel.grid(row=16, column=0, columnspan=2, padx=10, pady=5)
                self.BiologyLabel.place(relx = 0.114, rely = 0.61, anchor ='e')

                self.BiologyEntry = tk.Entry(self.tab1, width = 30, borderwidth=5)
                # self.BiologyEntry.grid(row=16, column=3, padx=10, pady=5)
                self.BiologyEntry.place(relx = 0.5, rely = 0.61, anchor ='e')

                
                # if self.nextClick <= int(self.numberOfStudentEntry.get()): 
                        
                print("I am here > ",self.nextClick)
                self.studentNameButton1 = tk.Button(self.tab1, text="Next", command=self.marksExceptionHandling, padx=2, pady=2, width=20, height=2)
                self.studentNameButton1.place(x=220,y=350, width=60)

                self.studentNameButton2 = tk.Button(self.tab1, text="Exit", command=exit, padx=10, pady=2, width=10, height=2)
                self.studentNameButton2.place(x=350,y=350, width=60)
                
            else:
                if self.attemptsStudents == 0:
                    messagebox.showerror("Error: Invalid Entry ", "Maximum limit has been reached, program will terminate now!")
                    exit()
                else:
                    messagebox.showerror("Error: Invalid Entry ", "You are left with {} attempts".format(self.attemptsStudents))
                    self.attemptsStudents -= 1
                    self.numberOfStudentEntry.delete(0, tk.END)

    
    """
    Method Name: createReport3

    Description:
    #This is the third report method, illustrating the number of students who were not accepted. These are students who did not meet the required scores and, as a result, did not qualify for admission to Humber College
    """
    def createReport3(self, result):
        z=0
        root = self.tab5
        univFont = font.Font(size=8,weight="bold")
        self.report1Label = tk.Label(root, text="REPORT 3: VIEW THE NUMBER OF STUDENTS THAT WERE NOT ACCEPTED BY HUMBER COLLEGE", font=univFont)
        self.report1Label.grid(row=4, column=1, columnspan=5, padx=10, pady=5)

        # Define a custom style for the heading
        s = ttk.Style()
        s.configure("mystyle.Treeview.Heading", font=('Helvetica', 8,'bold'))

        tree = ttk.Treeview(root, column=("c1"), show='headings',style="mystyle.Treeview")
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="NOT ACCEPTED")

        for row in range(0,len(result)):
            z += result[row][2].count("Not Accepted")
        
        
        tree.insert("", 'end', values =(z)) 
        
        tree.grid(row=10, column=0,columnspan=5, padx=10, pady=5)
    
    
    def marksExceptionHandling(self):
        
        # if (self.MathsEntry.get().isdigit() and self.ScienceEntry.get().isdigit() and self.LanguageEntry.get().isdigit() and self.DramaEntry.get().isdigit() and self.MusicEntry.get().isdigit() and self.BiologyEntry.get().isdigit()) and (1 <= int(self.MathsEntry.get()) >=100 and 1 <= int(self.ScienceEntry.get()) >= 100 and 1 <= int(self.LanguageEntry.get()) >= 100  and 1 <= int(self.DramaEntry.get()) >=100 and 1 <= int(self.MusicEntry.get()) >=100 and 1 <= int(self.BiologyEntry.get()) >=100):
        if self.MathsEntry.get().isdigit() and 1 <= int(self.MathsEntry.get()) <= 100 and self.ScienceEntry.get().isdigit() and 1 <= int(self.ScienceEntry.get()) <= 100 and self.DramaEntry.get().isdigit() and 1 <= int(self.DramaEntry.get()) <= 100 and self.MusicEntry.get().isdigit() and 1 <= int(self.MusicEntry.get()) <= 100 and self.LanguageEntry.get().isdigit() and 1 <= int(self.LanguageEntry.get()) <= 100 and self.BiologyEntry.get().isdigit() and 1 <= int(self.BiologyEntry.get()) <= 100:
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print("Validated") 

            if self.nextClick < int(self.numberOfStudentEntry.get()): 
                self.nextClick += 1
            # if self.nextClick == int(self.numberOfStudentEntry.get()): 
                self.fetchMarksAndName()

            
                
        else:
            print("Wy I am here")                    
            messagebox.showerror("Error: Invalid Entry ", "All the Marks should be between (1 to 100)")
            

    
    """
    Method Name: fetchMarksAndName
    description:
    1. The `fetchMarksAndName` method retrieves marks and names entered by the user.
    2. Marks for various subjects are extracted from corresponding entry fields.
    3. The method appends the student marks and name to lists for further processing.
    4. If all student entries are completed, it disables input fields and buttons, calculates grades, creates reports, and notifies the user of successful submission.
    """
    def fetchMarksAndName(self):
        result=[]

        # student marks input
        Ma = int (self.MathsEntry.get())
        Sc = int (self.ScienceEntry.get())
        La = int (self.LanguageEntry.get())
        Dr = int (self.DramaEntry.get())
        Mu = int (self.MusicEntry.get())
        Bi = int (self.BiologyEntry.get())


        
        # student marks appended in a list
        self.student_marks.append(Admission(Ma,Sc,La,Dr,Mu,Bi))
        self.student_names.append(self.StudentNameEntry.get())
        print("self.nextClick = ",self.nextClick)
        print("int(self.numberOfStudentEntry.get() = ", int(self.numberOfStudentEntry.get()))
        if self.nextClick == int(self.numberOfStudentEntry.get()):

            print(self.nextClick == int(self.numberOfStudentEntry.get()), "self.nextClick == int(self.numberOfStudentEntry.get()):", self.nextClick , int(self.numberOfStudentEntry.get()))

            # self.studentNameButton1.destroy()
            # self.studentNameButton2.destroy()
            self.studentNameButton1.config(state='disabled')
            self.numberOfStudentEntry.config(state='disabled')
            self.StudentNameEntry.config(state='disabled')
            self.MathsEntry.config(state='disabled')
            self.ScienceEntry.config(state='disabled')
            self.LanguageEntry.config(state='disabled')
            self.DramaEntry.config(state='disabled')
            self.MusicEntry.config(state='disabled')
            self.BiologyEntry.config(state='disabled')
            
            obj3 = Admission()
            print(" I am here, take this input and try again........")
            print(self.student_names, self.student_marks)
            result = obj3.calculateGrades(self.student_names, self.student_marks)
            self.createReport1(result)
            self.createReport2(result)
            self.createReport3(result)
            self.createReport4(result)
            newResult = obj3.viewSubmittedDetails(self.student_names, self.student_marks)
            self.view_grades_table(newResult)
    
            messagebox.showinfo("Successfully submitted applicant records", "You will be prompted to view the record")
            self.tab2.focus()

        else:
            #self.nextClick += 1
            self.entrStudentRecords()
            
    
    """
    Method Name: view_grades_table
    
    Description: 
    Review all the student records that have been entered. For instance, the system contains the names and corresponding details of 30 students.
    """
    def view_grades_table(self, result):
        print("finally ======== ",result)
        univFont = font.Font(size=8,weight="bold")
        self.studentRecordLabel = tk.Label(self.tab2, text="SUBMITTED RECORDS: REVIEW THE APPLICANTS DETAILS WHO HAVE APPLIED TO HUMBER COLLEGE", font=univFont)
        self.studentRecordLabel.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        root = self.tab2
        # Define a custom style for the heading
        s = ttk.Style()
        s.configure("mystyle.Treeview.Heading", font=('Helvetica', 8,'bold'))

        tree = ttk.Treeview(root, column=("c1", "c2","c3", "c4","c5", "c6","c7"), show='headings',style="mystyle.Treeview")
        tree.column("#1", anchor=tk.CENTER,  width=200)
        tree.heading("#1", text="STUDENT NAME")
        tree.column("#2", anchor=tk.CENTER,  width=100)
        tree.heading("#2", text="MATHS")
        tree.column("#3", anchor=tk.CENTER,  width=100)
        tree.heading("#3", text="SCIENCE")
        tree.column("#4", anchor=tk.CENTER,  width=100)
        tree.heading("#4", text="LANGUAGE")
        tree.column("#5", anchor=tk.CENTER,  width=100)
        tree.heading("#5", text="DRAMA")
        tree.column("#6", anchor=tk.CENTER,  width=100)
        tree.heading("#6", text="MUSIC")
        tree.column("#7", anchor=tk.CENTER,  width=100)
        tree.heading("#7", text="BIOLOGY")

        print("-----------in Tkinter view records------------")        

        for a,b,c,d,e,f,g in result:
            tree.insert("", 'end', values =(a,b,c,d,e,f,g)) 

        for i in range(len(result)):
            print(result[i])
        

        tree.grid(row=10, column=1,columnspan=5, padx=10, pady=5)
        
        Table1LabelFont = font.Font(slant="italic",size=8)
        self.Table1Label = tk.Label(root, text="(scroll to view all records)                        ", font=Table1LabelFont)
        self.Table1Label.grid(row=45, column=0, columnspan=2)
    
    """
    Method Name: createReport1
    Description:
    #This is the first report method that presenting the calculated GPAs alongside the names of the Schools they are shortlisted for.
    """
    
    def createReport1(self, result):
        print(result)

        root = self.tab3
        univFont = font.Font(size=8,weight="bold")
        self.report1Label = tk.Label(self.tab3, text="REPORT 1: EXAMINE THE NUMBER OF ACCEPTED STUDENTS DISTRIBUTED PER SCHOOL", font=univFont)
        self.report1Label.grid(row=4, column=1, columnspan=3, padx=10, pady=5)

        s = ttk.Style()
        s.configure("mystyle.Treeview.Heading", font=('Helvetica', 8,'bold'))

        tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings', selectmode ='browse',style="mystyle.Treeview")
        tree.grid(row=10, column=1,columnspan=5, padx=10, pady=5)


        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="STUDENT NAME")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="GPA")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="SCHOOL")

        for x, y, z in result:
            tree.insert("", 'end', values =(x, y, z)) 

        Table2LabelFont = font.Font(slant="italic",size=8)
        self.Table2Label = tk.Label(self.tab3, text="(scroll to view all records)                                        ", font=Table2LabelFont, justify=tk.LEFT)
        self.Table2Label.grid(row=45, column=0, columnspan=3, padx=10, pady=5)


    """
    Method Name: createReport2

    Description:
    1 The createReport2 method generates a report displaying the total number of students selected in each school.
    2 It initializes variables to count the number of students selected in each school.
    3 The method sets up the layout for the report in the specified tab.
    4 A Treeview widget is used to organize and display the data in a tabular format.
    5 The method then iterates through the result list to count the number of students selected in each school.
    6 Finally, it inserts the calculated counts into the Treeview widget and displays it in the tab.   
    """
    
    def createReport2(self, result):
        soe = 0
        sob = 0
        ls = 0
        
        root = self.tab4
        univFont = font.Font(size=8,weight="bold")
        self.report1Label = tk.Label(root, text="REPORT 2: TOTAL STUDENTS SELECTED IN EACH SCHOOL BASED ON THEIR CUT-OFF PERCENTAGE", font=univFont)
        self.report1Label.grid(row=4, column=1, columnspan=3, padx=10, pady=5)

        s = ttk.Style()
        s.configure("mystyle.Treeview.Heading", font=('Helvetica', 8,'bold'))

        tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings',style="mystyle.Treeview")
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="SCHOOL OF ENGINEERING")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="SCHOOL OF BUSINESS")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="LAW SCHOOL")

        
        print(result.count("Law School"))
        print()

        for row in range(0,len(result)):
            print(result[row][2])
            if result[row][2] == "School of Engineering":
                soe += 1
            elif result[row][2] == "School of Business":
                sob += 1
            elif result[row][2] == "Law School":
                ls += 1
        
        tree.insert("", 'end', values =(soe, sob, ls)) 
        
        tree.grid(row=10, column=1,columnspan=5, padx=10, pady=5)


    """
    Method Name: createReport4

    Description:
    # Rejection Reasoning: This method is for the fourth report, offering insights into how much the GPA fell short for students who did not qualify for admission to Humber College.
    """
    def createReport4(self, result):
        root = self.tab7
        univFont = font.Font(size=8,weight="bold")
        self.report1Label = tk.Label(root, text="REPORT 4: REVIEW THE REJECTED STUDENT REPORT, NOTING THEIR PERCENTAGE SCORE DIFFERENCES", font=univFont)
        self.report1Label.grid(row=4, column=1, columnspan=3, padx=10, pady=5)

        s = ttk.Style()
        s.configure("mystyle.Treeview.Heading", font=('Helvetica', 8,'bold'))

        tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5"), show='headings',style="mystyle.Treeview")
        tree.column("#1", anchor=tk.CENTER, width=200)
        tree.heading("#1", text="STUDENT NAME")
        tree.column("#2", anchor=tk.CENTER, width=100)
        tree.heading("#2", text="GPA OBTAINED")
        tree.column("#3", anchor=tk.CENTER, width=100)
        tree.heading("#3", text="MIN CUT-OFF")
        tree.column("#4", anchor=tk.CENTER, width=150)
        tree.heading("#4", text="DIFFERENTIAL GPA")
        tree.column("#5", anchor=tk.CENTER, width=100)
        tree.heading("#5", text="RESULT")

        filtered_rows = [row for row in result if "Not Accepted" in row]
        print("I am 11111111")
        print(filtered_rows)

        for x, y, z in filtered_rows:
            print(x,y,70, max(0,70-int(y)),z)
            tree.insert("", 'end', values =(x,y,70, max(0,70-int(y)),z))
        
       
        tree.grid(row=10, column=1,columnspan=5, padx=10, pady=5)

 

    """
    Method Name: help

    Description:
    #method contains: Login help button information
    """
    def help(self):
        pwdWindow2 = tk.Tk()
        pwdWindow2.geometry("380x160")
        pwdWindow2.title("Humber Helpdesk")
        helpLabel = tk.Label(pwdWindow2, text="Password Criteria:\n 1. Have 10 or more characters                                                       \n 2. Have uppercase (Minimum 1 is mandatory)                          \n 3. Have lowercase (Minimum 1 is mandatory)                          \n 4. Have numbers (Minimum 2 is mandatory)                            \n 5. Have 1 special characters. e.g.,   @ # $ * ( ) - _ = + . ? ! & %\n 6. Maximum 3 attempts will be provided                                  ")
        helpLabel.grid(row=2, column=1,columnspan=2, padx=10, pady=5)
        closeButton = tk.Button(pwdWindow2, text="Close", command=pwdWindow2.destroy, width=10)
        closeButton.grid(row=20, column=1, padx=1, pady=1, columnspan=2)

    """
    Method Name: veiwAboutUs

    Description:
    This is the last tab in the application for viewing the static details in the table
    """
    def veiwAboutUs(self):

        self.about1label = tk.Label(self.tab6, text="About Humber College Admission Application                                               ", font=("Helvetica", 10),justify=tk.LEFT)
        self.about1label.grid(row=1, column=1, padx=10)
        #self.about1label.pack(pady=2)
        

        root = self.tab6

        s = ttk.Style()
        s.configure("mystyle.Treeview.Heading", font=('Helvetica', 8,'bold'))

        tree = ttk.Treeview(root, column=("c1", "c2"), show='headings',style="mystyle.Treeview")
            
        #anchor - n, ne, e, se, s, sw, w, nw, or center
        tree.column("#1", anchor=tk.W,  width=200)
        tree.heading("#1", anchor=tk.W, text="FIELD")
        tree.column("#2", anchor=tk.W,  width=300)
        tree.heading("#2", anchor=tk.W, text="DESCRIPTION")
        
        aboutUs = [['VERSION:','1.00.0 (user setup)'],
                   ['RELEASE DATE:','2024-04-01'],
                   ['OPERATING SYSTEM:','OS.Windows_NT x64'],
                   ['TEAM 4 DEVELOPERS:',' '],
                   [' ','Asha Thaiparambil Devassy (N01650149)'],
                   [' ','Chakshu Madan (N01649164)'],
                   [' ','Devika Pradeep (N01649286)'],
                   [' ','Kavin Ravi (N01649313)'],
                   [' ','Sandeep Sree Kumar (N01649378)']
                   ]
        

        for a in aboutUs:
            print(a)
            tree.insert("", 'end', values =(a)) 

        tree.grid(row=10, column=1, columnspan=5, padx=10)
        


        