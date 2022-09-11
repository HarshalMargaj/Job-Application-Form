###################################################################################
#                            * JOB APPLICATION FORM *                             #
###################################################################################

from tkinter import *
from tkinter import ttk, messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile

root = Tk()
root.geometry("1210x770")
root.minsize(1210, 770)
root.maxsize(1210, 770)
root.title("Job Application Form")
root.configure(bg="white")


def upload_file():
    file = filedialog.askopenfilename()

    if file:
        cv_value.set(file)
        fob = open(file, "r")


def submit():

    with open("job_applications.csv", "a") as f:
        f.write(
            f"{registration_number_input.get()}, {firstname_input.get()}, {middlename_input.get()}, {lastname_input.get()}, {fullname_input.get()}, {gender_input.get()}, {dob_input.get()}, {year_input.get()}, {dept_input.get()}, {program_input.get()}, {bloodgroup_input.get()}, {mail_input.get()}, {institute_mail_input.get()}, {contact_inptu.get()}, {alt_contact_input.get()}, {language_input.get()}, {high_quali_input.get()}, {cur_degree_cgpa_input.get()}, {CheckVar1.get()}, {CheckVar2.get()}, {tech_interest_input.get()}, {strength_input.get()}, {weakness_input.get()}, {hobbies_input.get()}, {aadhar_num_input.get()}, {pan_num_input.get()}, {ssc_input.get()}, {hsc_dip_input.get()}, {cpi_input.get()}, {dip_12_input.get()}, {backlog_input.get()}, {active_backlog_input.get()}, {edu_input.get()}, {university_input.get()}, {institute_input.get()}, {ssc_percentage_input.get()}, {ssc_passing_input.get()}, {check1.get()}, {dip_edu_input.get()}, {dip_uni_input.get()}, {dip_ist_input.get()}, {dip_per_input.get()}, {dip_passing_input.get()}, {check2.get()}, {gradu_edu_input.get()},{gradu_uni_input.get()}, {gradu_ints_input.get()}, {gradu_per_input.get()}, {gradu_passing_input.get()}, {check3.get()}, {address1_text.get(1.0, END)}, {cur_pin_input.get()}, {cur_country_input.get()}, {address2_text.get(1.0, END)}, {permanent_pin_input.get()},{permanent_country_input.get()}, {cv_value.get()}\n"
        )


# creating frame
f = Frame(root)

# Creating Job Application Form Label
job_label = Label(f,
                  text="Job Application Form",
                  font="RobotoMono 50 bold",
                  fg="white",
                  bg="#F7901C",
                  padx=355,
                  pady=10)

job_label.grid(row=0, columnspan=4)
f.grid()


##################################################################################################
#                                  * Personal Details Section *                                  #
##################################################################################################
# Creating Notebook
my_notebook = ttk.Notebook(root)
my_notebook.grid()
# Creating second frame
f1 = Frame(my_notebook, padx=125, pady=10)
# Adding personal details tab in notebook
my_notebook.add(f1, text="Personal Details")

# Creating registration number Label
reg_label = Label(f1, 
                  text="Registration Number", 
                  font="RobotoMono 16 bold", 
                  fg="#4d5156")
reg_label.grid(row=1, column=0, sticky="w")

# Creating Registration Number entry
registration_number_input = Entry(f1)
registration_number_input.grid(row=2, column=0, sticky="w", pady=10, padx=(0, 40))

# Creating First Name Label
firstname_label = Label(f1, 
                        text="First Name", 
                        font="RobotoMono 16 bold", 
                        fg="#4d5156")
firstname_label.grid(row=1, column=1, sticky="w")

# Creating First Name entry
firstname_input = Entry(f1)
firstname_input.grid(row=2, column=1, sticky="w", padx=(0, 40))

# Creating Middle Name Label
middlename_label = Label(f1, 
                         text="Middle Name", 
                         font="RobotoMono 16 bold", 
                         fg="#4d5156")
