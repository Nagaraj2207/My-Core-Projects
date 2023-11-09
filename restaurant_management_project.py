#Here we import online_food_ordering_system_validation for validation.
import online_food_ordering_system_validation as my_validation

# Here we import datetime,re,tabulate and random modules.

import datetime
import re
import tabulate
import random
import time

# Here we create Usder Class.

class User:

    # Here we Create Constructor for User class.
    
    def __init__(self):
        self.online_system_name = "friends"
        self.user_name = ""
        self.user_email_id = ""
        self.user_address = ""
        self.__user_password = ""
        self.user_phone_number = ""
        self.user_information = {'9095493828':
                                 {'1.Name': 'NAGARAJ', '3.Address': 'NO.12 Street:MiddleStreet Near:kovil Pincode:625106 City:Madurai State:Tamil Nadu', '2.Email id': 'dnagaraj3828@gmail.com',
                                  'User Id': 'dnagaraj3828', 'Password': 'Dnagaraj@2207', '4.Phone Number': '9095493828'},
                                  '9095493820': {'1.Name': 'JOTHI', '3.Address': 'NO.13 Street:southstreet Near:Kovil Pincode:123467 City:Sivaganga State:Tamil Nadu', '2.Email id': 'jothiarul1212@gmail.com',
                                                 'User Id': 'jothiarul1212', 'Password': 'Jothiarul@1212', '4.Phone Number': '9095493820'}
                                 }
        self.overall_payment_details = {'9095493828':
                                           {'1.Card Details': {'Card Name': 'Nagaraj', 'Card Number': '1234-1234-1234-1234', 'Expire Date': '12/2030', 'CVV': '123'},
                                            '2.Internet Banking Details': {'User Net ID': 'naga2207', 'Net Password': 'Dnagaraj@2207'},
                                            '3.Mobile UBI': {'UBI ID': 'dnagaraj3828@ybl', 'UBI Mobile Number': '9095493828', 'UBI PIN': '1234'}},
                                        '9095493820':
                                           {'1.Card Details': {'Card Name': 'Jothi', 'Card Number': '1234-1234-1234-1234', 'Expire Date': '12/2030', 'CVV': '123'},
                                            '2.Internet Banking Details': {'User Net ID': 'jothi2207', 'Net Password': 'Jothiarul@1212'},
                                            '3.Mobile UBI': {'UBI ID': 'jothiarul1212@ybl', 'UBI Mobile Number': '9095493820', 'UBI PIN': '1234'}}
                                        }
        self.user_password_dict = {}

    # Here we create address_details() function for get the address details.

    def address_details(self):
        address = 1
        print("\n"+("="*35))
        print("\n*** Enter The Adderess Details Below ***")
        print("\n"+("="*35))
        while address:
            try:
                str_num = 1
                while str_num:
                    try:
                        street_num = input("\nEnter the Door Number:")
                        street_num = street_num.replace(" ","")
                        my_validation.street_number_validation(street_num)
                        str_num = 0
                    except Exception as er:
                        print(er)
                str_name = 1
                while str_name:
                    try:
                        street_name = input("\nEnter the Street Name (or) Village Name:")
                        street_name = street_name.replace(" ","")
                        my_validation.street_name_validation(street_name)
                        str_name = 0
                    except Exception as er:
                        print(er)
                land = 1
                while land:
                    try:
                        land_mark = input("\nEnter the Nearby Landmark:")
                        land_mark = land_mark.replace(" ","")
                        my_validation.landmark_validation(land_mark)
                        land = 0
                    except Exception as er:
                        print(er)
                code = 1
                while code:
                    try:
                        pin_code = input("\nEnter your Pincode:")
                        pin_code = pin_code.replace(" ","")
                        my_validation.pinncode_validation(pin_code)
                        code = 0
                    except Exception as er:
                        print(er)
                city = 1
                while city:
                    try:
                        user_city = input("\nEnter your City:")
                        user_city = user_city.replace(" ","")
                        my_validation.city_validation(user_city)
                        city = 0
                    except Exception as er:
                        print(er)
                self.user_address = "NO."+street_num+" "+"Street:"+street_name+" "+"Near:"+land_mark+" "+"Pincode:"+pin_code+" "+"City:"+user_city+" "+"State:"+"Tamil Nadu"
                address = 0
            except Exception as er:
                print(er)

    # Here we create user_input() get the User's input.

    def user_input(self):
        print("\n"+("="*35))
        print("\n*** Enter Your Details Below ***")
        print("\n"+("="*35))
        name = 1
        while name:
            try:
                self.user_name = input("\nEnter the Name:").upper()
                self.user_name = self.user_name.replace(" ","")
                my_validation.user_name_validation(self.user_name)
                self.user_details["1.Name"] = self.user_name
                name = 0
            except Exception as er:
                print(er)
                
        self.address_details()
        self.user_details["3.Address"] = self.user_address

        email = 1
        while email:
            try:
                self.user_email_id = input("\nEnter the Email:")
                self.user_email_id = self.user_email_id.replace(" ","")
                my_validation.user_email_id_validation(self.user_email_id)
                if self.user_information != {}:
                    for x,my_dict in self.user_information.items():
                        if my_dict["2.Email id"] == self.user_email_id:
                            check_value = 0
                            break
                        else:
                            check_value = 1

                    if check_value > 0:
                        self.user_details["2.Email id"] = self.user_email_id
                        email = 0
                    else:
                        print("\nYou already entered this Email id.")
                        email = 1

                else:
                    self.user_details["2.Email id"] = self.user_email_id
                    email = 0
            except Exception as er:
                print(er)
        self.user_id = self.user_email_id.split("@")[0]
        print("\n"+("*"*35))
        print("\n*** Your User Id is:{} ***".format(self.user_id))
        print("\n"+("*"*35))
        self.user_details["User Id"] = self.user_id
        
        password = 1
        while password:
            try:
                self.__user_password = input("\nEnter your password:")
                self.__user_password = self.__user_password.replace(" ","")
                my_validation.user_password_validation(self.__user_password)
                conf_password = input("\nRe-enter and confirm your password:")
                conf_password = conf_password.replace(" ","")
                if conf_password != self.__user_password:
                    raise Exception ("\nPassword and confirm Password are not same!!!")
                else:
                    self.user_details["Password"] = self.__user_password
                    password = 0
            except Exception as er:
                print(er)

        ph_num = 1
        while ph_num:
            try:
                self.user_phone_number = input("\nEnter your Phone Number:")
                self.user_phone_number = self.user_phone_number.replace(" ","")
                my_validation.user_phone_number_validation(self.user_phone_number)
                if self.user_information != {}:
                    for x,my_dict in self.user_information.items():
                        if my_dict["4.Phone Number"] == self.user_phone_number:
                            check_value = 0
                            break
                        else:
                            check_value = 1

                    if check_value > 0:
                        self.user_details["4.Phone Number"] = self.user_phone_number
                        self.user_information[self.user_phone_number] = self.user_details
                        ph_num = 0
                        self.payment_details()
                        if self.total_user_payment_details != {}:
                            self.overall_payment_details[self.user_phone_number] = self.total_user_payment_details
                            print(self.overall_payment_details)
                            self.total_user_payment_details = {}
                    else:
                        print("\nYou already entered this phone number.")
                        ph_num = 1

                else:
                    self.user_details["4.Phone Number"] = self.user_phone_number
                    self.user_information[self.user_phone_number] = self.user_details
                    ph_num = 0
                    self.payment_details()
                    if self.total_user_payment_details != {}:
                        self.overall_payment_details[self.user_phone_number] = self.total_user_payment_details
                        self.total_user_payment_details = {}
            except Exception as er:
                print(er)

    # Here we create add_Card() function for Add card details.
                
    def add_Card(self):
        print("\n"+("="*35))
        print("\n*** Enter Your Card Details Below ***")
        print("\n"+("="*35))
        card_name = 1
        while card_name:
            try:
                user_card_name = input("\nEnter Cardholder's Name:")
                user_card_name = user_card_name.replace(" ","")
                my_validation.user_name_validation(user_card_name)
                self.user_payment_details["Card Name"] = user_card_name
                card_name = 0
            except Exception as er:
                print(er)

        card_num = 1
        while card_num:
            try:
                __user_card_num = input("\nEnter the Card Number:")
                __user_card_num = __user_card_num.replace(" ","")
                my_validation.card_number_validation(__user_card_num)
                self.user_payment_details["Card Number"] = __user_card_num
                card_num = 0
            except Exception as er:
                print(er)

        ex_date = 1
        while ex_date:
            try:
                __expire_date = input("\nEnter the Expiration Date:")
                __expire_date = __expire_date.replace(" ","")
                my_validation.card_expire_date_validation(__expire_date)
                current_date = datetime.date.today()
                expiration_date_pattern = datetime.datetime.strptime(__expire_date,"%m/%Y")
                expiration_month = expiration_date_pattern.month
                expiration_year = expiration_date_pattern.year
                expiration_start_date = datetime.datetime(expiration_year, expiration_month, 1).date()
                valid_years = range(2023, 2031)
                if expiration_start_date < current_date:
                    raise Exception ("\nCard has expired,please update to current year {}.".format(current_date.year))
                elif expiration_year not in valid_years:
                    raise Exception ("\nInvalid expiration year. Please enter a date between 2023 and 2030.")
                else:
                    self.user_payment_details["Expire Date"] = __expire_date
                    ex_date = 0
            except Exception as er:
                print(er)

        cvv = 1
        while cvv:
            try:
                __user_cvv = input("\nEnter the CVV Number:")
                __user_cvv = __user_cvv.replace(" ","")
                my_validation.cvv_validation(__user_cvv)
                self.user_payment_details["CVV"] = __user_cvv
                print("\n*** Card Added Successfully!!! ***")
                cvv = 0
            except Exception as er:
                print(er)

    # Here we create add_net_banking() function for  Add Net Banking.

    def add_net_banking(self):
        print("\n"+("="*35))
        print("\n*** Enter Your Net Banking Details Below ***")
        print("\n"+("="*35))
        net_id = 1
        while net_id:
            try:
                __user_net_id = input("\nAdd the NetBanking User Id:")
                __user_net_id = __user_net_id.replace(" ","")
                my_validation.net_id_validation(__user_net_id)
                self.user_payment_details["User Net ID"] = __user_net_id
                net_id = 0
            except Exception as er:
                print(er)
                
        net_pass = 1        
        while net_pass:
            try:
                __user_net_password = input("\nEnter the NetBanking Password:")
                __user_net_password = __user_net_password.replace(" ","")
                my_validation.user_password_validation(__user_net_password)
                self.user_payment_details["Net Password"] = __user_net_password
                print("\n*** Net Banking Added Successfully!!! ***")
                net_pass = 0
            except Exception as er:
                print(er)

    # Here we create add_mobile_ubi() function Add Mobile Ubi details.

    def add_mobile_ubi(self):
        print("\n"+("="*35))
        print("\n*** Enter Your Mobile UBI Details Below ***")
        print("\n"+("="*35))
        ubi = 1
        while ubi:
            try:
                __user_ubi_id = input("\nEnter the UBI ID:")
                __user_ubi_id = __user_ubi_id.replace(" ","")
                my_validation.ubi_id_validation(__user_ubi_id)
                self.user_payment_details["UBI ID"] = __user_ubi_id 
                ubi = 0
            except Exception as er:
                print(er)

        ubi_num = 1
        while ubi_num:
            try:
                ubi_mobile_number = input("\nEnter Your UBI Mobile Number:")
                ubi_mobile_number = ubi_mobile_number.replace(" ","")
                my_validation.user_phone_number_validation(ubi_mobile_number)
                self.user_payment_details["UBI Mobile Number"] = ubi_mobile_number
                ubi_num = 0
            except Exception as er:
                print(er)

        pin = 1
        while pin:
            try:
                __ubi_pin = input("\nEnter Your UBI PIN:")
                __ubi_pin = __ubi_pin.replace(" ","")
                my_validation.ubi_pin_validation(__ubi_pin)
                self.user_payment_details["UBI PIN"] = __ubi_pin
                print("\n*** Mobile UBI Added Successfully!!! ***")
                pin = 0
            except Exception as er:
                print(er)

    # Here we create payment_details() for Add the Payment deatils.
                
    def payment_details(self):
        self.user_payment_details = {}
        self.total_user_payment_details = {}
        print("\n"+("<>~"*15))
        print("\n{:>28}***Welcome To Add User's Payment Details Page ***".format(" ",self.online_system_name.upper()))
        print("\n{:<23}".format(" "),("~<>"*43))
        pay_choice1 = 1
        while pay_choice1:
                print("\n{:>28}1.Add Credit/Debit Card".format(" "))
                print("\n{:>28}2.Add Internet Banking".format(" "))
                print("\n{:>28}3.Add Mobile Payments/UBI's".format(" "))
                print("\n{:>28}4.Exit".format(" "))
                pay_choice = input("\nEnter Your choice:")
                if pay_choice == "1":
                    if "1.Card Details" not in self.total_user_payment_details:
                        self.add_Card()
                        self.total_user_payment_details ["1.Card Details"] = self.user_payment_details
                        self.user_payment_details = {}
                    else:
                        print("\nSorry!!!,You Already Add the Card,if you want to update the Card.Please login and update the card in View payment Details Option.")
                elif pay_choice == "2":
                    if "2.Internet Banking Details" not in self.total_user_payment_details:
                        self.add_net_banking()
                        self.total_user_payment_details ["2.Internet Banking Details"] = self.user_payment_details
                        self.user_payment_details = {}
                    else:
                        print("\nSorry!!!,You Already Add the Internet Banking,if you you want to update the Internet Banking.Please login and update the Internet Banking in View payment Details Option.")
                        
                elif pay_choice == "3":
                    if "3.Mobile UBI" not in self.total_user_payment_details:
                        self.add_mobile_ubi()
                        self.total_user_payment_details ["3.Mobile UBI"] = self.user_payment_details
                        self.user_payment_details = {}
                    else:
                        print("\nSorry!!!,You Already Add the Mobile UBI,if you want to update the Mobile UBI.Please login and update the Mobile UBI in View payment Details Option.")
                elif pay_choice == "4":
                    print(self.total_user_payment_details)
                    pay_choice1 = 0
                else:
                    print("\nPlease Enter the correct Given Choice(1-4)!!!")

    # Here we craete user_register() function for user's Registeration.

    def user_register(self):
        self.user_details = {}
        self.temp_name = ""
        print("\n"+("<>~"*15))
        print("\n{:>28}*** Welcome to the User's Register Page ***".format(" ",self.online_system_name.upper()))
        print("\n{:<23}".format(" "),("~<>"*43))
        self.user_input()
        for item in self.user_details:
            if self.user_details[item] == self.user_name:
                self.temp_name = self.user_name
        print("\n"+("o~"*35))
        print("\n{:>23}*** Hai {} ***".format(" ",self.temp_name))
        print("\n{:>9}*** Welcome to {} Online Food Odering System ***".format(" ",self.online_system_name.upper()))
        print("\n"+("o~"*35))

    # Here we create format_user_details() function for format the user details.

    def format_user_details(self,user_dict):
        self.formatted_items3 = {}
        for field,value in user_dict.items():
            if field == "Password":
                formatted_value = re.sub(r"^[A-Z]{1}[a-z]+[0-9\W_]+",r"xxxxxxx",value)
            else:
                formatted_value = value
            self.formatted_items3[field] = formatted_value

    # Here we create view_user_details() function for View user details.

    def view_user_details(self):
        print("\n"+("="*35))
        print("\n*** Enter Your Register Details Below ***")
        print("\n"+("="*35))
        ol_num = 1
        while ol_num:
            try:
                old_num = input("\nEnter the Register Phone Number:")
                old_num = old_num.replace(" ","")
                my_validation.user_phone_number_validation(old_num)
                ol_num = 0
            except Exception as er:
                print(er)
        up_ph_num = ""
        if old_num == self.log_user_name:
            for key,item in self.user_information.items():
                print(key)
                print("AAAAAA")
                if key == old_num:
                    print("\n"+("="*35))
                    print("\n*** User's Details are ***")
                    print("\n"+("="*35))
                    self.format_user_details(self.user_information[key])
                    print(tabulate.tabulate(([x,y]for x,y in self.formatted_items3.items()),headers =["User Details"],tablefmt = 'grid'))
                    up_user = 1
                    while up_user:
                        up_choice = input("\nDo you want to Update your Details(y/n):")
                        if up_choice == "n":
                            up_user = 0
                        elif up_choice == "y":
                            choose = 1
                            while choose:
                                self.format_user_details(self.user_information[key])
                                print(tabulate.tabulate(([x,y]for x,y in self.formatted_items3.items()),headers =["User Details"],tablefmt = 'grid'))
                                print("\n"+("="*35))
                                print("\n*** Enter Your Updated User's Details Below ***")
                                print("\n"+("="*35))
                                up_choose = input("\nEnter the Number to update the User Details (1-4) or press q to quit:")
                                for item,value_dict in self.user_information.items():
                                    if item == old_num:
                                        if up_choose == "1":
                                            upp_name = 1
                                            while upp_name:
                                                try:
                                                    up_name = input("\nEnter the updated Name:").upper()
                                                    up_name = up_name.replace(" ","")
                                                    my_validation.user_name_validation(up_name)
                                                    value_dict["1.Name"] = up_name
                                                    upp_name = 0
                                                except Exception as er:
                                                    print(er)
                                        elif up_choose == "2":
                                            upp_em_name = 1
                                            while upp_em_name:
                                                try:
                                                    up_email_name = input("\nEnter the updated Email:")
                                                    up_email_name = up_email_name.replace(" ","")
                                                    my_validation.user_email_id_validation(up_email_name)
                                                    value_dict["2.Email id"] = up_email_name
                                                    up_email_name = up_email_name.split("@")[0]
                                                    value_dict["User Id"] = up_email_name
                                                    upp_em_name = 0
                                                except Exception as er:
                                                    print(er)
                                        elif up_choose == "3":
                                            self.address_details()
                                            value_dict["3.Address"] = self.user_address
                                        elif up_choose == "4":
                                            upp_ph_num = 1
                                            while upp_ph_num:
                                                try:
                                                    up_ph_num = input("\nEnter the updated Phone Number:")
                                                    up_ph_num = up_ph_num.replace(" ","")
                                                    my_validation.user_phone_number_validation(up_ph_num)
                                                    value_dict["4.Phone Number"] = up_ph_num
                                                    upp_ph_num = 0
                                                except Exception as er:
                                                    print(er)
                                        elif up_choose == "q":
                                            print("\nDetails Updated Successfully!!!")
                                            choose = 0
                                            up_user = 0
                                        else:
                                            print("\nPlease Enter the correct choice!!!")
                            
                        else:
                            print("\nPlease Enter the Correct Choice (y/n)!!!")
        else:
            print("\nThis Number is not Registered in our Portal")
        if up_ph_num != "":
            self.user_information[up_ph_num] = self.user_information.pop(old_num)
            self.log_user_name = up_ph_num

    # Here we create format_payment_details() for format payment details.

    def format_payment_details(self,payment_dict):
        self.formatted_items2 = {}
        for key,item in payment_dict.items():
            formatted_item = {}
            for field,value in item.items():
                if key == "1.Card Details":
                    if field == 'Card Number':
                        formatted_value = re.sub(r"(\d{4})-(\d{4})-(\d{4})-(\d{4})", r"xxx-xxxx-xxxx-\4", value)
                    elif field == 'CVV':
                        formatted_value = re.sub(r"\d{3}",r"xxx",value)
                    else:
                        formatted_value = value
                elif key == "2.Internet Banking Details":
                    if field == 'Net Password':
                        formatted_value = re.sub(r"^[A-Z]{1}[a-z]+[0-9\W_]+",r"xxxxxxx",value)
                    else:
                        formatted_value = value
                elif key == "3.Mobile UBI":
                    if field == 'UBI PIN':
                        formatted_value = re.sub(r"\d{4}",r"xxxx",value)
                    else:
                        formatted_value = value
                formatted_item[field] = formatted_value
            self.formatted_items2[key] = formatted_item

    # Here we create view_user_payment_details() for View user payment details.
            
    def view_user_payment_details(self):
        print("\n"+("="*35))
        print("\n*** The Payment's Details are ***")
        print("\n"+("="*35))
        ol_py_num = 1
        while ol_py_num:
            try:
                old_pay_num = input("\nEnter the Register Phone Number:")
                old_pay_num = old_pay_num.replace(" ","")
                my_validation.user_phone_number_validation(old_pay_num)
                ol_py_num = 0
            except Exception as er:
                print(er)
        if old_pay_num == self.log_user_name:
            for key,item in self.user_information.items():
                if key == old_pay_num:
                    self.format_payment_details(self.overall_payment_details[key])
                    print(tabulate.tabulate(([x,y]for x,y in self.formatted_items2.items()), headers=["Payment Details"], tablefmt='grid'))
                    up_pay = 1
                    while up_pay:
                        up_pay_choice = input("\nDo you want to Update your Details(y/n):")
                        if up_pay_choice == "n":
                            up_pay = 0
                        elif up_pay_choice == "y":
                            pay_choose = 1
                            while pay_choose:
                                print("\n"+("="*35))
                                print("\n*** Enter Your Updated Paymant Details Below ***")
                                print("\n"+("="*35))
                                self.format_payment_details(self.overall_payment_details[key])
                                print(tabulate.tabulate(([x,y]for x,y in self.formatted_items2.items()), headers=["Payment Details"], tablefmt='grid'))
                                up_pay_choose = input("\nEnter the Number to update the Payment Details or press q to quit:")
                                for x,values in self.overall_payment_details.items():
                                    if x == old_pay_num:
                                        if up_pay_choose == "1":
                                            if "1.Card Details" in values:
                                                self.add_Card()
                                                values["1.Card Details"] = self.user_payment_details
                                            else:
                                                print("\nCard Details Not Added.")
                                        elif up_pay_choose == "2":
                                            if "2.Internet Banking Details" in values:
                                                self.add_net_banking()
                                                values["2.Internet Banking Details"] = self.user_payment_details
                                            else:
                                                print("\nInternet Banking Details Not Added.")
                                        elif up_pay_choose == "3":
                                            if "3.Mobile UBI" in values:
                                                self.add_mobile_ubi()
                                                values["3.Mobile UBI"] = self.user_payment_details
                                            else:
                                                print("\nMobile UBI is not Added.")
                                        elif up_pay_choose == "q":
                                            print("\nPayment Details Updated Successfully!!!")
                                            pay_choose = 0
                                            up_pay = 0
                                        else:
                                            print("\nPlease Enter the correct Choice!!!")
                        else:
                            print("\nPlease enter the corect choice (y/n)!!!")
        else:
            print("\nThis Phone Number Not Register in our Portal")

    #  Here we create view_profile() for View Profile Main Menu.
    
    def view_profile(self):  
        view_choice = 1
        while view_choice:
            print("\n"+("<>~"*15))
            print("\n{:>28}*** Welcome to the View and Update User's Profile Page ***".format(" ",self.online_system_name.upper()))
            print("\n{:<23}".format(" "),("~<>"*43))
            print("\n{:>28}1.User Details".format(" "))
            print("\n{:>28}2.User Payment Details".format(" "))
            print("\n{:>28}3.Exit".format(" "))
            user_view_choice = input("\nEnter the Choice:")
            if user_view_choice == "1":
                self.view_user_details()
            elif user_view_choice == "2":
                if self.overall_payment_details != {}:
                    self.view_user_payment_details()
            elif user_view_choice == "3":
                view_choice = 0
            else:
                print("\nPlese enter the correct choice (1-3)!!!")

    # Here we create otp_generator() for otp generation.

    def otp_generator(self):
        random_num = random.randrange(1000,10000)
        self.random_num1 = str(random_num)

    # Here we create change_password() for change the Password.
        
    def change_password(self):
        print("\n"+("<>~"*15))
        print("\n{:>28}*** Welcome to Changing the User's Password Page ***".format(" ",self.online_system_name.upper()))
        print("\n{:<23}".format(" "),("~<>"*43))
        up_ph_num = 1
        while up_ph_num:
            try:
                cur_ph_num = input("\nEnter Your Current User Phone Number:")
                cur_ph_num = cur_ph_num.replace(" ","")
                my_validation.user_phone_number_validation(cur_ph_num)
                if cur_ph_num == self.log_user_name:
                    up_ph_num = 0
                else:
                    print("\nEntered Phone Number is incorrect,Please Enter the correct Register Phone Number!!!")
            except Exception as er:
                print(er)
        cur_pass = 1
        while cur_pass:
            print("\n"+("="*35))
            print("\n*** Enter Your Login Details Below ***")
            print("\n"+("="*35))
            try:
                cur_password = input("\nEnter Your Current User Password:")
                cur_password = cur_password.replace(" ","")
                for item,value_dict in self.user_information.items():
                    if item == cur_ph_num:
                        if value_dict["Password"] == cur_password:
                            cur_pass = 0
                        else:
                            print("\nEntered Password is incorrect,Please Enter the correct Register Password!!!")
            except Exception as er:
                print(er)

        up_pass = 1
        while up_pass:
            try:
                new_password = input("\nEnter Your New User Password:")
                new_password = new_password.replace(" ","")
                my_validation.user_password_validation(new_password)
                up_pass = 0
            except Exception as er:
                print(er)
        otp = 1
        while otp:
             self.otp_generator()
             print("\nYour OTP is {}".format(self.random_num1))
             user_otp = input("\nEnter the OTP which send to your Registered Mobile Number:")
             if user_otp == self.random_num1:
                 for item,value_dict in self.user_information.items():
                     if item == cur_ph_num:
                         value_dict["Password"] = new_password
                         print(self.user_information)
                         print("\nSuccessfully Changed the Password!!!")
                         otp = 0    
             else:
                 print("\nEntered OTP is incorrect,Please Enter the correct OTP!!!")

    # Here we view_profile_change_password() for main Menu.
            
    def view_profile_change_password(self):
        print("\n"+("="*35))
        print("\n*** Enter Your Register Details Below ***")
        print("\n"+("="*35))
        log_name = 1
        while log_name:
            self.log_user_name = input("\nEnter Your Mobile Number:")
            if self.log_user_name in self.user_information:
                log_name = 0
            else:
                print("\nEntered Phone number is wrong,Please Enter the correct Phone Number!!!")

        log_name = 1
        while log_name:
            self.log_user_id = input("\nEnter Your User Id:")
            for item,value_dict in self.user_information.items():
                if item == self.log_user_name:
                    if self.log_user_id == value_dict["User Id"]:
                        check_value = 0
                        break
                    else:
                        check_value = 1
                    
            if check_value == 0:
                log_name = 0
            else:
                print("\nEntered User Id is wrong,Please Enter the correct User Id!!!")

        log_password = 1
        while log_password:
            self.log_user_password = input("\nEnter Your Register User Password:")
            for item,value_dict in self.user_information.items():
                if item == self.log_user_name:
                    if self.log_user_password == value_dict["Password"]:
                        check_value = 0
                        break
                    else:
                        check_value = 1
                
            if check_value == 0:
                log_password = 0
            else:
                print("\nEntered Password is incorrect,Please Enter the correct Register Password!!!")
        log_choice = 1
        while log_choice:
            print("\n"+("<>~"*15))
            print("\n{:>28}*** Welcome to the User's Profile Page ***".format(" ",self.online_system_name.upper()))
            print("\n{:<23}".format(" "),("~<>"*43))
            print("\n{:>28}1.View Profile".format(" "))
            print("\n{:>28}2.Change Password".format(" "))
            print("\n{:>28}3.Exit".format(" "))
            user_log_choice = input("\nEnter the choice:")
            if user_log_choice == "1":
                self.view_profile()
            elif user_log_choice == "2":
                self.change_password()
            elif user_log_choice == "3":
                log_choice = 0
            else:
                print("\nPlease Enter the correct Choice!!!")

