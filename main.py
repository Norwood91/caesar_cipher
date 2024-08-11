from alphabet import alphabet

alphabet_list = alphabet


def caesar_cipher(original_text, shift_amount, direction):
    output = ''

    if direction == 'decode':
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output += letter
        else:
            swapped_index = alphabet.index(letter) + shift_amount
            swapped_index %= len(alphabet)
            output += alphabet[swapped_index]
    print(f"The {direction}d text is: {output}")


def run_program():
    running = True
    while running:

        direction = input("Type encode to encrypt a message, or decode to decrypt a message:\n").lower()
        user_input = input("Please type a message:\n").lower()
        shift_amount = int(input("How far do you want the letters shifted? (Type a number. 1, 2, 3, etc.):\n"))

        caesar_cipher(original_text=user_input, shift_amount=shift_amount, direction=direction)

        restart_cipher = input(
            "Would you like to encode or decode another message? If yes, type 'yes', if no, type 'no'"
            "to exit:\n").lower()
        if restart_cipher == 'no':
            running = False
            print("Thanks for using the program, goodbye!")


if __name__ == "__main__":
    run_program()
