variable_balance = 0 

def deposit(amount):
    global variable_balance
    variable_balance += amount
    return variable_balance

amount1 = int(input("how macch money you deposit :")) 

print(deposit(amount1))
