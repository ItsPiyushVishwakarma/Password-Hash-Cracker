import hashlib

print("1. MD5")
print("2. SHA1")
print("3. SHA256")
print("4. SHA512")

choice = input("Select the hashing algorithm (1-4): ")

attempts = 0

if choice == '1':
    algorithm = 'md5'
elif choice == '2':
    algorithm = 'sha1'
elif choice == '3':
    algorithm = 'sha256'
elif choice == '4':
    algorithm = 'sha512'
else:
    print("Invalid choice.")
    exit()

print(f"Selected algorithm: {algorithm}")

target_hash = input("Enter the hash to crack: ")
print("Target Hash:", target_hash)

wordlist = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "abc123",
    "letmein",
    "monkey",
    "dragon",
    "111111",
    "baseball",
    "hello",
    "welcome",
    "admin",
    "login",
    "cybersecurity",
    "iloveyou"
]

found = False

for word in wordlist:

    hash_value = hashlib.new(
        algorithm, 
        word.encode()
        ).hexdigest()
    
    if hash_value == target_hash:

        print(f"Password found: {word}")
        found = True
        break

    if not found:
        print("Password not found in the wordlist.")

