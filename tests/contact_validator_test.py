from src.contact_validator import mask_email, normalize_email, validate_email, validate_phone


def test_validate_email_accepts_valid_address():
    assert validate_email("person@example.com")


def test_validate_email_rejects_missing_domain():
    assert not validate_email("person@example")


def test_normalize_email_strips_and_lowercases():
    assert normalize_email("  Person@Example.COM ") == "person@example.com"


def test_validate_phone_accepts_formatted_number():
    assert validate_phone("+1 (555) 123-4567")


def test_validate_phone_rejects_short_number():
    assert not validate_phone("555-1234")


def test_mask_email_basic():
    assert mask_email("alice@example.com") == "a***e@example.com"


def test_mask_email_masks_short_local_part():
    assert mask_email("ab@example.com") == "**@example.com"