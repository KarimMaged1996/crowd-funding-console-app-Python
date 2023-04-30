import datetime
import ast
import user
class Project:
    all_projects=[]
    total_donations = 0
    target_accomplished = False
    def __init__(self,title,details,target,start,end,owner):
        self.title=title
        self.details=details
        self.target=target
        self.start=start
        self.end=end
        self.owner=owner
        
        self.all_projects.append(self)

    def modify_title(self,user,new_title):
        if user == self.owner:
            self.title = new_title
        else:
            return False
    def modify_details(self,user,new_details):
        if user == self.owner:
            self.details = new_details
        else:
            return False
    def modify_target(self,user,new_target):
        if user == self.owner:
            self.target = new_target
        else:
            return False
        
    def modify_start(self,user,new_start):
        if user == self.owner:
            self.start = new_start
        else:
            return False
    def modify_end(self,user,new_end):
        if user == self.owner:
            self.end = new_end
        else:
            return False
        
    @classmethod
    def display_all_projects(cls):
        for proj in cls.all_projects:
            if proj.target_accomplished == False:
              print('-----------------------------------\n')
              print(f"title: {proj.title}\nDetails: {proj.details}\nStart date: {proj.start}\nEnd date: {proj.end}\nTotal Donations: {proj.total_donations}")
              print('-----------------------------------\n')

    @classmethod
    def display_user_projects(cls,user):
        for proj in cls.all_projects:
            if proj.owner == user:
              print('-----------------------------------\n')
              print(f"title: {proj.title}\nDetails: {proj.details}\nStart date: {proj.start}\nEnd date: {proj.end}\nTotal Donations: {proj.total_donations}")
              print('-----------------------------------\n')

    def donate(self,donation):
        today = datetime.date.today()
        if self.target != 0 and self.end > today:
            if donation < self.target:
                self.target -= donation
                self.total_donations += donation
            else:
                self.target = 0
                self.target_accomplished = True
                self.total_donations += donation
        elif self.target == 0:
            print('the project already accomplished its target. Thank you for your support')
        elif self.end < today:
            print(f"{self.title} already closed, the end date was {self.end}") 
    @classmethod
    def save(cls):
        projects = open('./projects.txt','w')
        for proj in cls.all_projects:
            projects.write(f"{{'title':'{proj.title}','details':'{proj.details}','target':{proj.target},'start':'{proj.start}','end':'{proj.end}','owner':{proj.owner}}}\n")
        projects.close()
    @classmethod
    def load(cls):
        projects = open ('./projects.txt','r')
        for project in projects:
            dict_project = ast.literal_eval(project)
            start = dict_project['start'].split('-')
            end = dict_project['end'].split('-')
            cls(dict_project['title'],dict_project['details'],int(dict_project['target']),datetime.date(int(start[0]),int(start[1]),int(start[2])),datetime.date(int(end[0]),int(end[1]),int(end[2])),dict_project['owner'])
        projects.close()

    
    def __str__(self):
        return f"{self.__dict__}"

# proj1 = Project('proj1', 'new proj', 100000, datetime.date.today(),datetime.date(2023,10,15))
# proj2 = Project('proj2', 'new proj2', 500000, datetime.date(2023,7,6),datetime.date(2023,12,1))
# proj3 = Project('proj3', 'new proj3', 250000, datetime.date(2024,5,5),datetime.date(2024,8,10))
# proj3.donate(5000)

# Project.save()
# Project.load()
# print(Project.all_projects)



# user1 = user.User()
# # print(user1)
# # print(User.instances)
# user1.set_first_name('karim')
# user1.set_last_name('maged')
# user1.set_email('karim.maged2020@yahoo.com')
# user1.set_password('karim123456')
# user1.set_phone('01119030428')
# user1.add_instance()

# user2 = user.User()
# user2.set_first_name('sarah')
# user2.set_last_name('maged')
# user2.set_email('sarah.maged2020@yahoo.com')
# user2.set_password('sarah123456')
# user2.set_phone('01119030419')
# user2.add_instance()
# user2.set_first_name('salma')

# proj1 = Project('proj1', 'new proj', 100000, datetime.date.today(),datetime.date(2023,10,15),user1)
# proj2 = Project('proj2', 'new proj2', 500000, datetime.date(2023,7,6),datetime.date(2023,12,1),user1)
# proj3 = Project('proj3', 'new proj3', 250000, datetime.date(2024,5,5),datetime.date(2024,8,10),user2)
# proj3.donate(5000)
# Project.save()
# Project.load()
# Project.display_all_projects()

# test ="{'title':'proj1','details':'new proj','target':100000,'start':'2023-04-30','end':'2023-10-15','owner':{'first_name':'karim','last_name':'maged','email':'karim.maged2020@yahoo.com','password':'karim123456','phone':'01119030428'}}"
# test2 = ast.literal_eval(test)
# print(type(test2))
