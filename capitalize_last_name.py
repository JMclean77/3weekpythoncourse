def names():
    full_name = input("Enter the full name: ")
    if not isinstance(full_name, str):
        raise TypeError("Name must be a string")

    parts= full_name.strip().split()
    if len(parts) != 2:
        return ValueError( "Invalid input please enter a first and last name")

    first_name= parts[0].capitalize()
    last_name= parts[1].upper()

    return f"{first_name} {last_name}"
try:
    result = names()
    print(result)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
