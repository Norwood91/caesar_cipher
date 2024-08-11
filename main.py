from alphabet import  alphabet

alphabet_list = alphabet

def caesar_cipher(original_text, shift_amount, direction):

    # variable to store the cipher
    output = ''

    # if direction is equal to decode, then multiply the shift amount by -1. This is basically switching
    # positive numbers to negative and vice versa
    if direction == 'decode':
        shift_amount *= -1

    # Loop over the passed in text value
    for letter in original_text:
        if letter not in alphabet:

            # If letter or symbol not in alphabet list, add that to the output variable
            output += letter
        else:
            # get the index number of the current letter in the loop and add that index number to the shift amount
            # Again, swapped index is going to be a number
            swapped_index = alphabet.index(letter) + shift_amount

            # Reassign swapped index with the current number in swapped_index modulo by the length of the alphabet list
            # This will make sure we don't run into the out of range error, and it will return the same number that was
            # previously stored inside of swapped_index
            swapped_index %= len(alphabet)

            # Finally, we are passing the swapped_index to the alphabet list in order to get the letter that is stored
            # at the passed in index, and we are adding that letter to the output variable.
            output += alphabet[swapped_index]
    print(f"The {direction}d text is: {output}")

running = True
while running:

    # Ask user for input
    direction = input("Type encode to encrypt a message, or decode to decrypt a message:\n").lower()
    user_input = input("Please type a message:\n").lower()
    shift_amount = int(input("How far do you want the letters shifted? (Type a number. 1, 2, 3, etc.):\n"))

    caesar_cipher(original_text=user_input, shift_amount=shift_amount, direction=direction)



