import random
from beverages import HotBeverage

class CoffeeMachine:
    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__()
            self.name = "empty cup"
            self.price = 0.90
            self._description = "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self):
        self.drinks_served = 0
        self.max_drinks = 10

    def repair(self):
        self.drinks_served = 0

    def serve(self, beverage_class):
        if not issubclass(beverage_class, HotBeverage):
            raise TypeError("Must be a HotBeverage type")
        
        if self.drinks_served >= self.max_drinks:
            raise self.BrokenMachineException()
        
        self.drinks_served += 1
        return beverage_class() if random.random() > 0.5 else self.EmptyCup()

if __name__ == '__main__':
    from beverages import Coffee, Tea, Chocolate, Cappuccino
    
    machine = CoffeeMachine()
    drinks = [Coffee, Tea, Chocolate, Cappuccino]
    
    try:
        print("\n=== Testing Coffee Machine ===")
        
        # First round until break
        print("\n--- First service round ---")
        while True:
            try:
                drink = machine.serve(random.choice(drinks))
                print(f"\n-> Serving attempt {machine.drinks_served}:")
                print(drink)
            except CoffeeMachine.BrokenMachineException as e:
                print(f"\n---> Machine broke! :{e}")
                break
        
        # Repair and second round
        print("\n🔧 Repairing machine...\n")
        machine.repair()
        
        print("--- Second service round ---")
        while True:
            try:
                drink = machine.serve(random.choice(drinks))
                print(f"\n -> Serving attempt {machine.drinks_served}:")
                print(drink)
            except CoffeeMachine.BrokenMachineException as e:
                print(f"\n---> Machine broke again! :{e}")
                break
                
    except Exception as e:
        print(f"An unexpected error occurred: {e}")