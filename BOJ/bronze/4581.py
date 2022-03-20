
while True:
    vote = input()
    if vote == "#":
        break
    if vote.count("A") >= len(vote)/2:
        print("need quorum")
    else:
        if vote.count("Y") > vote.count("N"):
            print("yes")
        elif vote.count("Y") < vote.count("N"):
            print("no")
        elif vote.count("Y") == vote.count("N"):
            print("tie")


