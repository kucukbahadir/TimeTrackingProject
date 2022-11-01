from utils import load_json,generate_usr_lst,update_json
import json

class User: 
    def __init__(self, name, email) :
        self.name=name
        self.email=email

    def add_user(self,lst):      
        lst.append({'user': [{'user_name': self.name, 'user_email': self.email}]})
    
    def unique_user(self,lst):
        b = True
        for i in lst:
            for key in i:
                if key == "user_name":
                    if i[key]==self.name:
                        #print(self.name)
                        b= False
        return b

    def unique_email(self,lst):
        b= True
        #print(f"full list in function{lst}")
        for i in lst:
            for key in i:
                #print(i[key])
                if key == "user_email":
                    #print(f"i am in key {i[key]}")
                    if i[key]==self.email:
                        b= False
        return b    


lst=[]
usr_lst = []
lst = load_json(lst)
#print (lst)

usr_lst = generate_usr_lst(lst)
#print(usr_lst)

user1 = User("Shatha","shatha@yahoo.com")
#if user1.unique_user(usr_lst):
if user1.unique_email(usr_lst):  
        user1.add_user(lst)

user2 = User("farah","farah@yahoo.com")
#if user2.unique_user(usr_lst):
if user2.unique_email(usr_lst): 
        user2.add_user(lst)

usr_lst = generate_usr_lst(lst)
#print(f"this should be full list {usr_lst}")
user3 = User("Al","fara@yahoo.com")
#if user3.unique_user(usr_lst):  
if user3.unique_email(usr_lst):
        user3.add_user(lst)

usr_lst = generate_usr_lst(lst)
#print(lst)
update_json(lst)
#for i in usr_lst:
 #   for key in i:
  #      print(i[key])