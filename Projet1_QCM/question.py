#!/usr/bin/env python
# question.py
import random

class Question:
    def __init__(self, question_text, options, correct_option):
        self.question_text = question_text
        self.options = options
        self.correct_option = correct_option

    def check_answer(self, user_answer):
        return user_answer.lower() == self.correct_option.lower()

    def get_options(self):
        return self.options

    def get_correct_option(self):
        return self.correct_option

    def get_question_text(self):
        return self.question_text
