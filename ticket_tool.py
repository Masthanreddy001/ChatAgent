from servicenow import create_ticket

def raise_ticket():

    short_desc = input("Enter short description: ")
    long_desc = input("Enter long description: ")

    ticket = create_ticket(short_desc, long_desc)

    print("Ticket created:", ticket)