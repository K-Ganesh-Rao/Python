line1 = ["[]","[]","[]"]  #List
line2 = ["[]","[]","[]"]
line3 = ["[]","[]","[]"]
map = [line1,line2,line3]  #2D matrix of list consisting of Rows and columns
print("Hiding your treassur! X marks the spot.")
position = input()          #1st input is acgaracter and followed by a number ex:B3
letter = position[0].lower()    #Takes 1st character converts to a lower case 
abc = ["a","b","c"]
letter_index = abc.index(letter)  #index of a 1st input letter
number_index = int(position[1]) - 1  #index of number -1 is to match 0 indexing format 
map[number_index][letter_index] = "X"
print(f"{line1}\n{line2}\n{line3}")

#   A   B   C
#   1   1   1
#   2   2   2
#   3   3   3
