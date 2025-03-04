alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("type 'encode' to encrypt,type 'decode' to deccrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("type the number:\n"))

#FOR DECODE
#todo 1
def decrypt (message,number):
    #todo 2
    output_text = ""
    for letter in message:
        if letter in alphabet:
           shifted_position = alphabet.index(letter) - number
           shifted_position %= len(alphabet) #to keep range btw 0 -25
           output_text += alphabet[shifted_position]
        else:
            output_text_text += letter
    print(f"Here is the decoded result: {output_text}")

decrypt(message=text, number=shift)