middlename_label.grid(row=1, column=2, sticky="w")

# Creating Middle Name entry
middlename_input = Entry(f1)
middlename_input.grid(row=2, column=2, sticky="w", pady=10, padx=(0, 40))

# Creating Last Name label
lastname_label = Label(f1, 
                       text="Last Name", 
                       font="RobotoMono 16 bold", 
                       fg="#4d5156")
lastname_label.grid(row=1, column=3, sticky="w")

# Creating Last Name entry
lastname_input = Entry(f1)
lastname_input.grid(row=2, column=3, sticky="w")

# Creating Full Name label
fullname_label = Label(f1, 
                       text="Full Name", 
                       font="RobotoMono 16 bold", 
                       fg="#4d5156")
fullname_label.grid(row=4, column=0, sticky="w")

# Creating Full Name entry
fullname_input = Entry(f1)
fullname_input.grid(row=5, column=0, sticky="w", pady=10)

# Creating Gender label
gender_label = Label(f1, 
                     text="Gender", 
                     font="RobotoMono 16 bold", 
                     fg="#4d5156")
gender_label.grid(row=4, column=1, sticky="w")

# Creating Gender entry
gender_input = Entry(f1)
gender_input.grid(row=5, column=1, sticky="w")

# Creating Date of Birth label
dob_label = Label(f1, 
                  text="Date Of Birth", 
                  font="RobotoMono 16 bold", 
                  fg="#4d5156")
dob_label.grid(row=4, column=2, sticky="w")

# Creating Date of Birth entry
dob_input = Entry(f1)
dob_input.grid(row=5, column=2, sticky="w")

# Creating Year Of Study label
year_label = Label(f1, 
                   text="Year Of Study", 
                   font="RobotoMono 16 bold", 
                   fg="#4d5156")
year_label.grid(row=4, column=3, sticky="w")

# Creating Year Of Study combobox
year_input = ttk.Combobox(f1, width=19)
year_input["values"] = ("FY", 
                        "SY", 
                        "TY", 
                        "BTech")
year_input.grid(row=5, column=3, sticky="w")

# Creating Department label
dept_label = Label(f1, 
                   text="Department", 
                   font="RobotoMono 16 bold", 
                   fg="#4d5156")
dept_label.grid(row=7, column=0, sticky="w")

# Creating Department combobox
dept_input = ttk.Combobox(f1, width=19)
dept_input["values"] = ("Electronics and communication Engineering", 
                        "Electrical Engineering",
                        "Mechanical engineering",
                        "Information Technology",
                        "Artificial intelligence",
                        "Data Science",
                        "Artificial intelligence and machine learning ",
                        "Agriculture Engineering",
                        "Food technology",
                        "Cyber security",
                        "Information Science and engineering",
                        "Biomedical Engineering",
                        "Electronics and Instrumentation Engineering",
                        "Mechatronics",
                        "Instrumentation and Control",
                        "Mining Engineering",
                        "Production engineering",
                        "Dairy technology",
                        "Marine Engineering",
                        "Big Data Analytics",
                        "Automation and Robotics",
                        "Petroleum Engineering",
                        "Instrumentation Engineering",
                        "Ceramic Engineering",
                        "Chemical Engineering",
                        "Structural Engineering",
                        "Transportation Engineering",
                        "Construction Engineering",
                        "Power Engineering",
                        "Robotics Engineering",
                        "Textile Engineering",
                        "Smart Manufacturing & Automation",
                        "Aeronautical Engineering",
                        "Automobile Engineering",
                        "Civil Engineering",
                        "Computer Science and Engineering",
                        "Biotechnology Engineering",
                        "Electrical and Electronics Engineering",
                        "Automation and Robotics",
                        "Petroleum Engineering",
                        "Information technology",)
dept_input.grid(row=8, column=0, sticky="w", pady=10)

# Creating Program label
program_label = Label(f1, 
                      text="Program", 
                      font="RobotoMono 16 bold", 
                      fg="#4d5156")
