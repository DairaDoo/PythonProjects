from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # empty string that will receive all objects of question data.


# for each loop to iterate over each element in questionData, create an object of Question and append it to the list.
for question in question_data:
    question_bank.append(Question(question['question'], question['correct_answer']))


# pass question_bank to quiz brain
quizBrain = QuizBrain(question_bank)

while quizBrain.still_has_question():
    quizBrain.next_question()

print(f"You've completed the quiz")
print(f"Your final score was: {quizBrain.score}/{quizBrain.question_number}")
