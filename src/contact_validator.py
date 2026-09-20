"""Validation helpers for common contact details."""

import re


def validate_email(email: str) -> bool:
    """Return whether an email has a simple, valid shape."""
    return bool(re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email))


def normalize_email(email: str) -> str:
    """Normalize an email for comparison."""
    return email.strip().lower()


def validate_phone(phone: str) -> bool:
    """Return whether a phone contains 10 to 15 digits."""
    digits = re.sub(r"\D", "", phone)
    return 10 <= len(digits) <= 15


def mask_email(email: str) -> str:
    """Mask the middle of an email's local part while preserving its domain."""
    local_part, domain = email.split("@", 1)
    if len(local_part) <= 2:
        masked_local = "*" * len(local_part)
    else:
        masked_local = f"{local_part[0]}{'*' * (len(local_part) - 2)}{local_part[-1]}"
    return f"{masked_local}@{domain}"