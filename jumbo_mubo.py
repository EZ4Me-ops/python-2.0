import random

def jumble_up(word):
    wordlist=list(word)
    random.shuffle(wordlist)
    return "".join(wordlist)

camp_cretaceous=["trex","baryonyx","branchiosaurus","spinosaurus","indominourex","Scorpiosrex"]

for round_number in range(5):

    selected=random.choice(camp_cretaceous)
    jumbled=jumble_up(selected)
    print("round",round_number+1)
    answer=input("here is the scrambled word "+jumbled)

    if answer == selected:
        print("good job beta you are not a faliure yaya ")
    else:
        print("i knew you were a faliure the correct word was"+selected)