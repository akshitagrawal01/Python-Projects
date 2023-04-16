def design(values):
    for items in values:
        output = ""
        for value in range(items):
            output += "x"
        print(output)


design(values=[5, 1, 3, 1, 1])
