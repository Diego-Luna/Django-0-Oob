class HotBeverage:
    def __init__(self):
        self.price = 0.30
        self.name = "hot beverage"
        self._description = "Just some hot water in a cup." 
    
    def description(self):
        return self._description 

    def __str__(self):
        return f"""name : {self.name}
price : {self.price:.2f}
description : {self._description}"""

class Coffee(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "coffee"
        self.price = 0.40
        self._description = "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "tea"

class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "chocolate"
        self.price = 0.50
        self._description = "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "cappuccino"
        self.price = 0.45
        self._description = "Un po' di Italia nella sua tazza!"

if __name__ == '__main__':
    try:
        print("\n=== Testing all beverages ===")
        beverages = [
            HotBeverage(),
            Coffee(),
            Tea(),
            Chocolate(),
            Cappuccino()
        ]

        # # Display each beverage
        for beverage in beverages:
            print("\n" + "=" * 30 + "\n")
            print(f"> Testing {beverage.__class__.__name__}:\n")
            print(beverage)
        print("\n" + "=" * 30 + "\n")

    except Exception as e:
        print(f"An error occurred: {e}")