class Restaurant(User): # Here we inherit User Class

    # Here we create constructor for Restaurant Class.
    
    def __init__(self):
        super().__init__()
        self.admin_user_name = "nagaraj2207"
        self.admin_password = "dnagaraj@2207"
        self.total_restaurants = {'FARIZRESTAURANT':
                                {'1.Name': 'FARIZRESTAURANT', '2.Address': 'NO.12 Street:NorthStreet Near:Bustand Pincode:625106 City:Madurai State:Tamil Nadu', '3.FSSAI Number': '12345098761234', '4.Phone Number': '9095493828',
                                'Menu Items': [['DOSA', '20'], ['IDLY', '10'], ['CHICKEN RICE', '100'], ['GRILL', '200'], ['NOODLES', '100'], ['DISCOUNT', 'Above 350 25% Offer']]
                                 }, 'RAHUMAN':
                                  {'1.Name': 'RAHUMAN', '2.Address': 'NO.10 Street:KKNagar Near:college Pincode:625176 City:Madurai State:Tamil Nadu', '3.FSSAI Number': '12345678901234', '4.Phone Number': '6379253529',
                                   'Menu Items': [['CHICKEN BIRYANI', '200'], ['MUTTON BIRYANI', '300'], ['NAATUKOLI BIRYANI', '250'], ['PRAWN BIRYANI', '280'], ['DISCOUNT', 'Above 350 25% Offer']]
                                    }
                                  }

    # Here we create add_menu_items() function for Add Menu Items.

    def add_menu_items(self):
        menu = 1
        while menu:
            try:
                total_menu = input("\nEnter How many number of menu items do you want to Add:")
                total_menu = total_menu.replace(" ","")
                my_validation.total_menu_validation(total_menu)
                total_menu = int(total_menu)
                menu = 0
            except Exception as er:
                print(er)
                
        while total_menu:
            try:
                men = 1
                while men:
                    try:
                        menu_item = input("\nEnter the Menu Item:").upper()
                        menu_item = menu_item.replace(" ","")
                        my_validation.item_name_validation(menu_item)
                        men = 0
                    except Exception as er:
                        print(er)
                it_pri = 1
                while it_pri:
                    try:
                        item_price = input("\nEnter the Item Price:")
                        item_price = item_price.replace(" ","")
                        my_validation.item_price_validation(item_price)
                        it_pri = 0
                    except Exception as er:
                        print(er)
                if self.menu_item != []:
                    for x in range(len(self.menu_item)):
                        if self.menu_item[x][0] == menu_item:
                            check_value = 0
                            break
                        else:
                            check_value = 1
                    if check_value > 0:
                        self.menu_item.append([menu_item,item_price])
                        print(f"\n*** {menu_item} Added Successfully!!! ***")
                        total_menu -= 1
                    else:
                        print("\nThis Menu Item is Already Added!!!")
                else:
                    self.menu_item.append([menu_item,item_price])
                    print(f"\n*** {menu_item} Added Successfully. ***")
                    total_menu -= 1
            except Exception as er:
                print(er)
        discount = 1
        while discount:
            discount_choice = input("\nDo you want to Give the Discount of 25% offer when user buy the items above Rs.350 (y/n):").lower()
            if discount_choice == "y":
                self.menu_item.append(["DISCOUNT","Above 350 25% Offer"])
                discount = 0
            elif discount_choice == "n":
                discount = 0
            else:
                print("\nPlease Enter the correct choice!!!")
        self.restaurant["Menu Items"] = self.menu_item

    # Here we Create add_restaurant() function for Add the Restaurant.

    def add_restaurant(self):
        self.menu_item = []
        self.restaurant = {}
        print("\n"+("="*35))
        print("\n*** Enter The Restaurant Details Below ***")
        print("\n"+("="*35))
        name = 1
        while name:
            try:
                rest_name = input("\nEnter the restaurant name:").upper()
                rest_name = rest_name.replace(" ","")
                my_validation.user_name_validation(rest_name)
                if self.total_restaurants != {}:
                    for key,item in self.total_restaurants.items():
                        if rest_name == item["1.Name"]:
                            check_value = 0
                            break
                        else:
                            check_value = 1
                    if check_value > 0:
                        self.restaurant["1.Name"] = rest_name
                        name = 0
                    else:
                        print("\nThis Restaurant Name already Register in our Portal.")

                else:
                    self.restaurant["1.Name"] = rest_name
                    name = 0
            except Exception as er:
                print(er)
        self.address_details()
        self.restaurant["2.Address"] = self.user_address
        
        fssai = 1
        while fssai:
            try:
                fssai_number = input("\nEnter the FSSAI number:")
                fssai_number = fssai_number.replace(" ","")
                my_validation.fssai_num_validation(fssai_number)
                if self.total_restaurants != {}:
                    for key,item in self.total_restaurants.items():
                        if fssai_number == item["3.FSSAI Number"]:
                            check_value = 0
                            break
                        else:
                            check_value = 1
                    if check_value > 0:
                        self.restaurant["3.FSSAI Number"] = fssai_number
                        fssai = 0
                    else:
                        print("\nYou Already Register this FSSAI Nummber in our Portal.")

                else:
                    self.restaurant["3.FSSAI Number"] = fssai_number
                    fssai = 0
            except Exception as er:
                print(er)

        rest_ph_num = 1
        while rest_ph_num:
            try:
                rest_phone_num = input("\nEnter the restaurant Contact Number:")
                rest_phone_num = rest_phone_num.replace(" ","")
                my_validation.user_phone_number_validation(rest_phone_num)
                if self.total_restaurants != {}:
                    for key,item in self.total_restaurants.items():
                        if rest_phone_num == item["4.Phone Number"]:
                            check_value = 0
                            break
                        else:
                            check_value = 1
                    if check_value > 0:
                        self.restaurant["4.Phone Number"] = rest_phone_num
                        rest_ph_num = 0
                    else:
                        print("\nYou Already Register this Phone Nummber in our Portal.")

                else:
                    self.restaurant["4.Phone Number"] = rest_phone_num
                    rest_ph_num = 0
            except Exception as er:
                print(er)
        self.add_menu_items()
        self.menu_item = []
        self.total_restaurants[rest_name] = self.restaurant

    # Here we create format_table_details() Function for format the Menu Items.

    def format_table_details(self, user_dict):
        self.formatted_items1 = {}
        for field, value in user_dict.items():
            if field != "Menu Items":
                self.formatted_items1[field] = value

    # Here we create show_table() Function for print the Menu Items.

    def show_table(self,user_dict):
        self.formatted_items2 = []
        for field, value in user_dict.items():
            if field == "Menu Items":
                self.formatted_items2.extend(value)

    # Here we create update_menu_items() functions for Upadte the Menu Items.
        
    def update_menu_items(self):
        count1 = 0
        upp_choice = 1
        while upp_choice:
            print("\n"+("="*35))
            print("\n*** Enter The Restaurant Details Below ***")
            print("\n"+("="*35))
            up_name = input("\nEnter the name of the restaurant to update:").upper()
            up_name = up_name.replace(" ","")
            for key,value_dict in self.total_restaurants.items():
                if key == up_name:
                    count1 = 0
                    choose = 1
                    while choose:
                        self.show_table(self.total_restaurants[up_name])
                        print(tabulate.tabulate(( x for x in self.formatted_items2),headers = ["Item","Price"],tablefmt = "grid"))
                        up_choose = input("\nEnter 1 to Continue the Update or press Q to quit:")
                        if up_choose == "1":
                            print("\n"+("="*35))
                            print("\n*** Enter The Items Details Below ***")
                            print("\n"+("="*35))
                            men = 1
                            while men:
                                try:
                                    menu_item = input("\nEnter the Item name to Update:").upper()
                                    menu_item = menu_item.replace(" ","")
                                    my_validation.item_name_validation(menu_item)
                                    men = 0
                                except Exception as er:
                                    print(er)
                            for x in range(len(self.total_restaurants[key]["Menu Items"])):
                                if value_dict["Menu Items"][x][0] == menu_item:
                                    count = 0
                                    if menu_item != "DISCOUNT":
                                        it_pri = 1
                                        while it_pri:
                                            try:
                                                item_price = input("\nEnter the Item Price:")
                                                item_price = item_price.replace(" ","")
                                                my_validation.item_price_validation(item_price)
                                                it_pri = 0
                                            except Exception as er:
                                                print(er)
                                        count = 0
                                        count1 = 0
                                        value_dict["Menu Items"][x][1] = item_price
                                        break
                                    else:
                                        discount = 1
                                        while discount:
                                            discount_choice = input("\nDo you want to Give the Discount of 25% offer when user buy the items above Rs.350 (y/n)").lower()
                                            if discount_choice == "y":
                                                value_dict["Menu Items"][x][1] = "Above 350 25% Offer"
                                                discount = 0
                                                count = 0
                                                count1 = 0
                                                break
                                            elif discount_choice == "n":
                                                value_dict["Menu Items"].pop(x)
                                                discount = 0
                                                count1 = 0
                                                count = 0
                                                break
                                            else:
                                                print("\nPlease Enter the correct choice!!!")
                                else:
                                    count = 1
                                    
                            if count > 0:
                                print("\nMenu Item Not Found")
        
                        elif up_choose == "q":
                            print("\n*** Menu Items Updated Successfully!!! ***")
                            choose = 0
                            count1 = 0
                            upp_choice = 0
                            break
                        else:
                            print("\nPlease Enter the correct Choice (1/q)!!!")
                else:
                    count1 = 1
            if count1 > 0:
                print("\nRestaurant Not Found!!!")

    # Here we create update_restaurant_details() function for Update the Restaurant Details.
                
    def update_restaurant_details(self):
        check_value = 0
        update_name = ""
        upp_choice = 1
        while upp_choice:
            print("\n"+("="*35))
            print("\n*** Enter The Restaurant Details Below ***")
            print("\n"+("="*35))
            up_name = input("\nEnter the name of the restaurant to update:").upper()
            up_name = up_name.replace(" ","")
            for key,value_dict in self.total_restaurants.items():
                if key == up_name:
                    check_value = 0
                    choose = 1
                    while choose:
                        self.format_table_details(self.total_restaurants[key])
                        print(tabulate.tabulate(([key,value] for key, value in self.formatted_items1.items()),headers = ["FIELDS","USER DETAILS"],tablefmt = "grid"))
                        up_choose = input("\nEnter the Number to update the Restaurant Details (1-4) or press q to quit:")
                        if up_choose == "1":
                            upp_name = 1
                            while upp_name:
                                try:
                                    update_name = input("\nEnter the updated restaurant Name:").upper()
                                    update_name = update_name.replace(" ","")
                                    my_validation.user_name_validation(update_name)
                                    value_dict["1.Name"] = update_name
                                    upp_name = 0
                                    check_value = 0
                                    break
                                except Exception as er:
                                    print(er)
                                    
                        elif up_choose == "2":
                            self.address_details()
                            value_dict["2.Address"] = self.user_address
                            check_value = 0
                            
                        elif up_choose == "3":
                            up_fssai = 1
                            while up_fssai:
                                try:
                                    up_fssai_number = input("\nEnter the Updated FSSAI number:")
                                    up_fssai_number = up_fssai_number.replace(" ","")
                                    my_validation.fssai_num_validation(up_fssai_number)
                                    value_dict["3.FSSAI Number"] = up_fssai_number
                                    up_fssai = 0
                                    check_value = 0
                                except Exception as er:
                                    print(er)
                        
                        elif up_choose == "4":
                            up_ph_num = 1
                            while up_ph_num:
                                try:
                                    up_phone_num = input("\nEnter the Updated restaurant Contact Number:")
                                    up_phone_num = up_phone_num.replace(" ","")
                                    my_validation.user_phone_number_validation(up_phone_num)
                                    value_dict["4.Phone Number"] = up_phone_num
                                    up_ph_num = 0
                                    check_value = 0
                                    break
                                except Exception as er:
                                    print(er)

                        elif up_choose == "q":
                            print("\nRestaurant Details Updated Successfully!!!")
                            upp_choice = 0
                            choose = 0
                            check_value = 0
                            break
                        else:
                            print("\nPlease Enter the Correct choice (1-4) or q to Quit!!!")
                    break
                else:
                    check_value = 1
            if check_value > 0:
                print("\nRestaurant Not Found!!!")
            if update_name != "" :
                self.total_restaurants[update_name] = self.total_restaurants.pop(up_name)
                up_name = update_name 
                update_name = ""

    # Here we update_restaurant() function for Update the Restaurant's Main Menu.
                        
    def update_restaurant(self):
        up_choice = 1
        while up_choice:
            print("\n"+("<>~"*15))
            print("\n{:>28}*** Wecome to the Restaurant Update Page ***".format(" ",self.online_system_name.upper()))
            print("\n{:<23}".format(" "),("~<>"*43))
            print("\n{:>28}1.Upadate the Restaurant Details".format(" "))
            print("\n{:>28}2.Update the Menu Items".format(" "))
            print("\n{:>28}3.Exit".format(" "))
            up_choose = input("\nEnter Your Choice:")
            if up_choose == "1":
                self.update_restaurant_details()
            elif up_choose == "2":
                self.update_menu_items()
            elif up_choose == "3":
                up_choice = 0
            else:
                print("\nPlease Enter the correct Choice!!!")

    # Here we create delete_restaurant() function for Delete the Restaurant.

    def delete_restaurant(self):
        print("\n"+("<>~"*15))
        print("\n{:>28}*** Wecome to the Restaurant Delete Page ***".format(" ",self.online_system_name.upper()))
        print("\n{:<23}".format(" "),("~<>"*43))
        dl_name = 1
        while dl_name:
            for key,value_dict in self.total_restaurants.items():
                print("\nRestaurant Name:{}".format(key))
                self.show_table(self.total_restaurants[key])
                print(tabulate.tabulate(( x for x in self.formatted_items2),headers = ["Item","Price"],tablefmt = "grid")) 
                print("\n")
            print("\n"+("="*35))
            print("\n*** Enter The Restaurant Details Below ***")
            print("\n"+("="*35))
            del_name = input("\nEnter the name of the restaurant to delete or Press q to exit:").upper()
            del_name = del_name.replace(" ","")
            if del_name in self.total_restaurants:
                del self.total_restaurants[del_name]
                print(f"\nRestaurant '{del_name}' deleted successfully.")
                dl_name = 0
                del_choose = 0
            elif del_name == "Q":
                dl_name = 0
                del_choose = 0
            else:
                print(f"\nRestaurant not found.")

    # Here we create Restaurant Main Menu Function.
                
    def rest_main_menu(self):
        admin = 1
        while admin:
            print("\n"+("<>~"*15))
            print("\n{:>28}*** Wecome to the Admin Page ***".format(" ",self.online_system_name.upper()))
            print("\n{:<23}".format(" "),("~<>"*43))
            print("\n{:>28}1.Add Restaurant".format(" "))
            print("\n{:>28}2.Update Restaurant".format(" "))
            print("\n{:>28}3.Delete Restaurant".format(" "))
            print("\n{:>28}4.Exit".format(" "))
            admin_choice = input("\nEnter your Choice:")
            if admin_choice == "1":
                self.add_restaurant()
                print(self.total_restaurants)
            elif admin_choice == "2":
                if self.total_restaurants != {}:
                    self.update_restaurant()
                else:
                    print("\nThere is No Restaurant's Added in our Portal,Please first add the Restaurant")
            elif admin_choice == "3":
                if self.total_restaurants != {}:
                    self.delete_restaurant()
                else:
                    print("\nThere is No Restaurant's Added in our Portal,Please first add the Restaurant")
            elif admin_choice == "4":
                admin = 0
            else:
                print("\nPlease Enter the corrct choice!!!")




