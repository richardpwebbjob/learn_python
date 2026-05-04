# helpers.py

# Multiply quantity by price to compute item total
def calculate_total(quantity, price):
    """Calculate total for a single item"""
    return quantity * price

# Format a numeric amount as a USD currency string
def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"
