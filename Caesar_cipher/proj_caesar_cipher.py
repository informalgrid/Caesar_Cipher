# todo's 
# 1.create a function called 'encrypt() that takes 'orignal_text' and 
# shift_amount as 2 inputs
# 2.indside the 'encrypt' function. shift each letter of the orignal_text
#  forwards in the alphabet by the shift 
# amount and print the encrypted text.
# 3. what will happen if you shift letter z and how will you encounter it #

alphabets =["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def caeser(orignal_text, shifting_amount, encode_or_decode):


    cipher_value = ""
    if encode_or_decode =="decode":
            shifting_amount *= (-1)
    for letter in orignal_text:

        if letter not in alphabets:
             cipher_value +=letter

        else:

            shifted_value = alphabets.index(letter) + shifting_amount
            shifted_value %= len(alphabets)
            cipher_value += alphabets[shifted_value]

    print(cipher_value)

should_continue = True

while should_continue:


    intention = input("Type 'decode' if you want to decode and type 'encode if you want to Encode:\n").lower()
    message = input("Enter your message:\n").lower()
    shift = int(input("Enter shifting value: \n"))

    caeser(message, shift, intention)

    conti_nue = input("Type yes if you want to continue and type no if you want to quit : \n")

    if conti_nue == "no":
         should_continue= False
         print("goodbye")

    