class OrderManage(Restaurant): # Here we inherit Restaurant Class.

    # Here we create show_table1() for print formatted the Menu Items.
    
    def show_table1(self,user_dict):
        self.formatted_items3 = []
        for field, value in user_dict.items():
            if field == "Menu Items":
                self.formatted_items3.extend(value)

    # Here we create discount_calc() function for Discount calculation.

    def discount_calc(self,amount,order_items):
        self.discount_amount = 0
        discount = 25
        if amount >= 350:
            self.discount_amount = amount*(discount/100)
            order_items.append(["Discount 25%","Minus",float(self.discount_amount)])

    # Here we create tax_delivery_caluculation() function for total Calculation of items.
            
    def tax_delivery_caluculation(self,total_price,order_items,key,total_restaurants):
        tax_percent = 5
        delivery = 40
        if total_price <= 100:
            order_items.append(["Delivery Charge","0",delivery])
            total_price1 =total_price + delivery
        else:
            order_items.append(["Delivery Charge","0",float(delivery)])
            tax = total_price *(tax_percent/100)
            self.order_items.append(["Tax Charge","0",float(tax)])
            total_price1 = total_price + tax + delivery
        for prod in total_restaurants[key]["Menu Items"]:
            if "DISCOUNT" in prod:
                print("AAA")
                self.discount_calc(self.total_price,self.order_items)
                total_price1 -= self.discount_amount 
                order_items.append(["Total Price","0",float(total_price1)])
                count = 0
                break
            else:
                count = 1
        if count > 0:
            order_items.append(["Total Price","0",float(total_price1)])
                
    # Here we create order_menu_items() function for Order the menu Items.
   
    def order_menu_items(self):
        self.order_items = []
        self.total_price = 0
        orr_choice = 1
        while orr_choice:
            print("\n"+("="*35))
            print("\n*** Enter The Restaurant Details Below ***")
            print("\n"+("="*35))
            or_name = input("\nEnter the name of the restaurant to order:").upper()
            or_name = or_name.replace(" ","")
            if or_name not in self.total_order_items:
                for key,value_dict in self.total_restaurants.items():
                    if key == or_name:
                        num_list1 = [x for x in range(1,(len(self.total_restaurants[key]["Menu Items"])+1))]
                        choose = 1
                        while choose:
                            self.show_table1(self.total_restaurants[or_name])
                            table = [[num_list1[i]] + self.formatted_items3[i] for i in range(len(num_list1))]
                            print(tabulate.tabulate(table,headers = ["S.No","Item","Price"],tablefmt = "grid"))
                            order_choice = input("\nEnter the Number to order the Foods in the Menu Items (or) press q to Quit:").upper()
                            for x in range(1,(len(self.total_restaurants[key]["Menu Items"])+1)):
                                if str(x) == order_choice:
                                    x = int(x)
                                    if value_dict["Menu Items"][x-1][0] != "DISCOUNT":
                                        quant = 1
                                        while quant:
                                            try:
                                                quantity = input("\nEnter the quantity of the Foods:")
                                                quantity = quantity.replace(" ","")
                                                my_validation.quantity_validation(quantity)
                                                quant = 0
                                            except Exception as er:
                                                print(er)
                                        price_calc = int(quantity)*int(value_dict["Menu Items"][x-1][1])
                                        self.total_price += price_calc
                                        item_exists = False
                                        for item in self.order_items:
                                            if item[0] == value_dict["Menu Items"][x-1][0]:
                                                item[1] += int(quantity)
                                                item[2] += price_calc
                                                item_exists = True
                                                break
                                        if not item_exists:
                                            self.order_items.append([value_dict["Menu Items"][x-1][0],int(quantity),float(price_calc)])
                                        check_value = 0
                                        count_value1 = 0
                                        break
                                    else:
                                        print("\nDISCOUNT is not a food name it mentioned because this Restaurant gives the discount when you buy total above Rs.350")
                                        check_value = 0
                                        count_value1 = 0
                                        break

                                elif order_choice == "Q":
                                    print("\nFoods Order Taken,Please wait untill Deliver.")
                                    if self.order_items != []:
                                        self.tax_delivery_caluculation(self.total_price,self.order_items,key,self.total_restaurants)    
                                        self.total_order_items[key] = self.order_items
                                    self.order_items = []
                                    choose = 0
                                    orr_choice = 0
                                    check_value = 0
                                    count_value1 = 0
                                    break
                                else:
                                    check_value = 1    
                            if check_value > 0:
                                print("\nPlease Enter the correct choice!!!")
                        break
                    else:
                        count_value1 = 1
                if count_value1 > 0:
                    print("\nRetaurant Name Not found,Please Enter the correct Name!!!")
                
            else:
                print("\nYour Order is Already Taken in our Restaurant wait untill its deliver (or) cancel the current order!!!")
                orr_choice = 0

    # Here we create place_order() function for Place the Place the Order's.
    
    def place_order(self):
        print("\n"+("<>~"*15))
        print("\n{:>28}*** Wecome to the Place Order's Page ***".format(" ",self.online_system_name.upper()))
        print("\n{:<23}".format(" "),("~<>"*43))
        food_order = 1
        while food_order:
            print("\n"+("="*35))
            print("\n*** The Availabile Restaurant's are ***")
            print("\n"+("="*35))
            for key,item in self.total_restaurants.items():
                print(f"Restaurant Name: {item['1.Name']}")
                print(f"Address: {item['2.Address']}")
                print(f"Contact Information: {item['4.Phone Number']}")
                print("Menu Items:")
                print(tabulate.tabulate(( x for x in item["Menu Items"]),headers = ["Item","Price"],tablefmt = "grid"))
            or_choice = 1
            while or_choice:
                order_choice = input("\nPRESS 1 to continue or PRESS q to EXIT:")
                if order_choice == "1":
                    self.order_menu_items()
                    or_choice = 0
                elif order_choice == "q":
                    or_choice = 0
                    food_order = 0
                else:
                    print("\nPlease Enter the correct choice (1/q)!!!")

    # Here we create track_order() function for track the Orders.

    def track_order(self):
        print("\n"+("<>~"*15))
        print("\n{:>28}*** Wecome to the Track Order's Page ***".format(" ",self.online_system_name.upper()))
        print("\n{:<23}".format(" "),("~<>"*43))
        tr_or = 1
        while tr_or:
            delivery_person_names = ["Prakash","Peter","Arun","Ramesh","Ragul"]
            delivery_person_phone_num = ["9988774532","9098786754","8087675545","9879076655","7889095609"]
            delivery_time = ["5","10","15","20","25"]
            tr_ord = 1
            print("\n"+("="*35))
            print("\n*** Enter The Restaurant Details Below ***")
            print("\n"+("="*35))
            while tr_ord:
                try:
                    track_order = input("\nEnter the Restaurant Name to Track Your Order:").upper()
                    track_order = track_order.replace(" ","")
                    my_validation.user_name_validation(track_order)
                    tr_ord = 0
                except Exception as er:
                    print(er)
            for key,item in self.total_order_items.items():
                if key == track_order:
                    print("\nThe Ordered items are:")
                    print(tabulate.tabulate(item,headers = ["Item","Quantity","Price"],tablefmt = "grid"))
                    del_time = random.choice(delivery_time)
                    print("\nYour Order is Ready in {} minutes please wait!!!".format(del_time))
                    del_person = random.choice(delivery_person_names)
                    print("\nYour Order is Deliver by {}".format(del_person))
                    del_ph_num = random.choice(delivery_person_phone_num)
                    print("\nDelivery Person {}'s Contact Number is {}:".format(del_person,del_ph_num))
                    del_ph = 1
                    while del_ph:
                        user_del_ph_num = input("\nIf want to contact PRESS 1 and PRESS 0 to exit:")
                        if user_del_ph_num == "1":
                            print("\nPlease wait...")
                            time.sleep(5)
                            print("\nI will reach you soon!!!")
                            del_ph = 0
                            count = 0
                            tr_or = 0
                        elif user_del_ph_num == "0":
                            print("\nIf you want the cancel the order please cancel Before its deliverder!!!")
                            count = 0
                            tr_or = 0
                        else:
                            print("\nPlease Enter the correct choice 0 and 1!!!")
                    break
                else:
                    count = 1
            if count > 0:
                print("\nYour order is not found!!!")

    # Here we Create cancel_order() function for Cancel the Order's.

    def cancel_order(self):
        print("\n"+("<>~"*15))
        print("\n{:>28}*** Wecome to the Cancel Order's Page ***".format(" ",self.online_system_name.upper()))
        print("\n{:<23}".format(" "),("~<>"*43))
        print("\n"+("="*35))
        print("\n*** The Avilable Restaurant's are***")
        print("\n"+("="*35))
        for key,item in self.total_order_items.items():
            print("\nRestaurant Name: {}".format(key))
            print("\nYour Orders are:")
            print(tabulate.tabulate(item,headers = ["Item","Quantity","Price"],tablefmt = "grid"))
        dl_rest = 1
        while dl_rest:
            cn_choice = input("\nPRESS 1 To Continue or PRESS q to Exit:").lower()
            if cn_choice == "1":
                can_ord = 1
                while can_ord:
                    print("\n"+("="*35))
                    print("\n*** Enter The Restaurant Details Below ***")
                    print("\n"+("="*35))
                    try:
                        cancel_order = input("\nEnter the Restaurant Name to Cancel Your Order or q to Exit:").upper()
                        cancel_order = cancel_order.replace(" ","")
                        my_validation.user_name_validation(cancel_order)
                        can_ord = 0
                    except Exception as er:
                        print(er)
                if cancel_order in self.total_order_items:
                    del self.total_order_items[cancel_order]
                    print(f"\nYour Order Cancel Successfully In our {cancel_order} Restaurant!!!")
                    dl_rest = 0
                else:
                    print("\nRestaurant Not Found!!!")
            elif cn_choice == "q":
                dl_rest = 0
            else:
                print("\nPlease Enter the correct Choice (1/q)!!!")

    # Here we create order_main_menu() for Order the Food Items.

    def order_main_menu(self):
        self.total_order_items = {}
        or_main = 1
        while or_main:
            print("\n"+("<>~"*15))
            print("\n{:>28}*** Wecome to the FOODS Order Page ***".format(" ",self.online_system_name.upper()))
            print("\n{:<23}".format(" "),("~<>"*43))
            print("\n{:>28}1.Place Order".format(" "))
            print("\n{:>28}2.Track Order".format(" "))
            print("\n{:>28}3.Cancel Order".format(" "))
            print("\n{:>28}4.Exiit".format(" "))
            order_main_choice = input("\nEnter Your choice:")
            if order_main_choice == "1":
                self.place_order()
            elif order_main_choice == "2":
                if self.total_order_items != {}: 
                    self.track_order()
                else:
                    print("\nThere is no order to track,First Place the Order")
            elif order_main_choice == "3":
                if self.total_order_items != {}:
                    self.cancel_order()
                else:
                    print("\nThere is no order to Cancel,First Place the Order")
            elif order_main_choice == "4":
                print("\nThank You!!!")
                or_main = 0
            else:
                print("\nPlease Enter the Correct Choice (1-4)!!!")

