import time
import sys
from rich.table import Table
from rich.console import Console
import shelve

ascend=["a","b","c","d","e","f","g","h","i","j","k","l"
        ,"m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

adminno={'232499R':'honoi08',
         '90786FT':'79pixsw',
         '108734G':'lavender90'}

user=["user"]
adding=[]
changes=[]
deletes=[]
failure=[]
class Employee:
    def __init__(self,name,employee_id,department,job_title,annual_salary,status):
        self.__name=name
        self.__id=employee_id
        self.__department=department
        self.__title=job_title
        self.__annual_salary=annual_salary
        self.__status=status

    def set_name(self,name):
        self.__name=name
    def set_id(self,employee_id):
        self.__id=employee_id
    def set_dept(self,department):
        self.__department=department
    def set_title(self,job_title):
        self.__title=job_title
    def set_annual_salary(self,annual_salary):
        self.__annual_salary=annual_salary
    def set_status(self,status):
        self.__status=status

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_dept(self):
        return self.__department
    def get_title(self):
        return self.__title
    def get_annual_salary(self):
        return self.__annual_salary
    def get_status(self):
        return self.__status


def login():
    a=False
    i=0
    x=0
    while a == False:
        i+=1
        username=input("enter admin no./employee ID here: ")
        passwd=input("enter password here: ")
        print(i)

        if adminno.get(username) == passwd:
            a = True
            failure.append(i)
            user[0]=username
            menu()
        if i==5:
            print("You will be locked out for 30 seconds")
            time.sleep(30)
        if i>5 and i<=10:
            print("you will be locked out for 20 seconds")
            time.sleep(20)
        if i>10:
            x+=1
            print("You have been locked out for ",x," hours")
            time.sleep(360*x)


def menu():
   U_choice=""
   while U_choice != "q":
    print("Enter 1 to display table,")
    print("Enter 2 to add")
    print("Enter 3 to sort by department")
    print("Enter 4 to sort employee by salary.")
    print("Enter 5 to update")
    print("Enter 6 to delete data.")
    print("Press q to quit.")
    U_choice=input("Enter num here: ")
    if U_choice == "1":
        display()
    if U_choice == "2":
        add()
    if U_choice == "3":
        dept_sort()
    if U_choice == "4":
        salary_sort()
    if U_choice == "5":
        update()
    if U_choice == "6":
        delete()
    else:
        print("Thanks for using")
        log()


def display():
    table=Table(title="Employees",expand=True)
    rows=[]
    columns=["ID","Name","Department","Job Title","Annual Salary","Employment Status"]
    employee_dict.update({"ID": {}})
    del employee_dict["ID"]
    IDs=list(employee_dict.keys())
    for i in range(len(IDs)):
        z=IDs[i]
        w=str(z)
        y=int(w)
        rows.append([str(IDs[i]),employee_dict[y]["Name"],employee_dict[y]["Department"],
                    employee_dict[y]["Job title"],"$"+"%0.2f"%(employee_dict[y]["Annual Salary"]),
                    str(employee_dict[y]["Employment Status"])]
                    )
    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*row)
    table.show_lines=True
    console = Console()
    console.print(table)
    time.sleep(3)
    menu()

def add():
    print("Press 1 enter manually, 2-4 to autofill names (for me to make it look lived in)")
    U_input=input('enter num here: ')
    if U_input == '1':
        n="y"
        while n == "y":
         try:
          Id=int(input("enter employee id here: "))
          name=input("enter name here: ")
          Dept=input("enter department here: ")
          title=input("enter title here: ")
          Salary=float(input("enter annual salary here:$ "))
          status=bool(input("enter employment status here (enter True or False): "))
          e=Employee(name,Id,Dept,title,Salary,status)
          id = e.get_id()
          employee_dict.update({"ID": {}})
          employee_dict[id] = employee_dict["ID"]
          del employee_dict["ID"]
          employee_dict[id]['Name'] = e.get_name()
          employee_dict[id]['Department'] = e.get_dept()
          employee_dict[id]['Job title'] = e.get_title()
          employee_dict[id]['Annual Salary'] = e.get_annual_salary()
          employee_dict[id]['Employment Status'] = e.get_status()
          db["ID"] = employee_dict
          adding.append(id)
          employee_dict.update({"ID": {}})
          n = input("do you wish to add another user? y/n: ").lower()
         except:
            if ValueError:
                print("There was a error with the value, sending you back to menu. ")
                employee_dict.update({"ID": {}})
                time.sleep(3)
                menu()
        menu()
    if U_input == '2':
        e = Employee(name="Nathan", employee_id=10009, department='Technology',
                     job_title='Project Head', annual_salary=100000.00, status=True)
        id=e.get_id()
        employee_dict.update({"ID": {}})
        employee_dict[id]=employee_dict["ID"]
        del employee_dict["ID"]
        employee_dict[id]['Name'] = e.get_name()
        employee_dict[id]['Department'] = e.get_dept()
        employee_dict[id]['Job title'] = e.get_title()
        employee_dict[id]['Annual Salary'] = e.get_annual_salary()
        employee_dict[id]['Employment Status'] = e.get_status()
        db["ID"] = employee_dict
        adding.append(id)
        employee_dict.update({"ID":{}})
        menu()
    if U_input == "3":
        e = Employee(name="Terrance", employee_id=10007, department='Tourism',
                     job_title='Employee', annual_salary=82000.00, status=True)
        id = e.get_id()
        employee_dict.update({"ID": {}})
        employee_dict[id] = employee_dict["ID"]
        del employee_dict["ID"]
        employee_dict[id]['Name'] = e.get_name()
        employee_dict[id]['Department'] = e.get_dept()
        employee_dict[id]['Job title'] = e.get_title()
        employee_dict[id]['Annual Salary'] = e.get_annual_salary()
        employee_dict[id]['Employment Status'] = e.get_status()
        db["ID"] = employee_dict
        adding.append(id)
        employee_dict.update({"ID": {}})
        menu()
    if U_input == "4":
        e = Employee(name="Bartholomew", employee_id=10008, department='Property',
                     job_title='Agent', annual_salary=90000.50, status=True)
        id = e.get_id()
        employee_dict.update({"ID": {}})
        employee_dict[id] = employee_dict["ID"]
        del employee_dict["ID"]
        employee_dict[id]['Name'] = e.get_name()
        employee_dict[id]['Department'] = e.get_dept()
        employee_dict[id]['Job title'] = e.get_title()
        employee_dict[id]['Annual Salary'] = e.get_annual_salary()
        employee_dict[id]['Employment Status'] = e.get_status()
        db["ID"] = employee_dict
        adding.append(id)
        employee_dict.update({"ID": {}})
        menu()

