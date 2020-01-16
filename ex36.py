from random import randrange

def rock_paper_scissors():
  history = []

  for i in range(0, 5):
    print("Choose rock (0), paper (1) or scissors (2): ")
    choice = input("> ")
    history.append(choice)
    opponents_choice = randrange(3)
  
    if choice == "0" and opponents_choice == 1:
      print("You lose.")
    elif choice == "0" and opponents_choice == 2:
      print("You win.")
    elif choice == "1" and opponents_choice == 0:
      print("You win.")
    elif choice == "1" and opponents_choice == 2:
      print("You lose.")
    elif choice == "2" and opponents_choice == 0:
      print("You lose.")
    elif choice == "2" and opponents_choice == 1:
      print("You win.")
    else:
      print("Tie")
  
  for i in history:
    print(f"Choice: {i}")

rock_paper_scissors()