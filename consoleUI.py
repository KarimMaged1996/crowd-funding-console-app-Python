import user, project, re, ast

def login():
    while True:
        print('<.................welcome to Crowdspark.................>')
        print ('Do you want to login or create a new account')
        print('1-LogIn')
        print('2-Create a new account')
        reply = input()
        if reply != '1' and reply != '2':
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
                    current_user = user_dict
            else:
                print('This Email does not Exist')
            
            if current_user:
                input_password = input (f"welcome {current_user['first_name']} Please enter your password\n")
                for i in range(2):
                    if input_password == current_user['password']:
                        print ('you logged in successfully')
                    else:
                      input_password = input ('The password you entered is not correct. please re-enter the password\n')  


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
            

login()

