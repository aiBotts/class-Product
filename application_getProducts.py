# This program creates a class called Product.
# It will ask the user to enter a product's name, price, and the discount percentage.
# It will display the discount amount along with the discounted price.

# Create the Product class
class Product:
    # Using the initializer method to take and initialize values for name, price, and discountPercent
    def __init__(self, name, price, discountPercent):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent

    # Returning the discount amount
    def discountAmount(self):
        # Multiply the price by the discountPercent / 100 to get the discountAmount
        return self.price * self.discountPercent / 100

    # Returning the discountedPrice
    def discountPrice(self):
        # Subtract discountAmount from price to get the discountedPrice
        return self.price - self.discountAmount()

    # Converting to a string for testing and formatting
    def __str__(self):
        return '\nName: {}\nPrice: {}\nDiscount Percentage: {}%'.format(self.name, self.price, self.discountPercent)


# Asking the user for the product information for two products
userInput_1 = input('Product name: ')
userPrice_1 = float(input('Product price: '))
userDiscount_1 = float(input('Product discount percent: '))
product_1 = Product(userInput_1, userPrice_1, userDiscount_1)
print()

userInput_2 = input('Product two name: ')
userPrice_2 = float(input('Product two price: '))
userDiscount_2 = float(input('Product two discount percent: '))
product_2 = Product(userInput_2, userPrice_2, userDiscount_2)
print()

# Print product_1 (__str__ will executed automatically)
print(product_1)

# Print discount and discountPrice for product_1
print('Discount:', product_1.discountAmount())
print('Discounted Price:', product_1.discountPrice())
print()

# Print product_2 (__str__ will be executed automatically)
print(product_2)

# Print discount and discountPrice for product_2
print('Discount:', product_2.discountAmount())
print('Discounted Price:', product_2.discountPrice())

