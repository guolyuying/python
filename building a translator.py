def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
        translation = translation + "\n"
    return translation
result = translate(input("Enter a phrase: "))
print(result)
