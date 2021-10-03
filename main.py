ca = 0  # first option
cb = 0  # second option
cn = 0  # neutral

num = int(input("enter the number of voters : "))
print("Enter two options for voting")
option1 = input()
option2 = input()

if option1[0] == option2[0]:
    print(
        f"enter {option1[0]} for {option1} and {option2[0:2]} for {option2} and anykey for neutral")

    for _ in range(num):
        choice = input("Enter your choice:")
        if choice == option1[0]:
            ca += 1
        elif choice == option2[0:2]:
            cb += 1
        else:
            cn += 1


else:
    print(
        f"enter {option1[0]} for {option1} and {option2[0]} for {option2} and anykey for neutral")
    for _ in range(1, num+1):
        choice = input("Enter your choice:")
        if choice == option1[0]:
            ca += 1
        elif choice == option2[0]:
            cb += 1
        else:
            cn += 1
# for typos nothing important ig
if ca == 0 or ca == 1:
    print(f"{option1} got {ca} vote")
else:
    print(f"{option1} got {ca} votes")

if cb == 0 or ca == 1:
    print(f"{option2} got {ca} vote")
else:
    print(f"{option2} got {cb} votes")


if cn == 0 or cn == 1:
    print(f"{cn} vote is not in any side")
else:
    print(f"{cn} votes is not in any side")
