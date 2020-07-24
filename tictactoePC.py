import os ,time
os.system('color 0a')
Fmat = """
________________
| 1  | 2  | 3  |
|____|____|____|
| 4  | 5  | 6  |
|____|____|____|
| 7  | 8  | 9  |
|____|____|____|
\n"""

title = """
▀▀█▀▀ ▀█▀ ▒█▀▀█ 　 ▀▀█▀▀ ░█▀▀█ ▒█▀▀█ 　 ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀▀ 
░▒█░░ ▒█░ ▒█░░░ 　 ░▒█░░ ▒█▄▄█ ▒█░░░ 　 ░▒█░░ ▒█░░▒█ ▒█▀▀▀ 
░▒█░░ ▄█▄ ▒█▄▄█ 　 ░▒█░░ ▒█░▒█ ▒█▄▄█ 　 ░▒█░░ ▒█▄▄▄█ ▒█▄▄▄
--------------- [+] Made by GHOSTH4CK3R ----------------- \n"""
print(title)
print("Position Format : ",Fmat)
time.sleep(0.4)
graph = Fmat

def win ():
    
    if graph[20] == "X" and graph[25] == "X" and graph[30] == "X"  :  # horizontal
        print("***Player 1 won ***")
        print("Won by placing 3 X's Horizontally")
        return True
    if graph[20] == "O" and graph[25] == "O" and graph[30] == "O"  :
        print("***Player 2 won ***")
        print("Won by placing 3 O's Horizontally") 
        return True    
    if graph[54] == "X" and graph[59] == "X" and graph[64] == "X"  :
        print("***Player 1 won ***")
        print("Won by placing 3 X's Horizontally")
        return True
    if graph[54] == "O" and graph[59] == "O" and graph[64] == "O"  :
        print("***Player 2 won ***")
        print("Won by placing 3 O's Horizontally")  
        return True   
    if graph[88] == "X" and graph[93] == "X" and graph[98] == "X"  :
        print("***Player 1 won ***")
        print("Won by placing 3 X's Horizontally")
        return True
    if graph[88] == "O" and graph[93] == "O" and graph[98] == "O"  :
        print("***Player 2 won ***")
        print("Won by placing 3 O's Horizontally") 
        return True    

    if graph[20] == "X" and graph[54] == "X" and graph[88] == "X"  :  # vertical
        print("***Player 1 won ***")
        print("Won by placing 3 X's Vertically")
        return True
    if graph[20] == "O" and graph[54] == "O" and graph[88] == "O"  :
        print("***Player 2 won ***")
        print("Won by placing 3 O's Vertically")  
        return True   
    if graph[25] == "X" and graph[59] == "X" and graph[93] == "X"  :
        print("***Player 1 won ***")
        print("Won by placing 3 X's Vertically")
        return True
    if graph[25] == "O" and graph[59] == "O" and graph[93] == "O"  :
        print("***Player 2 won ***")
        print("Won by placing 3 O's Vertically")    
        return True 
    if graph[30] == "X" and graph[64] == "X" and graph[98] == "X"  :
        print("***Player 1 won ***")
        print("Won by placing 3 X's Vertically")
        return True
    if graph[30] == "O" and graph[64] == "O" and graph[98] == "O"  :
        print("***Player 2 won ***")
        print("Won by placing 3 O's Vertically") 
        return True    

    if graph[20] == "X" and graph[59] == "X" and graph[98] == "X"  :  # diagonal
        print("***Player 1 won ***")
        print("Won by placing 3 X's Diagonaly")
        return True
    if graph[20] == "O" and graph[59] == "O" and graph[98] == "O"  :
        print("***Player 2 won ***")
        print("Won by placing 3 O's Diagonaly")  
        return True   
    if graph[30] == "X" and graph[59] == "X" and graph[88] == "X"  :
        print("***Player 1 won ***")
        print("Won by placing 3 X's Diagonaly")
        return True
    if graph[30] == "O" and graph[59] == "O" and graph[88] == "O"  :
        print("***Player 2 won ***")     
        print("Won by placing 3 O's Diagonaly")  
        return True     
    


while True:
   
    usr1 = input("Player 1's Turn (X) > ")
    if usr1.isnumeric() :
      try:
          graph = graph.replace(usr1,"X")          
      except Exception as e:
          print("Enter numbers in position format")
    else:
        print("input numbers only !!!")
        continue  
    time.sleep(0.5)
    os.system('cls')
    print(title)
    print(graph)
    #win()
    if win() == True:
        break
    usr2 = input("Player 2's Turn (O) > ")
    if usr2.isnumeric() :
      try:
          graph = graph.replace(usr2,"O")          
      except Exception as e:
          print("Enter numbers in position format")
          continue
    else:
        print("input numbers only !!!")
        continue  
    time.sleep(0.5)
    os.system('cls')
    print(title)
    print(graph)
    win()
    #if win() == True:
    #    break

input("\nExit >")