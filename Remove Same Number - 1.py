value = input("Enter Numbers using commas: ")
value_list = value.split(",")
value_list = [int(x) for x in value_list]  # convert each element to an integer
value_list.sort(reverse=False)

i = 0
while i < len(value_list):
    j = i + 1
    while j < len(value_list):
        if value_list[i] == value_list[j]:
            value_list.pop(j)
        else:
            j += 1
    i += 1

print(value_list)
