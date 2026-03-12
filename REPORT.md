# Project Report: Hangman Word Game

This report documents learnings, challenges, and reflections on developing a Hangman game using CoPilot for guided learning.

---

## First Impressions - Initial Take on the Project Assignment

### Initial Thoughts
The project was to build a Hangman word-guessing game in Python, applying software engineering principles to keep the code clean and maintainable. The challenge was not just making it work, but structuring it well from the start.

### Assumptions Made
- Input validation should happen at the UI layer, not inside state transition functions
- The game should support replaying without restarting the program
- The word source should be flexible (file-based, with fallback)
- State should be immutable; functions should not modify inputs directly

### Points Needing Clarification
- **Separation of concerns**: Which layer handles input validation? (Answer: UI layer before calling state functions)
- **Display logic**: How to handle non-alphabetic characters like spaces and hyphens? (Answer: Always reveal them to aid player comprehension)
- **Return values**: What should `play_game()` return? (Answer: A boolean for simplicity and clarity)

---

## Key Learnings

### Computer Science Concepts and Technical Skills

1. **Pure Functions & Immutability**
   - `update_game_state()` doesn't modify inputs; it returns new values
   - Makes the function testable and predictable
   - Avoids hidden state and side effects

2. **Separation of Concerns**
   - **Mechanics layer** (`update_game_state`): Game rules only
   - **Display layer** (`get_display_word`): UI rendering only
   - **Orchestration layer** (`play_game`): Game flow and loop management
   - **Entry point**: Replay logic and word selection

3. **State Normalization**
   - Internal state uses lowercase letters for consistency
   - Display layer preserves original casing for user experience
   - Checking: `char.lower() in guessed_letters`

4. **Robust Fallbacks**
   - `load_word()` reads from file but never crashes
   - Always has a hardcoded list as fallback
   - Makes the game production-ready

5. **Input Validation Strategy**
   - Validation happens *before* calling state-modifying functions
   - Invalid input doesn't count as a turn
   - Keeps game logic pure and focused

### Insights about Using CoPilot Effectively

1. **Ask specific questions about design before coding**
   - "How should I handle non-alphabetic characters?" led to a better design decision
   - Clarifying edge cases upfront prevents rework

2. **Use Socratic mode for learning**
   - Questions guided me to think through the problem systematically
   - Discovering the answer myself made the solution feel more solid

3. **Start with the easiest function**
   - Building `get_display_word()` first was a good warm-up
   - It clarified how the display logic should work before building the orchestrator

4. **Separate modeling concerns from implementation**
   - Discussing architecture (loop conditions, return values, state) before coding saved time
   - Clear design meant faster, cleaner implementation

### New Concepts or Tools Encountered

- **List comprehensions** for data transformation in one line
- **Graceful degradation** (file read with fallback)
- **Explicit loop conditions** instead of hidden breaks
- **Git journaling** practices for tracking development

---

## Report on CoPilot Prompting Experience

### Types of prompts that worked well

1. **Design clarification questions**
   - "Should `play_game()` take `secret_word` as a parameter or load it internally?"
   - These prompted clear thinking before coding

2. **Edge case exploration**
   - "What if someone enters multiple characters?" or "What about non-alphabetic characters?"
   - Helped identify and handle edge cases systematically

3. **Architecture validation**
   - "Where should input validation live?"
   - Ensured sound separation of concerns

4. **Code review requests with implementation guidance**
   - "What should `get_display_word()` return and how?"
   - Combined analysis with actionable implementation steps

### Types of prompts that did not work well or failed

1. **Vague requests without context**
   - "Make the game better" didn't lead anywhere useful
   - Being specific about requirements was essential

2. **Asking for full implementations too early**
   - Before thinking through design, full-code requests would have led to rework
   - Better to design first, then implement

---

## Limitations, Hallucinations and Failures

### Examples of Issues Encountered

None significant in this project. The AI stayed focused on the design and implementation architecture rather than inventing features or APIs.

### Analysis of Why These Issues Occurred / Did Not Occur

- **Socratic mode** encouraged me to think critically, catching potential issues before coding
- Design decisions were explicit and validated before implementation
- Incremental implementation meant each step was reviewable and testable

---

## AI Trust

### When did I trust the AI?
- When asking about design patterns and separation of concerns
- When reviewing functions for edge cases
- When implementing straightforward functions like `get_display_word()`

### When did I stop trusting it?
- Never had to; the AI stayed focused on the project scope

### What signals or patterns indicated low reliability?
- Asking for complete implementations without design context might have led to over-engineered solutions
- This was avoided by maintaining clear, incremental steps

---

## What I Learned

### What did you learn about software development?

1. **Design before code pays off**
   - Spending time on architecture upfront saves rework later
   - Clear function contracts (inputs, outputs, side effects) make implementation straightforward

2. **Separation of concerns is not optional**
   - Keeping state, display, and orchestration separate makes the code testable and maintainable
   - Makes it easy to change one layer without breaking others

3. **Pure functions are powerful**
   - Functions that don't modify inputs or depend on global state are predictable
   - They're easier to test and understand

4. **Handle edge cases explicitly**
   - Non-alphabetic characters, duplicate guesses, invalid input—all need explicit handling
   - Thinking through them upfront prevents bugs

### What did you learn about using AI tools?

1. **AI is best as a thought partner, not a code generator**
   - Questions that prompt reflection are more valuable than full code dumps
   - Explaining design decisions back to the AI helped validate them

2. **Incremental guidance beats massive implementations**
   - Building one function at a time and testing assumptions is faster than implementing everything at once
   - The AI's questions kept me on track

3. **Clear communication is critical**
   - "I want `play_game()` to receive `secret_word` as a parameter" was much clearer than "build the game loop"
   - Specificity leads to better results

### When should you trust AI? When should you double-check it?

**Trust it for:**
- Design and architecture advice, especially when validated against requirements
- Identifying edge cases and testing scenarios
- Code review and refactoring suggestions
- Syntax and API usage (with verification for critical parts)

**Double-check it for:**
- Complete system implementations without seeing incremental steps
- Claims about library functions you're unfamiliar with
- Optimization or performance suggestions (verify with measurement)

---

## Reflection

### Did AI make you faster? Why or why not?

**Yes**, significantly. The AI answered design questions in seconds that might have taken me minutes to think through. It also caught edge cases I might have missed. However, the speed came from *good questions*, not from asking for complete code.

### Did you feel in control of the code?

**Completely**. Because of the Socratic approach and incremental implementation, I made every design decision and wrote every line. The AI was a guide, not the author.

### Would you use AI the same way next time? What would you change?

**Yes, with this approach:**
1. Design discussion upfront (Socratic mode asking clarifying questions)
2. Incremental implementation (one function at a time)
3. Regular code review and validation
4. Document decisions in the journal as you go

I might experiment with:
- Building tests *during* implementation, not after
- Even more explicit edge case documentation upfront
- Asking the AI to help draft docstrings before implementation