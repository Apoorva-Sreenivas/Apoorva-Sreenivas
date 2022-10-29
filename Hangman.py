
import random

words_list=["redundancy","stack","flood","overflow","submerge","hurdles","saddle","pile","overcome","backup","bagpiper","buffalo","independence","arbitrary","supermarket","excellent","exuberance","awkward","absurd","collaboration","jigsaw","jackpot","refreshment","bookworm","umbrella","anonymous","xylophone","zombie","unknown","jukebox","transportation","transplant","pneumonia","syndrome","photosynthesis","calligraphy","jogging","engagement","institution","joyful","audience","ambience","ambassador","vulnerable","vigorous","abruptly","beekeeper","avenue","larynx","elimination","puzzling","publication","nightmare","nightingale","kingfisher","quorum","qualification","election","aeration","variation","richshaw","absolutely","estimation","examination","evaluation","plankton","rhizobium","parthenium","pathogens","planetarium","articulation","galaxy","galvanization","blossoming ","microwave","microphone","microprocessor","mysterious","matrices","lymph","jaundice","dilution","purification","metallurgy","electrification","refrigeration","polarization","porcupine","concatenation","regurgitation","extraordinary","crackers","nowadays","yesterday","oxygenation","exaggeration","employment","overwhelmed","kingdom","procrastination"]
lives=6
word=""
used_letters=[]

word=random.choice(words_list)
word=word.upper()
word=list(word)

for i in range(word.count(" ")): 
  word.remove(" ")

print("WELCOME TO HANGMAN")
print("Let's play")
out_word=["-"]*len(word)    
found=True
while found:
     print()
     print("Number of Lives :",lives)
     for x in out_word:
      print(x,end="")     
     print("\n Used Letters: ",end="")
     for x in used_letters:
      print(x,end=" ")
     print()
     print("Guess a letter : ",end="")
     inputch=input().upper()
     if inputch in used_letters: 
       print("You have already used the letter try again")
     else:
       used_letters.append(inputch)
       if(inputch in word): 
        for i in range(len(word)):
          if word[i]==inputch:
            out_word[i]=inputch
        if(out_word.count("-")==0):
          for x in out_word:
            print(x,end="") 
          print()
          found=False
       else:
          lives-=1
          if lives==0:
            break;
          print("Life Lost")
          print("Try Again")
          
if(found):
  print("You Lost\nYour word was",end=" ")
  for x in word:
    print(x,end="")
  print("\nBetter luck next time")
else:
  print("Congratulations you have won")
print("Thank you for playing")