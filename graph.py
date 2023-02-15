import concurrent.futures
import bcrypt
import time
import matplotlib.pyplot as plt

# A list of passwords to hash
passwords = ['password1', 'password2', 'password3', 'password4']

def hash_password(password):
    """Hash a password using bcrypt"""
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

# Record the time it takes to hash all the passwords using different number of processors
number_of_processors = [1, 2, 4, 8, 16]
time_to_hash = []
for n in number_of_processors:
    with concurrent.futures.ThreadPoolExecutor(max_workers=n) as executor:
        start_time = time.time()
        _ = [executor.submit(hash_password, password) for password in passwords]
        end_time = time.time()
        elapsed_time = end_time - start_time
        time_to_hash.append(elapsed_time)

# Plot the results
plt.plot(number_of_processors, time_to_hash, 'ro-')
plt.xlabel("Number of Processors")
plt.ylabel("Time to Hash (seconds)")
plt.title("Impact of Parallelism on Bcrypt")

# Show the plot
plt.show()
