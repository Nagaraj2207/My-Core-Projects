# Here we create re and datime module.
import re
import datetime

# Here we create Multiple function for validation.

def user_name_validation(string_name):
    if string_name.isdigit():
        raise Exception ("\nName must be a string.")
    elif len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nName should not be empty.")
    elif len(string_name)<=2:
        raise Exception ("\nPlease Enter the proper Name.")

def user_email_id_validation(user_string):
    email_pattern = re.search(r"^[a-z0-9]+([\._]?[a-z0-9]+)*@[a-z]{5}+\.[a-z]{2,3}$",user_string)
    if len(user_string.split("@")[0]) < 6 or len(user_string.split("@")[0]) > 15:
        raise Exception ("\nEmail should be in the length of 6 to 15")
    elif not email_pattern:
        raise Exception ("\nEmail should be in the correct pattern (Eg:dnagaraj3828@gamil.com)")

def street_number_validation(user_string):
    street_number_pattern = re.search(r"^\d+[A-Za-z]?$",user_string)
    if len(user_string) == 0:
        raise Exception ("\nStreet Number Sholud not be empty.")
    elif not street_number_pattern:
        raise Exception ("\nStree Number Should be in this pattern (Eg:123A)")

def street_name_validation(user_string):
    street_name_pattern = re.search(r'^[A-Za-z1-9\s-]+$',user_string)
    if len(user_string) < 3:
        raise Exception ("\nStreet Name Sholud be in  length of Greater than or Equal to 3 character.")
    elif not street_name_pattern:
        raise Exception ("\nStree Name Should be in this pattern (Eg:Main Street (or)1st street)")

def landmark_validation(string_name):
    if string_name.isdigit():
        raise Exception ("\nLandmark must be a string.")
    elif len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nLandmark should not be empty.")
    elif len(string_name)< 5:
        raise Exception ("\nPlease Enter the proper Landmark.")

def pinncode_validation(string_name):
    if not string_name.isdigit():
        raise Exception ("\nPincode must be a Number.")
    elif len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nPincode should not be empty.")
    elif len(string_name) != 6:
        raise Exception ("\nPlease Enter the correct Pincode.")

def city_validation(string_name):
    if string_name.isdigit():
        raise Exception ("\nCity must be a string.")
    elif len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nCity should not be empty.")
    elif len(string_name) < 6:
        raise Exception ("\nPlease Enter the proper City.")

def card_number_validation(string_name):
    card_pattern = re.search(r"^\d{4}-\d{4}-\d{4}-\d{4}$",string_name)
    if len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nCard Number should not be empty.")
    elif not card_pattern:
        raise Exception ("\nCard Number should 16 digits and in the correct Format (Eg:1234-5678-9012-3456)")

def is_valid_date(date_string):
    try:
        datetime.datetime.strptime(date_string,"%m/%Y")
        return True
    except ValueError:
        return False

def card_expire_date_validation(string_name):
    if not is_valid_date(string_name):
        raise Exception ("\nExpire Date should be in this format (Eg:12/2023)")
    

def cvv_validation(string_name):
    if not string_name.isdigit():
        raise Exception ("\nCVV must be a Number.")
    elif len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nCVV should not be empty.")
    elif len(string_name) != 3:
        raise Exception ("\nPlease Enter the correct CVV it contain only 3 digits (Eg:123).")

def net_id_validation(string_name):
    net_id_pattern = re.search(r"^[a-z]{3,10}+[0-9]{2,6}$",string_name)
    if len(string_name) < 5 or len(string_name) > 20:
        raise Exception ("\nUser Id should be in the length of 5 to 20 charcters.")
    elif not net_id_pattern:
        raise Exception ("\nUser Id should be 3 small character and atleast 2 numbers and in this Format (Eg:john123)")

def ubi_id_validation(string_name):
    ubi_id_pattern = re.search(r"^[a-z0-9]{10,15}+@[a-z]{3,5}",string_name)
    if not ubi_id_pattern:
        raise Exception ("\nUBI ID must be in the length of 10 to 15 and in this format (Eg:ramkumar1234@ybl)")

def ubi_pin_validation(string_name):
    if not string_name.isdigit():
        raise Exception ("\nPIN must be a Number.")
    elif len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nPIN should not be empty.")
    elif len(string_name) != 4:
        raise Exception ("\nPIN should be in the length of 4 (Eg:1234).")


def user_password_validation(user_string):
    password_pattern = re.search(r"^[A-Z]{1}[a-z0-9]+[a-z0-9\W_]", user_string)
    if len(user_string) < 3 or len(user_string) > 20:
        raise Exception ("\nPassword should be in the length of 3 to 20")
    elif user_string.endswith(" "):
        raise Exception ("\npassword should not endswith space")
    elif not password_pattern:
        raise Exception ("\npassword should be starts with Capital Letter Eg:Nagaraj@007.")


def user_phone_number_validation(string_name):
    ph_num_pattern = re.match("^[6-9]{1}[0-9]{9}$",string_name)
    if string_name.isalpha():
        raise ValueError ("\nPhone Number must be in digits (or) numbers.")
    elif len(string_name) != 10:
        raise Exception ("\nPhone Number must be 10 digits")
    elif not ph_num_pattern:
        raise Exception ("\nPhone Number must be starts with 6-9 and 10 digits(Eg:6379276534)")

def fssai_num_validation(string_name):
    fssai_pattern = re.search(r"^\d{14}$",string_name)
    if len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nFSSAI Should not be Empty")
    elif not fssai_pattern:
        raise Exception ("\nFSSAI Number must be 14 Numbers and in this format (Eg:12345678901234)")

def total_menu_validation(string_name):
    if not string_name.isdigit():
        raise Exception ("\nTotal Menu Number must be in digits.")
    elif len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nTotal Menu Number must not be Empty.")
    elif int(string_name) <= 0 or int(string_name) > 10:
        raise Exception ("\nMust Add Minimum 1 menu item and Maximum 10 menu items.")

def item_name_validation(string_name):
    if string_name.isdigit():
        raise Exception ("\nItem Name must be a string.")
    elif len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nItem Name should not be empty.")
    elif len(string_name)<=2:
        raise Exception ("\nPlease Enter the proper Item Name.")

def item_price_validation(string_name):
    if not string_name.isdigit():
        raise Exception ("\nItem Price must be in digits.")
    elif len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nItem Price must not be Empty.")
    elif int(string_name) < 5:
        raise Exception ("\nItem Price Atleast Minimum Rs.5.00 and More.")

def quantity_validation(string_name):
    if not string_name.isdigit():
        raise Exception ("\nQuantity Number must be in digits.")
    elif len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nQuantity Number must not be Empty.")
    elif int(string_name) <= 0:
        raise Exception ("\nQuantity number should be greater than Zero")

def total_price_validation(string_name):
    if string_name.isalpha():
        raise Exception ("\nTotal Price must be in digits.")
    elif len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nTotal Price must not be Empty.")
    elif int(string_name) <= 0:
        raise Exception ("\nTotal Price must be Greater than Zero!!!")

    
        
    
