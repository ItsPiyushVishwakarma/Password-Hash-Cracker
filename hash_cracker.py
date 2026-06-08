import hashlib
import time

print("=" * 40)
print("PASSWORD HASH CRACKER")
print("=" * 40)

target_hash = input("\nEnter the hash to crack: ")

hash_length = len(target_hash)

if hash_length == 32:
    algorithm = "md5"

elif hash_length == 40:
    algorithm = "sha1"

elif hash_length == 64:
    algorithm = "sha256"

elif hash_length == 128:
    algorithm = "sha512"

else:
    print("Unknown hash type!")
    exit()

print(f"\nDetected Algorithm: {algorithm.upper()}")

with open("wordlist.txt", "r") as file:
    wordlist = file.readlines()

attempts = 0
found = False

start_time = time.time()

for word in wordlist:

    word = word.strip()

    attempts += 1

    hash_value = hashlib.new(
        algorithm,
        word.encode()
    ).hexdigest()

    if hash_value == target_hash:

        end_time = time.time()

        print("\n" + "=" * 40)
        print("PASSWORD HASH CRACKER REPORT")
        print("=" * 40)

        print(f"Algorithm : {algorithm.upper()}")
        print(f"Password  : {word}")
        print(f"Attempts  : {attempts}")
        print(
            f"Time      : {end_time - start_time:.4f} seconds"
        )
        print("Status    : SUCCESS")

        print("=" * 40)

        found = True

        break

if not found:

    end_time = time.time()

    print("\n" + "=" * 40)
    print("PASSWORD HASH CRACKER REPORT")
    print("=" * 40)

    print(f"Algorithm : {algorithm.upper()}")
    print(f"Attempts  : {attempts}")
    print(
        f"Time      : {end_time - start_time:.4f} seconds"
    )
    print("Status    : PASSWORD NOT FOUND")

    print("=" * 40)