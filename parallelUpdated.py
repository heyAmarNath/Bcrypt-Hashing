import bcrypt
import concurrent.futures
import time

# Get the password from the user
password = input("Enter the password to hash: ").encode('utf-8')

# Generate a hash of the password using bcrypt
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)

# Load a dictionary of common passwords
with open('Password List/dummypass.txt') as f:
    passwords = [line.strip().encode('utf-8') for line in f]

# Try to crack the hash using the dictionary with different number of processors
number_of_processors = [1, 2, 4, 8, 16]
time_to_crack = []
for n in number_of_processors:
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=n) as executor:
        for pwd in passwords:
            if bcrypt.checkpw(pwd, hashed_password):
                end_time = time.time()
                elapsed_time = end_time - start_time
                time_to_crack.append(elapsed_time)
                print(f"Password cracked with {n} processors in {elapsed_time:.4f} seconds")
                break


# Print the result
if time_to_crack:
    print(f"Time to crack: {min(time_to_crack):.4f} seconds")
else:
    print("Password not found.")

# Plot the results
import matplotlib.pyplot as plt
plt.plot(number_of_processors, time_to_crack, 'ro-')
plt.xlabel("Number of Processors")
plt.ylabel("Time to Crack (seconds)")
plt.title("Impact of Parallelism on Bcrypt Password Cracking")
plt.show()
