import sys

while True:
    print("tyoe exit to exit")
    response = input()
    if response == "exit":
        sys.exit()
    print("you type" + response + ".")