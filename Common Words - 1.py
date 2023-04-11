words1 = input("Enter First Sentence: ")
words2 = input("Enter Second Sentence: ")
l1, l2, l3 = words1.split(" "), words2.split(" "), []
for word1 in l1:
    for word2 in l2:
        if word1 == word2:
            l3.append(word1)   
l4 = []
for word in l3:
    if word not in l4:
        l4.append(word) 
print(l4)
