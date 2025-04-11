import json

class flash_cards:
    def __init__(self, flashcard, answer):
        self.flashcard = flashcard
        self.answer = answer
        flashcard = input("What is your question kid? Type question:")
        answer = input("What is your answer to this question big guy? Type answer:")