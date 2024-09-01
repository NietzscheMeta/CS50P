def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[2:].isupper() and s[2:].isalpha() and s[:2].isdigit() and len(s) >= 2 and len(s) <= 6 and not s[:2].startswith("0"):
        return True
    else:
        return False
    ...


main()