program_label.grid(row=7, column=1, sticky="w")

# Creating Program combobox
program_input = ttk.Combobox(f1, width=19)
program_input["values"] = ("BTech Electronics and communication Engineering",
                           "BTech Electrical Engineering",
                           "BTech Mechanical engineering",
                           "BTech Information Technology",
                           "BTech Artificial intelligence",
                           "BTech Data Science",
                           "BTech Artificial intelligence and machine learning ",
                           "BTech Agriculture Engineering",
                           "BTech Food technology",
                           "BTech Cr security",
                           "BTech Information Science and engineering",
                           "BTech Biomedical Engineering",
                           "BTech Electronics and Instrumentation Engineering",
                           "BTech Mechatronics",
                           "BTech Instrumentation and Control",
                           "BTech Mining Engineering",
                           "BTech Production engineering",
                           "BTech Dairy technology",
                           "BTech Marine Engineering",
                           "BTech Big Data Analytics",
                           "BTech Automation and Robotics",
                           "BTech Petroleum Engineering",
                           "BTech Instrumentation Engineering",
                           "BTech Ceramic Engineering",
                           "BTech Chemical Engineering",
                           "BTech Structural Engineering",
                           "BTech Transportation Engineering",
                           "BTech Construction Engineering",
                           "BTech Power Engineering",
                           "BTech Robotics Engineering",
                           "BTech Textile Engineering",
                           "BTech Smart Manufacturing & Automation",
                           "BTech Aeronautical Engineering",
                           "BTech Automobile Engineering",
                           "BTech Civil Engineering",
                           "BTech Computer Science and Engineering",
                           "BTech Biotechnology Engineering",
                           "BTech Electrical and Electronics Engineering",
                           "BTech Automation and Robotics",
                           "BTech Petroleum Engineering",
                           "BTech Information technology"
                           "BE Electronics and communication Engineering"
                           "BE Electrical Engineering",
                           "BE Mechanical engineering",
                           "BE Information Technology",
                           "BE Artificial intelligence",
                           "BE Data Science",
                           "BE Artificial intelligence and machine learning ",
                           "BE Agriculture Engineering",
                           "BE Food technology",
                           "BE Cyber security",
                           "BE Information Science and engineering",
                           "BE Biomedical Engineering",
                           "BE Electronics and Instrumentation Engineering",
                           "BE Mechatronics",
                           "BE Instrumentation and Control",
                           "BE Mining Engineering",
                           "BE Production engineering",
                           "BE Dairy technology",
                           "BE Marine Engineering",
                           "BE Big Data Analytics",
                           "BE Automation and Robotics",
                           "BE Petroleum Engineering",
                           "BE Instrumentation Engineering",
                           "BE Ceramic Engineering",
                           "BE Chemical Engineering",
                           "BE Structural Engineering",
                           "BE Transportation Engineering",
                           "BE Construction Engineering",
                           "BE Power Engineering",
                           "BE Robotics Engineering",
                           "BE Textile Engineering",
                           "BE Smart Manufacturing & Automation",
                           "BE Aeronautical Engineering",
                           "BE Automobile Engineering",
                           "BE Civil Engineering",
                           "BE Computer Science and Engineering",
                           "BE Biotechnology Engineering",
                           "BE Electrical and Electronics Engineering",
                           "BE Automation and Robotics",
                           "BE Petroleum Engineering",
                           "BE Information technology",)
program_input.grid(row=8, column=1, sticky="w")

# Creating bloodgroup label
bloodgroup_label = Label(f1, 
                         text="Select Blood Group", 
                         font="RobotoMono 16 bold", 
                         fg="#4d5156")
bloodgroup_label.grid(row=7, column=2, sticky="w")

