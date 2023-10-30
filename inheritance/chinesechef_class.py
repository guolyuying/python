from chef_class import Chef

class ChineseChef(Chef): # In ChineseChef class, use all the functions in Chef class
    def make_fried_rice(self): # In ChineseChef class, add a new function which doesn't exist in Chef class
        print("The chef makes fried rice")
    def make_special_dish(self): # Override the make_special_dish function inherited from Chef class.
        print("The chef makes orange chicken") # So ChineseChef's special dish is orange chicken instead of bbq ribs