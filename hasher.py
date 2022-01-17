import random
import hashlib
import time

print("---------- Hasher ALPHA - 1.3 ----------")
print("----- The intuitive Hash Generator -----\n")

hash_type = input("Which type of hashing algorithm do you want to use? ")
hash_select_str = str(hash_type)
hash_wait = input("How many seconds do you want to add to the output wait-time? Please input the value in seconds. ")
hash_wait_int = int(hash_wait)

if hash_select_str == "sha256":

    number1 = random.randint(0, 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number2 = random.randint(0, 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number3 = random.randint(0, 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number4 = random.randint(0, 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number5 = random.randint(0, 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number6 = random.randint(0, 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number7 = random.randint(0, 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number8 = random.randint(0, 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number9 = random.randint(0, 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number10 = random.randint(0, 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)

    encoded1 = bytes(str(number1), 'utf-8')
    encoded2 = bytes(str(number2), 'utf-8')
    encoded3 = bytes(str(number3), 'utf-8')
    encoded4 = bytes(str(number4), 'utf-8')
    encoded5 = bytes(str(number5), 'utf-8')
    encoded6 = bytes(str(number6), 'utf-8')
    encoded7 = bytes(str(number7), 'utf-8')
    encoded8 = bytes(str(number8), 'utf-8')
    encoded9 = bytes(str(number9), 'utf-8')
    encoded10 = bytes(str(number10), 'utf-8')

    sha_result1 = hashlib.sha256(encoded1)
    sha_result2 = hashlib.sha256(encoded2)
    sha_result3 = hashlib.sha256(encoded3)
    sha_result4 = hashlib.sha256(encoded4)
    sha_result5 = hashlib.sha256(encoded5)
    sha_result6 = hashlib.sha256(encoded6)
    sha_result7 = hashlib.sha256(encoded7)
    sha_result8 = hashlib.sha256(encoded8)
    sha_result9 = hashlib.sha256(encoded9)
    sha_result10 = hashlib.sha256(encoded10)

    encoded_twice1 = bytes(str(sha_result1), 'utf-8')
    encoded_twice2 = bytes(str(sha_result2), 'utf-8')
    encoded_twice3 = bytes(str(sha_result3), 'utf-8')
    encoded_twice4 = bytes(str(sha_result4), 'utf-8')
    encoded_twice5 = bytes(str(sha_result5), 'utf-8')
    encoded_twice6 = bytes(str(sha_result6), 'utf-8')
    encoded_twice7 = bytes(str(sha_result7), 'utf-8')
    encoded_twice8 = bytes(str(sha_result8), 'utf-8')
    encoded_twice9 = bytes(str(sha_result9), 'utf-8')
    encoded_twice10 = bytes(str(sha_result10), 'utf-8')

    result1 = hashlib.sha256(encoded_twice1)
    result2 = hashlib.sha256(encoded_twice2)
    result3 = hashlib.sha256(encoded_twice3)
    result4 = hashlib.sha256(encoded_twice4)
    result5 = hashlib.sha256(encoded_twice5)
    result6 = hashlib.sha256(encoded_twice6)
    result7 = hashlib.sha256(encoded_twice7)
    result8 = hashlib.sha256(encoded_twice8)
    result9 = hashlib.sha256(encoded_twice9)
    result10 = hashlib.sha256(encoded_twice10)

    time.sleep(hash_wait_int)

    print("\nHash 1:", result1)
    print("Hash 2:", result2)
    print("Hash 3:", result3)
    print("Hash 4:", result4)
    print("Hash 5:", result5)
    print("Hash 6:", result6)
    print("Hash 7:", result7)
    print("Hash 8:", result8)
    print("Hash 9:", result9)
    print("Hash 10:", result10, "\n")

elif hash_select_str == "sha1":
    number1 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number2 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number3 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number4 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number5 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number6 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number7 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number8 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number9 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number10 = random.randint(0,
                              9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)

    encoded1 = bytes(str(number1), 'utf-8')
    encoded2 = bytes(str(number2), 'utf-8')
    encoded3 = bytes(str(number3), 'utf-8')
    encoded4 = bytes(str(number4), 'utf-8')
    encoded5 = bytes(str(number5), 'utf-8')
    encoded6 = bytes(str(number6), 'utf-8')
    encoded7 = bytes(str(number7), 'utf-8')
    encoded8 = bytes(str(number8), 'utf-8')
    encoded9 = bytes(str(number9), 'utf-8')
    encoded10 = bytes(str(number10), 'utf-8')

    sha_result1 = hashlib.sha1(encoded1)
    sha_result2 = hashlib.sha1(encoded2)
    sha_result3 = hashlib.sha1(encoded3)
    sha_result4 = hashlib.sha1(encoded4)
    sha_result5 = hashlib.sha1(encoded5)
    sha_result6 = hashlib.sha1(encoded6)
    sha_result7 = hashlib.sha1(encoded7)
    sha_result8 = hashlib.sha1(encoded8)
    sha_result9 = hashlib.sha1(encoded9)
    sha_result10 = hashlib.sha1(encoded10)

    encoded_twice1 = bytes(str(sha_result1), 'utf-8')
    encoded_twice2 = bytes(str(sha_result2), 'utf-8')
    encoded_twice3 = bytes(str(sha_result3), 'utf-8')
    encoded_twice4 = bytes(str(sha_result4), 'utf-8')
    encoded_twice5 = bytes(str(sha_result5), 'utf-8')
    encoded_twice6 = bytes(str(sha_result6), 'utf-8')
    encoded_twice7 = bytes(str(sha_result7), 'utf-8')
    encoded_twice8 = bytes(str(sha_result8), 'utf-8')
    encoded_twice9 = bytes(str(sha_result9), 'utf-8')
    encoded_twice10 = bytes(str(sha_result10), 'utf-8')

    result1 = hashlib.sha1(encoded_twice1)
    result2 = hashlib.sha1(encoded_twice2)
    result3 = hashlib.sha1(encoded_twice3)
    result4 = hashlib.sha1(encoded_twice4)
    result5 = hashlib.sha1(encoded_twice5)
    result6 = hashlib.sha1(encoded_twice6)
    result7 = hashlib.sha1(encoded_twice7)
    result8 = hashlib.sha1(encoded_twice8)
    result9 = hashlib.sha1(encoded_twice9)
    result10 = hashlib.sha1(encoded_twice10)

    time.sleep(hash_wait_int)

    print("\nHash 1:", result1)
    print("Hash 2:", result2)
    print("Hash 3:", result3)
    print("Hash 4:", result4)
    print("Hash 5:", result5)
    print("Hash 6:", result6)
    print("Hash 7:", result7)
    print("Hash 8:", result8)
    print("Hash 9:", result9)
    print("Hash 10:", result10, "\n")

elif hash_select_str == "sha512":
    number1 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number2 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number3 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number4 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number5 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number6 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number7 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number8 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number9 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number10 = random.randint(0,
                              9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)

    encoded1 = bytes(str(number1), 'utf-8')
    encoded2 = bytes(str(number2), 'utf-8')
    encoded3 = bytes(str(number3), 'utf-8')
    encoded4 = bytes(str(number4), 'utf-8')
    encoded5 = bytes(str(number5), 'utf-8')
    encoded6 = bytes(str(number6), 'utf-8')
    encoded7 = bytes(str(number7), 'utf-8')
    encoded8 = bytes(str(number8), 'utf-8')
    encoded9 = bytes(str(number9), 'utf-8')
    encoded10 = bytes(str(number10), 'utf-8')

    sha_result1 = hashlib.sha512(encoded1)
    sha_result2 = hashlib.sha512(encoded2)
    sha_result3 = hashlib.sha512(encoded3)
    sha_result4 = hashlib.sha512(encoded4)
    sha_result5 = hashlib.sha512(encoded5)
    sha_result6 = hashlib.sha512(encoded6)
    sha_result7 = hashlib.sha512(encoded7)
    sha_result8 = hashlib.sha512(encoded8)
    sha_result9 = hashlib.sha512(encoded9)
    sha_result10 = hashlib.sha512(encoded10)

    encoded_twice1 = bytes(str(sha_result1), 'utf-8')
    encoded_twice2 = bytes(str(sha_result2), 'utf-8')
    encoded_twice3 = bytes(str(sha_result3), 'utf-8')
    encoded_twice4 = bytes(str(sha_result4), 'utf-8')
    encoded_twice5 = bytes(str(sha_result5), 'utf-8')
    encoded_twice6 = bytes(str(sha_result6), 'utf-8')
    encoded_twice7 = bytes(str(sha_result7), 'utf-8')
    encoded_twice8 = bytes(str(sha_result8), 'utf-8')
    encoded_twice9 = bytes(str(sha_result9), 'utf-8')
    encoded_twice10 = bytes(str(sha_result10), 'utf-8')

    result1 = hashlib.sha512(encoded_twice1)
    result2 = hashlib.sha512(encoded_twice2)
    result3 = hashlib.sha512(encoded_twice3)
    result4 = hashlib.sha512(encoded_twice4)
    result5 = hashlib.sha512(encoded_twice5)
    result6 = hashlib.sha512(encoded_twice6)
    result7 = hashlib.sha512(encoded_twice7)
    result8 = hashlib.sha512(encoded_twice8)
    result9 = hashlib.sha512(encoded_twice9)
    result10 = hashlib.sha512(encoded_twice10)

    time.sleep(hash_wait_int)

    print("\nHash 1:", result1)
    print("Hash 2:", result2)
    print("Hash 3:", result3)
    print("Hash 4:", result4)
    print("Hash 5:", result5)
    print("Hash 6:", result6)
    print("Hash 7:", result7)
    print("Hash 8:", result8)
    print("Hash 9:", result9)
    print("Hash 10:", result10, "\n")

elif hash_select_str == "md5":
    number1 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number2 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number3 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number4 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number5 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number6 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number7 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number8 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number9 = random.randint(0,
                             9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number10 = random.randint(0,
                              9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)

    encoded1 = bytes(str(number1), 'utf-8')
    encoded2 = bytes(str(number2), 'utf-8')
    encoded3 = bytes(str(number3), 'utf-8')
    encoded4 = bytes(str(number4), 'utf-8')
    encoded5 = bytes(str(number5), 'utf-8')
    encoded6 = bytes(str(number6), 'utf-8')
    encoded7 = bytes(str(number7), 'utf-8')
    encoded8 = bytes(str(number8), 'utf-8')
    encoded9 = bytes(str(number9), 'utf-8')
    encoded10 = bytes(str(number10), 'utf-8')

    sha_result1 = hashlib.md5(encoded1)
    sha_result2 = hashlib.md5(encoded2)
    sha_result3 = hashlib.md5(encoded3)
    sha_result4 = hashlib.md5(encoded4)
    sha_result5 = hashlib.md5(encoded5)
    sha_result6 = hashlib.md5(encoded6)
    sha_result7 = hashlib.md5(encoded7)
    sha_result8 = hashlib.md5(encoded8)
    sha_result9 = hashlib.md5(encoded9)
    sha_result10 = hashlib.md5(encoded10)

    encoded_twice1 = bytes(str(sha_result1), 'utf-8')
    encoded_twice2 = bytes(str(sha_result2), 'utf-8')
    encoded_twice3 = bytes(str(sha_result3), 'utf-8')
    encoded_twice4 = bytes(str(sha_result4), 'utf-8')
    encoded_twice5 = bytes(str(sha_result5), 'utf-8')
    encoded_twice6 = bytes(str(sha_result6), 'utf-8')
    encoded_twice7 = bytes(str(sha_result7), 'utf-8')
    encoded_twice8 = bytes(str(sha_result8), 'utf-8')
    encoded_twice9 = bytes(str(sha_result9), 'utf-8')
    encoded_twice10 = bytes(str(sha_result10), 'utf-8')

    result1 = hashlib.md5(encoded_twice1)
    result2 = hashlib.md5(encoded_twice2)
    result3 = hashlib.md5(encoded_twice3)
    result4 = hashlib.md5(encoded_twice4)
    result5 = hashlib.md5(encoded_twice5)
    result6 = hashlib.md5(encoded_twice6)
    result7 = hashlib.md5(encoded_twice7)
    result8 = hashlib.md5(encoded_twice8)
    result9 = hashlib.md5(encoded_twice9)
    result10 = hashlib.md5(encoded_twice10)

    time.sleep(hash_wait_int)

    print("\nHash 1:", result1)
    print("Hash 2:", result2)
    print("Hash 3:", result3)
    print("Hash 4:", result4)
    print("Hash 5:", result5)
    print("Hash 6:", result6)
    print("Hash 7:", result7)
    print("Hash 8:", result8)
    print("Hash 9:", result9)
    print("Hash 10:", result10, "\n")

else:
    print("Please choose a valid algorithm.\n")

save_confirmation = input("Do you want to save the results? (Y)es or (N)o. ")
if save_confirmation is "Y":
    file_write = "Hash 1:", result1, ", Hash 2:", result2, ", Hash 3:", result3, ", Hash 4:", result4, ", Hash 5:", result5, ", Hash 6:", result6, ", Hash 7:", result7, ", Hash 8:", result8, ", Hash 9:", result9, ", Hash 10:", result10
    f = open("HashSave_Hasher.txt", "w")
    f.write(str(file_write))
    f.close()
    print("Saved (in HashSave_Hasher.txt). \n")
elif save_confirmation is "N":
    print("Not saved. \n")
else:
    print("Please input a valid value. \n")

print("Copyright - Kaamadan Studios, 2021\n")
input("Press Enter to Exit")