def dept_sort():
    table = Table(title="Employees")
    employee_dict.update({"ID": {}})
    del employee_dict["ID"]
    x=len(employee_dict)
    columns=["Department","Name","ID"]
    sorted = []
    rows = []
    IDs = list(employee_dict.keys())
    for i in range(x):
        a = IDs[i]
        b = str(a)
        y = int(b)
        d=employee_dict[y]["Department"]
        n=employee_dict[y]["Name"]
        sorted.append(d+" "+"|"+" "+n+" "+"|"+" "+str(a))
    for i in range(x-1,0,-1):
        for y in range(i):
            init=sorted[y]
            g = init[0].lower()
            v = ascend.index(g)
            last=sorted[y+1]
            z = last[0].lower()
            q = ascend.index(z)
            if q < v:
                tmp = sorted[y]
                sorted[y]=sorted[y+1]
                sorted[y+1]=tmp
    for y in range(len(sorted)):
        rows.append(sorted[y].split("|"))

    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*row)
    table.show_lines=True
    console = Console()
    console.print(table)
    employee_dict.update({"ID": {}})
    time.sleep(3)
    menu()
def salary_sort():
    table = Table(title="Employees")
    employee_dict.update({"ID": {}})
    del employee_dict["ID"]
    x = len(employee_dict)
    salary=[]
    final=[]
    names=[]
    columns=["Annual Salary","Name","ID"]
    rows=[]
    IDs = list(employee_dict.keys())
    for i in range(x):
        a = IDs[i]
        b = str(a)
        q = int(b)
        d=employee_dict[q]["Annual Salary"]
        n=employee_dict[q]["Name"]
        salary.append(d)
        names.append(n+" "+"|"+" "+str(q))
    for i in range(len(salary)):
        bigNdx = i
        for j in range(i+1,len(salary)):
            if salary[j] > salary[bigNdx]:
                bigNdx=j
        if bigNdx != i:
            tmp = salary[i]
            tmp2 = names[i]
            salary[i] = salary[bigNdx]
            names[i] = names[bigNdx]
            salary[bigNdx] = tmp
            names[bigNdx] = tmp2
    for i in range(len(salary)):
        a=names[i]
        b=salary[i]
        final.append("$"+"%0.2f"%(b)+" "+"|"+" "+a)
    for i in range(len(final)):
        rows.append(final[i].split("|"))

    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*row)
    table.show_lines=True
    console = Console()
    console.print(table)
    employee_dict.update({"ID": {}})
    time.sleep(3)
    menu()

def update():
    Loop = "y"
    while Loop == "y":
       try:
        ID=int(input("enter employee ID to update: "))
        name = input("enter name here: ")
        Dept = input("enter department here: ")
        title = input("enter title here: ")
        Salary = float(input("enter annual salary here:$ "))
        status = bool(input("enter employment status here (enter True or False): "))
        e=Employee(name,ID,Dept,title,Salary,status)
        employee_dict[ID]["Name"]=e.get_name()
        employee_dict[ID]["Department"]=e.get_dept()
        employee_dict[ID]["Job title"]=e.get_title()
        employee_dict[ID]["Annual Salary"]=e.get_annual_salary()
        employee_dict[ID]["Employment Status"]=e.get_status()
        db["ID"] = employee_dict
        changes.append(ID)
        Loop=input("do you wish to update more than once? y/n: ").lower()
        employee_dict.update({"ID": {}})
       except:
           if ValueError or KeyError:
               print("There was an error with the data keyed.")
               employee_dict.update({"ID": {}})
               time.sleep(3)
               menu()
    menu()

def delete():
     loop = "y"
     while loop == "y":
         try:
           ID=int(input("enter employee ID to delete: "))
           del employee_dict[ID]
           db["ID"] = employee_dict
           deletes.append(ID)
           employee_dict.update({"ID":{}})
           loop= input("do you wish to delete more? y/n: ")
         except:
            if ValueError:
                employee_dict.update({"ID": {}})
                print("error with values. ")
                time.sleep(3)
                menu()
     menu()

def log():
    f=open("logfile.txt","a")
    f.write("number of login attempts: "+str(failure[0])+"\n")
    f.write("admin using: "+user[0]+",")
    for i in range(len(adding)):
        f.write("added: "+str(adding[i])+", ")
    for i in range(len(changes)):
        f.write("updated: "+str(changes[i])+", ")
    for i in range(len(deletes)):
        f.write("deleted: "+str(deletes[i])+", ")
    f.write("\n")
    f.close()
    sys.exit()

employee_dict={

}

db=shelve.open("ID","c")
try:
    if 'ID' in db:
        employee_dict=db['ID']
    for i in range(len(db)):
        del str
    else: db['ID']=employee_dict
except: print("error in accessing database")

#login()
menu()


