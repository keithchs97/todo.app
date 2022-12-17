import main_functions  # Retrieving created functions from external file
# NOTE: BOTH FILES MUST BE IN THE SAME DIRECTORY

import time


print(time.strftime("%d-%b-%Y, %H:%M %p"))

while True:
    user_action = (input("Type add, show, edit, complete or exit: "))

    if user_action.startswith("add"):

        todos = main_functions.read_file()
        todo = user_action[4:] + '\n'

        # ==== Adding new item to list ====
        todos.append(todo.title())

        main_functions.write_file(todos)

        print(f"'{user_action[4:].title()}' has been added to the To Do list!\n")

    elif user_action.startswith("show"):

        todos = main_functions.read_file()
        # ==== Displaying current To Do list ====
        print("\nTo do list: ")
        for index, item in enumerate(todos):
            item = item.strip("\n")  # removing break line from todos
            string = f"{index + 1}. {item}"  # f-string!
            print(string)
        print("\n")

    elif user_action.startswith("edit"):
        todos = main_functions.read_file()

        try:
            # ==== Getting user input ====
            edit_var = int(user_action[5:])
            print(f"You are editing: {edit_var}. {todos[edit_var - 1]}")
            new_todo = input("Enter new to do: ")

            # ==== Replacing item in list with new To Do
            todos[edit_var - 1] = new_todo.title() + "\n"

            # writing to text file with EXCEPTION HANDLING
            main_functions.write_file(todos)
            print("To do list has been updated!\n")

        except ValueError:
            print("Your command is not valid. Try again. \n")
            continue  # ignores all the other elif and goes back to line 2

        except IndexError:
            print("There is no item with that number. Try again. \n")
            continue  # ignores all the other elif and goes back to line 2

    elif user_action.startswith("complete"):
        todos = main_functions.read_file()
        try:

            # ==== Getting user input ====
            edit_var = int(user_action[9:])
            print(f"You have removed: {edit_var}. {todos[edit_var - 1]}")
            todo_to_remove = todos[edit_var - 1].strip('\n')

            # ==== Removing item from list ====
            todos.pop(edit_var - 1)

            # writing to text file with EXCEPTION HANDLING
            main_functions.write_file(todos)

        except ValueError:
            print("Your command is not valid. Try again. \n")
            continue  # ignores all the other elif and goes back to line 2

        except IndexError:
            print("There is no item with that number. Try again. \n")
            continue  # ignores all the other elif and goes back to line 2

    elif user_action.startswith("exit"):
        break

    else:
        print("You have entered an unknown command. Try again.\n")

print("Bye!")
