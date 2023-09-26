import Admin as admin
from User import  Application
user=Application(str,str,str,str,str)
# start code
temp_variable=1
temp=True
Temp_var=True
while Temp_var :
    print("1.ADMIN LOGIN")
    print("2.USER LOGIN")
    print("3.USER REGISTRATION")
    print("4.EXIT")
    inp=int(input("Where You Want to Login??..select your otion: "))
    if temp_variable == 0:
        temp=True
# check input
    if inp == 1:
       print("Login AS  Admin Panel..")
       username=input("Enter a Username ")
       password = input("Enter a Password ")
       if admin.admin_info[username] == password:
         print("you Logged in ********** Successfully  ********************")
         while Temp_var:
            print("1.ADD NEW FOOD ITEM")
            print("2.EDIT FOOD ITEM")
            print("3.VIEW MENU LIST")
            print("4.REMOVE FOO ITEM")
            print("5.EXIT")
            admin_input = int(input("SELECT YOUR OPTION:"))
               
            if admin_input == 1:
                admin.add_food_item()
            elif admin_input == 2:
                admin.edit_food_item()
            elif admin_input == 3:
                admin.show_menu_item()
            elif admin_input == 4:
                admin.removing_food_item()
            elif admin_input == 5:
                print(f"You're Exit to the admin panel   {username}")
                Temp_var = False
            else:
                print("Wrong input Please Read Carefully Instruction  !!!")

       else :
           print("Invalid Credentials !!!!! ")


    elif inp == 2 :
      print("Login As User Panel..")
      email_enter = input("ENTER EMAIL:")
      password = input("ENTER PASSWORD")

      if Application.login(email_enter,password):

        while temp:
            choice_user = int(input(f"{email_enter},SELECT USER OPTIONS 1.PLACE NEW ORDER 2. ORDER HISTORY 3.UPDATE PROFILE 4.EXIT"))
            if choice_user == 1:
                user. place_new_order()

            elif choice_user == 2:
                user.order_history_see()

            elif choice_user ==3:
                user.update_profile()
                temp=False
                temp_variable=0

            elif choice_user == 4:
                print("You're Successfully looged out")
                temp = False
                temp_variable = 0



            else:
                print("Wrong Number Please follow this Instruction  ")

    elif inp == 3:

      new_email = input("Enter new  Email ")
      if new_email in user.login_info.keys():
        print("Email Already Registered.......")
      else :
        print("Enter Your Detail Here <<<<<-")
        new_name = input("Enter new  Name ")
        new_phone_no = int(input("Enter new  Phone No "))
        new_Address = input("Enter new  Address ")
        new_password = input("Enter new  Password ")
        user=Application(new_email,new_name,new_phone_no,new_Address,new_password)

        print("Your have Registered Successfully.......")
        print("Now you can Login... ")


    elif inp == 4:
        Temp_var=False
        exit()

    else :
      print("Follow option's ")
