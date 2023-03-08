#!/usr/bin/python3
'''writing to a file'''


def write_file(filename="", text=""):
    '''1wirtes to a file'''
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)


if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)