s = input("Enter a string value: ")
Text = {}

for ch in s:
    if ch in Text:
        Text[ch] += 1
    else:
        Text[ch] = 1

    result = -1

    for ch in s:
        if Text[ch] == 1:
            result = ch
            break

print(result)        