# Creating bloodgroup combobox
bloodgroup_input = ttk.Combobox(f1, width=19)
bloodgroup_input["values"] = ("A positive (A+)",
                              "A negative (A-)",
                              "B positive (B+)",
                              "B negative (B-)",
                              "O positive (O+)",
                              "O negative (O-)",
                              "AB positive (AB+)",
                              "AB negative (AB-)",)
bloodgroup_input.grid(row=8, column=2, sticky="w")

# Creating Personal Email label
mail_label = Label(f1, 
                   text="Personal Email", 
                   font="RobotoMono 16 bold", 
                   fg="#4d5156")
mail_label.grid(row=7, column=3, sticky="w")

# Creating Personal Email entry
mail_input = Entry(f1)
mail_input.grid(row=8, column=3, sticky="w")

# Creating Institute Email label
institute_mail_label = Label(f1, 
                             text="Institute Email", 
                             font="RobotoMono 16 bold", 
                             fg="#4d5156")
institute_mail_label.grid(row=10, column=0, sticky="w")

# Creating Institute Email entry
institute_mail_input = Entry(f1)
institute_mail_input.grid(row=11, column=0, sticky="w", pady=10)

# Creating contact number label
contact_label = Label(f1, 
                      text="Contact Number", 
                      font="RobotoMono 16 bold", 
                      fg="#4d5156")
contact_label.grid(row=10, column=1, sticky="w")

# Creating contact number entry
contact_inptu = Entry(f1)
contact_inptu.grid(row=11, column=1, sticky="w")

# Creating alternate contact number label
alt_contact_label = Label(f1, 
                          text="Alternate Contact Number", 
                          font="RobotoMono 16 bold", 
                          fg="#4d5156")
alt_contact_label.grid(row=10, column=2, sticky="w", padx=(0, 20))

# Creating alternate contact number entry
alt_contact_input = Entry(f1)
alt_contact_input.grid(row=11, column=2, sticky="w")

# Creating language label
language_label = Label(f1, 
                       text="Language", 
                       font="RobotoMono 16 bold", 
                       fg="#4d5156")
language_label.grid(row=10, column=3, sticky="w")

# Creating language entry
language_input = Entry(f1)
language_input.grid(row=11, column=3, sticky="w")

# Creating highest Qualification label
high_quali_label = Label(f1, 
                         text="Highest Qualification", 
                         font="RobotoMono 16 bold", 
                         fg="#4d5156")
high_quali_label.grid(row=13, column=0, sticky="w")

# Creating highest Qualification combobox
high_quali_input = ttk.Combobox(f1, width=19)
high_quali_input["values"] = ("SSC", 
                              "HSC/Diploma", 
                              "BE/BTech", 
                              "Ms/MTech")
high_quali_input.grid(row=14, column=0, sticky="w", pady=(5, 0))

# Creating current degree latest cgpa label
cur_degree_cgpa_label = Label(f1, 
                              text="Current Degree Latest CGPA", 
                              font="RobotoMono 16 bold", 
                              fg="#4d5156")
cur_degree_cgpa_label.grid(row=13, column=1, sticky="w")

# Creating current degree latest cgpa entry
cur_degree_cgpa_input = Entry(f1)
cur_degree_cgpa_input.grid(row=14, column=1, sticky="w")

# Creating checkbuttons
CheckVar1 = StringVar()
CheckVar2 = StringVar()
C1 = Checkbutton(f1,
                 text="Are you going for higher studies?",
                 variable=CheckVar1,
                 onvalue="Yes",
                 offvalue="No",
                 wraplength=150,
                 justify="left",)

C2 = Checkbutton(f1,
                 text="Are you placed?",
                 variable=CheckVar2,
                 onvalue="Yes",
                 offvalue="No",
                 height=5,
                 width=20,)

C1.grid(row=14, column=2, sticky="w")
C2.grid(row=14, column=3, sticky="w")

# Creating technical interest label
tech_interest_label = Label(f1, 
                            text="Technical Interest", 
                            font="RobotoMono 16 bold", 
                            fg="#4d5156")
