"""
Name(s): Jake Quan
Name of Project: Python 0 Adventure Game
"""

#Write the main part of your program here. Use of the other pages is optional.
yesans = ["yes", "y", "Y", "Yes", "YES"]
noans = ["no", "n", "N", "No", "NO"]

print("""Welcome to the adventure! Let's begin!

You are boarding a flight to Fiji for vacation. A weird man approaches you, asking you to 'deliver the package.'
Will you accept his offer? (Yes/No)

""")
ans1 = input("//")
if ans1 in yesans:
  print("\nThe military police of Fiji stop you when you land. They demand to know who gave you the package. Will you tell them? (Yes/No)")
  ans2 = input("//")
  if ans2 in yesans:
    print("\nThey detain you. Try to escape? (Yes/No)")
    end4 = input("//")
    if end4 in yesans:
      print("The OUTLAW ending. You escape, but your passport is no longer valid and the Fijian government is hunting you down. You won't be home again for 9 years.")
    elif end4 in noans:
      print("The RETURN TICKET ending. The Fijian government sends you home.")
  elif ans2 in noans:
    print("\nThey assume you're just an ignorant traveler, and let you leave with the package. A rebel Fijian paramilitary group approaches you as you leave the airport, thanking you immensely. They tell you the package contains evidence that the Fijian government is corrupt. Give them the package? (Yes/No)")
    end3 = input("//")
    if end3 in yesans:
      print("The BENEDICT ARNOLD ending. You give them the package, and they successfully overthrow the government of Fiji. As thanks, they make you Vice President of Fiji.")
    elif end3 in noans:
      print("The PRISONER ending. You are thrown into a Fijian rebel prison.")
elif ans1 in noans:
  print("He mutters something unintelligible and walks away. Board the plane? (Yes/No)")
  ans3 = input("//")
  if ans3 in yesans:
    print("You land a few hours later in Fiji. But a rebel paramilitary group takes you hostage. Try to flee? (Yes/No)")
    end2 = input("//")
    if end2 in yesans:
      print("THAT WAS SO BRAVE! You successfully escape and are saved by the US military. You are a national hero, and have a happy ending.")
    elif end2 in noans:
      print("The WARRIOR ending. You assist the Fijian rebels in defeating their corrupt government, and become a Fijian military captain.")
  elif ans3 in noans:
    print("You go home, confused by the encounter. Turn on the TV? (Yes/No)")
    end1 = input("//")
    if end1 in yesans:
      print("YOU WIN. You find out civil war has just erupted in Fiji. You used your common sense and sure are glad you didn't go!")
    elif end1 in noans:
      print("YAWN. You chose the boring ending. Don't expect anything interesting to happen.")
else:
 print("You didn't type yes or no. Goodbye.")
#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
#whatsyourname = input("Write your name: ")
