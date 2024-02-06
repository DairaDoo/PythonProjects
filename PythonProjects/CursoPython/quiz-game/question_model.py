class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __str__(self):
        cadena = f"Text: {self.text} | Answer: {self.answer}"
        return cadena
