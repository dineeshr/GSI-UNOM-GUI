from tkinter import *
def ins():
    instr = Tk()
    instr.geometry('1920x1080')
    instr.configure(bg='#8d5524')
    instr.title("GRADING SNIPPET AND INVESTIGATOR - UNIVERSITY OF MADRAS")
    heading = Label(instr,text = "INSTRUCTIONS",font=20,fg="#000").place(x = 620,y = 20)
    p1=Label(instr,text = """1. Insert the URL of the result website, Name of the sheet, Name of the file, Path to location of where to save the file in the text boxes and Students' Registration Numbers and Date of Birth in the List Box one below the other and click "OK" .""").place(x = 80,y = 100)
    p2=Label(instr,text = """2. Students' Names and Registration Numbers which are scraped will be printed in the Reference Box one below the other for users' reference .""").place(x = 80,y = 140)
    p3=Label(instr,text = """3. The excel sheet created will be saved in the given location in the "path" Text Box .""").place(x = 80,y = 180)
    p4=Label(instr,text = """4. In the excel sheet, Students' Name and Registration Numbers will be appended in the first and second column .""").place(x = 80,y = 220)
    p5=Label(instr,text = """5. The marks and analysis will be appended in the respective columns .""").place(x = 80,y = 260)
    instr.mainloop()