# import database module
import os
import random, csv

from database import CSV, DB, Table


def initializing():
    data_base = DB()
    person_csv = CSV("persons.csv")
    person1 = person_csv.read_file()
    add1 = Table("persons table", person1)
    data_base.insert(add1)
    login_csv = CSV("login.csv")
    person2 = login_csv.read_file()
    add2 = Table("login table", person2)
    data_base.insert(add2)
    project_csv = CSV("Project.csv")
    person3 = project_csv.read_file()
    add3 = Table("Project table", person3)
    data_base.insert(add3)
    Advisor_pending_request_csv = CSV("Advisor_pending_request.csv")
    person4 = Advisor_pending_request_csv.read_file()
    add4 = Table("Advisor_pending_request table", person4)
    data_base.insert(add4)
    Member_pending_request_csv = CSV("Member_pending_request.csv")
    person5 = Member_pending_request_csv.read_file()
    add5 = Table("Member_pending_request table", person5)
    data_base.insert(add5)
    return data_base


def login():
    data = initializing()
    login_table = data.search("login table")
    username = input("username: ")
    password = input("password: ")
    _list = []
    for i in login_table.table:
        if username == i['Username'] and password == i['Password']:
            _list.append(i["ID"])
            _list.append(i["Role"])
            return _list
        else:
            continue


def exit():
    myFile1 = open('persons.csv', 'w')
    writer1 = csv.writer(myFile1)
    writer1.writerow(['ID', 'First', 'Last', 'Type'])
    for dictionary in data.search("persons table").table:
        writer1.writerow(dictionary.values())
    myFile1.close()
    myFile2 = open('login.csv', 'w')
    writer2 = csv.writer(myFile2)
    writer2.writerow(['ID', 'Username', 'Password', 'Role'])
    for dictionary in data.search("login table").table:
        writer2.writerow(dictionary.values())
    myFile2.close()
    myFile3 = open('Project.csv', 'w')
    writer3 = csv.writer(myFile3)
    writer3.writerow(['ProjectID', 'Title', 'Lead', 'Member1', 'Member2',
                      'Advisor', 'Status'])
    for dictionary in data.search("Project table").table:
        writer3.writerow(dictionary.values())
    myFile3.close()
    myFile4 = open('Advisor_pending_request.csv', 'w')
    writer4 = csv.writer(myFile4)
    writer4.writerow(['ProjectID', 'to_be_advisor', 'Response',
                      'Response_date'])
    for dictionary in data.search("Advisor_pending_request table").table:
        writer4.writerow(dictionary.values())
    myFile4.close()
    myFile5 = open('Member_pending_request.csv', 'w')
    writer5 = csv.writer(myFile5)
    writer5.writerow(['ProjectID', 'to_be_member', 'Response',
                      'Response_date'])
    for dictionary in data.search("Member_pending_request table").table:
        writer5.writerow(dictionary.values())
    myFile5.close()


class Student:
    def __init__(self):
        for i in data.search("Member_pending_request table").table:
            self.ID = i["ProjectID"]

    def check(self):
        print("1.create a project")
        print("2.read the project details")
        print("3.be a member")

    def create_project(self):
        project = input("Enter project name: ")
        _list = []
        x = random.randrange(1, 10**6)
        _list.append(x)
        data.search("login table").update("ID", val[0], "Role", "lead")
        data.search("persons table").update("ID", val[0], "Type", "lead")
        return x, project

    def read_project_detail(self):
        print(data.search("Project table"))

    def be_member(self):
        a = input("Accept or Deny(a/n): ")
        if a == "a":
            data.search("login table").update("ID", val[0], "Role", "member")
            for i in data.search("Project table").filter(lambda x: x[
                "ProjectID"] == self.ID).table:
                if i["Member1"] == "None":
                    data.search("Project table").update("ProjectID", self.ID,
                                                        "Member1", val[0])
                    data.search("Member_pending_request table").update(
                        "to_be_member", val[0], "Response", "Accepted")
                    data.search("persons table").update("ID", val[0], "Type",
                                                        "member")
                elif i["Member2"] == "None":
                    data.search("Project table").update("ProjectID",
                                                        self.ID, "Member2", val[0])
                    data.search("Member_pending_request table").update(
                        "to_be_member", val[0], "Response", "Accepted")
                    data.search("persons table").update("ID", val[0], "Type",
                                                        "member")
        else:
            data.search("Member_pending_request table").update("to_be_member", val[0],
                                                          "Response", "Deny")


