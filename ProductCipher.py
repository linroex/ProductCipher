def main():
    key = '15,11,19,18,16,03,07,14,02,20,04,12,09,06,01,05,17,13,10,08'
    plain_text = 'distributed anonymous'.replace(' ','')
    encrypted_text = list(plain_text)

    key = key.split(',')

    for index, char in enumerate(plain_text):
        new_index = key.index(str(index + 1).zfill(2))
        # print(new_index + 1)
        # encrypted_text += plain_text[new_index]
        encrypted_text[new_index] = char
        # encrypted_text[index] = 1

        # print(index)
    encrypted_text = "".join(encrypted_text)

    print(encrypted_text.upper())

if __name__ == '__main__':
    main()