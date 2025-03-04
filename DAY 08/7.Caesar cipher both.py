alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("type 'encode' to encrypt,type 'decode' to deccrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("type the number:\n"))

def caesar (message,number,encode_decode):

    output_text = ""
    for letter in message:
        if encode_decode == 'decode':
            number *= -1
        
        shifted_position = alphabet.index(letter) - number
        shifted_position %= len(alphabet) #to keep range btw 0 -25
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_decode}d result: {output_text}")

caesar(message=text, number=shift, encode_decode=direction)
