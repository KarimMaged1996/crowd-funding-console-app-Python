import user, project, re, ast, datetime

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
            pass
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


