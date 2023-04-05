def return_10():
    return 10

def add (int1, int2):
    return int1 + int2

def subtract (int1, int2):
    return int1 - int2

def multiply (int1, int2):
    return int1 * int2

def divide (int1, int2):
    return int1 / int2

def length_of_string (str):
    return len(str)

def join_string (str1, str2):
    return str1 + str2

def add_string_as_number (str1, str2):
    return int(str1) + int(str2)

def number_to_full_month_name (int):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[int - 1]

def number_to_short_month_name (int):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return months[int - 1]

# ---------------------

def volume_of_cube(int):
    return int * int * int

def reverse_string (str):
    return str[::-1]

def fahrenheit_to_celsius(fahr):
    return round((fahr - 32) * (5 / 9), 2)