class PaymentMange(OrderManage): # Here we create inherit OrderManage class.

    # Here we Create format_payment_details1() function for format the card details.
    
    def format_payment_details1(self,payment_dict):
        self.formatted_items3 = {}
        for key,item in payment_dict.items():
            formatted_item = {}
            for field,value in item.items():
                if key == "1.Card Details":
                    if field == 'Card Number':
                        formatted_value = re.sub(r"(\d{4})-(\d{4})-(\d{4})-(\d{4})", r"xxx-xxxx-xxxx-\4", value)
                    elif field == 'CVV':
                        formatted_value = re.sub(r"\d{3}",r"xxx",value)
                    else:
                        formatted_value = value
                elif key == "2.Internet Banking Details":
                    if field == 'Net Password':
                        formatted_value = re.sub(r"^[A-Z]{1}[a-z]+[0-9\W_]+",r"xxxxxxx",value)
                    else:
                        formatted_value = value
                elif key == "3.Mobile UBI":
                    if field == 'UBI PIN':
                        formatted_value = re.sub(r"\d{4}",r"xxxx",value)
                    else:
                        formatted_value = value
                formatted_item[field] = formatted_value
            self.formatted_items3[key] = formatted_item

    # Here we create bill_payment() funtion pay the Bill.
            
    def bill_payment(self):
        print("\n"+("<>~"*15))
        print("\n{:>28}*** Wecome to the Bill Payment Page ***".format(" ",self.online_system_name.upper()))
        print("\n{:<23}".format(" "),("~<>"*43))
        print("\n"+("="*35))
        print("\n*** Enter Your Login Details Below ***")
        print("\n"+("="*35))
        pay_num = 1
        while pay_num:
            try:
                pay_ph_num = input("\nEnter Your Login Mobile Number To Pay the Bill:")
                pay_ph_num = pay_ph_num.replace(" ","")
                my_validation.user_phone_number_validation(pay_ph_num)
                if pay_ph_num == self.log_ph_num:
                    for key,item in self.total_order_items.items():
                        print("\nRestaurant Name: {}".format(key))
                        print("\nYour Orders are:")
                        print(tabulate.tabulate(item,headers = ["Item","Quantit","Price"],tablefmt = "grid"))
                    py_ord = 1
                    while py_ord:
                        try:
                            pay_order = input("\nEnter the Restaurant Name to Pay Your Order:").upper()
                            pay_order = pay_order.replace(" ","")
                            my_validation.user_name_validation(pay_order)
                            for key1,value in self.total_order_items.items():
                                count = 0
                                if key1 == pay_order:
                                    for items in value:
                                        if items[0] == "Total Price":
                                            py_price = 1
                                            while py_price:
                                                pay_price = input("\nEnter the Total Price to pay the Orders:")
                                                pay_price = pay_price.replace(" ","")
                                                if float(pay_price) == float(items[2]):
                                                    print("AAA")
                                                    py_price = 0
                                                    py_ord = 0
                                                    count = 0
                                                else:
                                                    print("\nPlease Enter the correct Total Price")
                                    break
                                else:
                                    count = 1
                            if count > 0:
                                print("\nYour Order is not found in this Restaurant!!!")

                        except Exception as er:
                            print(er)
                    if pay_order in self.total_order_items:
                        print("SSS")
                        del self.total_order_items[pay_order]
                    pay_num = 0
                else:
                    print("\nEntered Phone number is wrong,Please Enter the correct Phone Number!!!")
            except Exception as er:
                print(er)
        temp = 1
        while temp:
            for key,my_dict in self.user_information.items():
                if key == pay_ph_num:
                    print("Correct")
                    for key1,item in self.overall_payment_details.items():
                        if key1 == pay_ph_num:
                            print("pay")
                            print("\n"+("o~"*7))
                            print("\nHai {}".format(my_dict["1.Name"]))
                            print("\n"+("o~"*7))
                            print("\n"+("="*35))
                            print("\nYour Payment Details are:")
                            print("\n"+("="*35))
                            self.format_payment_details1(item)
                            print(tabulate.tabulate(([x,y]for x,y in self.formatted_items3.items()), headers=["Payment Details"], tablefmt='grid'))
                            pay_choice = 1
                            while pay_choice:
                                print("\n"+("<>~"*15))
                                print("\n{:>28}*** Wecome to the Payment Option's Page ***".format(" ",self.online_system_name.upper()))
                                print("\n{:<23}".format(" "),("~<>"*43))
                                print("\n{:>28}1.Credit/Debit Card".format(" "))
                                print("\n{:>28}2.Internet Banking".format(" "))
                                print("\n{:>28}3.Mobile Payments/UBI's".format(" "))
                                print("\n{:>28}4.Cash On Deliver".format(" "))
                                print("\n{:>28}5.Exit".format(" "))
                                pay_choose = input("\nEnter Your choice:")
                                if pay_choose == "1":
                                    if "1.Card Details" in item:
                                        py_cvv = 1
                                        while py_cvv:
                                            try:
                                                pay_cvv = input("\nEnter the card cvv Number:")
                                                pay_cvv = pay_cvv.replace(" ","")
                                                my_validation.cvv_validation(pay_cvv)
                                                if pay_cvv == self.overall_payment_details[key1]["1.Card Details"]["CVV"]:
                                                    print("\nThank you,Payment was Successfull.Your Oder is on the way Please wait...")
                                                    time.sleep(5)
                                                    print("\nOrder Delivered Enjoy Your Food!!!")
                                                    py_cvv = 0
                                                    pay_choice = 0
                                                    temp = 0
                                                else:
                                                    print("\nCVV Number is incorrect,Please Enter the correct CVV Number")
                                            except Exception as er:
                                                print(er)
                                        
                                    else:
                                        print("\nSorry!!!,Your Card is Not Added in our Portal.")
                                elif pay_choose == "2":
                                    if "2.Internet Banking Details" in item:
                                        py_net = 1
                                        while py_net:
                                            try:
                                                pay_net_password = input("\nEnter Your Net Banking Password:")
                                                pay_net_password = pay_net_password.replace(" ","")
                                                my_validation.user_password_validation(pay_net_password)
                                                if pay_net_password == self.overall_payment_details[key1]["2.Internet Banking Details"]["Net Password"]:
                                                    print("\nThank you,Payment was Successfull.Your Oder is on the way Please wait...")
                                                    time.sleep(5)
                                                    print("\nOrder Delivered Enjoy Your Food!!!")
                                                    py_net = 0
                                                    pay_choice = 0
                                                    temp = 0
                                                else:
                                                    print("\nNet Banking Password is incorrect,Please Enter the Correct Net Banking Password")
                                            except Exception as er:
                                                print(er)
                                        
                                    else:
                                        print("\nSorry!!!,Your Internet Banking is Not Added in our Portal.")
                                        
                                elif pay_choose == "3":
                                    if "3.Mobile UBI" in item:
                                        py_ubi = 1
                                        while py_ubi:
                                            try:
                                                pay_ubi_num = input("\nEnter Your Mobile UBI PIN")
                                                pay_ubi_num = pay_ubi_num.replace(" ","")
                                                my_validation.ubi_pin_validation(pay_ubi_num)
                                                if pay_ubi_num == self.overall_payment_details[key1]["3.Mobile UBI"]["UBI PIN"]:
                                                    print("\nThank you,Payment was Successfull.Your Oder is on the way Please wait...")
                                                    time.sleep(5)
                                                    print("\nOrder Delivered Enjoy Your Food!!!")
                                                    py_ubi = 0
                                                    pay_choice = 0
                                                    temp = 0
                                                else:
                                                    print("\nUBI PIN is incorrect,Please Enter the correct UBI PIN")
                                            except Exception as er:
                                                print(er)
                                    else:
                                        print("\nSorry!!!,Your Mobile UBI is Not Added in our Portal.")
                                elif pay_choose == "4":
                                    print("\nThank You,Our Delivery Boy will collect the cash in your Home!!!")
                                    time.sleep(5)
                                    print("\nThank you,Payment Successfull")
                                    time.sleep(2)
                                    print("\nOrder Delivered Enjoy Your Food!!!")
                                    pay_choice = 0
                                    temp = 0
                                elif pay_choose == "5":
                                    pay_choice = 0
                                    temp = 0
                                else:
                                    print("\nPlease Enter the correct Given Choice(1-5)!!!")

