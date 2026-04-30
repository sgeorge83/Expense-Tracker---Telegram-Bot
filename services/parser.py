import re
from dataclasses import dataclass


@dataclass
class ParsedExpense:
    amount: float
    category: str
    description: str
    currency: str = "AED"


CATEGORY_KEYWORDS = {
    "food": ["lunch", "dinner", "coffee", "groceries", "food"],
    "transport": ["fuel", "taxi", "uber", "metro", "transport"],
    "bills": ["internet", "electricity", "bill"],
    "shopping": ["mall", "shopping", "amazon"],
    "salary": ["salary", "income"],
}


def categorize(text: str) -> str:
    lower = text.lower()
    for category, words in CATEGORY_KEYWORDS.items():
        if any(word in lower for word in words):
            return category
    return "other"


def parse_text_expense(text: str) -> ParsedExpense | None:
    match = re.findall(r"([+-]?\d+(?:\.\d+)?)", text)
    if not match:
        return None
    amount = float(match.group(-1))
    category = categorize(text)
    return ParsedExpense(amount=amount, category=category, description=text.strip())
