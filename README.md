# Flashcard Learning App

This is a Python GUI-based flashcard application using Tkinter and Pandas. The app helps users learn French words by displaying a French word on a card, flipping it after a delay to reveal the English meaning, and tracking words the user has learned.

## Features
- Display a French word on a flashcard.
- Automatically flip the card after a delay to show the English translation.
- Mark words as known to remove them from the learning set.
- Save progress so that users don’t have to relearn known words.

### How It Works
- A French word is displayed on the flashcard.
- After 3 seconds, the card flips to reveal the English translation.
- If the user knows the word, they can click the ✔️ button, and the word is removed from future practice.
- If the user does not know the word, they can click the ❌ button to see another word.
- The progress is saved in `words_to_learn.csv`.



