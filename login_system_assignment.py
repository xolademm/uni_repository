"""
Create a login system that uses files to check if
a username and password match.
We must also create a user if they have not yet
been created. There should be a limit of 5 attempts.
Store usernames in one file, and passwords in another
"""

#creating files
f1 = open("C:\\Users\\user\\Documents\\temp_file_xola1.txt","r+")
f2 = open("C:\\Users\\user\\Documents\\temp_file_xola2.txt", "r+")

#allowing files to be read
c1 = f1.read()
c2 = f2.read()

#function for new users to sign up
def SignUp():
    new_user = input("Enter your new user name: ")
    new_password = input("Enter your new password: ")
    with open("C:\\Users\\user\\Documents\\temp_file_xola1.txt", "a") as f:
        f.write(new_user + "\n")
    with open("C:\\Users\\user\\Documents\\temp_file_xola2.txt", "a") as f:
        f.write(new_password + "\n")
    print("account created")
    return

 
#function for existing users to log in
def loginSystem():
   #number of login attempts
 max_attempts = 5
 attempts = 0

   
 while attempts < max_attempts:
    print("Welcome to the login system")
    print("Enter your username and password when prompted")
    print("What is your Username?")
    user = input()
    print("What is your password?")
    password = input()
    if c1.find(user) != -1 and c2.find(password) != -1:
     print("Successful Login")
     return
    elif c1.find(user) != -1 and c2.find(password) == -1:
     print("password incorrect, try logging in again")
     attempts += 1
     if attempts < max_attempts:
        print(f"You have {max_attempts - attempts} attempts left.")
        
     else:
            print("Maximum attempts reached. acces denied")
            return 

    elif c1.find(user) == -1:
      print("account not found")
      account = int(input("do you want to create a new account, input 1 for yes or 0 for no: "))
      if account == 0:
        print("ok")
        return

      elif account == 1:
        SignUp()
        return
      else:
        print("invalid") 
        return
 
loginSystem()