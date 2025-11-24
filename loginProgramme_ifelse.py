#login program and identation

#Taking Email and password from user

Email = str(input(" Enter Your Email :"))
Password = str(input('Enter Your Password :'))

#correct Email
correct_email = "ariyanhridoy921@gmail.com"
correct_pass = '123456789'

#checking email with if else
if Email == correct_email and Password == correct_pass:
    print("Login Successfull")
elif Email == correct_email and Password != correct_pass :
    #tell The user
    print("Wrong Pasword")
    print("Enter Your Password again :")
    Password= str(input())
    if Password == correct_pass:
        print('Login Succesfull')
    else :
        print("Forget Password! Try To Reset Password....")     
else :
    print("INVALID")