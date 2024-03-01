alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    shifted_text = ''
    for i in text:
        position = alphabet.index(i)
        shifted_position = position + shift
        if shifted_position > 25:
            shifted_position -= 25
            
        shifted_text += alphabet[shifted_position]
        
    print(f"The encoded text is {shifted_text}")