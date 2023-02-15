# # import concurrent.futures
# # import bcrypt

# # def encrypt_password(password):
# #     salt = bcrypt.gensalt()
# #     hashed_password = bcrypt.hashpw(password.encode(), salt)
# #     return hashed_password

# # def encrypt_passwords_in_parallel(passwords):
# #     with concurrent.futures.ThreadPoolExecutor() as executor:
# #         results = [executor.submit(encrypt_password, password) for password in passwords]
# #         return [result.result() for result in results]

# # passwords = ["password1", "password2", "password3", "password4"]
# # encrypted_passwords = encrypt_passwords_in_parallel(passwords)

# import time
# import bcrypt
# import concurrent.futures

# def normal_bcrypt(password):
#     salt = bcrypt.gensalt()
#     hashed_password = bcrypt.hashpw(password.encode(), salt)
#     return hashed_password

# def parallel_bcrypt(password):
#     salt = bcrypt.gensalt()
#     hashed_password = bcrypt.hashpw(password.encode(), salt)
#     return hashed_password

# def encrypt_passwords_in_parallel(passwords):
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         results = [executor.submit(parallel_bcrypt, password) for password in passwords]
#         return [result.result() for result in results]

# passwords = ["password1", "password2", "password3", "password4"]

# start_time = time.time()
# encrypted_passwords_normal = [normal_bcrypt(password) for password in passwords]
# normal_time = time.time() - start_time

# start_time = time.time()
# encrypted_passwords_parallel = encrypt_passwords_in_parallel(passwords)
# parallel_time = time.time() - start_time

# print("Normal bcrypt time: ", normal_time)
# print("Parallel bcrypt time: ", parallel_time)


import time
import bcrypt
import concurrent.futures

def normal_bcrypt(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

def parallel_bcrypt(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

def encrypt_passwords_in_parallel(passwords):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(parallel_bcrypt, password) for password in passwords]
        return [result.result() for result in results]

def read_passwords_from_file(file_path):
    with open(file_path, 'r') as file:
        passwords = file.read().splitlines()
    return passwords

passwords = read_passwords_from_file("passwords.txt")

# start_time = time.time()
# encrypted_passwords_normal = [normal_bcrypt(password) for password in passwords]
# normal_time = time.time() - start_time
# print("Normal bcrypt time: ", normal_time)

start_time = time.time()
encrypted_passwords_parallel = encrypt_passwords_in_parallel(passwords)
parallel_time = time.time() - start_time

print("Parallel bcrypt time: ", parallel_time)
