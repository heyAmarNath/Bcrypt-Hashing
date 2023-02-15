import bcrypt
# Get the password from the user
pas = input("Enter the password to hash: ")
password = pas.encode('utf-8')

# Generate a hash of the password using bcrypt
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)

# Load a dictionary of common passwords
with open('Password List/dummypass.txt') as f:
    passwords = [line.strip() for line in f]

# Try to crack the hash using the dictionary
for pwd in passwords:
    if bcrypt.checkpw(pwd.encode('utf-8'), hashed_password):
        print(f'Password found: {pwd}')
        break
else:
    print('Password not found')
