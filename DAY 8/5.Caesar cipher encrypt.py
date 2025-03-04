alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("type 'encode' to encrypt,type 'decode' to deccrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("type the number:\n"))

#FOR ENCODE
#todo 1
def encrypt(message,number):
    #todo 2
    cipher_text = ""
    for letter in message:
        if letter in alphabet:
           shifted_position = alphabet.index(letter) + number
           shifted_position %= len(alphabet) #to keep range btw 0 -25
           cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter
    print(f"Here is the encoded result: {cipher_text}")
    
#todo 3
encrypt(message=text, number=shift)



