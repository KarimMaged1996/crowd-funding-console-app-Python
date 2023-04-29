import datetime
class Project:
    all_projects=[]
    target_accomplished = False
    def __init__(self,title,details,target,start,end):
        self.title=title
        self.details=details
        self.target=target
        self.start=start
        self.end=end
        
        self.all_projects.append(self)
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
            else:
                self.target = 0
                self.target_accomplished = True
        elif self.target == 0:
            print('the project already accomplished its target. Thank you for your support')
        elif self.end < today:
            print(f"{self.title} already closed, the end date was {self.end}") 

    
    


    def __str__(self):
        return f"{self.__dict__}"

proj1 = Project('proj1', 'new proj', 100000, datetime.date.today(),datetime.date(2023,10,15))
proj2 = Project('proj2', 'new proj2', 500000, datetime.date(2023,7,6),datetime.date(2023,12,1))
proj3 = Project('proj3', 'new proj3', 250000, datetime.date(2024,5,5),datetime.date(2024,8,10))

Project.display_all_projects()