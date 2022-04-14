import json, re
from os.path import exists

jsonfile = 'signup.json'

def makejson():
    print('signup.json not found. creating one...')
    data = {"user": {}}
    jsonwrite(data)

def jsonopen():
    with open(jsonfile, 'r') as fp:
        data = json.load(fp)
    return data

def jsonwrite(data):
    with open(jsonfile, 'w' ) as fp:
        json.dump(data, fp, indent=4)

def signup():
    data = jsonopen()
    u = input('username: (5-15 characters, lowercase alphabets, numbers, _, . allowed) ')
    if u in data['user']:
        print('username', u, 'is already in use. please choose a different one')
        return None
    
    if not 5 <= len(u) <= 15:
        if len(u) < 5:
            print('username', u, 'is too short! please type at least 5 characters')
        else:
            print('username', u, 'is too long! please type 15 or less characters')
        return None
    
    res = re.match('^[a-z0-9_.]+$', u)
    if res:
        pass
    else:
        print('username', u, 'does not meet the criteria(5-15 characters, lowercase alphabets, numbers, _, . allowed)')
        return None

    p = input('password: ')
    n = input('name: ')
    newUser = {u: {'name': n, 'password': p}}
    data['user'].update(newUser)
    jsonwrite(data)
    print('user', u, 'created!')

def login():
    data = jsonopen()

    u = input("username? ")
    if u in data['user']:
        print('user', u, 'exist')
        p = input("password? ")
        if p == data['user'][u]['password']:
            print('Welcome', u+'!')
        else:
            print('incorrect password for', u)
    else:
        print('no such user')

def removeAcc():
    data = jsonopen()
    u = input('which account would you like to remove? ')
    if u in data['user']:
        p = input('account %s found. please type a password to remove' % u)
        if p == data['user'][u]['password']:
            del data['user'][u]
            jsonwrite(data)
            print('goodbye', u)
        else:
            print('incorrect password for', u)
    else:
        print('user', u, 'not found')

while True:
    file_exists = exists(jsonfile)
    if file_exists:
        pass
    else:
        makejson()
    print('q: quit')
    print('s: signup')
    print('l: login')
    print('r: remove account')
    user = input('choose an option: ')
    if user.lower() == 'q' :
        break
    elif user.lower() == 's':
        signup()
    elif user.lower() == 'l':
        login()
    elif user.lower() == 'r':
        removeAcc()
    else:
        print("please type q, s, or l")
        continue
    print('')