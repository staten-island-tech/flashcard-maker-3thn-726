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
    def stuient_game():
        sthrek = 0
        poent = 0
        corrrrret = 0
        with open("FlashCards.json", "r") as fs:
            json.load(fs)

if mode.lower() == "t":
    teachers.make_flashcards()
elif mode.lower()== "s":
    studient.studient_game()
else:
    for i in range(0, 10):
        print("I gv u so ezy nstrukshuns, y u so dum")