tech_interest_label.grid(row=16, column=0, sticky="w")

# Creating technical interest entry
tech_interest_input = Entry(f1)
tech_interest_input.grid(row=17, column=0, sticky="w", pady=10)

# Creating strength label
strength_label = Label(f1, 
                       text="Strength", 
                       font="RobotoMono 16 bold", 
                       fg="#4d5156")
strength_label.grid(row=16, column=1, sticky="w")

# Creating strength entry
strength_input = Entry(f1)
strength_input.grid(row=17, column=1, sticky="w")

# Creating weakness label
weakness_label = Label(f1, 
                       text="Weakness", 
                       font="RobotoMono 16 bold", 
                       fg="#4d5156")
weakness_label.grid(row=16, column=2, sticky="w")

# Creating weakness entry
weakness_input = Entry(f1)
weakness_input.grid(row=17, column=2, sticky="w")

# Creating hobbies label
hobbies_label = Label(f1, 
                      text="Hobbies", 
                      font="RobotoMono 16 bold", 
                      fg="#4d5156")
hobbies_label.grid(row=16, column=3, sticky="w")

# Creating hobbies entry
hobbies_input = Entry(f1)
hobbies_input.grid(row=17, column=3, sticky="w")

# Creating aadhar number label
aadhar_num_label = Label(f1, 
                         text="Aadhar Number", 
                         font="RobotoMono 16 bold", 
                         fg="#4d5156")
aadhar_num_label.grid(row=19, column=0, sticky="w")

# Creating aadhar number entry
aadhar_num_input = Entry(f1)
aadhar_num_input.grid(row=20, column=0, sticky="w", pady=10)

# Creating pan number label
pan_num_label = Label(f1, 
                      text="Pan Number", 
                      font="RobotoMono 16 bold", 
                      fg="#4d5156")
pan_num_label.grid(row=19, column=1, sticky="w")

# Creating pan number entry
pan_num_input = Entry(f1)
pan_num_input.grid(row=20, column=1, sticky="w")

# Creating ssc percentage label
ssc_label = Label(f1, 
                  text="SSC Percentage", 
                  font="RobotoMono 16 bold", 
                  fg="#4d5156")
ssc_label.grid(row=19, column=2, sticky="w")

# Creating ssc percentage entry
ssc_input = Entry(f1)
ssc_input.grid(row=20, column=2, sticky="w")

# Creating hsc/diploma percentage label
hsc_dip_label = Label(f1, 
                      text="HSC/Diploma Percentage", 
                      font="RobotoMono 16 bold", 
                      fg="#4d5156")
hsc_dip_label.grid(row=19, column=3, sticky="w")

# Creating hsc/diploma percentage entry
hsc_dip_input = Entry(f1)
hsc_dip_input.grid(row=20, column=3, sticky="w")

# Creating graduation latest cgpa label
cpi_label = Label(f1, 
                  text="Graduation Latest CGPA", 
                  font="RobotoMono 16 bold", 
                  fg="#4d5156")
cpi_label.grid(row=22, column=0, sticky="w")

# Creating graduation latest cgpa entry
cpi_input = Entry(f1)
cpi_input.grid(row=23, column=0, sticky="w", pady=10)

# Creating 12th or diploma label
dip_12_label = Label(f1, 
                     text="12th or Diploma", 
                     font="RobotoMono 16 bold", 
                     fg="#4d5156")
dip_12_label.grid(row=22, column=1, sticky="w")

# Creating 12th or diploma entry
dip_12_input = Entry(f1)
dip_12_input.grid(row=23, column=1, sticky="w")

# Creating no. of backlog label
backlog_label = Label(f1, 
                      text="No. of backlog", 
                      font="RobotoMono 16 bold", 
                      fg="#4d5156")
backlog_label.grid(row=22, column=2, sticky="w")

# Creating no. of backlog entry
backlog_input = Entry(f1)
backlog_input.grid(row=23, column=2, sticky="w")

