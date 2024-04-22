import tkinter as tk

class Admission:
    attempts = 3
    entrStu = 0
    itr = 0
    pwdDigit = 0
    pwdUpper = 0
    pwdSpecial = 0
    stuNameList = []
    stuMarks = []
    individual_score_gpa =[]

    
    #Initializes an instance of the Admission class with default subject weights.
    
    def __init__(self, math=1, science=1, lang=1, drama=1, music=1, bio=1):
        self.math = math
        self.science = science
        self.lang = lang
        self.drama = drama
        self.music = music
        self.bio = bio

    def welcomeNote(self):
        return "WELCOME TO HUMBER COLLEGE!"

    # Validates the given password based on folling criteria:
    # Should not be less than 10 characters.
    # Should contain at least one upper case letter.
    # Should contain two or three numbers.
    # Should contain one special character
    def passwordValidation(self, password):
        pwdDigit = 0
        pwdUpper = 0
        pwdSpecial = 0
    
        for i in password:
            if i.isupper():
                pwdUpper += 1
        
            if i.isdigit():
                pwdDigit += 1
                
            if i.isalnum() == False or i.isspace() == False:
                pwdSpecial += 1
            
        if len(password) >= 10 and pwdUpper >= 1 and pwdDigit >= 2 and pwdSpecial >= 1:
            return True
        else:
            return False
        
    
    # Handles the process of entering student details, validating the number of students entered.
    def enterStudent(self, entrStu, itr=1):
        es = 0
        attempts = 3-itr

        if entrStu >= 1 and entrStu <= 50:
            
            for i in range(0, entrStu):
                self.stuNameList.append(input(f"Enter the name of the student {i+1} :"))
            
            es = self.stuNameList

        else:
            if attempts >= 1 and attempts <= 3:
                itr += 1
                print("Invalid Enter! Please try again [{} more attempt(s) left]".format(attempts))
                es = self.enterStudent(int(input("Enter the number of students (1 - 50 ONLY): ")), itr)
            else:
                es = False
    
        return es
                
    # Calculates and returns the overall grade based on subject weights.
    def enterGrades(self):
        subjectCredit = [4,5,4,3,2,4]
        return ((self.math*4)+(self.science*5)+(self.lang*4)+(self.drama*3)+(self.music*2)+(self.bio*4))//sum(subjectCredit)
    
    #Retrieves subject marks for a student
    def retrieveMarks(self):
        return self.math,self.science,self.lang,self.drama,self.music,self.bio
    

    # Calculates grades and categorizes students into different schools based on their grades.
    def calculateGrades(self, studentName, studentMarks):
        result=[]
        print("-------------- Result is out --------------")
        for i in range (len(studentMarks)):
            
            print("Student ", studentName[i]," total gpa is ", studentMarks[i].enterGrades())

            if studentMarks[i].enterGrades() <= 100 and studentMarks[i].enterGrades() > 90:
                result.append([studentName[i], studentMarks[i].enterGrades(), "School of Engineering"])

            elif studentMarks[i].enterGrades() <= 90 and studentMarks[i].enterGrades() > 80:
                result.append([studentName[i], studentMarks[i].enterGrades(), "School of Business"])
            
            elif studentMarks[i].enterGrades() <= 80 and studentMarks[i].enterGrades() > 70:
                result.append([studentName[i], studentMarks[i].enterGrades(), "Law School"])
            
            elif studentMarks[i].enterGrades() <= 70:
                result.append([studentName[i], studentMarks[i].enterGrades(), "Not Accepted"])
        
        return result

    # Retrieves and formats student details for viewing.
    def viewSubmittedDetails(self, studentName, studentMarks):
        savedResult=[]
        merged=[]
        print("-------------- View Records --------------")
        print("len(studentMarks) = ", len(studentMarks))


        for i in range(len(studentName)):
            merged = [studentName[i]] + list(studentMarks[i].retrieveMarks())
            savedResult.append(merged)
    
        #print(savedResult)
        return savedResult

    # Calculates additional GPA needed to meet a minimum requirement.
    def calculate_additional_gpa(self, min_gpa, current_gpa):
            print(min_gpa , current_gpa, min_gpa - current_gpa, max(0, min_gpa - current_gpa))
            return max(0, min_gpa - current_gpa)