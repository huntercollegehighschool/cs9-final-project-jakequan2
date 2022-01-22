#Use of this page is optional. If you use code here, make sure either import page4 or from page4 import * appear on your main.py page.
whatsyourname = input("Write your name: ")
print("Hey", whatsyourname,"!")
print("Are you ready to play Hangman?")
word = "Caramel"
write = ''
guesscount = 8
while guesscount > 0:
  wrongtry = 0
  for char in word:
    if char in write:
      print(char)
    else:
      wrongtry += 1
      
if wrongtry == 0:
  print("You win! Congrats!")
guess = input("Choose a letter")
write = write + guess
if guess not in write:
  guesscount -= 1
  print ("No no no. Try again.")
  print (guesscount,"turns left")
elif guesscount == 0:
  print("Game over! Better luck next time")