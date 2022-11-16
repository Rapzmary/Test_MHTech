
from Test_MH import manageText

def Login(data):
    checkdata = manageText.checkdata_intext(data["email"])
    return 

def register(data):
    message = ""
    checkdata = manageText.checkdata_intext(data["email"])
    if checkdata == True:
        message = "Duplicate Email"
    else:
        message = "Regiter success"
        manageText.adddata_intext_Data_user(data)
    return message

def Logout(Token):
    return