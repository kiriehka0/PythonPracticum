a1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
      'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
a2 = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
      '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--',
      '....-', '.....', '-....', '--...', '---..', '----.']
sl = dict(zip(a1, a2))
for x in input().split():
    s = [sl[y.upper()] for y in x]
    print(" ".join(s))
