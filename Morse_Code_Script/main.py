# The purpose of this code is to quickly convert a sentence put in by the user
# into morse code. Currently there are only letters, numbers, and some special characters.

# The morse code for each letter/number is put into a dictionary set.
# To expand the amount of letters/characters that can be put into code for, simply create
# another pair into the MORSE_CODE set.
#   {LETTER/CHARACTER}: {MORSE CODE FORM}
# MORSE_CODE is constant as it won't be changed during runtime.
MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.', '0': '-----',
              '?': '..--..', '!': '-.-.--', '.': '.-.-.-', ',': '--..--', ';': '-.-.-.', ':': '---...',
              '+': '.-.-.', '-': '-....-', '/': '-..-.', '=': '-...-', ' ': '/'}

running = True

print('-. MORSE CODE CONVERTER .-')
print('To begin using the morse code converter, simply type the sentence you want to convert into morse code.')
print('Type x to exit.')

# Making this statement into a 'while true' statement instead of a 'while running' statement would
# work in this program. Since I consider it as bad practice to have a loop with a constant condition
# that cannot be changed during runtime, I stored the condition into a boolean.
while running:
    print('___________')
    converted_text = ''
    normal_text = input('INPUT: ')

    # In order to leave the loop, the user has to type x into the chat. This can result a problem when the user
    # wants to find the morse code for just 'x' but that isn't too much of a problem. Another thing to note is that
    # in order for this to work properly, the exit condition must be checked before the elif. This is because the x
    # will be converted to morse code if the conversion if-block came before the exit if-block.
    if normal_text.upper() == 'X':
        running = False
        break
    elif normal_text != '':

        # This is where the conversion takes place. The character in the variable 'normal_text', is used as a key
        # to find the correct code in the MORSE_CODE array.
        for character in normal_text:
            converted_text += (MORSE_CODE[character.upper()] + ' ')

    print(converted_text)