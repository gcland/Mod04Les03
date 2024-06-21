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
        if new_allocated_budget < 0:
            raise ValueError(f"Budget cannot be less than $0.00.")
        else:
            self.__allocated_budget = new_allocated_budget

    def add_expense(self, amount):
        if 0 < amount < self.get_allocated_budget():
            expense_name = input("What is the expense name? ")
            self.set_allocated_budget(self.get_allocated_budget() - amount)
            print(f"\nExpense:'{expense_name}' logged for ${amount}.\nNew remaining budget for {self.get_category_name()}: {self.get_allocated_budget()}.")
        else:
            print("Invalid expense value or expense exceeds budget.")

food = BudgetCategory("Food", 1000)
food.add_expense(100)
