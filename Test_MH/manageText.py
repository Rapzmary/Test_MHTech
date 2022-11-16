import ast
def checkdata_intext(email):
    with open("./Test_MH/Data_user.txt") as f:
            lines = f.readlines()
    duplicate = False
    for i in lines:
        i= i[0:len(i)-1]
        if i == email:
            duplicate = False
    print("คำตอบ")
    print(duplicate)
    return duplicate

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
    message = ""
    try:
        f = open('./Test_MH/Text_Datauser/'+email+'.txt')
        read=(f.readlines())[0]
        dictdata = ast.literal_eval(read)
    except:
        message = "Email not found"

    
