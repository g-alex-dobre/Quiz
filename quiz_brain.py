class Quizz_brain:
  
  def __init__(self,question_bank):
    self.question_list = question_bank
    self.question_number = 0
    self.score = 0
  
  def nextquestion(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    useranswer = input(f"Q.{self.question_number}.{current_question.text} True/False")
    self.check_answer(useranswer,current_question.answer)
    


  def quiz_still_has_questions(self):
    if self.question_number < len(self.question_list):
      return True
    else:
      return False
  
  def check_answer(self, useranswer, correctanswer):
    if useranswer.lower() == correctanswer.lower():
      self.score += 1
      ok = True
    else:
      ok = False
    print(f"The correct answer was {correctanswer}")
    print(f"Your current score is {self.score}/{self.question_number} \n")
    return ok
