import re

class User:
    instances = []
    def __init__(self,first_name=None,last_name=None,email=None,password=None,phone=None):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.phone=phone
        # self.logged=False

    def set_first_name(self,fName):
        if re.fullmatch("[a-zA-z]+",fName):
            self.first_name = fName
        else:
            return False
        
    def set_last_name(self,lName):
        if re.fullmatch("[a-zA-z]+",lName):
            self.last_name = lName
        else:
            return False

    def set_email(self,mail):
        if re.fullmatch("[a-zA-z0-9+-_.]+@[a-zA-z0-9]+\.com",mail):
            self.email = mail
        else:
            return False
    
    def set_password(self,passcode):
        if re.fullmatch(".{8,}",passcode):
            self.password = passcode
        else:
            return False
        
    def set_phone(self,num):
        if re.fullmatch("^[0][1][1][1|2|0][0-9]{7}",num):
            self.phone = num
        else:
            return False
    
    def add_instance(self):
        if (self.first_name and self.last_name and self.email and self.password and self.phone):
            self.instances.append(self.__dict__)

    # def log_in(self,mail,password):
    #     if mail == self.email and password == self.password:
    #         self.logged = True

    # def log_out(self):
    #     self.logged = False
    
    # to be able to print the user as dictionary for debugging
    def __str__(self):
        return f"{{'first_name':'{self.first_name}','last_name':'{self.last_name}','email':'{self.email}','password':'{self.password}','phone':'{self.phone}'}}"
    
    @classmethod
    def save(cls):
        users_file = open('./users.txt','a')
        for user in cls.instances:
            users_file.write(f"{user}\n")
        users_file.close()

        
  
# user1 = User()
# # print(user1)
# # print(User.instances)
# user1.set_first_name('karim')
# user1.set_last_name('maged')
# user1.set_email('karim.maged2020@yahoo.com')
# user1.set_password('karim123456')
# user1.set_phone('01119030428')
# user1.add_instance()

# user2 = User()
# user2.set_first_name('sarah')
# user2.set_last_name('maged')
# user2.set_email('sarah.maged2020@yahoo.com')
# user2.set_password('sarah123456')
# user2.set_phone('01119030419')
# user2.add_instance()
# user2.set_first_name('salma')

# User.save()

# test = open('./users.txt','r')
# for line in test:
#     print(type(line))

# test2 = '{"name": "karim", "age": 27}'
# test3 = dict(test2)
# print(type(test3))


