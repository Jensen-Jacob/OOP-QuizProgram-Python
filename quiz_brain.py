class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0
        self.lives = 3

    def still_has_questions(self):
        if self.lives > 0:
            return self.question_number < len(self.question_bank)

    def next_question(self):
        question = self.question_bank[self.question_number]
        self.question_number += 1
        while True:
            try:
                user_answer = input(f"Q.{self.question_number}: {question.text} (True/False): ").capitalize()
                if user_answer != "True" and user_answer != "False":
                    raise Exception("Please answer 'True' or 'False'")
                else:
                    break
            except Exception as e:
                print(e)
        if user_answer == question.answer:
            self.score += 1
            print(f"Correct! Your score: {self.score}/{self.question_number}\nLives remaining: {self.lives}\n")
        else:
            self.lives -= 1
            print(f"Oops, that was wrong. Your score: {self.score}/{self.question_number}")
            print(f"The correct answer was: {question.answer}\nLives Remaining: {self.lives}\n")