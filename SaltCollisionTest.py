# Import the BCrypt library
import bcrypt

# Generate two random passwords
password1 = "password1"
password2 = "password2"
collide = False
count = 0
# Generate a random salt
while collide!=True and count==100:
    salt = bcrypt.gensalt()

    # Hash the passwords using the same salt
    hash1 = bcrypt.hashpw(password1.encode('utf-8'), salt)
    hash2 = bcrypt.hashpw(password2.encode('utf-8'), salt)
    
   
    # Compare the resulting hashes
    if hash1 == hash2:
        print("Salt collision detected!")
        collide = True
    else:
        count+=1
        print("Salt collision not detected. " ,count)
