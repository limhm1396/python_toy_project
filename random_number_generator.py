import string
import secrets

data = string.ascii_letters + string.digits + string.punctuation
password_length = 16
password = ''.join(secrets.choice(data) for i in range(password_length))
print(password)