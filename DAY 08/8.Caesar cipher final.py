#todo 1
import art
print(art.logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar (message,number,encode_decode):

    output_text = ""
    if encode_decode == 'decode':
        number *= -1
    for letter in message:
        #todo 2
        if letter not in alphabet:
            output_text += letter
        
        shifted_position = alphabet.index(letter) - number
        shifted_position %= len(alphabet) #to keep range btw 0 -25
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_decode}d result: {output_text}")


#todo 3
should_countinue = True
while should_countinue:
   
  direction = input("type 'encode' to encrypt,type 'decode' to deccrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("type the number:\n"))


  caesar(message=text, number=shift, encode_decode=direction)

  restart = input("type 'yes' if you want to go again.Otherwise, type 'no'.\n").lower()
  if restart == "no":
   should_countinue = False
   print("Goodbye")

  