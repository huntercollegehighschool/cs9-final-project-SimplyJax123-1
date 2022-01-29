import time
import random



def start():
  print("You wake up in a foreign room. You attempt to look around, but nothing is visible in the darkness.")
  time.sleep(1)
  print("You hear a voice. Do you attempt to call out for help, or stay silent?")

  choice = input("Enter call (C), or silent (S)")
  while choice!= "C" and choice != "S":
    print("You must choose call (C), or silent (S) ")
    choice = input("Enter call (C), or silent (S)")
  if choice == "C":
    call()
  elif choice == "S":
    silent()

def call():
  print("You call out into the darkness, \"Please save me.\"")
  time.sleep(1)
  print("There's no response. You call out again \"Please. I have a family.\"")
  time.sleep(.5)
  print("\"Can you shut up... No one's going to save you now.\"")
  print("There's a way to get out, but you must find it on your own. Once you do, we'll let you out. But, until then, you're stuck.")
  print("Do you want to search the room for clues, or check your pockets for any tools?")
  choice = input("Enter S(search), or C(check)")
  while choice!= "C" and choice != "S":
    print("You must choose S(search), or C(check) ")
    choice = input("Enter S(search), or C(check))")
  if choice == "C":
    pockets()
  elif choice == "S":
    room()

def room():
  print("You find a button. Do you press it, or go check your pockets?")
  choice = input("Enter Press(P), or Check (C)")
  while choice!= "C" and choice != "P":
    print("You must choose Press(P), or Check(C)")
    choice = input("Enter Press(P), or Check(C)")
  if choice == "C":
    pockets()
  elif choice == "P":
    print("A voice blares: A poison gas will be releasing in 5 seconds.")
    choice = input("Scream something, maybe it'll save you")
    print("You were unsuccessful. You die.")







def pockets():
  print("In your pockets you find a lighter, a flashlight, and some twine.")
  print("\"I don't remember putting these in here. I guess they're important\", You think.")
  print("The only thing you see in a room is a hook, attached to the wall above. ")
  choice = input("Would you like to tie a loop in the twine and try to get up(T), turn on the flashlight(F), or try and light the room on fire(L)? ")
  while choice!= "T" and choice != "F" and choice != "L":
    print("You must choose to tie(T), flashlight(F), or lighter(L)")
    choice = input("Enter tie(T), flashlight(F), or lighter(L)")
  if choice == "T":
    tie()
  elif choice == "F":
    flashlight()
  elif choice == "L":
    lighter()

def tie():
  print("You tie the rope. It takes a few tries, but you manage to throw it onto the hook.")
  choice = input("Do you try to climb the rope (C), or try lighting it on fire (L)?")
  while choice!= "C" and choice != "L":
    print("You must choose climb(C), or fire(L) ")
    choice = input("Choose climb(C), or fire(L)")
  if choice == "C":
    print("You start climbing. Once you get around 10 feet off the ground, you fall and crack your skull opoen. Game over.")
  elif choice == "S":
    print("You light the rope on fire. It reveals the room, a gray concrete box. However, to your dismay, the floor is made out of wood. It catches on fire, and quickly burns you to a crisp. Game over.")

def flashlight():
  print("You turn on the flashlight, and start pacing around. You find a button.")
  choice = input("Do you press it? (Y/N)")
  while choice!= "Y" and choice != "N":
    choice = input("Do you press it? (Y/N")
  if choice == "Y":
    print("The button releases a cloud of poison gas. You die within minutes. Game Over.")
  elif choice == "N":
    print("You walk around in circles, with no purpose. The 24 hours quickly passes, and the man comes back. You're brought away to a foreign land, with a promise that you'll never see your family again. Game Over.")

def lighter():
  print("You use the lighter. The room lights on fire, killing you instantly.")
  lastwords = input("do you have any last words?")
  if lastwords == "mrchengiscool":
    print("You have revived, and been teleported out of the room. You win!")
  else:
    print("You died. Game over.")

def silent():
  print("You hear the person come back. You hear them speak. \"I'm sure they'll never guess the cheat code. Only Mr. Cheng would be able to do that. He's so cool.\"")
  print("He walks off. You wait for a while, and call out to him when he comes back.")
  call()

start()
