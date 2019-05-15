class ShoppingCart:
    # write your code here
    #Update your shopping_cart.py file to include an __init__ method. 
    # This should define three default attributes: 'total', which
    # should be set to 0, 'employee_discount', set to None and 'items', set to a blank list. 
    #The line of code below should work and produce the previewed output once you do this.
    
    def __init__(self, total=0, employee_discount=None, items=[]):
        self.total = total
        self.employee_discount = employee_discount
        self.items = items.copy()
    
    # Define an instance method called add_item that will add an item to our cart. 
    # It should take in the name of an item, its price and an optional quantity. 
    # The method should increase the shopping cart's total by the appropriate amount 
    # and return the new total for the shopping cart.
    
    def add_item(self, name, price, quantity=1):
        self.total += price * quantity
        self.items.append([name, price, quantity])
        return self.total
    def mean_item_price(self):
        total_quantity = 0
        for item_grp in self.items:
            total_quantity += item_grp[2]
        try:
            return self.total / total_quantity
        except:
            print('No items in shopping cart!')

    def median_item_price(self):
        price_list = []
        for item_grp in self.items:
            price_list += [item_grp[1]] * item_grp[2]
        price_list.sort()
        n = len(price_list)
        if n%2 ==0:
            return (price_list[n//2] + price_list[n//2-1])/2
        else:
            return price_list[n//2]
                
            
        return self.total / total_quantity        

    
#   Now, define an instance method called apply_discount that applies a discount if one is provided and returns the discounted total. For example, if you initialize a new shopping cart with a discount of 20% then our total should be discounted in the amount of 20%. So, if our total were $100, after the discount you only would owe $80.

#If our shopping cart does not have an employee discount, then it should return a string saying: "Sorry, there is no discount to apply to your cart :("
    def apply_discount(self):
        if self.employee_discount:
            return self.total * (1 - self.employee_discount / 100)
        else:
            print("Sorry, there is no discount to apply to your cart :(")

    def void_last_item(self):
        if self.items:
            self.total += -(self.items[-1][1] * self.items[-1][2])
            self.items.pop()
            return self.total
        else:
            print("There are no items in your cart!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    