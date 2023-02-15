import bcrypt
import time
import concurrent.futures

# Get the password from the user
pas = input("Enter the password to hash: ")
password = pas.encode('utf-8')

# Generate a hash of the password using bcrypt
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)

# Load a dictionary of common passwords
with open('Password List/dummypass.txt') as f:
    passwords = [line.strip() for line in f]

# Record the time taken to crack the password using different number of processors
number_of_processors = [1, 2, 4, 8, 16]
time_to_crack = []
for n in number_of_processors:
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=n) as executor:
        for pwd in passwords:
            future = executor.submit(bcrypt.checkpw, pwd.encode('utf-8'), hashed_password)
            if future.result():
                print(f'Password found: {pwd}')
                break
    end_time = time.time()
    elapsed_time = end_time - start_time
    time_to_crack.append(elapsed_time)
    print(f'Time taken to crack password with {n} processor(s): {elapsed_time:.2f} seconds')

# Plot the results
import matplotlib.pyplot as plt
plt.plot(number_of_processors, time_to_crack, 'ro-')
plt.xlabel("Number of Processors")
plt.ylabel("Time to Crack (seconds)")
plt.title("Impact of Parallelism on Bcrypt")

# Show the plot
plt.show()
