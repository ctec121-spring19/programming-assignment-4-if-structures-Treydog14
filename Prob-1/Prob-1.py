# Module 3
#   Programming Assignment 4
#     Prob-1.py

# <Trevor Bromley>

def shippingCost(subtotal):
    shippingCost = 2.99
    # enter code here to test for free
    if subtotal >= 10.00:
        shippingCost = 0


    return shippingCost

def unitTest():
    print("Shipping cost if subtotal < 10.00:\t", shippingCost(5.99))
    # enter additional test code here
    print()


if __name__ == "__main__":
    unitTest()