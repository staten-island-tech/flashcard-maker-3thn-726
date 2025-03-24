import json

class flashcards:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def display(self):
        print(self.question, self.answer)

techer_or_student = input("techer or studnet mode(t or s):")
if techer_or_student == "t":
    class student:
elif techer_or_student == "s":
    class teacher:
        
else: print("Error")
