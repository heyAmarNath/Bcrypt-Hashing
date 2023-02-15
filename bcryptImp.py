import bcrypt
import time
import random

# Generate a random numeric password and check the time required by brute force to crack
digit =  int(input("Number of digit: "))
firstValue = 10**(digit-1)
lastValue = (10**digit)-1

rand = str(random.randint(firstValue,lastValue))
print('Random number is: ', rand)
userPass = rand.encode()

start = time.time()

for pwd in range(firstValue,lastValue,1):
  encodedPass = str(pwd).encode()
  salt = bcrypt.gensalt(rounds=12)
  # print(salt)
  hashed = bcrypt.hashpw(encodedPass, salt)
  # print(hashed)
  if(bcrypt.checkpw(userPass, hashed)):
    break
  # print(bcrypt.checkpw(userPass, hashed), pwd)

end = time.time()

print("Time required to crack ",end - start)

print(hashed)