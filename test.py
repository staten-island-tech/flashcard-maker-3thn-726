import json

mode = input("Are you a teacher or a student ")

class teachers():
    def make_flashcards():
        p = {}
        while True:
            a = input("Do you want to make a question? ")
            if a.lower() == "yes":
                question = input("What is your question mud? ")
                answer = input("What is your answer big boy? ")
                p[question] = answer

            elif a.lower() == "no":
                print("Shoo rat you stink of poor")
                break
            
            else:
                print("Lock dafuq in twin time to study")
        with open("FlashCards.json", "w") as file:
            json.dump(p, file, indent=4)
            
           




if mode.lower() == "teacher":
    teachers.make_flashcards()
