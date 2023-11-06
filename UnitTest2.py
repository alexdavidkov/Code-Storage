import unittest
from unittest.mock import patch
import io

# Import the quiz_game function from your code
from PythonQuizGame import quiz_game

class TestQuizGame(unittest.TestCase):

    @patch("builtins.input", side_effect=["yes", "central processing unit", "graphics processing unit", "random access memory", "power supply"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_quiz_game(self, mock_stdout, mock_input):
        quiz_game()
        output = mock_stdout.getvalue()

        self.assertIn("Welcome to my computer quiz!", output)
        self.assertIn("You got 4 questions correct!", output)
        self.assertIn("You got 100.0%.", output)

if __name__ == "__main__":
    unittest.main()

    
    
