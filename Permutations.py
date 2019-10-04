import sys

#approach solutions in tree like fashion and simulate depth first search build recursively
#my_list acts as a container for the characters we insert and remove from my_string as different permutations are built
def permutate(my_list, my_string, output_list):
  if(my_list != []): # not an empty list
    for i in range(0, len(my_list)):
      my_string += my_list.pop(i)
      permutate(my_list, my_string, output_list) # recursive call to move to next "tree node"
      my_list.insert(i, my_string[len(my_string) - 1:])
      my_string = my_string[:-1]

    if(my_string == ""): #print outputs in ascending order after returning to starting position
      output_string = ", ".join(output_list)
      print(output_string)
  else: # tree leaf, print and travel back up
    output_list.append(my_string) 

def main():
    file = open(sys.argv[1], "r")

    if file.mode == "r": #Check if file opened 
        lines = file.read().splitlines()
        for string in lines: #Permutate and print each output for each line in the list
            string_list = list(string)
            string_list.sort() #My permutate algorithm requires characters of a string to be in ascending order at start

            permutate(string_list, "", [])
    else:
        print("File passed as argument could not be opened.")

if __name__ == '__main__':
    main()

""" for testing algorthim before introducing file input
test_string = "abcd"
test_list = list(test_string)
test_list.sort()

permutate(test_list, "")
"""
