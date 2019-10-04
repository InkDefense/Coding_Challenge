#approach solutions in tree like fashion
#simulate depth first search build recursively
def permutate(my_list, my_string):
  if(my_list != []): # not an empty list
    for i in range(0, len(my_list)):
      my_string += my_list.pop(i)
      permutate(my_list, my_string) # recursive call to move to next "tree node"
      my_list.insert(i, my_string[len(my_string) - 1:])
      my_string = my_string[:-1]
  else: # tree leaf, print and travel back up
    print(my_string) 


test_string = "abcd"
test_list = list(test_string)
test_list.sort()

permutate(test_list, "")
