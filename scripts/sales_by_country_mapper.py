#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    
    # Skip empty lines and header
    if not line or line.startswith('Invoice'):
        continue

    # Split the line by ','
    parts = line.split(',')
    if len(parts) == 8:
        invoice,stockcode,description,quantity,invoicedate,price,customer_ID,country  = parts
        try:     
            if len(parts) >= 8:
                # Extract fields (assuming last 6 fields are: quantity, date, time, price, customer_id, country)
                quantity = int(quantity)
                price = float(price)
                
                # Calculate total sale
                total_sale = quantity * price
                
                # Emit key-value pair
                print(f"{country}\t{total_sale}")
                
        except (ValueError, IndexError) as e:
            # Skip malformed lines
            continue
