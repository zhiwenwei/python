_username = 'zww'
_password = '123'
username = input("input your username:")
password = input("input your password:")
if username == _username and password == _password:
    print("welcome user {name} login...".format(name=username))
else:
    print("invalid username or passsword!!!")