romans = {
    "1": "I",
    "2": "II",
    "3": "III",
    "4": "IV",
    "5": "V",
    "6": "VI",
    "7": "VII",
    "8": "VIII",
    "9": "IX",
    "10": "X",
    "40": "XL",
    "50": "L",
    "60": "LX"

}
number = int(input("Enter Your Number: "))
if number in range(1, 11):
    rom_num = romans.get(str(number))
    print(rom_num)

elif number in range(11, 40):
    rom_num = ((number // 10)*(romans.get("10"))) + \
        romans.get(str(number % 10))
    print(rom_num)

elif number in range(40, 50):
    rom_num = romans.get("40") + romans.get(str(number - 40))
    print(rom_num)

elif number in range(50, 60):
    rom_num = romans.get("50") + romans.get(str(number - 50))
    print(rom_num)

elif number in range(60, 70):
    rom_num = romans.get("60") + romans.get(str(number - 60))
    print(rom_num)
