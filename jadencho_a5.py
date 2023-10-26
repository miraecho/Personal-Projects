# For this program, I will list items that are on sale from Amazon. The user has 5
# different categories to choose from, and each category will have 3 items. First, the program
# will ask the user to select a category. Each category will have 3 items, and the user will have
# to select 1 item out of the 3. Information such as its color, price, and its type and/or brand will
# be displayed for each item.


categories = ['Clothing', 'Electronics', 'Fruits', 'School Supplies', 'Home Maintenance']
items = [['T-shirt', 'Jeans', 'Jacket'],
         ['Laptop', 'Cell Phone', 'TV'],
         ['Apple', 'Banana', 'Orange'],
         ['Pencils', 'Highlighters', 'Staplers'],
         ['Vacuum', 'Duster', 'Floor Mat']]

print 'Welcome to Amazon'
print '-' * 7
# User can start shopping here if he or she chooses to do so
user_shop = raw_input('Would you like start shopping today? (Y or N)? ')
while user_shop == 'Y':
    print 'We have 5 different categories for you to choose from. The categories are:'
    for category in categories:
        print category
    user_category = raw_input('\nEnter a category you would like to choose from: ')

    # If the user selects clothing, then the user gets to choose between
    # T-shirt, jeans, or jacket, respectively
    if user_category == categories[0]:
        print 'The following pieces of clothing are for sale:'
        for clothing in items[0]:
            print clothing
        user_selection = raw_input('\nSelect an item you want more information on: ')
        if user_selection == items[0][0]:
            print 'Here is the information on this ' + items[0][0] + ':\n1) Color: Red\n2) Brand: Levi\'s\n3) Price: $17.99\n'
        elif user_selection == items[0][1]:
            print 'Here is the information on this ' + items[0][1].lower() + ':\n1) Color: Blue\n2) Brand: Calvin Klein\n3) Price: $18.99\n'
        else:
            print 'Here is the information on this ' + items[0][2].lower() + ':\n1) Color: Gray\n2) Brand: Columbia\n3) Price: $20.88\n'

    # If the user selects electronics, then the user gets to choose between
    # laptop, cell phone, or TV, respectively
    elif user_category == categories[1]:
        print 'The following electronics are for sale:'
        for electronic in items[1]:
            print electronic
        user_electronics = raw_input('\nSelect an electronic item you want more information on: ')
        if user_electronics == items[1][0]:
            print 'Here is the information on this ' + items[1][0].lower() + ':\n1) Color: Black\n2) Type: DELL\n3) Price: $700.00\n'
        elif user_electronics == items[1][1]:
            print 'Here is the information on this ' + items[1][1].lower() + ':\n1) Color: Gray\n2) Type: Android\n3) Price: $500.00\n'
        else:
            print 'Here is the information on this ' + items[1][2].lower() + ':\n1) Color: Black\n2) Brand: LED\n3) Price: $1200.00\n'
    
    # If the user selects fruits, then the user gets to choose between
    # apple, banana, or orange, respectively
    elif user_category == categories[2]:
        print 'The following fruits are for sale:'
        for fruit in items[2]:
            print fruit
        user_fruit = raw_input('\nSelect a fruit you want more information on: ')
        if user_fruit == items[2][0]:
            print 'Here is the information on this ' + items[2][0].lower() + ':\n1) Color: Red\n2) Type: Fuji\n3) Price: $5.99\n'
        elif user_fruit == items[2][1]:
            print 'Here is the information on this ' + items[2][1].lower() + ':\n1) Color: Yellow\n2) Type: Plantain\n3) Price: $6.99\n'
        else:
            print 'Here is the information on this ' + items[2][2].lower() + '\n1) Color: Orange\n2) Type: Navel\n3) Price: $4.20\n'

    # If the user selects school supplies, then the user gets to choose between
    # pencils, highlighters, or staplers, respectively
    elif category == categories[3]:
        print 'The following school supplies are for sale:'
        for school_supply in items[3]:
            print school_supply
        user_supply = raw_input('\nSelect the school supply you want more information on: ')
        if user_supply == items[3][0]:
            print 'Here is the information on these ' + items[3][0].lower() + ':\n1) Color: Yellow\n2) Brand: Ticonderoga\n3) Price: $7.00\n'
        elif user_supply == items[3][1]:
            print 'Here is the information on these ' + items[3][1].lower() + ':\n1) Color: Yellow\n2) Brand: Sharpie\n3) Price: $9.99\n'
        else:
            print 'Here is the information on these ' + items[3][2].lower() + ':\n1) Color: Black\n2) Brand: Swingline\n3) Price: $8.00\n'

    # Otherwise choose between vacuum, duster, or floor mat, respectively
    else:
        print 'The following home maintenance products are on sale:'
        for home_products in items[4]:
            print home_products
        user_home = raw_input('\nSelect the home maintenance product you need more information on: ')
        if user_home == items[4][0]:
            print 'Here is the information on this ' + items[4][0].lower() + ':\n1) Color: White\n2) Brand: Dyson\n3) Price: $21.99\n'
        elif user_home == items[4][1]:
            print 'Here is the information on this ' + items[4][1].lower() + ':\n1) Color: Yellow\n2) Brand: Swiffer\n3) Price: $19.99\n'
        else:
            print 'Here is the information on this ' + items[4][2].lower() + ':\n1) Color: Black\n2) Brand: DEXI\n3) Price: $17.99\n'

    # Exits the loop if the user chooses to quit
    user_shop = raw_input('Would you like to continue shopping (Enter Y to continue, N for quit)? ')
print '-' * 7
print 'Thank you for using Amazon. Please come again.'
