import user, project, re, ast, datetime

def modify_proj(project,logged_user):
    while True:
        print('1-Change project title')
        print('2-Change project details')
        print('3-change project target')
        print('4-change start date')
        print('5-change end date')
        print ('6-Delete a Project')
        print('7-Exit')
        choice = input()
        #01 change title
        if choice == '1':
            while True:
                title = input ('please enter the new title\n')
                if title != '':
                    break
            if project.modify_title(logged_user,title) == False:
                print('This Project is not yours to modify\n')
            else:
                project.modify_title(logged_user,title)
                break
        #02 change details
        elif choice == '2':
            while True:
                details = input ('please enter the new details\n')
                if details != '':
                    break
            if project.modify_details(logged_user,details) == False:
                 print('This Project is not yours to modify\n')
            else:
                project.modify_details(logged_user,details)
                break
        #03 change target
        elif choice == '3':
            while True:
                target = input ('please enter the new target\n')
                if re.fullmatch('[0-9]+',target):
                    break
            if project.modify_target(logged_user,target) == False:
                print('This Project is not yours to modify')
            else:
                project.modify_target(logged_user,target)
                break
        #04 change start date
        elif choice == '4':
            while True:
                start = input ('please enter the new date eg: 2023,5,6\n')
                if start != '':
                    break
            start_arr = start.split(',')
            start_date = datetime.date(int(start_arr[0]),int(start_arr[1]),int(start_arr[2])) 
            if project.modify_start(logged_user,start_date) == False:
                print('This Project is not yours to modify')
            else:
                project.modify_start(logged_user,start_date)
                break
        #05 change end date
        elif choice == '5':
            while True:
                end = input ('please enter the new date eg: 2023,5,6\n')
                if end != '':
                    break
            end_arr = end.split(',')
            end_date = datetime.date(int(end_arr[0]),int(end_arr[1]),int(end_arr[2])) 
            if project.modify_end(logged_user,end_date) == False:
                print('This Project is not yours to modify')
            else:
                project.modify_end(logged_user,end_date)
                break
        #06 delete project
        elif choice == '6':
           if project.del_project(logged_user,project.title) == False:
               print('This Project is not yours to modify')
           else:
               project.del_project(logged_user,project.title)
               break
        #07 exit
        elif choice == '7':
            break

        else:
            print ('This input is invalid please choose from the menu')



def logged(logged_user):
    project.Project.load()
    # print(project.Project.all_projects)
    while True:
        print(f"Welcome to your profile {logged_user.first_name} {logged_user.last_name}")
        print('here is the main menu')
        print('1-Create a Project')
        print('2-view your projects')
        print('3-Modify Your project(s)')
        print('4-See All avaialable Projects')
        print('5-Donate to a project')
        print('6-Log Out')
        choice = input()
        # create a project
        if choice == '1':
            # get title
            while True:
              title = input('enter the title of the project\n')
              if title != "":
                  break
            # get details
            while True:
              details = input('type the details about the project\n')
              if details != "":
                  break
            # get target
            while True:
              target = input('type the target of the project,it must be numbers\n')
              if re.fullmatch('[0-9]+',target):
                  break
            # get start date
            while True:
              start = input('type the date using this format yy,mm,dd and exclude leading zero eg: 2023,5,25\n')
              if start != "":
                  break
              
            # get end date
            while True:
              end = input('type the date using this format yy,mm,dd and exclude leading zero eg: 2023,5,25\n')
              if end != "":
                  break
            start_arr = start.split(',')
            end_arr = end.split(',')
            project.Project(title,details,int(target),datetime.date(int(start_arr[0]),int(start_arr[1]),int(start_arr[2])),datetime.date(int(end_arr[0]),int(end_arr[1]),int(end_arr[2])),logged_user)
            project.Project.save()
         

        # View your projects
        elif choice == '2':
            project.Project.all_projects = []
            project.Project.load()
            project.Project.display_user_projects(logged_user)
        # modify your projects
        elif choice == '3':
            proj = input ('please type the name of the project you want to modify\n')
            for one in project.Project.all_projects:
                if one.title == proj:
                    current_proj = one
                    modify_proj(current_proj,logged_user)
                    project.Project.save()
                    print(f"{proj} was modified successfully\n")
                    break
                
            else:
                print("this project doesn't exist")
        # see all available projects
        elif choice == '4':
            project.Project.all_projects = []
            project.Project.load()
            project.Project.display_all_projects()
        # Donate to a project
        elif choice == '5':
            proj = input ('please type the name of the project you want to donate to\n')
            for one in project.Project.all_projects:
                if one.title == proj:
                    current_proj = one
                    while True:
                      donation = input ('how much do you want to donate\n')
                      if re.fullmatch('[0-9]+',donation):
                          break
                    current_proj.donate(int(donation))
                    project.Project.save()
                    print(f"you donated to {proj} successfully\n")
                    break
                
            else:
                print("this project doesn't exist")
        # Log out
        elif choice == '6':
          break
        else:
             print ('the input you provided is invalid. please choose from the menu')
             continue
        

def login():
    while True:
        print('<.................welcome to Crowdspark.................>')
        print ('Do you want to login or create a new account')
        print('1-LogIn')
        print('2-Create a new account')
        print('3-Exit')
        reply = input()
        if reply != '1' and reply != '2' and reply != '3':
            print ('the input you provided is invalid. please choose from the menu')
            continue
        

        # if user wanted to log in
        elif reply == '1':
            current_user = False
            mail = input('Please type in your logIn email\n')
            users = open('./users.txt','r')
            for line in users:
                user_dict = ast.literal_eval(line)
                if user_dict['email'] == mail:
                    current_user = user.User()
                    current_user.set_first_name(user_dict['first_name'])
                    current_user.set_last_name(user_dict['last_name'])
                    current_user.set_email(user_dict['email'])
                    current_user.set_password(user_dict['password'])
                    current_user.set_phone(user_dict['phone'])
                    break
            else:
                print('This Email does not Exist')
            
            if current_user:
                # print(current_user)
                input_password = input (f"welcome {current_user.first_name} Please enter your password\n")
        
                if input_password == current_user.password:
                    print ('you logged in successfully\n')
                    logged(current_user)
                else:
                    input_password = input ('The password you entered is not correct. press Enter to continue\n')  


        # if user chose to create an account
        elif reply == '2':
            u = user.User()
            # loop for the first name
            while True:
                fname = input('Please Enter your first name. it can only be English characters, no numbers or special characters allowed:\n')
                u.set_first_name(fname)
                if u.set_first_name(fname) != False:
                    break
            # loop for the last name
            while True:
                lname = input('Please Enter your last name. it can only be English characters, no numbers or special characters allowed:\n')
                u.set_last_name(lname)
                if u.set_last_name(lname) != False:
                    break
            
            # loop for the email name
            while True:
                email = input('Please Enter your E-mail:\n')
                u.set_email(email)
                if u.set_email(email) != False:
                    break
                
            # loop for the phone number
            while True:
                phone = input('Please Enter your Phone Number:\n')
                u.set_phone(phone)
                if u.set_phone(phone) != False:
                    break
            # loop for the password
            while True:
                password = input('Please enter a password. it must be at least 8 characters\n')
                if u.set_password(password) == False:
                    print('Invalid password\n')
                else:
                    password2= input ('please retype your password\n')
                    if password2 != password:
                        print ("passwords don't match\n")
                        continue
                    elif password2 == password:
                        u.set_password(password)
                        break
            u.add_instance()
            print(user.User.instances)
            u.save()
            print ('your account was created successfully. Now you have to login\n') 
        elif reply == '3':
            break        
            

login()


