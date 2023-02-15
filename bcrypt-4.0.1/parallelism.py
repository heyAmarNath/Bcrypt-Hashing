import pbkdf2_sha256

# Set the number of threads to use for parallelism
pbkdf2_sha256.set_num_threads(4)

# Hash the password with a salt and specified number of iterations
hashed_password = pbkdf2_sha256.encrypt("password", salt="salt", rounds=12000)

print(hashed_password)
