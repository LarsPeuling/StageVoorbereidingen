class product:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def __str__(self):
        return f"Product[ID: {self.id}, Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}]"
    
    
class warehouse:
    def __init__(self):
        self.products = []
        
    # adds product to the self.products list
    # if product with the same id already exists, it will not be added again   
    def add_product(self, product):
        if self.get_product_by_id(product.id) is None:
            self.products.append(product)
        else:
            print("Product with this ID already exists.")
            return
        print("product added successfully")
    
    def update_quantity(self, id, quantity):
        prod = self.get_product_by_id(id)
        if prod is not None:
            prod.quantity = quantity
            print("Quantity updated successfully")
        else:
            print("Product not found.")
            
        if prod.quantity + quantity < 0:
            print("Insufficient stock to remove the specified quantity.")    
        else:
            print("Product not found.")
            
    def remove_product(self, id):
        prod = self.get_product_by_id(id)
        if prod is not None:
            self.products.remove(prod)
            print("Product removed successfully")
        else:
            print("Product not found.")
            
    def view_products(self):
        if not self.products:
            print("No products in the warehouse.")
            return
        
        for product in self.products:
            print(product)
    
    # retrieve product by id
    # if product is inside the self.products list, the product is returned
    # if the product is not in the self.products list, None is returned (the product is not inside the warehouse)
    def get_product_by_id(self, id):
        for product in self.products:
            if product.id == id:
                return product
        return None
    
    
    
    
    
def main():
    wh = warehouse()
    while True:
        print("\nLars' Warehouse Management System")
        print("----------------------------------")
        print("1. Add product")
        print("2. View products")
        print("3. Update product quantity")
        print("4. Remove product")
        print("5. Exit")
        
        
        choise = input("Enter your choice (1-5): \n")
        
        if choise == '1':
            try:
                pId = int(input("Enter product ID: "))
                pName =  input("Enter product name: ")
                pQty = int(input("Enter product quantity: "))
                pPrice = float(input("Enter product price: "))
            
                if pQty == 0 or pPrice == 0:
                    print("Quantity and Price must be greater than zero.")
                    continue
            
                prod = product(pId, pName, pQty, pPrice)
                wh.add_product(prod)
                
            except ValueError:
                print("Invalid input. Please enter correct data types.")
                
        
        if choise == '2':
            wh.view_products()
        
        if choise == '3':
            try:
                pId = int(input("Enter the product Id to update the quantity: "))
                pQty = int(input("Enter the new quantity: "))
                wh.update_quantity(pId, pQty)
            except ValueError:
                print("Invalid input. Please enter correct data types.")
            
        if choise == '4':
            try:
                pId = int(input("Enter the product Id to remove: "))
                wh.remove_product(pId)
            except ValueError:
                print("Invalid input. Please enter correct data types.")
            
        if choise == '5':
            print("Exiting the system. Goodbye!")
            return
        
if __name__ == "__main__":
    main()
        