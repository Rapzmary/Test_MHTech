import ast
from Test_MH import encode
def checkdata_intext(email):
    with open("./Test_MH/Data_user.txt") as f:
            lines = f.readlines()
    duplicate = False
    for i in lines:
        i= i[0:len(i)-1]
        if i == email:
            duplicate = True
    print("คำตอบ")
    print(duplicate)
    return duplicate
    
def checktoken_intext(email,token):
    Status=False
    f = open('./Test_MH/Text_Datauser/'+email+'.txt')
    read=f.readlines()
    f.close()
    dictdata = ast.literal_eval(read[0])
    if dictdata['Token'] == token:
        Status = True
    return Status

def adddata_intext_Data_user(data):
    f = open('./Test_MH/Data_user.txt', 'a')
    f.write(data['email']+"\n")
    f.close()
   # f1 = open('./Test_MH/'+"dd"+'.txt','w')
    f2 = open('./Test_MH/Text_Datauser/'+ data['email']+'.txt', 'w')
    text = data.dict()
    text['Login'] = False
    text['Token'] =""
    f2.write(str(text))
    f2.close()

def checkdata_for_login(email,password):
    datasend={}
    Token=""
    message = ""
    try:
        f = open('./Test_MH/Text_Datauser/'+email+'.txt')
        read=f.readlines()
        f.close()
        print(read)
        dictdata = ast.literal_eval(read[0])
        if dictdata['password'] == password:
            dictdata['Login'] == True
            Token = encode.encode_token(email)
            dictdata['Token'] = Token
            fw =  open('./Test_MH/Text_Datauser/'+email+'.txt','w')
            fw.write(str(dictdata))
            fw.close()
            message = "Login success"
        else:
            message = "Password incorrect"
    except:     
        message = "Email not found"
    datasend['message'] = message
    datasend['Token']=Token
    return datasend

    
