username = "addmin"
password = "12345678"
user_input = str(input("Enter your Username : "))
pass_input = complex(input("Enter your Username : "))
print(type(pass_input))

if username == "addmin" and pass_input == complex("12345678"):
    print("login Success !!!")
else:
    print("Invalid Username or Password")