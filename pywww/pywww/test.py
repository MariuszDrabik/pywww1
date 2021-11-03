from os import environ

SECRET_KEY = environ.get('pywww1')

print(SECRET_KEY)