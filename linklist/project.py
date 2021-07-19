from os import system
import sqlite3
from colorama import init
from termcolor import colored

init()
cls = lambda:system('cls')
db_name = "db.sqlite"

class menu:
    def start(self):
        connect = sqlite3.connect(db_name)
        c = connect.cursor()

        c.execute("SELECT * FROM `freelancer`")
        global freelancer_list
        freelancer_list = freeLancers()
        for i in c.fetchall():
            freelancer_list.add_end(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
        
        c.execute("SELECT * FROM `project`")
        global project_list
        project_list = projects()
        for i in c.fetchall():
            project_list.add_end(i[0],i[1],i[2],i[3],i[4],i[5])
        
        c.execute("SELECT * FROM `employer`")
        global employer_list
        employer_list = employers()
        for i in c.fetchall():
            employer_list.add_end(i[0],i[1],i[2],i[3],i[4])
        
        connect.close()
        k.menu()

    def menu(self):
        while True:
            cls()
            print(70*"_")
            print("|{:-^68}|".format("wellcome"))
            print("|"+68*"-"+"|"+"\n\n")
            print("--Main Menu")
            print()
            print("    |- 1) Login as Freelacer")
            print("    |- 2) Login as Employer")
            print()
            print("    |- 3) Register as Freelacer")
            print("    |- 4) Register as Employer")
            print()
            print("    |- 5) Exit")
            print("\n")
            key = input("Choose menu item(1-5): ")

            if key == "1":
                k.login(1)
            elif key == "2":
                k.login(2)
            elif key == "3":
                k.register_freelancer()
            elif key == "4":
                k.register_employer()
            elif key == "5":
                exit()
    
    def login(self,key):
        cls()
        print(70*"_")
        print("|{:-^68}|".format("Login"))
        print("|"+68*"-"+"|"+"\n\n")
        print("--Login\n")

        while True:
            username = input("-Enter Username: ")
            password = input("-Enter password: ")
            if key == 1:
                node = freelancer_list.login(username,password)
                if node == False:
                    print(colored("\n \t Error: Username/password does not match!!!", 'red'))
                else:
                    k.freelancer_profile(node)
            elif key == 2:
                node = employer_list.login(username,password)
                if node == False:
                    print(colored("\n \t Error: Username/password does not match!!!", 'red'))
                else:
                    k.employer_profile(node)

    def register_freelancer(self):
        cls()
        print(70*"_")
        print("|{:-^68}|".format("Register as Freelacer"))
        print("|"+68*"-"+"|"+"\n\n")
        print("--Register as Freelacer\n")
        username = input("\tEnter Username: ")
        password = input("\tEnter Password: ")
        firstname = input("\tEnter Firstname: ")
        lastname = input("\tEnter Lastname: ")
        abilities = input("\tEnter Abilities: ")
        bio = input("\tEnter Bio: ")

        connect = sqlite3.connect(db_name)
        c = connect.cursor()
        c.execute("INSERT INTO `freelancer` (firstname,lastname,abilities,bio,username,password) VALUES ('{}','{}','{}','{}','{}','{}')".format(firstname,lastname,abilities,bio,username,password))
        connect.commit()
        c.execute("SELECT id FROM `freelancer`")
        id = c.fetchall()[-1]
        id = int(id[0])
        connect.close()

        node = freelancer_list.add_end(id,firstname,lastname,abilities,bio,username,password)
        k.freelancer_profile(node)

    def register_employer(self):
        cls()
        print(70*"_")
        print("|{:-^68}|".format("Register as Employer"))
        print("|"+68*"-"+"|"+"\n\n")
        print("--Register as Employer\n")
        username = input("\tEnter Username: ")
        password = input("\tEnter Password: ")
        firstname = input("\tEnter Firstname: ")
        lastname = input("\tEnter Lastname: ")

        connect = sqlite3.connect(db_name)
        c = connect.cursor()
        c.execute("INSERT INTO `employer` (firstname,lastname,username,password) VALUES ('{}','{}','{}','{}')".format(firstname,lastname,username,password))
        connect.commit()
        c.execute("SELECT id FROM `employer`")
        id = c.fetchall()[-1]
        id = int(id[0])
        connect.close()

        node = employer_list.add_end(id,firstname,lastname,username,password)
        k.employer_profile(node)

    def freelancer_profile(self,node):
        while True:
            cls()
            print(70*"_")
            print("|{:-^68}|".format("Freelancer Profile"))
            print("|"+68*"-"+"|"+"\n\n")
            print("{:15}{}\n".format("ID:",node.id))
            print("{:15}{}\n".format("Username:",node.username))
            print("{:15}{}\n".format("Fristname:",node.firstname))
            print("{:15}{}\n".format("Lastname:",node.lastname))
            print("{:15}{}\n".format("Abilities:",node.abilities))
            print("{:15}{}\n".format("Bio:",node.bio))
            print("\n\n--Menu:")
            print("    |- 1) Edit Profile")
            print("    |- 2) Search Project")
            print("    |- 3) Delete Account")
            print("    |- 4) Log Out")
            print("    |- 5) Exit")
            key = input("Choose menu item(1-5): ")
            
            if key == "1":
                k.edit_freelancer(node)
            elif key == "2":
                k.search(node)
            elif key == "3":
                key = input("Are you sure you want to clear your account? (y-n):")
                if key == "y":
                    freelancer_list.delete(node.id)
                    k.menu()
            elif key == "4":
                k.menu()
            elif key == "5":
                exit()
    
    def edit_freelancer(self,node):
        print("\n\t",colored("(Please fill the below inputs)","green"))
        print("\t",colored("(Let it be blank if you don't want to change any)","yellow"),"\n")
        username = input("\tEnter New Username: ")
        password = input("\tEnter New Password: ")
        firstname = input("\tEnter New Firstname: ")
        lastname = input("\tEnter New Lastname: ")
        abilities = input("\tEnter New Abilities: ")
        bio = input("\tEnter New Bio: ")
        freelancer_list.edit(node,firstname,lastname,abilities,bio,username,password)
        k.freelancer_profile(node)

    def employer_profile(self,node):
        while True:
            cls()
            print(70*"_")
            print("|{:-^68}|".format("employer Profile"))
            print("|"+68*"-"+"|"+"\n\n")
            print("{:15}{}\n".format("ID:",node.id))
            print("{:15}{}\n".format("Username:",node.username))
            print("{:15}{}\n".format("Fristname:",node.firstname))
            print("{:15}{}\n".format("Lastname:",node.lastname))
            print("\n\n--Menu:")
            print("    |- 1) Edit Profile")
            print("    |- 2) Add project")
            print("    |- 3) My project")
            print("    |- 4) Delete Account")
            print("    |- 5) Log Out")
            print("    |- 6) Exit")
            key = input("Choose menu item(1-6): ")
            
            if key == "1":
                k.edit_employer(node)
            elif key == "2":
                k.add_project(node)
            elif key == "3":
                k.my_project(node)
            elif key == "4":
                key = input("Are you sure you want to clear your account? (y-n):")
                if key == "y":
                    employer_list.delete(node.id)
                    k.menu()
            elif key == "5":
                k.menu()
            elif key == "6":
                exit()

    def edit_employer(self,node):
        print("\n\t",colored("(Please fill the below inputs)","green"))
        print("\t",colored("(Let it be blank if you don't want to change any)","yellow"),"\n")
        username = input("\tEnter New Username: ")
        password = input("\tEnter New Password: ")
        firstname = input("\tEnter New Firstname: ")
        lastname = input("\tEnter New Lastname: ")
        employer_list.edit(node,firstname,lastname,username,password)
        k.employer_profile(node)

    def my_project(self,node):
        project = project_list.my_project(node.id)
        while True:
            cls()
            print(90*"—")
            print("|{:^88}|".format("My Projects"))
            print("|"+88*"—"+"|")
            print("|{:^4}|{:^15}|{:^35}|{:^20}|{:^10}|".format("ID","Title","Description","Abilities","Price"))
            for i in project:
                print("|"+88*"—"+"|")
                
                title = i.title if len(i.title) <= 15 else  i.title[0:12]+"..."
                description = i.description if len(i.description) <= 35 else  i.description[0:32]+"..."
                abilities = i.abilities if len(i.abilities) <= 20 else  i.abilities[0:17]+"..."

                print("|{:^4}|{:^15}|{:<35}|{:<20}|{:10,}|".format(i.id,title,description,abilities,i.price))
            print(90*"—"+"\n\n")

            key = input("Enter the ID of one of the projects to edit OR Enter 'b' to Go back: ")
            if key == 'b':
                k.employer_profile(node)
            elif key == "":
                pass
            else:
                k.edit_project(node,key,node.id)

    def edit_project(self,node,id,owner_id):
        project = project_list.employer_search(id,owner_id)
        if project == False:
            print(colored("\n \t You do not have a project with ID {}".format(id), 'red'))
        else:
            cls()
            print(70*"_")
            print("|{:-^68}|".format("Edit project"))
            print("|"+68*"-"+"|"+"\n\n")
            print("{:15}{}\n".format("ID:",project.id))
            print("{:15}{}\n".format("Title:",project.title))
            print("{:15}{}\n".format("Description:",project.description))
            print("{:15}{}\n".format("Abilities:",project.abilities))
            print("{:15}{:,}$\n".format("Price:",project.price))
            print("\n\t",colored("(Please fill the below inputs)","green"))
            print("\t",colored("(Let it be blank if you don't want to change any)","yellow"),"\n")

            key = input("If you want to delete this project, enter the word 'delete', otherwise press Enter.")
            if key == "delete":
                project_list.delete(int(id),0)
                input("Press Any key ... ")
                k.my_project(node)
            
            title = input("Enter New Title: ")
            description = input("Enter New Description: ")
            abilities = input("Enter New abilities: ")
            price = input("Enter New Price: ")
            project_list.edit(id,title,description,abilities,price)
        
        input("Press Any key ... ")
        k.my_project(node)
    
    def add_project(self,node):
        cls()
        print(70*"—")
        print("|{:^68}|".format("Add Project"))
        print("|"+68*"_"+"|"+"\n\n")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        abilities = input("Enter abilities: ")
        while True:
            try:
                price = int(input("Enter Price: "))
                break
            except:
                print(colored("\n \t Error: Please enter the price in the number!!!", 'red'))

        connect = sqlite3.connect(db_name)
        c = connect.cursor()
        c.execute("INSERT INTO `project` (owner_id,title,description,abilities,price) VALUES ('{}','{}','{}','{}',{})".format(node.id,title,description,abilities,price))
        connect.commit()
        c.execute("SELECT id FROM `project`")
        id = c.fetchall()[-1]
        id = int(id[0])
        connect.close()

        project_list.add_end(id,node.id,title,description,abilities,price)
        k.employer_profile(node)

    def search(self,node):
        project = project_list.freelancer_search(node.abilities)
        while True:
            cls()
            print(90*"—")
            print("|{:^88}|".format("Projects tailored to your abilities"))
            print("|"+88*"—"+"|")
            print("|{:^4}|{:^15}|{:^35}|{:^20}|{:^10}|".format("ID","Title","Description","Abilities","Price"))
            for i in project:
                print("|"+88*"—"+"|")
                
                title = i.title if len(i.title) <= 15 else  i.title[0:12]+"..."
                description = i.description if len(i.description) <= 35 else  i.description[0:32]+"..."
                abilities = i.abilities if len(i.abilities) <= 20 else  i.abilities[0:17]+"..."

                print("|{:^4}|{:^15}|{:<35}|{:<20}|{:10,}|".format(i.id,title,description,abilities,i.price))
            print(90*"—"+"\n\n")
            key = input("-Enter 'b' to Go Back: ")
            if key == "b":
                k.freelancer_profile(node)

class freeLanser:
    def __init__(self,id,firstname,lastname,abilities,bio,username,password):
        self.id = id
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.abilities = abilities
        self.bio = bio
        self.next = None

class project:
    def __init__(self,id,owner_id,title,description,abilities,price):
        self.id = id
        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.abilities = abilities
        self.price = price
        self.next = None

class employer:
    def __init__(self,id,firstname,lastname,username,password):
        self.id = id
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.next = None

class freeLancers:
    def __init__(self):
        self.head = None
    
    def add_end(self,id,firstname,lastname,abilities,bio,username,password):
        if self.head == None:
            self.head = freeLanser(id,firstname,lastname,abilities,bio,username,password)
            return self.head
        else:
            node = self.head
            while node.next != None:
                node = node.next
            node.next = freeLanser(id,firstname,lastname,abilities,bio,username,password)
        return node.next
    
    def login(self,username,password):
        node = self.head
        while node != None:
            if node.username == username and node.password == password:
                return node
            node = node.next
        return False
    
    def edit(self,node,firstname,lastname,abilities,bio,username,password):
        node.firstname = node.firstname if len(firstname) == 0 else firstname
        node.lastname = node.lastname if len(lastname) == 0 else lastname
        node.abilities = node.abilities if len(abilities) == 0 else abilities
        node.bio = node.bio if len(bio) == 0 else bio
        node.username = node.username if len(username) == 0 else username
        node.password = node.password if len(password) == 0 else password
        
        connect = sqlite3.connect(db_name)
        c = connect.cursor()
        c.execute("UPDATE `freelancer` SET firstname='{}',lastname='{}',abilities='{}',bio='{}',username='{}',password='{}' WHERE id = {}".format(node.firstname,node.lastname,node.abilities,node.bio,node.username,node.password,node.id))
        connect.commit()
        connect.close()

    def delete(self,id):
        connect = sqlite3.connect(db_name)
        c = connect.cursor()
        c.execute("DELETE FROM `freelancer` WHERE id={}".format(id))
        connect.commit()
        connect.close()

        if self.head.id == id:
            temp = self.head.next
            del(self.head)
            self.head = temp
            return ""
        
        q = self.head
        node = self.head.next
        while True:
            if node.id == id:
                q.next = node.next
                del(node)
                break
            q = node
            node= node.next

class projects:
    def __init__(self):
        self.head = None
    
    def add_end(self,id,owner_id,title,description,abilities,price):
        if self.head == None:
            self.head = project(id,owner_id,title,description,abilities,price)
        else:
            node = self.head
            while node.next != None:
                node = node.next
            node.next = project(id,owner_id,title,description,abilities,price)
    
    def my_project(self,owner_id):
        projects = []
        node = self.head
        while node != None:
            if owner_id == node.owner_id:
                projects.append(node)
            node = node.next
        return projects
    
    def employer_search(self,id,owner_id):
        try:
            id = int(id)
        except:
            return False
        
        node = self.head
        while True:
            if id == node.id and owner_id == node.owner_id:
                return node
            if node.next == None:
                break
            node = node.next
        return False

    def freelancer_search(self,abilities):
        project = []
        node = self.head
        while node != None:
            for i in node.abilities.split(","):
                if i in abilities:
                    project.append(node)
                    break
            node = node.next
        return project
    
    def edit(self,id,title,description,abilities,price):
        node = self.head
        while node.next != None:
            if id == node.id:
                break
            node = node.next
        node.title = node.title if len(title) == 0 else title
        node.description = node.description if len(description) == 0 else description
        node.abilities = node.abilities if len(abilities) == 0 else abilities
        node.price = node.price if len(price) == 0 else int(price)

        connect = sqlite3.connect(db_name)
        c = connect.cursor()
        c.execute("UPDATE `project` SET title='{}',description='{}',abilities='{}',price={} WHERE id = {}".format(node.title,node.description,node.abilities,node.price,node.id))
        connect.commit()
        connect.close()

    def delete(self,id,owner_id):
        connect = sqlite3.connect(db_name)
        c = connect.cursor()
        c.execute("DELETE FROM `project` WHERE id={}".format(id))
        connect.commit()
        connect.close()

        if self.head != None:
            if self.head.id == id or self.head.owner_id == owner_id:
                temp = self.head.next
                del(self.head)
                self.head = temp
                return ""
            
            q = self.head
            node = self.head.next
            while node != None:
                if node.id == id or node.owner_id == owner_id:
                    q.next = node.next
                    del(node)
                    node = q
                q = node
                node= node.next

class employers:
    def __init__(self):
        self.head = None
    
    def add_end(self,id,firstname,lastname,username,password):
        if self.head == None:
            self.head = employer(id,firstname,lastname,username,password)
            return self.head
        else:
            node = self.head
            while node.next != None:
                node = node.next
            node.next = employer(id,firstname,lastname,username,password)
        return node.next
    
    def login(self,username,password):
        node = self.head
        while node != None:
            if node.username == username and node.password == password:
                return node
            node = node.next
        return False
    
    def edit(self,node,firstname,lastname,username,password):
        node.firstname = node.firstname if len(firstname) == 0 else firstname
        node.lastname = node.lastname if len(lastname) == 0 else lastname
        node.username = node.username if len(username) == 0 else username
        node.password = node.password if len(password) == 0 else password
        
        connect = sqlite3.connect(db_name)
        c = connect.cursor()
        c.execute("UPDATE `employer` SET firstname='{}',lastname='{}',username='{}',password='{}' WHERE id = {}".format(node.firstname,node.lastname,node.username,node.password,node.id))
        connect.commit()
        connect.close()
    
    def delete(self,id):
        connect = sqlite3.connect(db_name)
        c = connect.cursor()
        c.execute("DELETE FROM `employer` WHERE id={}".format(id))
        c.execute("DELETE FROM `project` WHERE owner_id={}".format(id))
        connect.commit()
        connect.close()

        project_list.delete(0,id)

        if self.head.id == id:
            temp = self.head.next
            del(self.head)
            self.head = temp
            return ""
        
        q = self.head
        node = self.head.next
        while True:
            if node.id == id:
                q.next = node.next
                del(node)
                break
            q = node
            node= node.next

k = menu()
k.start()
#—