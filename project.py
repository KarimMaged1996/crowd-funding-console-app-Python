import datetime
import ast
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
              print(f"title: {proj.title}\nDetails: {proj.details}\nStart date: {proj.start}\nEnd date: {proj.end}\n")

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
            projects.write(f"{{'title':'{proj.title}','details':'{proj.details}','target':{proj.target},'start':'{proj.start}','end':'{proj.end}'}}\n")
        projects.close()
    @classmethod
    def load(cls):
        projects = open ('./projects.txt','r')
        for project in projects:
            dict_project = ast.literal_eval(project)
            start = dict_project['start'].split('-')
            end = dict_project['end'].split('-')
            cls(dict_project['title'],dict_project['details'],int(dict_project['target']),datetime.date(int(start[0]),int(start[1]),int(start[2])),datetime.date(int(end[0]),int(end[1]),int(end[2])))
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



