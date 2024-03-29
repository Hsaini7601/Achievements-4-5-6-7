def weight_conversion(weight, current_unit):
   
    
    if current_unit.lower() == 'kg':
        return weight * 2.20462  # the value of 1 kg = 2.20462 lb
    elif current_unit.lower() == 'lb':
        return weight * 0.453592  # the value of 1 lb = 0.453592 kg

def length_conversion(length, current_unit):
   # the value of 1 meter = 3.28084 feet and the value of 1 foot = 0.3048 meters

    if current_unit.lower() == 'm':
        return length * 3.28084  
    elif current_unit.lower() == 'ft':
        return length * 0.3048  
def main():
    
    print("Welcome to the unit conversion program!")
    conversion_type = input("What unit you want to convert? Enter '1' for weight or '2' for length: ").strip()

    if conversion_type == '1':
        weight = float(input("Enter the weight: ").strip())
        current_unit = input("Enter the  unit for the weight (kg or lb): ").strip()
        converted_weight = weight_conversion(weight, current_unit)
        print("The converted weight is: {:.2f} {}".format(converted_weight, 'lb' if current_unit.lower() == 'kg' else 'kg'))
    elif conversion_type == '2':
        length = float(input("Enter the length: ").strip())
        current_unit = input("Enter the  unit for the length (m or ft): ").strip()
        converted_length = length_conversion(length, current_unit)
        print("The converted length is: {:.2f} {}".format(converted_length, 'ft' if current_unit.lower() == 'm' else 'm'))
    else:
        print("Invalid input. Please enter '1' for weight unit conversion or '2' for length unit conversion.")

if __name__ == "__main__":
    main()
