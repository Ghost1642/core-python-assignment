def add_menu_item(menu, item):
    menu.append(item)
    return menu
def remove_menu_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} not found in the menu.")
    return menu
def check_menu_item(menu, item):
    if item in menu:
        return f'{item} is available'
    else:
        return f'{item} is not available'
initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"
menu = add_menu_item(initial_menu, add_item)
menu = remove_menu_item(menu, remove_item)
availability = check_menu_item(menu, check_item)
print(f"Updated menu: {menu}")
print(f"Availability: \"{availability}\"")
