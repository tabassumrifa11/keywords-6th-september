print('\033c')

def dueamount(b,g):
    return g-b


bill = int(input("Enter the bill:"))
given = int(input("Enter the given amount:"))


due = dueamount(bill,given)


print(f"Bill: {bill}\nGiven: {given}\nDue amount = {due}")