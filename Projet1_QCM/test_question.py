#Test unitaire (`test_qcm.py`)
import unittest
from question import Question

class TestQCM(unittest.TestCase):

    #Check bonne réponse
    def test_check_answer_correct(self):
        q = Question("Question de test", ["a) Réponse A", "b) Réponse B", "c) Réponse C"], "a")
        self.assertTrue(q.check_answer("a"))

    #Check mauvaise réponse
    def test_check_answer_incorrect(self):
        q = Question("Question de test", ["a) Réponse A", "b) Réponse B", "c) Réponse C"], "a")
        self.assertFalse(q.check_answer("b"))

    #Check options
    def test_get_options(self):
        q = Question("Question de test", ["a) Réponse A", "b) Réponse B", "c) Réponse C"], "a")
        self.assertEqual(q.get_options(), ["a) Réponse A", "b) Réponse B", "c) Réponse C"])

    #Check bonne options
    def test_get_correct_option(self):
        q = Question("Question de test", ["a) Réponse A", "b) Réponse B", "c) Réponse C"], "a")
        self.assertEqual(q.get_correct_option(), "a")

    #Check question
    def test_get_question_text(self):
        q = Question("Question de test", ["a) Réponse A", "b) Réponse B", "c) Réponse C"], "a")
        self.assertEqual(q.get_question_text(), "Question de test")

if __name__ == '__main__':
    unittest.main()
