from services.parser import parse_text_expense


def test_parse_text_expense_amount_and_category():
    parsed = parse_text_expense("Lunch 35")
    assert parsed is not None
    assert parsed.amount == 35
    assert parsed.category == "food"
