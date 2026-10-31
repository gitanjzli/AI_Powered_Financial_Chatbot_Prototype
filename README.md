# AI-Powered Financial Chatbot Prototype

## 1. Project overview
This is a beginner-friendly, rule-based Python chatbot prototype. It answers a
small set of predefined questions about financial performance. It demonstrates
basic chatbot logic and is not a machine-learning or production financial-advice
system.

## 2. Features
- Interactive command-line conversation.
- Five predefined financial questions.
- Case-insensitive matching and basic whitespace normalization.
- Financial amounts formatted in Indian Rupees.
- Help command and graceful exit.
- Automated tests for supported and unsupported queries.

## 3. Demonstration financial data
The current program uses illustrative figures only:
- Current revenue: ₹1,250,000
- Previous revenue: ₹1,100,000
- Current net income: ₹185,000
- Previous net income: ₹160,000
- Total expenses: ₹1,065,000
- Profit margin: 14.8%

IMPORTANT: Replace these values in the `FINANCIAL_DATA` dictionary in
`financial_chatbot.py` with the actual figures calculated in Task 1 before
submitting the final project.

## 4. Supported queries
1. What is the total revenue?
2. How has net income changed over the last year?
3. What are the total expenses?
4. What is the profit margin?
5. How has revenue changed?

Type `help` inside the chatbot to display these questions.

## 5. Requirements
- Python 3.8 or later
- No third-party packages are required for the command-line prototype.
- `pandas` and `Flask` are not required in this simplified version.

## 6. How to run
Open a terminal in this project folder and run:

```bash
python financial_chatbot.py
```

To run the automated tests:

```bash
python -m unittest -v test_financial_chatbot.py
```

## 7. Example interaction
```text
You: What is the total revenue?
Chatbot: The total revenue is ₹1,250,000.

You: What is the profit margin?
Chatbot: The profit margin is 14.8%.

You: exit
Chatbot: Thank you for using the Financial Chatbot. Goodbye!
```

## 8. How it works
1. The program receives a question through Python's `input()` function.
2. It converts the question to lowercase, removes surrounding spaces and
   normalizes repeated spaces.
3. An `if-elif-else` structure compares the question with supported query
   patterns.
4. The chatbot calculates year-over-year changes where needed and returns
   the corresponding response.
5. If no pattern matches, it displays a message explaining that the question
   is outside the prototype's supported scope.

## 9. Testing
The file `test_financial_chatbot.py` contains seven automated test cases:
revenue, net income change, expenses, profit margin, revenue change, unsupported
questions, and case/spacing normalization. Run the test command above to
reproduce the results.

## 10. Limitations
- This is a rule-based prototype, not a fully AI-trained chatbot.
- It only understands the predefined question patterns and their listed
  alternatives; it does not understand arbitrary natural language.
- It uses demonstration figures until Task 1 data is entered.
- It does not connect to live banking, accounting, or stock-market systems.
- It does not provide investment, tax, or other professional financial advice.
- It is intended for learning and demonstration, not production use.

## 11. Possible future improvements
- Load financial values from a CSV file using pandas.
- Add a Flask web interface.
- Use natural-language processing to recognize more ways of asking questions.
- Connect to a secure database and add authentication.
