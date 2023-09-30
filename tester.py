# Enter your code here. Read input from STDIN. Print output to STDOUT
numPeople = int(input())
phoneBook = {}
for i in range(numPeople):
    name, number = input().split(" ")
    phoneBook[name] = number

empty = False
while(empty == False):
    try:
        check = input()
    except EOFError:
        print("EOF")
        break

    if check in phoneBook:
        print(check + "=" + phoneBook[check])
    else:
        print("Not found")
