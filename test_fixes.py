from app import get_range_for_difficulty, check_guess


# --- Bug 1: Hard difficulty range was 1-50 (easier than Normal) ---

def test_hard_range_is_wider_than_normal():
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high, (
        f"Hard upper bound ({hard_high}) should be greater than Normal ({normal_high})"
    )

def test_hard_range_is_200():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 200, (
        f"Hard range should be (1, 200), got ({low}, {high})"
    )


# --- Bug 2: Hint messages were swapped ---

def test_too_high_message_says_go_lower():
    outcome, message = check_guess(90, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'Go LOWER' when guess is too high, got: {message}"

def test_too_low_message_says_go_higher():
    outcome, message = check_guess(10, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'Go HIGHER' when guess is too low, got: {message}"
