import re

def  phoneNumberValidator(phone_num: str)->bool: 
    result = bool(re.search(r"((\+49)|(0049))(\d+[10-99999])(\d+[100-999999])", phone_num))
    return result