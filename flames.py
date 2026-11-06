name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

# Convert names to lowercase and remove spaces
name1 = name1.replace(" ", "").lower()
name2 = name2.replace(" ", "").lower()

# Remove common letters
for letter in name1[:]:
    if letter in name2:
        name1 = name1.replace(letter, "", 1)
        name2 = name2.replace(letter, "", 1)

# Count remaining letters
count = len(name1 + name2)

flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

# FLAMES logic
while len(flames) > 1:
    index = (count % len(flames)) - 1

    if index >= 0:
        right = flames[index + 1:]
        left = flames[:index]
        flames = right + left
    else:
        flames = flames[:len(flames) - 1]

# Final result
print("Relationship status:", flames[0])