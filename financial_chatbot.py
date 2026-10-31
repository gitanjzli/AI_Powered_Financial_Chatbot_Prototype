"""
AI-Powered Financial Chatbot Prototype
A beginner-friendly, rule-based chatbot for answering predefined financial queries.

Note: The figures below are demonstration data. Replace them with the results
from your Task 1 financial analysis before final submission.
"""

import sys

FINANCIAL_DATA = {
    "total_revenue": 1250000,
    "previous_revenue": 1100000,
    "net_income": 185000,
    "previous_net_income": 160000,
    "total_expenses": 1065000,
    "profit_margin": 14.8,
}

def money(amount):
    """Format a number as Indian Rupees."""
    return f"₹{amount:,.0f}"

def simple_chatbot(user_query):
    """Return a predefined response for a supported financial question."""
    query = " ".join(user_query.lower().strip().rstrip("?!.").split())

    if query in ("what is the total revenue", "total revenue", "revenue"):
        return f"The total revenue is {money(FINANCIAL_DATA['total_revenue'])}."

    elif query in ("how has net income changed over the last year",
                   "net income change", "change in net income"):
        change = FINANCIAL_DATA["net_income"] - FINANCIAL_DATA["previous_net_income"]
        percent = (change / FINANCIAL_DATA["previous_net_income"]) * 100
        direction = "increased" if change >= 0 else "decreased"
        return (f"Net income has {direction} by {money(abs(change))} "
                f"({abs(percent):.1f}%) compared with the previous year.")

    elif query in ("what are the total expenses", "total expenses", "expenses"):
        return f"The total expenses are {money(FINANCIAL_DATA['total_expenses'])}."

    elif query in ("what is the profit margin", "profit margin"):
        return f"The profit margin is {FINANCIAL_DATA['profit_margin']:.1f}%."

    elif query in ("how has revenue changed", "revenue growth", "revenue change"):
        change = FINANCIAL_DATA["total_revenue"] - FINANCIAL_DATA["previous_revenue"]
        percent = (change / FINANCIAL_DATA["previous_revenue"]) * 100
        direction = "increased" if change >= 0 else "decreased"
        return (f"Revenue has {direction} by {money(abs(change))} "
                f"({abs(percent):.1f}%) compared with the previous year.")

    elif query in ("help", "what can you do", "show queries"):
        return (
            "You can ask me:\n"
            "1. What is the total revenue?\n"
            "2. How has net income changed over the last year?\n"
            "3. What are the total expenses?\n"
            "4. What is the profit margin?\n"
            "5. How has revenue changed?"
        )

    else:
        return ("Sorry, I can only answer predefined financial questions. "
                "Type 'help' to see the supported queries.")

def main():
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 55)
    print("       AI-POWERED FINANCIAL CHATBOT PROTOTYPE")
    print("=" * 55)
    print("Hello! Ask me a financial question.")
    print("Type 'help' to view supported questions or 'exit' to quit.\n")

    while True:
        try:
            user_query = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nChatbot: Goodbye!")
            break

        if user_query.lower().strip() in ("exit", "quit", "bye"):
            print("Chatbot: Thank you for using the Financial Chatbot. Goodbye!")
            break

        print("Chatbot:", simple_chatbot(user_query))
        print()

if __name__ == "__main__":
    main()
