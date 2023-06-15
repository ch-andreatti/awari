
fruits_list = ["bananas", "maçãs", "peras", "uvas", "laranjas"]

while True:

    user_input = str(input("Fruta: "))

    if user_input == "999":
        print(fruits_list)
        break
    
    else:
        if user_input not in fruits_list:
            fruits_list.append(user_input)