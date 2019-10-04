#@author: Taylor Ratliff
import json
import urllib.request

def deleteByID(todos, index):
    # confirm index is within range
    try:
        index -= 1 # adjust id to target correct index
        del todos[index]
        updateIDs(todos, index) # adjust ids to correspond to indices in dictionary list
    except:
        print("Index must be an interger in range of ", 0, "to", len(todos))
    

# update ids to match indicies
def updateIDs(todos, startIndex):
    for i in range(startIndex, len(todos)):
        todos[i].update({'id': i + 1})

# add todo task to end of list as most recent
def appendTodos(todos, userID, title, completed):
    todos.append(dict({'userID': userID, 'id' : len(todos) + 1, 'title': title, 'completed': completed}))

# menu function to allow user input
def menu():

    for i in range(0, 3): # user gets 3 attempts to input a number 1-4
        print("1. Append todo")
        print("2. Delete todo by id")
        print("3. Print todo list")
        print("4. Quit")

        option = int(input("Enter numerical value for selection: "))

        try:
            if(option > 0 and option < 5):
                return option
            else:
                print("Must select a valid option.")
        except:
            print("Must enter a numerical input.")

    return 4 # return option to quit script after 3 failed attempts
    
# starting point of python script
def main():
    try:
        with urllib.request.urlopen("http://jsonplaceholder.typicode.com/todos") as url:
            todos = json.loads(url.read())

        selection = menu() #print menu and get user selection
        while selection != 4:
            if (selection == 1):
                try:
                    userID = input("Enter User ID: ")
                    title = input("Enter title: ")
                    completed = input("Enter completed status(True or False): ")

                    if(completed.lower == "true"): #ensure proper input, default to False
                        completed = True
                    else:
                        completed = False

                    appendTodos(todos, userID, title, completed)
                except Exception as e: #unexpected error
                    print(e)
            elif (selection == 2):
                try:
                    todoID = int(input("Enter id of todo to delete: "))
                    deleteByID(todos, todoID)
                except:
                    print("todoID must have an integer input")
                    
            else: # print todos
                for i in todos:
                    print(i)

            print("\n")        
            selection = menu()
            
    except:
        print("Todo resource could not be located.  Exiting script.")

# execute python script from main
if __name__ == '__main__':
    main()

    """ Previous test statements

    appendTodos(todos, 500, "some stuff i wrote", False)    

    print(todos[199])

    print(todos[200])

    deleteByID(todos, 201)

    print(todos[199])

    """
