from conversion import (    km_to_miles, miles_to_km,    celsius_to_fahrenheit, fahrenheit_to_celsius ) 
while True:    
    print("\\n--- UNIT CONVERTER ---")    
    print("1. Kilometres to Miles")    
    print("2. Miles to Kilometres")    
    print("3. Celsius to Fahrenheit")    
    print("4. Fahrenheit to Celsius")    
    print("5. Exit")    
    choice = input("Enter your choice (1-5): ")    
    if choice == "5":        
        print("Exiting Unit Converter. Thank you!")        
        break    
    elif choice in ("1", "2", "3", "4"):        
        value = float(input("Enter value to convert: "))        
        if choice == "1":            
            result, unit = km_to_miles(value), "miles"        
        elif choice == "2":            
            result, unit = miles_to_km(value), "km"        
        elif choice == "3":            
            result, unit = celsius_to_fahrenheit(value), "degrees F"        
        else:            
            result, unit = fahrenheit_to_celsius(value), "degrees C"        
        print(f"Converted value: {result:.2f} {unit}")    
    else:        
        print("Invalid choice. Please select 1 to 5.")