def int_to_roman(num):
    values = [1, 4, 5, 9, 10, 40, 50, 90, 100]
    roman_numeral = {
        "1": "I",
        "4": "IV",
        "5": "V",
        "9": "IX",
        "10": "X",
        "40": "XL",
        "50": "L",
        "90": "XC",
        "100": "C",
        "400": "CD",
        "500": "D",
        "900": "CM",
        "1000": "M"
    }
    
    smaller_numbers = [n for n in values if n < num]
    if smaller_numbers:
        smaller = max(smaller_numbers)
    else:
        smaller = 1
    
    roman_numeral_str = roman_numeral[str(smaller)] * (num // smaller)
    if num % smaller > 0:
        roman_numeral_str += int_to_roman(num % smaller)
    return roman_numeral_str

number = int(input("Enter your number: "))
roman_numeral = int_to_roman(number)
print(roman_numeral)
