import time

def encode_token(email):
    timenow= time.ctime()
    stringT =  email+" "+timenow
    str = stringT.encode('utf-8')
    return str.hex()