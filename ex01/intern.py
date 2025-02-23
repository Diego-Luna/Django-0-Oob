
class Coffee:
    def __str__(self):
        return "This is the worst coffee you ever tasted."

class Intern:
    def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
        self.Name = name
    
    def __str__(self):
        return self.Name
    
    def work(self):
        raise Exception("I'm just an intern, I can't do that...")
    
    def make_coffee(self):
        return Coffee()

if __name__ == '__main__':
    # Test cases 1
    try:
        print("\n=== Test Case 1 ===")
        # Create interns
        nameless_intern = Intern()
        mark = Intern("Mark")
        
        # Display names
        print(nameless_intern)
        print(mark)
        
        # Ask Mark to make coffee
        print(mark.make_coffee())
        
        # Ask nameless intern to work
        try:
            nameless_intern.work()
        except Exception as e:
            print(e)
            
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        print("\n=== Test Case 2: Additional Tests ===")
        
        # Test multiple interns
        print("Creating multiple internals:")
        interns = [Intern(f"Intern_{i}") for i in range(3)]
        for intern in interns:
            print(f"Nanme: {intern}")
            print(f"Brewed coffee: {intern.make_coffee()}")

        # Test work() with multiple interns
        print("\nTesting work() with multiple interns:")
        for intern in interns:
            try:
                intern.work()
            except Exception as e:
                print(f"{intern}: {e}")

    except Exception as e:
        print(f"Error: {e}")