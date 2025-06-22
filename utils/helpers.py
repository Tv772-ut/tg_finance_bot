# utils/helpers.py

def parse_amount(text):
    try:
        return float(text.replace(",", "").strip())
    except ValueError:
        return None

def format_currency(amount):
    return f"¥{amount:,.2f}"
