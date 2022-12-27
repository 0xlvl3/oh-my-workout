def open_menu(file):
    with open(file, "r") as menu:
        menu_open = menu.read()
    print(f"\n{menu_open}")
