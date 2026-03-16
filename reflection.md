# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? 
It ran but the game had some logic problems and didn’t behave correctly.
- List at least two concrete bugs you noticed at the start  
  One bug was that the tests expected check_guess() to return just "Win", "Too High", or "Too Low", but the function actually returned a tuple with a message too. Another bug was that the game text said to guess between 1 and 100, but some difficulty modes actually used a different range.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude suggested fixing the check_guess() function so it returned only the outcome instead of a tuple. I verified it by running the tests and seeing that they passed.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One time Claude suggested changing logic that wasn’t actually causing the test failure. After running the tests again, the error was still there so I knew the suggestion didn’t fix the real issue.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I ran the tests and checked if they passed without errors.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran the test that checks if guessing the correct number returns "Win". It showed me that the function output had to match exactly what the test expected.
- Did AI help you design or understand any tests? How?
AI helped explain what the tests were checking and what the function output needed to be.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns the whole program every time the user clicks something. Because of that, variables normally reset each time. Session state lets the app remember things like the secret number or score so the game keeps working.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - One habit I want to keep is running tests after making changes to make sure the code actually works.
- What is one thing you would do differently next time you work with AI on a coding task?
Next time I would check AI suggestions more carefully instead of assuming they are correct.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI can help find ideas and fixes, but the code still needs to be tested. AI code isn’t always correct.