# Creating no. of active backlog label
active_backlog_label = Label(f1, 
                             text="No. of active backlog", 
                             font="RobotoMono 16 bold", 
                             fg="#4d5156")
active_backlog_label.grid(row=22, column=3, sticky="w")

# Creating no. of active backlog entry
active_backlog_input = Entry(f1)
active_backlog_input.grid(row=23, column=3, sticky="w")

##################################################################################################
#                                  * Academics Details Section *                                 #
##################################################################################################

# Creating third frame
f2 = Frame(my_notebook, padx=170, pady=10)
# adding Academics Details tab in notebook
my_notebook.add(f2, text="Academics Details")

# Creating ssc details label
ssc_label = Label(f2, 
                  text="SSC Details", 
                  font="RobotoMono 16 bold", 
                  fg="#4d5156")
ssc_label.grid(row=1, column=0, sticky="w")

# creating education label
edu_label = Label(f2, 
                  text="Education", 
                  font="RobotoMono 16 bold", 
                  fg="#4d5156")
edu_label.grid(row=2, column=0, sticky="w", pady=10)

# creating education entry
edu_input = Entry(f2)
edu_input.grid(row=3, column=0, sticky="w", padx=(0, 80))

# creating university label
university_label = Label(f2, 
                         text="University", 
                         font="RobotoMono 16 bold", 
                         fg="#4d5156")
university_label.grid(row=2, column=1, sticky="w")

# creating university entry
university_input = Entry(f2)
university_input.grid(row=3, column=1, sticky="w", padx=(0, 80))

# creating institute name label
institute_label = Label(f2, 
                        text="Institute Name", 
                        font="RobotoMono 16 bold", 
                        fg="#4d5156")
institute_label.grid(row=2, column=2, sticky="w")

# creating institute name entry
institute_input = Entry(f2)
institute_input.grid(row=3, column=2, sticky="w", padx=(0, 80))

# Creating percentage label
ssc_percentage_label = Label(f2, 
                             text="Percentage", 
                             font="RobotoMono 16 bold", 
                             fg="#4d5156")
ssc_percentage_label.grid(row=5, column=0, sticky="w", pady=10)

# creating percentage entry
ssc_percentage_input = Entry(f2)
ssc_percentage_input.grid(row=6, column=0, sticky="w", pady=(0, 10))

# creating passing year label
ssc_passing_label = Label(f2, 
                          text="Passing Year", 
                          font="RobotoMono 16 bold", 
                          fg="#4d5156")
ssc_passing_label.grid(row=5, column=1, sticky="w")

# creating passing year entry
ssc_passing_input = Entry(f2)
ssc_passing_input.grid(row=6, column=1, sticky="w")

# creating checkbutton 
check1 = StringVar()
ssc_quali_label = Checkbutton(f2,
                              text="Highest Qualification",
                              font="RobotoMono 16 bold",
                              fg="#4d5156",
                              variable=check1,
                              onvalue="Yes",
                              offvalue="No",)
ssc_quali_label.grid(row=6, column=2, sticky="w")

# creating HSC/Diploma label
hsc_dip_edu_label = Label(f2, 
                          text="HSC/Diploma Details", 
                          font="RobotoMono 16 bold", 
                          fg="#4d5156")
hsc_dip_edu_label.grid(row=8, column=0, sticky="w")

# creating education label
dip_edu_label = Label(f2, 
                      text="Education", 
                      font="RobotoMono 16 bold", 
                      fg="#4d5156")
dip_edu_label.grid(row=9, column=0, sticky="w", pady=10)

# creating education entry
dip_edu_input = Entry(f2)
dip_edu_input.grid(row=10, column=0, sticky="w")

# creating university label
dip_uni_label = Label(f2, 
                      text="University", 
                      font="RobotoMono 16 bold", 
                      fg="#4d5156")
dip_uni_label.grid(row=9, column=1, sticky="w")

