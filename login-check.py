#program ktory sprawdza login i haslo prawidlowe

login_registration=("mangotango")
pass_registration=("qwerty1")

login_input=input("Enter login: ")
pass_input=input("Enter password: ")

if login_input == login_registration and pass_input == pass_registration:
    print("You've been logged in")

if login_input != login_registration:
    print("Login incorrect")
    
if pass_input != pass_registratio:
    print("Password incorrect")
