def filter_names_starting_with_m(names):
   if not isinstance(names, list):
        raise TypeError("Input 'names' must be a list.")
    
    return [name for name in names if name.startswith('M')]

if __name__ == "__main__":
    test_names = ["Bosch", "Mexico", "Mango", "Mark", "Blr", "Clean code"]

    filtered_names = filter_names_starting_with_m(test_names)
    print(f"Original names: {test_names}")
    print(f"Names starting with 'M': {filtered_names}")

    # Example demonstrating error handling for non-list input
    try:
        filter_names_starting_with_m("not a list")
    except TypeError as e:
        print(f"Error: {e}")
