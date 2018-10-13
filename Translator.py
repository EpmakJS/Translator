def translate(phrase):
    translation = ""

    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "V"
            else:
                translation += "v"
        else:
            translation += letter

    return translation

print(translate(input("Enter a word: ")))