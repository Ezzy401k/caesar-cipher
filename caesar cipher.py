import art
import alphabet

letter = alphabet.alphabet

print(art.logo)
# looping parameter.
play_again = True
# if the looping parameter remains True after the run do it again.
while play_again:
    # Accept users input.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = input("Type the shift number:\n")

    # check if the user has inputted a number.
    if shift.isnumeric() == True:
        shift = int(shift)

        # if the user input correctly continue else inform them.
        if direction == "encode" or direction == "decode":
            # defining a new function that dose the cipher.
            def caesar(text,shift,direction):
                # create an empty string.
                shifted_text = ""
            
                # loop through the inputed text.
                for i in text:
                    # if i is in the letter module.
            
                    if i in letter:
                        # grab the position of the character in the letter array.
                        position = letter.index(i)
                        # if the inputted shift is greater than 26 calculate the reminder and use it as the new shift.
            
                        if shift > 26:
                            new_shift= shift % 26
            
                        else:
                        # if its less than 26 dont change it.
                            new_shift = shift
            
                        # if the user wants to encode use this.
                        if direction == "encode":
                            # grab the new position by suming the shift with the old position.
                            shifted_position = position + new_shift
                            
                            # if the shift is greater 26 loop to the start.
                            if shifted_position > 25:
                                shifted_position -= 26
                        
                        # if the user wants to decode use this.
                        elif direction == "decode":
                            shifted_position = position - new_shift
                            if shifted_position < 0:
                                shifted_position += 26
                        
                        # the new text,
                        shifted_text += letter[shifted_position]
                    else:

                        # if there are non alphabetic characters dont touch them.
                        shifted_text += i
                    
                # print the final output.
                print(f"The {direction}d text is {shifted_text}.")
            
            # calling the function.
            caesar(text,shift,direction)

        # if a wrong input is inputted show this.
        else: 
            print(f"The inputted text is {direction}, whicth is not accepted.\nplease enter a valid input.")
    else:
        print("please enter a number.")
    # ask the user if they want to go again.
    play = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    # if the user wants to stop.
    if play == "no":
        play_again == False
        print("Goodbye!")
    # if the user inputter a wrong parameter.
    else:
        print("please enter a valid input.")