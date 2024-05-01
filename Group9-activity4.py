import csv

"""
Group 9 activity 4

Members: 
Elsayed, Mahmoud, mee5011: Main function
Mersha, Yeshiwas, yym2283: read_data and positive
Nathershah, Faizahnadir, fn6379: Article class and Cart Class

Manifesto: The program is used to create a shopping cart.

It allows the customer to add products into their shopping cart and checkout.

Github link: https://github.com/Mahmoud-Elsayed3/Group9-Activity4.git





"""

class Article:
    """Class to represent an article in the inventory."""
    
    def __init__(self, name, inventory, price):
        """

        Parameters:
        name (str): The name of the article.
        inventory (int): The quantity of the article in the inventory.
        price (float): The price of the article.

        """
        self.name = name
        self.inventory = inventory
        self.price = price
    
    def get_name(self):
        """Return the name of the article."""
        return self.name

    def get_price(self):
        """Return the price of the article."""
        return self.price

    def get_quantity(self):
        """Return the quantity of the article in the inventory."""
        return self.inventory

    def set_quantity(self, quantity):
        """
        quantity (int): The new quantity of the article.
        
        """
        self.inventory = quantity

    def __str__(self):
        """Return a string representation of the Article object."""
        return f"Article: {self.name}, Quantity: {self.inventory}, Price: ${self.price:.2f}"

class Cart:
    """Class to represent a shopping cart."""
    
    def __init__(self):
        """Start a Cart object with an empty list of purchased articles."""
        self.list_of_purchased = []
    
    def display_cart(self):
        """Display the articles in the shopping cart."""
        if not self.list_of_purchased:
            print("Shopping cart is empty.")
        else:
            for item in self.list_of_purchased:
                print(item)

    def add_product(self, article, quantity):
        """
        Add an article to the shopping cart.

        If the article is already in the cart, update its quantity.

        Parameters:
        article (Article): The article to add to the cart.
        quantity (int): The quantity of the article to add.
        """
        for item in self.list_of_purchased:
            if item.name == article.name:
                item.inventory += quantity
                return
        self.list_of_purchased.append(Article(article.name, quantity, article.price))
   
    def remove_product(self, article, quantity):
        """
        Remove an article from the shopping cart.

        If the article is not in the cart, do nothing.
        If the specified quantity exceeds the quantity in the cart, remove the article completely.

        Parameters:
        article (Article): The article to remove from the cart.
        quantity (int): The quantity of the article to remove.
        """
        for item in self.list_of_purchased:
            if item.name == article.name:
                if item.inventory <= quantity:
                    self.list_of_purchased.remove(item)
                else:
                    item.inventory -= quantity
                return
    
    def checkout(self):
        """
        Calculate the total cost of the articles in the shopping cart.

        Apply a 7% tax to the total cost.
        Apply a 10% discount to articles with a quantity of 3 or more.

        Returns:
        float: The total cost of the articles in the shopping cart.
        """
        total = 0
        for item in self.list_of_purchased:
            if item.inventory >= 3:
                total += item.price * item.inventory * 0.9
            else:
                total += item.price * item.inventory
        total *= 1.07  
        self.list_of_purchased.clear()  
        return total

def read_data(file_path):
    """
    Read data from a CSV file and return a dictionary of articles.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    dict: A dictionary of articles with article names as keys and Article objects as values.
    """
    INVENTORY = {}
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                inventory = int(row['inventory'])
                price = float(row['price'])
                INVENTORY[name] = Article(name, inventory, price)
    except FileNotFoundError:
        print("Error: The file path provided does not exist.")
    except ValueError:
        print("Error: Data format error in the file.")
    return INVENTORY

def positive(val):
    """

    Parameters:
    val (str): The prompt to display to the user.

    Returns:
    int: The positive integer entered by the user.
    """
    while True:
        try:
            value = int(input(val))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """Main function to run the shopping system."""
    
    # Load inventory from file
    INVENTORY = read_data('classes\products.csv')
    if not INVENTORY:
        print("Failed to load inventory. Exiting program.")
        return
    
    # Create a shopping cart
    cart = Cart()
    
    while True:
        # Display menu options
        print("\nMenu:")
        print("1. List all items in inventory")
        print("2. List items in shopping cart")
        print("3. Add an item to the shopping cart")
        print("4. Remove an item from the shopping cart")
        print("5. Checkout")
        print("6. Exit")
        
        # Get user choice
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # List all items in inventory
            for article in INVENTORY.values():
                print(article)
        
        elif choice == '2':
            # List items in shopping cart
            cart.display_cart()
        
        elif choice == '3':
            # Add an item to the shopping cart
            item_name = input("Enter the name of the item: ")
            if item_name in INVENTORY:
                item = INVENTORY[item_name]
                quantity = positive("Enter the quantity: ")
                if quantity <= item.inventory:
                    item.inventory -= quantity
                    cart.add_product(item, quantity)
                else:
                    print("Not enough inventory for this item.")
            else:
                print("Item not found in inventory.")
        
        elif choice == '4':
            # Remove an item from the shopping cart
            item_name = input("Enter the name of the item to remove: ")
            if item_name in INVENTORY:
                item = INVENTORY[item_name]
                quantity = positive("Enter the quantity to remove: ")
                cart.remove_product(item, quantity)
            else:
                print("Item not found in inventory.")
        
        elif choice == '5':
            # Checkout
            total_cost = cart.checkout()
            print(f"Total cost: ${total_cost:.2f}")
        
        elif choice == '6':
            # Exit the program
            print("Thank you for shopping with us!")
            break
        
        else:
            print("Invalid choice. Please try again.")
        
        # Continue
        resume = input("Would you like to continue? (y/n): ")
        if resume.lower() != 'y':
            print("Thank you for using the shopping system!")
            break

if __name__ == "__main__":
    main()
