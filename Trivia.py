def check_keep_playing(game):
  keep_playing = input("Do you want to try the other game? -> (Yes/No)")
  if keep_playing == "No":
    print("Well, it was a pleasure!")
  if keep_playing == "Yes":
    if game == 1:
      game = 2
      run_game(game)
    elif game == 2:
      game = 1
      run_game(game)
def run_game(game):
  points = 0
  #First game 
  if game == 1:
    print ("These are all social studies questions! Let's beging! ")

    g1_first = input ("What is the name of current president of Costa Rica? ->(Carlos Alvarado/Marito Mortadela/Jose Figueres) "
    if g1_first == "Carlos Alvarado:
      print("Correct!")
      points = points+1
    else:
      print("Incorrect, it is Carlos Alvarado")

    g1_second = input("When did Guanacaste become a new Costa Rican province? ->(1820/1921/1824) ")
    if g1_second == "1824":
      print("Correct!")
      points = points + 1 
    else: 
      print("Incorrect, it was in 1824")

    g1_third = input ("What was the name of the president who led the Costa Rican army against William Walker? -> (Jose Figueres/Braulio Carillo/Jose Mora Porras) ")
    if g1_third == "Jose Mora Porras":
      print("Correct!")
      points = points +1 
    else: 
      print("Incorrect, it was Jose Mora Porras")

    g1_fourth = input("Where do you tell poeple to go in Costa Rica when you are mad? ->(Jacó Beach/Fuente de la Hispanidad/El Gollo ")
    if g1_fourth == "Fuente de la Hispanidad"
      print("correct!")
      points = points +1 
    else: 
      print("Incorrect, it was Fuente de la Hispanidad")
  
    print ("You got",points,"/ 4", "points")

    check_keep_playing(game)
  #Second game 
  elif game == 2: 
    print ("Here we are, let´s beging")
  else: 
    print ("That is not an option, but  ")
#greeting and facts about the player 
print("Hello! This is a really fun game that you are going to enjoy ")
name = input("Would you tell me your name? ")
print ("What a nice name ", name, "nice to meet you!")
age = int (input("How old are you? ")) 

#Start of the game 
print("Ok, now I am going to let you choose the game you want to play")
game = int(input("Choose 1 or 2 -> "))
run_game(game)
check_keep_playing(game)