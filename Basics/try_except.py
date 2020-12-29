
while True:
    try:
        num = int(input("What's your fav number?\n"))
        print("Your fav number is:- ", num)
        break

    except ValueError:
        print("Please enter valid number!")

    # finally:
    #     print("End of loop!")
