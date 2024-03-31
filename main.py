# Write a function to convert numbers to text numerals
NUM_WORD = {
  0: 'zero',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
  100: 'hundred',
}
def text_numeral(num):
    """
    Takes in num and returns it in text format

    Parameters:
    num (int): positive integer below 100

    Example:
    text_numeral(15)
    'fifteen'
    """
    if num == 0:
        return "zero"

    result = ""
    for num1, word in sorted(NUM_WORD.items(), reverse=True):
        if num >= num1:
            count = num // num1
            if count > 1:
                result += f"{word} "
            else:
                result += f"{word} "
            num -= num1 * count
            if num == 0:
                break
    return result.strip()
