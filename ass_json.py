import json
class Employee:
    def __init__(self):
        self.information={}

    def emp_info(self):
        self.name = input("enter your name : ")
        # from datetime import date
        year = int(input("enter your DOB year : "))
        month = int(input("enter your DOB month : "))
        day = int(input("enter your DOB day : "))
        self.DOB = print(day,month,year)
        self.height = int(input("enter your height in CM: "))
        self.city = input("enter your city : ")
        self.state = input("enter your state : ")
        self.information = {"name":self.name,"DOB":self.DOB,"height":self.height,"city":self.city,"state":self.state}
        with open("employee.json","w") as f:
            json.dump(self.information,f)
        print(self.information)
x=Employee()
x.emp_info()
