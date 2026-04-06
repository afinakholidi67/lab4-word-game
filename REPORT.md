# CoPilot guided Hangman Game Report

## First Impressions:

Initially, the project seemed very time-consuming and perhaps not in the working sense but in the understanding/meeting expectations for a correct final report.

## Key Learnings

Collaborating with CoPilot(management of ressources, prompt writing)
Understanding suggestions 
Merging personal constraints with AI solutions
How to use AI to make up for bad human habits(code documentation, test writing, keeping a journal updated)

## CoPilot Prompting Experience

Mostly fluid. Sometimes needed a recontextualization in order to correctly treat a prompt(pointing to target files directly, being concise and efficient). When AI detects an anomaly(most of the time due to lacking information/access to information) instead of stopping and questioning, it rather pursues into flawed logic which can raise larger errors in the bigger scheme of things.

This not only uses up AI Tokens but also precious literal ressources on earth by essentially wasting a prompt due to human-sourced misinformation/vagueness. 

Aside from this issue, CoPilot was very responsive, with quick accurate actions when provided with the correct dataset.

## Limitations and Reliability

Since most errors caused by AI originate from bad human prompting, it is sometimes difficult to pinpoint exactly where the problem is in AI's functioning.

Throughout the project, major AI-related mistakes happened at 2 different points of the project.

## Overall Reflection

Overall an important lesson to be learned is that software development isn't all that linear. Sometimes in order to create a better end product it is needed to evaluate feedback from different sources and adapt to whatever tools is available. In the case of AI, rapidly evolving methods and apps surface everyday, making it quite difficult to filter through and keep a human side to every project. But that's why it is crucial to keep a human core to every project. AI is most effective when given most data, which doesn't happen when you make it start from scratch. Therefore the most useful way to implement AI into a project is to use it to generate tests, monitor every change and update, and advise on optimization.

## Testing : 

Several cases were to be tested for each requirement of the game. Upon asking AI for useful tests, it came up with this :
1. The choice of an initial word
2. The testing of a successful guess(non-duplicate)
3. The testing of an unsuccessful guess(non-duplicate)
4. The testing of a duplicate guess
5. The testing of case-sensitivity(is "A" treated as "a")

Upon the initial testing of this function, all tests came up successful and there were no issues.

One potential issue of this way of functioning, is that only the update_game_state function is being tested. Since the game was made to be interacted with through the terminal, there is no trivial way to test the whole code. This way of testing is therefore good for individual functions but doesn't ensure that the individual function works with all the others.

Another potential issue, is using the exact same target word for each test. This could turn out to be problematic because the case of the word being not following expected guidelines is not being tested. For example if the word is wrongfully loaded from the initial list of words, or if the word is a string of non-alphabetical characters. This is never tested and could therefore result in an error.

A last "minor" addition would be to test each of these cases situationally. for example, testing when the letter list is empty, full, lives empty, (etc...) for each test provided.