# College_Admission_project
**Requirement:** During the 1st Semester, I engaged in a Python project, leveraging advanced concepts including Object-Oriented Programming (OOP), Tkinter GUI framework, and more.
**Role & Reponsibility:** As a team manager, Python developer, and tester, my responsibilities encompassed the entire lifecycle of the project. I oversaw the development process, ensuring smooth collaboration among team members, and took charge of coding and testing phases to ensure the system's functionality and reliability. Additionally, I played a pivotal role in crafting an engaging and informative presentation using Microsoft PowerPoint to mark the project as complete

_Following are the functionality created in the project:_

**Welcome Message and Password Authentication:**
When the program starts, it displays a welcoming message: "Welcome to Humber College." The user is prompted to log in using a password. The password must adhere to specific rules: it must be at least 10 characters long, contain at least one uppercase letter, two or three numbers, and one special character. If the password is incorrect, the user is prompted to enter a new password. The system allows only three attempts to log in with a correct password.

**Entering Number of Students:**
After successful password authentication, the system asks the user to enter the number of students, which must be between 1 and 50. If the user enters a number outside this range, they are informed to enter a correct number. The system allows only three attempts for entering the correct number; otherwise, the program stops.

**Entering Student Information:**
Upon entering a valid number of students, the system prompts the user to enter the names of the students. The names are stored in a one-dimensional list. Then, the system prompts the user to enter the grades of the courses for each student in a two-dimensional list, considering the credit hours assigned to each course.

**Calculating GPA and Assigning Schools:**
The system calculates the GPA of each student based on the entered grades and credit hours using the formula: GPA = ∑ (Mark * Credit hours) / total credit hours. Subsequently, students are assigned to schools based on predefined GPA ranges: School of Engineering (90 >= GPA <= 100), School of Business (80 >= GPA < 90), Law School (70 >= GPA < 80), and Not accepted (GPA < 70).

_Following are the outcome of the project:_

In totality there are four reports has been created.

**Report 1 - Student Placement Overview:**
This report includes the names of students along with their GPA and the school/program they have been selected for. For instance, students with a GPA between 90 and 100 are assigned to the School of Engineering, those with a GPA between 80 and 90 to the School of Business, those with a GPA between 70 and 80 to the Law School, and those with a GPA less than 70 are marked as Not Accepted.

**Report 2 - Placement Statistics:**
This report provides an overview of the total number of students who have secured placement.

**Report 3 - Rejection Statistics:**
Here, the total count of students who have been rejected during the admission process is showcased.

**Report 4 - Shortfall Analysis of Rejected Students:**
This report analyzes the shortfall in GPA for students who have been rejected during the admission process, shedding light on how much their GPA fell short of the required criteria.
