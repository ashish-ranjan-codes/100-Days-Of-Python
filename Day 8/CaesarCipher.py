# Let's build Caesar Cipher

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# function to operate
def encode_or_decode(text, shift, direction):
        cipher_text = ''
        for ch in text:
            if ch in alphabet:
                position = alphabet.index(ch)
                if direction == 'encode':
                    position = (position+shift)%26
                else:
                    position = (position-shift)%26
                cipher_text += alphabet[position]
        
        print(f"Hey! Your {direction}d text is {cipher_text}.")

should_continue = True

while should_continue:
    direction = input("\nType 'Encode' to encript and 'Decode' to decrypt: ").lower()
    if direction == 'encode' or direction == 'decode':
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))
        encode_or_decode(text, shift, direction)
    else:
        print("Sorry! Wrong input.")

    restart = input("\nWant to continue? Yes or No: ").lower()
    if restart == 'no':
         should_continue = False
    
