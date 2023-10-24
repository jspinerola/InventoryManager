#Main Code

numOfProducts = input("Enter amount of products: ")
productList = []

for i in range(int(numOfProducts)):
    product = input("enter product: ")
    category = input("category: ")
    quantity = int(input("quantity: "))

    newProduct = {
        "Product": product,
        "Category": category,
        "Quantity": quantity
    }
    productList.append(newProduct)

for i in range(len(productList)):
    print(productList[i])

def selectProduct():
    num = int(input("Which product? (index value): "))
    yesorno = input("Add or subtract? (+ or -):")
    if yesorno == "+":
        productList[int(num)]["Quantity"] += 1
        print(productList[i]["Quantity"])
    elif yesorno == "-":
        productList[int(num)]["Quantity"] -= 1
        print(productList[i]["Quantity"])

userInput = ""
while userInput != "n":
    userInput = input("Do you want to change the quantity of a product? (y/n): ")
    if userInput == "n":
        break
    selectProduct()
