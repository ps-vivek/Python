<<<A simple Hangman game>>
<<GAME RULES>>
--------------
->Computer randomly picks a word of a length from an existing "words.txt" file. 
->A user is given 8 tries to guess the word.
->For every incorrect try, a guess is subtracted.
->The letters guessed are removed from the available letters and shown to the user before he makes the choice for current letter.
->If a user enters the letter that he has already guessed, a warning is thrown and the guesses are not subtracted.
->Enjoy playing the game!! 


<<Running the file>>
--------------------
The game was written in Python 2.7. 
To play the game, place the "Hangman.py" and "words.txt" file and run them from a folder. 

The codes has been tested to run under windows and linux environment.

TO run the file in both windows and Linux environment from a command prompt,run the following command:
python Hangman.py
