


def main ():
    iconFileName = 'icons.txt'
    with open(iconFileName, "r") as iconFD:
        line = iconFD.read()
        print(line)
    return True

if __name__ == "__main__":
    main()