class Login(PaymentMange): # Here we inherit PaymentMange Class.

    # Here we create user_login() function for User's Login
    
    def user_login(self):
        print("\n"+("="*35))
        print("\n*** Enter Your Register Details Below ***")
        print("\n"+("="*35))
        log_name = 1
        while log_name:
            self.log_ph_num = input("\nEnter Your Mobile Number:")
            if self.log_ph_num in self.user_information:
                log_name = 0
            else:
                print("\nEntered Phone number is wrong,Please Enter the correct Phone Number!!!")

        log_name = 1
        while log_name:
            log_user_id = input("\nEnter Your User Id:")
            for item,value_dict in self.user_information.items():
                if item == self.log_ph_num:
                    if log_user_id == value_dict["User Id"]:
                        check_value = 0
                        break
                    else:
                        check_value = 1
                    
            if check_value == 0:
                log_name = 0
            else:
                print("\nEntered User Id is wrong,Please Enter the correct User Id!!!")

        log_password = 1
        while log_password:
            log_user_password = input("\nEnter Your Register User Password:")
            for item,value_dict in self.user_information.items():
                if item == self.log_ph_num:
                    if log_user_password == value_dict["Password"]:
                        check_value = 0
                        break
                    else:
                        check_value = 1
                
            if check_value == 0:
                log_password = 0
            else:
                print("\nEntered Password is incorrect,Please Enter the correct Register Password!!!")
        log_choice = 1
        while log_choice:
            print("\n"+("<>~"*15))
            print("\n{:>28}*** Welcome to User's Login Page ***".format(" ",self.online_system_name.upper()))
            print("\n{:<23}".format(" "),("~<>"*43))
            print("\n{:>28}1.Place Food Order".format(" "))
            print("\n{:>28}2.Exit".format(" "))
            user_log_choice = input("\nEnter your choice:")
            if user_log_choice == "1":
                self.order_main_menu()
                if self.total_order_items != {}:
                    self.bill_payment()
            elif user_log_choice == "2":
                log_choice = 0
            else:
                print("\nPrint the correct choice!!!")


