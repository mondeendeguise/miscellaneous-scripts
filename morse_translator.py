morse_code = {
  'A' : '.-',
  'B' : '-...',
  'C' : '-.-.',
  'D' : '-..',
  'E' : '.',
  'F' : '..-.',
  'G' : '--.',
  'H' : '....',
  'I' : '..',
  'J' : '.---',
  'K' : '-.-',
  'L' : '.-..',
  'M' : '--',
  'N' : '-.',
  'O' : '---',
  'P' : '.--.',
  'Q' : '--.-',
  'R' : '.-.',
  'S' : '...',
  'T' : '-',
  'U' : '..-',
  'V' : '...-',
  'W' : '.--',
  'X' : '-..-',
  'Y' : '-.--',
  'Z' : '--..',
	' ' : '+'
  }

def translate(phrase):
  out = ("")
  for n in range(len(str(phrase))):
    out += f"{morse_code[phrase[n].upper()]}/"
  return out


def main():
  while True:
      usr_phrase = input(":")
      print(translate(usr_phrase))
if __name__ == '__main__':
  main()
