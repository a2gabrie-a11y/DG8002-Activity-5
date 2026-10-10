# Event Ticket Booth Program
TICKET_PRICES = {
    "general": 25.00,
    "student": 15.00,
    "vip": 60.00,
}
# Available tickets for each category
available_tickets = {
    "general": 12,
    "student": 8,
    "vip": 4,
}
# refactor the tax rate and discount threshold into constants for easier maintenance
TAX_RATE = 0.13
# Customers spending $100 or more receive a 10% discount.
DISCOUNT_THRESHOLD = 100.00


def show_menu():
    print("\n=== EVENT TICKETS ===")
    for category, price in TICKET_PRICES.items():
        print(f"{category.title()}: ${price:.2f} ({available_tickets[category]} left)")
    print("Type 'done' to finish your order.")


def calculate_subtotal(order):
    subtotal = 0
    for item in order:
        # Add the price of each ticket to the subtotal
        # FIX: Use the TICKET_PRICES dictionary to get the price of each ticket category.
        subtotal += TICKET_PRICES[item]
    return subtotal

def apply_discount(subtotal):
    # Customers spending more than $100 or equal to $100 receive a 10% discount.
    # FIX: Check if the subtotal is greater than or equal to the discount threshold and apply the discount accordingly.
    if subtotal >= DISCOUNT_THRESHOLD:
        return subtotal * 0.90
    return subtotal

def calculate_total(subtotal):
    # Calculate the total cost, applying the discount if applicable.
    # FIX: Use the apply_discount function to calculate the discounted subtotal before adding tax.
    # FIX: tax is now calculated on the discounted price, not the original subtotal.ge
    discounted = apply_discount(subtotal)
    return discounted + (discounted * TAX_RATE)


def print_receipt(order):
    print("\n=== RECEIPT ===")
    for item in order:
        print(f"{item.title()}: ${TICKET_PRICES[item]:.2f}")
    subtotal = calculate_subtotal(order)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Total (after discount and HST): ${calculate_total(subtotal):.2f}")


def run_ticket_booth():
    order = []
    while True:
        show_menu()
        category = input("Ticket category: ").strip().lower()
        if category == "done":
            break
        if category not in TICKET_PRICES:
            print("Unknown ticket category.")
            continue

        quantity = int(input("How many tickets? "))   
        if quantity > available_tickets[category]:   
            print("Not enough tickets available.")
            continue

        for _ in range(quantity):
            order.append(category)                    
        available_tickets[category] -= quantity
        print(f"Added {quantity} {category} ticket(s).")

    print_receipt(order)


run_ticket_booth()

