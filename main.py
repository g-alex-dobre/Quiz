from question_model import Question
from data import question_data
from quiz_brain import Quizz_brain
question_bank = []


for item in question_data:
  question_bank.append(Question(item["text"],item["answer"]))

quiz = Quizz_brain(question_bank)

while quiz.quiz_still_has_questions():
  quiz.nextquestion()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{len(question_bank)}")