class Lead:
    def __init__(self):
        for i in data.search("Project table").filter(lambda x: x["Lead"] ==
                                                               val[0]).table:
            self.ID = i["ProjectID"]
            self.status = i["Status"]

    def update_status(self):
        update = input("what did you have done: ")
        data.search("Project table").update("ProjectID", self.ID, "Status",
                                            update)

    def invite(self):
        invite = input("who do you want to invite?(student/faculty): ")
        if invite.lower() == "student":
            for i in data.search("Project table").filter(lambda x: x["ProjectID"] == self.ID).table:
                if i["Member1"] == 'None' or i["Member2"] == 'None':
                    print(data.search("persons table").filter(lambda x: x[
                                                "Type"] == "student"))
                    send_who = int(input("enter ID: "))
                    date = input("enter date: ")
                    dict_student_request = {"ProjectID": self.ID,
                                            "to_be_member": send_who,
                                            "Response": "pending",
                                            "Response_date": date}
                    data.search("Member_pending_request table").insert(dict_student_request)
        elif invite.lower() == "faculty":
            print(data.search("persons table").filter(lambda x: x["Type"] ==
                                                        "faculty"))
            send_who = int(input("enter ID: "))
            date = input("enter date: ")
            dict_advisor_request = {"ProjectID": self.ID,
                                    "to_be_advisor": send_who,
                                    "Response": "pending",
                                    "Response_date": date}
            data.search("Advisor_pending_request table").insert(
                dict_advisor_request)


class Member:
    def __init__(self):
        for i in data.search("Project table").filter(lambda x: x["Member1"] \
                or x["Member2"] == val[0]).table:
            self.ID = i["ProjectID"]
            self.status = i["Status"]
    def update_status(self):
        update = input("what did you have done: ")
        data.search("Project table").update("ProjectID", self.ID, "Status",
                                            update)

    def see(self):
        print(data.search("Project table").filter(lambda x: x["Member1"] or
                                            x["Member2"] == val[0]).table)


class Faculty:
    def __init__(self):
        for i in data.search("Advisor_pending_request table").filter(lambda
                                    x: x["to_be_advisor"] == val[0]).table:
            self.ID = i["ProjectID"]
            self.status = i["Response"]

    def be_advisor(self):
        print(data.search("Advisor_pending_request table").filter(lambda x: x[
                                                "to_be_advisor"] == val[0]))
        a = input("Accept or Deny(a/n): ")
        if a.lower() == "a":
            for i in data.search("Project table").filter(lambda x: x[
                                        "ProjectID"] == self.ID).table:
                if i["Advisor"] == "None":
                    data.search("login table").update("ID", val[0], "Role",
                                                      "advisor")
                    data.search("Project table").update("ProjectID", self.ID,
                                                        "Advisor", val[0])
                    data.search("Advisor_pending_request table").update(
                        "to_be_advisor", val[0], "Response", "Accepted")
                    data.search("persons table").update("ID", val[0], "Type",
                                                      "advisor")
        else:
            data.search("Advisor_pending_request table").update(
                "to_be_advisor", val[0], "Response", "Deny")


class Advisor:
    def __init__(self):
        for i in data.search("Project table").filter(lambda x: x["Advisor"]
                                                               == val[
                                                                   0]).table:
            self.ID = i["ProjectID"]

    def update_status(self):
        approve = input("Approve or not?(Approve/Not approve): ")
        data.search("Project table").update("ProjectID", self.ID, "Status",
                                            approve)

    def see(self):
        print(data.search("Project table").filter(lambda x: x["ProjectID"]
                                                            == self.ID))


