def is_invoice(text):
    signals = ["invoice", "total amount", "invoice #", "$"]
    return _has_signals(text, signals, min_hits=2)


def is_resume(text):
    signals = ["experience", "education", "skills", "email"]
    return _has_signals(text, signals, min_hits=2)


def is_utility_bill(text):
    signals = ["account", "kwh", "usage", "amount due"]
    return _has_signals(text, signals, min_hits=2)


def _has_signals(text, signals, min_hits):
    text = text.lower()
    hits = sum(1 for s in signals if s in text)
    return hits >= min_hits