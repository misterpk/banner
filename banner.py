
if __name__ == "__main__":
    name = input("Enter your name: ")
    banner = ""

    for i in range(len(name) + 4):
        banner += "*"

    print(banner)
    print("* " + name + " *")
    print(banner)