class Admin:
    def fix(self):
        fix = input("Which part do you want to fix: ")
        if fix.lower() == "id":
            first = int(input("Enter the ID: "))
            new_ID = int(input("Enter new ID: "))
            data.search("login table").update("ID", first, "ID", new_ID)
            if first == data.search("Project table").filter(lambda x: x[
                "Lead"]):
                data.search("Project table").update("Lead", first, "Lead",
                                                    new_ID)
            elif first == data.search("Project table").filter(lambda x: x[
                "Member1"]):
                data.search("Project table").update("Member1", first,
                                                    "Member1", new_ID)
                data.search("Member_pending_request table").update(
                    "to_be_member", first, "to_be_member", new_ID)
            elif first == data.search("Project table").filter(lambda x: x[
                "Member2"]):
                data.search("Project table").update("Member2", first,
                                                    "Member2", new_ID)
                data.search("Member_pending_request table").update(
                    "to_be_member", first, "to_be_member", new_ID)
            elif first == data.search("Project table").filter(lambda x: x[
                "Advisor"]):
                data.search("Project table").update("Advisor", first,
                                                    "Advisor", new_ID)
                data.search("Advisor_pending_request table").update(
                    "to_be_advisor", first, "to_be_advisor", new_ID)
            data.search("persons table").update("ID", first,
                                                "ID", new_ID)
        elif fix.lower() == "username":
            first = input("Enter your old username: ")
            new = input("Enter your new username: ")
            data.search("login table").update("Username", first, "Username",
                                              new)
        elif fix.lower() == "password":
            first = input("Enter your old password: ")
            new = input("Enter your new password: ")
            data.search("login table").update("Password", first, "Password",
                                              new)
        elif fix.lower() == "role":
            first = input("Enter your old role: ")
            new = input("Enter your new role: ")
            data.search("login table").update("Role", first, "Role", new)
            data.search("persons table").update("Type", first, "Type", new)
        elif fix.lower() == "title":
            first = input("Enter your old title: ")
            new = input("Enter your new title: ")
            data.search("Project table").update("Title", first, "Title", new)
        elif fix.lower() == "projectid":
            first = input("Enter your old ProjectID: ")
            new = input("Enter your new ProjectID: ")
            data.search("Project table").update("ProjectID", first,
                                                "ProjectID", new)
            data.search("Member_pending_request table").update(
                    "ProjectID", first, "ProjectID", new)
            data.search("Advisor_pending_request table").update("ProjectID",
                                                                first,
                                                                "ProjectID",
                                                                new)
        elif fix.lower() == "status":
            first = input("Enter your old status: ")
            new = input("Enter your new status: ")
            data.search("Project table").update("Status", first,
                                                "Status", new)
        elif fix.lower() == "first":
            first = input("Enter your old first: ")
            new = input("Enter your new first: ")
            data.search("persons table").update("First", first,
                                                "First", new)
        elif fix.lower() == "last":
            first = input("Enter your old last: ")
            new = input("Enter your new last: ")
            data.search("persons table").update("Last", first,
                                                "Last", new)

    def choose_eva(self):
        print(data.search("login table").filter(lambda x: x["Role"] ==
                                                          "faculty"))
        eva = int(input("Enter evaluator ID: "))
        data.search("login table").update("ID", eva, "Role", "evaluator")
        data.search("persons table").update("ID", eva, "Type", "evaluator")


class Evaluator:
    def update(self):
        print(data.search("Project table"))
        update = int(input("Enter Project ID you wanted to update: "))
        pass_or_not = input("Pass or not(pass/not pass): ")
        data.search("persons table").update("ProjectID", update, "Status",
                                            pass_or_not)


data = initializing()
val = login()
while True:
    if val[1].lower() == 'student':
        student = Student()
        student.check()
        num = int(input("please enter the num: "))
        if num == 1:
            ID, name = student.create_project()
            dict_create = {"ProjectID": ID, "Title": name, "Lead": val[0],
                           "Member1": "None", "Member2": "None", "Advisor":
                               "None", "Status": "created"}
            data.search("Project table").insert(dict_create)
        elif num == 2:
            student.read_project_detail()
        elif num == 3:
            student.be_member()
    elif val[1].lower() == "lead":
        lead = Lead()
        get = input("update or invite?: ")
        if get.lower() == "update":
            lead.update_status()
        elif get.lower() == "invite":
            lead.invite()
    elif val[1].lower() == "member":
        member = Member()
        get = input("update or see(u/s)?: ")
        if get == "u":
            member.update_status()
        elif get == "s":
            member.see()
    elif val[1].lower() == "faculty":
        faculty = Faculty()
        faculty.be_advisor()
    elif val[1].lower() == "advisor":
        advisor = Advisor()
        get = input("update or see(u/s)?: ")
        if get.lower() == "u":
            advisor.update_status()
        elif get.lower() == "s":
            advisor.see()
    elif val[1].lower() == "admin":
        admin = Admin()
        get = input("fix or choose(f/c): ")
        if get.lower() == "f":
            admin.fix()
        elif get.lower() == "c":
            admin.choose_eva()
    elif val[1].lower() == "evaluator":
        evaluator = Evaluator()
        get = input("want to correct the project?(y): ")
        if get.lower() == "y":
            evaluator.update()
    c = input("continue or exit(c/e): ")
    if c.lower() == "e":
        break

# once everyhthing is done, make a call to the exit function
initializing()
exit()
