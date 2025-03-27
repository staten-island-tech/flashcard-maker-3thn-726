import json
mode = input("Are you a techer or a studient? Type answer in t or s:")

class teachers():
    def make_flashcards():
        p = {}
        while True:
            a = input("Do you want to make a question? Answer Yes or No:")
            if a.lower() == "yes":
                question = input("What is your question kid? Type question:")
                answer = input("What is your answer to this question big guy? Type answer:")
                p[question] = answer
            elif a.lower() == "no":
                for i in range(0, 100):
                    print("GEEEEEEEEEEEEEETTTTTTTT OUUUUUUUUUUTTTT")
                break
            else:
                print("lck da hl n twin, time to stoooooooooooooooooooddddy for AP reeeerick.")
                print("Y u steal no stooody, no ricse fo u toonite")
        with open("FlashCards.json", "w") as file:
            json.dump(p, file, indent=4)

class studient():
    def stuient_card():
        sthrek = 0
        poent = 0
        corrrrret = 0
        with open("FlashCards.json", "r") as fs:
            flashcards = json.load(fs)
        for card in flashcards:
            print(card)
            a = input("Wat da anser?:")
            if a == flashcards[card]:
                poent = poent + 1
                sthrek = sthrek + 1
                print("correct")
                print("points:", poent)
                print("shrek:", sthrek)
                corrrrret = corrrrret + 1
                print("Corrrrrect answers so far:", corrrrret)
                if sthrek > 5:
                    poent = poent + 1
            else:
                print("u dum dum")
                sthrek = sthrek - sthrek
                quit = input("do u wanna to reset?:")
                if quit.lower == ("yes"):
                    sthrek = 0
                    poent = 0
                    corrrrret = 0
                    

                

if mode.lower() == "t":
    teachers.make_flashcards()
elif mode.lower()== "s":
    studient.stuient_card()
else:
    for i in range(0, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
        print("I gv u so ezy nstrukshuns, y u so dum")