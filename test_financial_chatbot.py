"""Basic automated tests for the financial chatbot."""
import unittest
from financial_chatbot import simple_chatbot

class TestFinancialChatbot(unittest.TestCase):
    def test_total_revenue(self):
        self.assertIn("₹1,250,000", simple_chatbot("What is the total revenue?"))

    def test_net_income_change(self):
        answer = simple_chatbot("How has net income changed over the last year?")
        self.assertIn("increased", answer)
        self.assertIn("₹25,000", answer)

    def test_total_expenses(self):
        self.assertIn("₹1,065,000", simple_chatbot("What are the total expenses?"))

    def test_profit_margin(self):
        self.assertIn("14.8%", simple_chatbot("What is the profit margin?"))

    def test_revenue_change(self):
        answer = simple_chatbot("How has revenue changed?")
        self.assertIn("increased", answer)
        self.assertIn("₹150,000", answer)

    def test_unknown_question(self):
        self.assertIn("Sorry", simple_chatbot("What is the share price?"))

    def test_case_and_spacing(self):
        self.assertIn("₹1,250,000", simple_chatbot("  WHAT IS THE TOTAL REVENUE  "))

if __name__ == "__main__":
    unittest.main(verbosity=2)
