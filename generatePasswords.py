import random
import string


def generatePasswords(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols

    temp = random.sample(all, length)

    password = "".join(temp)

    return password


def main():
    level_dict = {'low': 10, 'middle': 14, 'high': 18}

    while True:

        level = input(
            "Choose your password security level: [low - middle - high] or exit ")
        if level.lower() == 'exit':
            break
        elif (level == "low"):
            lenght = level_dict['low']
            print(generatePasswords(lenght))
        elif (level == "middle"):
            lenght = level_dict['middle']
            print(generatePasswords(lenght))
        elif (level == "high"):
            lenght = level_dict['high']
            print(generatePasswords(lenght))
        else:
            print('Input error.')


if __name__ == "__main__":
    main()