# creating university entry
dip_uni_input = Entry(f2)
dip_uni_input.grid(row=10, column=1, sticky="w")

# creating institute name label
dip_ist_label = Label(f2, 
                      text="Institute Name", 
                      font="RobotoMono 16 bold", 
                      fg="#4d5156")
dip_ist_label.grid(row=9, column=2, sticky="w")

# creating institute name entry
dip_ist_input = Entry(f2)
dip_ist_input.grid(row=10, column=2, sticky="w")

# creating percentage label
dip_per_label = Label(f2, 
                      text="Percentage", 
                      font="RobotoMono 16 bold", 
                      fg="#4d5156")
dip_per_label.grid(row=12, column=0, sticky="w", pady=10)

# creating percentage entry
dip_per_input = Entry(f2)
dip_per_input.grid(row=13, column=0, sticky="w", pady=(0, 10))

# creating passing year label
dip_passing_label = Label(f2, 
                          text="Passing Year", 
                          font="RobotoMono 16 bold", 
                          fg="#4d5156")
dip_passing_label.grid(row=12, column=1, sticky="w")

# creating passing year entry
dip_passing_input = Entry(f2)
dip_passing_input.grid(row=13, column=1, sticky="w")

# creating checkbutton
check2 = StringVar()
dip_qul_label = Checkbutton(f2,
                            text="Highest Qualification",
                            font="RobotoMono 16 bold",
                            fg="#4d5156",
                            variable=check2,
                            onvalue="Yes",
                            offvalue="No",)
dip_qul_label.grid(row=13, column=2, sticky="w")

# creating graduation details label
gradu_label = Label(f2, 
                    text="Graduation Details", 
                    font="RobotoMono 16 bold", 
                    fg="#4d5156")
gradu_label.grid(row=15, column=0, sticky="w")

# creating education label
gradu_edu_label = Label(f2, 
                        text="Education", 
                        font="RobotoMono 16 bold", 
                        fg="#4d5156")
gradu_edu_label.grid(row=16, column=0, sticky="w", pady=10)

# creating education entry
gradu_edu_input = Entry(f2)
gradu_edu_input.grid(row=17, column=0, sticky="w")

# creating university label
gradu_uni_label = Label(f2, 
                        text="University", 
                        font="RobotoMono 16 bold", 
                        fg="#4d5156")
gradu_uni_label.grid(row=16, column=1, sticky="w")

# creating university entry
gradu_uni_input = Entry(f2)
gradu_uni_input.grid(row=17, column=1, sticky="w")

# creating institute name label
gradu_ints_label = Label(f2, 
                         text="Institute Name", 
                         font="RobotoMono 16 bold", 
                         fg="#4d5156")
gradu_ints_label.grid(row=16, column=2, sticky="w")

# Creating Institute Name entry
gradu_ints_input = Entry(f2)
gradu_ints_input.grid(row=17, column=2, sticky="w")

# creating percentage label
gradu_per_label = Label(f2, 
                        text="Percentage", 
                        font="RobotoMono 16 bold", 
                        fg="#4d5156")
gradu_per_label.grid(row=18, column=0, sticky="w", pady=10)

# creating percentage entry
gradu_per_input = Entry(f2)
gradu_per_input.grid(row=19, column=0, sticky="w", pady=(0, 10))

# creating passing year label
gradu_passing_label = Label(f2, 
                            text="Passing Year", 
                            font="RobotoMono 16 bold", 
                            fg="#4d5156")
gradu_passing_label.grid(row=18, column=1, sticky="w")

# creating passing year entry
gradu_passing_input = Entry(f2)
gradu_passing_input.grid(row=19, column=1, sticky="w")

# creating checkbutton
check3 = StringVar()
gradu_is_high = Checkbutton(f2,
                            text="Highest Qualification",
                            font="RobotoMono 16 bold",
                            fg="#4d5156",
                            variable=check3,
                            onvalue="Yes",
                            offvalue="No")
