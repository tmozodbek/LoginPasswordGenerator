import random
import string
import time

BELGI = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_']

def getHashPassword(string):
    string = string.replace(" ", "")
    leng = len(string)

    result = random.choice(string)
    result += random.choice(string)
    result += random.choice(BELGI)

    return result

def getHashLogin(lastname, birth, firstname, thirdname):

    ans = ""
    ans+=thirdname[0]
    ans+=thirdname[1]
    ans+=birth[1]
    ans+=firstname[1]
    ans+=firstname[3]
    w = lastname[2] + lastname[3] + lastname[4]
    ans+=w[::-1]

    return ans
def LoginPassword(Last_Name, First_Name, Date_Of_Birth, Father_is_Name):
    
    password = ""
    login = ""

    password += getHashPassword(Last_Name)
    password += getHashPassword(First_Name)
    password += getHashPassword(Father_is_Name)
    password += getHashPassword(Date_Of_Birth)

    login += getHashLogin(Last_Name, Date_Of_Birth, First_Name, Father_is_Name)

    return [login, password]

Last_Name = 'Rajabboyev'
First_Name = 'Ozodbek'
Date_Of_Birth = '25.08.2006'
Father_is_Name = 'Jasur o`g`li'
print(LoginPassword(Last_Name, First_Name, Date_Of_Birth, Father_is_Name))  # 1
print(LoginPassword(Last_Name, First_Name, Date_Of_Birth, Father_is_Name))  # 2
print(LoginPassword(Last_Name, First_Name, Date_Of_Birth, Father_is_Name))  # 3
print(LoginPassword(Last_Name, First_Name, Date_Of_Birth, Father_is_Name))  # 4
print(LoginPassword(Last_Name, First_Name, Date_Of_Birth, Father_is_Name))  # 5
