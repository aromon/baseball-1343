from unittest import TestCase

from game import Game


class TestGame(TestCase):

    def setUp(self):
        super().setUp()
        self.game = Game()
    def test_exception_when_input_is_none(self):
        with self.assertRaises(TypeError):
            self.game.guess(None)

    def test_exception_when_input_length_is_unmatched(self):
        with self.assertRaises(TypeError):
            self.game.guess("12")