class Main(Login): # Here we inherit Login Class
    
    # Here we Create main_menu() function for Online Food Odering System.
    
    def main_menu(self):
        choice = 1
        while choice:
            print("\n"+("<>~"*15))
            print("\n{:>28}*** Welcome to {} Online Food Odering System ***".format(" ",self.online_system_name.upper()))
            print("\n{:<23}".format(" "),("~<>"*43))
            print("\n{:28}1.Admin Login".format(" "))
            print("\n{:28}2.User Register".format(" "))
            print("\n{:28}3.User Login".format(" "))
            print("\n{:28}4.View Profile and Change Password".format(" "))
            print("\n{:28}5.Exit".format(" "))
            main_choice = input("\nEnter Your Chooice:")
            if main_choice == "1":
                print("\n"+("="*35))
                print("\n*** Enter The Admin Details Below ***")
                print("\n"+("="*35))
                admin_choice = 1
                while admin_choice: 
                    user_admin_name = input("\nEnter the Register Admin user name:")
                    user_admin_name = user_admin_name.replace(" ","")
                    if user_admin_name == self.admin_user_name:
                        admin_choice = 0
                    else:
                        print("\nPlease Enter the Correct Admin User name!!!")
                admin_pass = 1
                while admin_pass:
                    user_admin_password = input("\nEnter the Register Admin Password:")
                    user_admin_password = user_admin_password.replace(" ","")
                    if user_admin_password == self.admin_password:
                        self.rest_main_menu()
                        admin_pass = 0
                    else:
                        print("\nPlease Enter the Correct Admin Password!!!")
            elif main_choice == "2":
                self.user_register()
                print(self.user_information)
                print(self.overall_payment_details)
            elif main_choice == "3":
                if self.total_restaurants != {}:
                    if self.user_information != {}:
                        self.user_login()
                    else:
                        print("\nThere is No User's Registered in our Portal,Please Register first.")
                else:
                    print("\nSorry!!!There is No Restaurant's Available for Order the Food's!!!")
            elif main_choice == "4":
                if self.user_information != {}:
                    self.view_profile_change_password()
                else:
                    print("\nThere is No User's Registered in our Portal,Please Register first.")
            elif main_choice == "5":
                print("\n"+("o~"*22))
                print("\n{:>28}*** Thank you for using {} Online Food Odering System ***".format(" ",self.online_system_name.upper()))
                print("\n{:<23}".format(" "),("~o"*64))
                choice = 0
            else:
                print("\nPlease Enter the Correct Choice!!!")


food_ordering_system = Main()
food_ordering_system.main_menu()





