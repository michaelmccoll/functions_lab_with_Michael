def return_10():
    return 10

def add(first_number,second_number):
    return (first_number + second_number)

def subtract(number_1, number_2):
    return (number_1 - number_2)

def multiply(number_1, number_2):
    return (number_1 * number_2)

def divide(number_1, number_2):
    return (number_1 / number_2)

def length_of_string(test_string):
    return len(test_string)

def join_string(string_1, string_2):
    return (string_1 + string_2)

def add_string_as_number(string_1, string_2):
    return (int(string_1) + int(string_2))

def number_to_full_month_name(number):
    months = {
        1:"January",
        2:"February",
        3:"March",
        4:"April",
        5:"May",
        6:"June",
        7:"July",
        8:"August",
        9:"September",
        10:"October",
        11:"November",
        12:"December"
    }
    return months[number]

def number_to_short_month_name(number):
    months = {
        1:"Jan",
        2:"Feb",
        3:"Mar",
        4:"Apr",
        5:"May",
        6:"Jun",
        7:"Jul",
        8:"Aug",
        9:"Sep",
        10:"Oct",
        11:"Nov",
        12:"Dec"
    }
    return months[number]

def cube(length):
    return length **3

def reverse(text_var):
    return text_var[::-1]

def converter(farenheit):
    return (farenheit - 32) * (5/9)