import re

def extract_invoice(text):
    return {
        "invoice_number": _match(r"(?:INV[-\s]?|Invoice\s+#)(\d+)", text),
        "date": _match(r"(\d{4}-\d{2}-\d{2})", text),
        "company": _match(r"Company[:\s]*(.+?)\s*Total Amount", text),
       "total_amount": _match(r"Total Amount[:\s]*\$?([\d,.]+)", text),
    }

def extract_resume(text):
    return {
        "name": _match(r"(^[A-Z][a-z]+\s[A-Z][a-z]+)", text),
        "email": _match(r"([\w\.-]+@[\w\.-]+)", text),
        "phone": _match(r"(\+?\d[\d\s\-]{7,})", text),
        "experience_years": _match(r"(\d+)\+?\s+years", text),
    }

def extract_utility_bill(text):
    return {
        "account_number": _match(r"Account Number[:\s]*([A-Z0-9\-]+)", text),
        "date": _match(r"(\d{4}-\d{2}-\d{2})", text),
        "usage_kwh": _match(r"([\d.]+)\s*kWh", text),
        "amount_due": _match(r"Amount Due[:\s]*\$?([\d.]+)", text),
    }

def _match(pattern, text, flags=0):
    match = re.search(pattern, text, flags | re.IGNORECASE)
    return match.group(1).strip() if match else None
