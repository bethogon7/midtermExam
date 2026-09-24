print("=========================================")
print('     Sales Record Management System ')
print("=========================================")
print('1. Add Sale Record')
print('2. View All Records & Summary Statistics')
print('3. Clear All Sales Data')
print('4. Exit System')
print("=========================================")

option= int(input('Enter the number of option you would like to execute : '))
if option==1:
    item=input('Enter item name: ')
    quantity=int(input('Enter quantity sold: '))
    pricePerUnit=float(input('Enter the price per unit: '))
    totalAmount= quantity * pricePerUnit
    print('Item name: ' + item)
    print('Quantity: '+ quantity)
    print('Price per unit: ' + pricePerUnit)
    print('Total amount: ' + totalAmount)


elif option==4:
    print('Thank you for using the Sales Record Management System')
    exit()







