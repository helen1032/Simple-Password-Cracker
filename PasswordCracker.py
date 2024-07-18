import hashlib

pass_filename = "Ashley-Madison.txt"

password = "booomer"

enc_password = password.encode("utf-8")

# changing the password into a hash
# websites don't save your actual password, they save it in a hash
password_hash = hashlib.md5(enc_password.strip()).hexdigest()
# the strip() removes any spaces after or line spaces

print(password_hash) # output: 12a5d54e6814c118b91874731352439a

pass_file = open(pass_filename, "r") # permissions set to read

for word in pass_file:
    enc_word = word.encode("utf-8")
    enc_hash = hashlib.md5(enc_word.strip()).hexdigest()

    if password_hash == enc_hash:
        print("This three-letter agency has been hacked. The password was " + word)
        quit()

print("The three-letter agency has a strong password")
