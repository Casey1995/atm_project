import getpass as p
import db

def loginAuth(username,password):
  attemps = 3
  #print('Welcome to Login page!')
  #usern = input('Enter username: ')
  #paswd = p.getpass(prompt='Enter password: ')
  user_name, passwd = db.query_db(db.login_query,username,password)[0]
  while True:
    if username.lower() == user_name and password == passwd:
      print('Your login was successful')
      return True
    else:
      attemps = attemps - 1
      print('Wrong credential entered. You have {} login attempts left'.format(attemps))
      usern = input('Enter username again: ')
      paswd = p.getpass(prompt='Enter password again: ')
      if attemps <= 1:
        print('Your account is locked out.')
        return False
