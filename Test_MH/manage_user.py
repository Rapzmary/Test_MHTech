from Test_MH import manageText

def Login(data):

    checkdata = manageText.checkdata_for_login(data["email"],data["password"])
    return checkdata

def register(data):
    message = ""
    checkdata = manageText.checkdata_intext(data["email"])
    if checkdata == True:
        message = "Duplicate Email"
    else:
        message = "Regiter success"
        manageText.adddata_intext_Data_user(data)
    return message

def checkToken(Token):
    v=bytes.fromhex(Token).decode('utf-8')
    x = v.split()
    
    return manageText.checktoken_intext(x[0],Token)

def Logout(Token):

    return