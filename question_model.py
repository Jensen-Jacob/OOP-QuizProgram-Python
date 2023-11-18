class Question:
    _id = 0

    def __init__(self, text, answer):
        self.id = Question._id
        Question._id += 1
        self.text = text
        self.answer = answer

    # def __repr__(self):
    #     return f"ID: {self.id}, Question: {self.text}, Answer: {self.answer}"