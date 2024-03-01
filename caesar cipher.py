import art
import alphabet

letter = alphabet.alphabet

print(art.logo)
play_again = True
while play_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode" or direction == "decode":
        
        def caesar(text,shift,direction):
            shifted_text = ""
            for i in text:
                if i in letter:
                    position = letter.index(i)
                    if shift > 26:
                        new_shift= shift % 26
                    else:
                        new_shift = shift
        
                    if direction == "encode":
                        shifted_position = position + new_shift
                        if shifted_position > 25:
                            shifted_position -= 26
                        
                    elif direction == "decode":
                        shifted_position = position - new_shift
                        if shifted_position < 0:
                            shifted_position + 26
                                
                    shifted_text += letter[shifted_position]
                else:
                    shifted_text += i
                
            print(f"The {direction}d text is {shifted_text}.")
        
        caesar(text,shift,direction)
    else: 
        print(f"The inputted text is {direction}, whicth is not accepted.\nplease enter a valid input.")

    play = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if play == "yes":
        play_again == True
    elif play == "no":
        play_again == False
        print("Goodbye!")
    else:
        print("please enter a valid input.")