shopping_list = []


def show_help():
    print('What should we pick up at the store? ')
    print("""
    
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    Enter 'SHOW' to show the list.
    """)

show_help()



def add_to_list(item):
    shopping_list.append(item)
    print(f'Your shopping list has: {len(shopping_list)}  items.')


def show_list():
    print('Here is your list: ' )
    for item in shopping_list:
        print(item)


while True:

    new_item = input("> ")


    if new_item == "DONE":
        break

    elif new_item == 'HELP':
        show_help()
        continue

    elif new_item == 'SHOW':
        show_list()
        continue

    add_to_list(new_item)

show_list()
