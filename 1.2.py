class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name
    
    def set_category_name(self, new_category_name):
        self.__category_name = new_category_name 
    
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_allocated_budget(self, new_allocated_budget):
        self.__allocated_budget = new_allocated_budget

    def __str__(self):
        return "Category name: %s, Allocated Budget: %s" % (self.__category_name, self.__allocated_budget)

def add_category(categories):
    category_name = input("Enter category name: ")
    allocated_budget = float(input("Enter allocated budget: "))
    if allocated_budget < 0:
        raise ValueError("Value cannot be negative.")
    categories[category_name] = BudgetCategory(category_name, allocated_budget)

def update_category_details(categories):
    category_name = input("Enter category name to update: ")
    if category_name in categories:
        while True:
            try:
                choice = input("\n1. Update category name\n2. Update allocated budget\n3. Quit\n")
                if choice == "1":
                    new_category_name = input("Enter new category name: ")
                    categories[category_name].set_category_name(new_category_name)
                    print(f"{category_name} updated name: {new_category_name}.")
                    break
                elif choice == "2":
                    new_allocated_budget = float(input("Enter allocated budget: "))
                    if new_allocated_budget < 0:
                        raise ValueError("Value cannot be negative.")
                    else:
                        categories[category_name].set_allocated_budget(new_allocated_budget)
                        print(f"{category_name} updated budget: {new_allocated_budget}.")
                    break
                elif choice == "3":
                    break
            except Exception as e:
                print(f"Error: {e}")
    else:
        print(f"{category_name} not found.")

def display_categories(categories):
    for y in categories.items():
        print(y)
        
def main():
    categories = {}
    while True:
        print("\n1. Add category\n2. Update category details\n3. Display categories\n4. Quit")
        choice = input("Enter selection: ")
        try:
            if choice == "1":
                add_category(categories)
            elif choice == "2":
                update_category_details(categories)
            elif choice == "3":
                display_categories(categories)
            elif choice == "4":
                break
        except Exception as e:
            print(f"Error: {e}")

main()
