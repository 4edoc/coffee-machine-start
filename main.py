MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


##start of the program
def prepare_espresso():
    check_resource()
    drink_ready = False


def prepare_latte():
    check_resource()
    drink_ready = False


def prepare_cappuccino():
    check_resource()
    if enough resource
        prepare coffee
    else
        refund money
    drink_ready = False

def shutdown():
    print("Machine would be shutdown for maintenance")
    break


def resource_report():
    """check the resource status from subtrating the original resource dict """""
    print(f"Resource status : {resources[water][milk][coffee]}")


off = 0
drink_ready = 0

def coffee_menu():
    user_input = input("What would you like ? (espresso/latte/cappuccino):  ").lower()
    # check the user's input to decide what to do next
    if user_input == "espresso":
        check_resource()
        pay_price()
        prepare_coffee_espresso()
    elif user_input == "latte":
        check_resource()
        prepare_coffe_latte()
    elif user_input == "cappuccino":
        check_resource()
        prepare_coffe_cappuccino()
    ## Turn off the coffee machine for maintenance
    elif user_input == "off":
        shutdown()

def coffee_program():
    if drink_ready == True:
        print(f"Your {user_input} is ready")
        coffee_program()


def print_report():
    user_input = input("Select Mode : Report /Off)
    if user_input == "report":
        print(resource_report())
    elif user_input == "off":
##        turn off the machine

## check transaction successful ?
def check_money():
    if user_input == espresso:
        check_amount == amount paid by the customer
        if overpaid then return the money
        ## Here is the $2.45 dollars in change.
            ## change should be rounded to 2 decimal places
        if underpaid, refund or aks for full money
    return if transaction is successfull

def make_coffee():
    check if transcation is successfull then prepare coffee
    check if enough resource to make coffee
        then deduct the ingredients from the coffee_machine_resources()
    print report before preparing the coffee
    print report after coffee is prepared

final_report():
    once the resource has been deducated the print "Here is your latte enjoy".