from getData import questions
import random
import os

class QuizGame:

    def __init__(self, difficulty = None):

        self.question_list = []
        self.q_number = 20
        self.score = 0
        self.answers = {}

        if difficulty == None:
            self.difficulty = random.choice(["easy, medium, hard"])
            self.question_list = questions[self.difficulty]
        else:
            self.difficulty = difficulty
            self.question_list = questions[self.difficulty]

    # get user answer and check if it is correct -> multiple choices
    def get_user_answer_multiple(self, correct_answer, number, question):
        user_answer = input("Answer: ").upper()
        while user_answer!= 'A' and user_answer != 'B' and user_answer != 'C' and user_answer != 'D':
            user_answer = input("Wrong character. Answer: ").upper()

        if user_answer == correct_answer:
            self.score += 1

        self.answers[number] = {}
        self.answers[number]['question'] = question
        self.answers[number]['correct_answer'] = correct_answer
        self.answers[number]['user_answer'] = user_answer

    # get user answer and check if it is correct -> boolean choices
    def get_user_answer_bool(self, correct_answer, number, question):
        user_answer = input("Answer: ").capitalize()
        while user_answer != "True" and user_answer != "False":
            user_answer = input("Answer: ").capitalize()

        if user_answer == correct_answer:
            self.score += 1

        self.answers[number] = {}
        self.answers[number]['question'] = question
        self.answers[number]['correct_answer'] = correct_answer
        self.answers[number]['user_answer'] = user_answer

    def print_question_bool(self, question, number):
        print()
        print(f"Q.{number} - {question} (True/False)")
        print()

    def print_choices(self, answers, question, number):
        random.shuffle(answers)
        print()
        print(f"Q.{number} - {question}")
        print()
        print(f"\tA - {answers[0]}")
        print(f"\tB - {answers[1]}")
        print(f"\tC - {answers[2]}")
        print(f"\tD - {answers[3]}")
        print("")

    def print_score(self):

        os.system('clear')
        print()
        print("|>")
        print(f"|> Your score ---> {self.score}/20")
        print()

        for key,value in self.answers.items():
            print("")
            print(f"|> Question -> {key} - {self.answers[key]['question']} ")
            print(f"|> User answer -> {self.answers[key]['user_answer']}")
            print(f"|> Correct answer -> {self.answers[key]['correct_answer']}")
            print()

    def game_mode(self):
        index_list = []
        i = 0
        while i < 20:
            index = random.randint(0,len(self.question_list)-1)

            if index not in index_list:
                index_list.append(index)
                #store question
                q = self.question_list[index]
                #check type
                if self.question_list[index]['type'] == 'multiple':
                    correct_answer = q['correct_answer']
                    answers = q['incorrect_answers'] + [correct_answer]
                    self.print_choices(answers, q['question'], i+1)
                    self.get_user_answer_multiple(correct_answer, i+1, q['question'])
                else:
                    correct_answer = q['correct_answer']
                    self.print_question_bool(q['question'], i+1)
                    self.get_user_answer_bool(correct_answer, i+1, q['question'])
                os.system('clear')
                i += 1
        self.print_score()
