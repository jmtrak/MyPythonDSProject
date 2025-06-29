def calculates_total_sales(sales_list):
    total = 0
    for item in sales_list:
        try:
            total += float(item)
        except ValueError:
            print(f"Warning: Skipping non-numeric item '{item}'.")
        except TypeError:
            print(f"Warning: Skipping invalid type '{type(item).__name__}' for '{item}'.")
        return total

# Example usage     
daily_figure_clean = [100.5, 250.0, 120, 90, 90.25] 

total1 = calculates_total_sales(daily_figure_clean)
print(f"Total sales: {total1}")

daily_figure_mixed = [100.5, "250.0", 120, 90, "error.value"]

total2 = calculates_total_sales(daily_figure_mixed)
print(f"Total sales (mixed): {total2}")