gradu_is_high.grid(row=19, column=2, sticky="w")

##################################################################################################
#                                  * Address Details Section *                                   #
##################################################################################################

# Creating Address Details Frame
f3 = Frame(my_notebook, padx=125, pady=10)
# Adding Address Details tab in notebook
my_notebook.add(f3, text="Address Details")

# Creating Current Address label
address1_label = Label(f3, 
                       text="Current Address", 
                       font="RobotoMono 16 bold", 
                       fg="#4d5156")
address1_label.grid(row=1, column=0, sticky="w")

# Creating input text for current address
address1_text = Text(f3, 
                     font="RobotoMono 16 bold", 
                     fg="#4d5156", 
                     width=40, 
                     height=5)
address1_text.grid(row=2, column=0, sticky="w", pady=10)

# Creating pincode label
cur_pin = Label(f3, 
                text="Pincode", 
                font="RobotoMono 16 bold", 
                fg="#4d5156")
cur_pin.grid(row=3, column=0, sticky="w")

# Creating pincode entry
cur_pin_input = Entry(f3)
cur_pin_input.grid(row=4, column=0, sticky="w")

# Creating country label
cur_country = Label(f3, 
                    text="Country", 
                    font="RobotoMono 16 bold", 
                    fg="#4d5156")
cur_country.grid(row=3, column=1, sticky="w")

# Creating country entry
cur_country_input = Entry(f3)
cur_country_input.grid(row=4, column=1, sticky="w")

# creating address label
address2_label = Label(f3, 
                       text="Permanent Address", 
                       font="RobotoMono 16 bold", 
                       fg="#4d5156")
address2_label.grid(row=7, column=0, sticky="w", pady=10)

# creating input text for address
address2_text = Text(f3, 
                     font="RobotoMono 16 bold", 
                     fg="#4d5156", 
                     width=40, 
                     height=5)
address2_text.grid(row=8, column=0, sticky="w")

# creating pincode label 
permanent_pin = Label(f3, 
                      text="Pincode", 
                      font="RobotoMono 16 bold", 
                      fg="#4d5156")
permanent_pin.grid(row=9, column=0, sticky="w")

# creating pincode entry
permanent_pin_input = Entry(f3)
permanent_pin_input.grid(row=10, column=0, sticky="w")

# creating country label
permanent_country = Label(f3, 
                          text="Country", 
                          font="RobotoMono 16 bold", 
                          fg="#4d5156")
permanent_country.grid(row=9, column=1, sticky="w")

# creating country entry
permanent_country_input = Entry(f3)
permanent_country_input.grid(row=10, column=1, sticky="w")

##################################################################################################
#                                     * Upload Resume Section *                                  #
##################################################################################################

# Creating Upload Resume Frame
f4 = Frame(my_notebook, padx=125, pady=10)
# Adding upload resume tab in notebook
my_notebook.add(f4, text="Upload Resume")

# Creating upload resume label
cv_label = Label(f4, 
                 text="Upload Resume", 
                 font="RobotoMono 20 bold", 
                 fg="#4d5156")
cv_label.grid(row=1, column=1, sticky="w", pady=10)

# creating variable
cv_value = StringVar()
cv_output = Label(f4, 
                  text="", 
                  textvariable=cv_value, 
                  bg="white", 
                  width=50)
cv_output.grid(row=2, column=1, sticky="w")

# Creating Buttons
# Upload Button
upload_button = Button(f4,
                       text="Upload",
                       font="RobotoMono 20 bold",
                       fg="#4d5156",
                       padx=5,
                       pady=5,
                       command=lambda: upload_file())
upload_button.grid(row=3, column=1, sticky="w", pady=20)

# Submit Button
submit_button = Button(f4,
                       text="Submit",
                       font="RobotoMono 20 bold",
                       fg="#4d5156",
                       padx=5,
                       pady=5,
                       command=submit)
submit_button.place(x=400, y=550)

# Creating Mainloop
root.mainloop()
