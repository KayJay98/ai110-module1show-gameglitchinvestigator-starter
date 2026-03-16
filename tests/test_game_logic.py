# fix me: imported from logic_utils which does not exist, causing an ImportError
# fixed: changed import to use app.py where check_guess is actually defined, and added sys.path so Python can find it from the tests/ subfolder
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import check_guess

# fix me: check_guess returns a tuple (outcome, message) but tests compared the whole tuple to a string, always failing
# fixed: unpacked the tuple with outcome, _ = check_guess(...) so only the outcome string is compared
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
