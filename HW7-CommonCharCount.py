def common_letters(string1, string2):
    string1 = input(">")
    string2 = input(">")

    s1 = set(string1)
    s2 = set(string2)

    common_char = s1 & s2

    return len(common_char)

print(common_letters(0,0))