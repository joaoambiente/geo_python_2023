"""
These functions are used in Ex3.
They are used to classify celsius temperatures and to convert fahrenheit temperatures to celsius 
"""

def temp_classifier(temp_celsius):
    """
    Function classifies input celsius temperatures into 4 classes [0 to 3] 
    input: temp_celsius: float | int  --> temperature in celsius
    output: class: int
    """
    my_class = 0
    # Temperatures below -2 degrees Celsius
    if temp_celsius < -2:
        my_class = 0
    # Temperatures equal or warmer than -2, but less than +2 degrees Celsius
    elif -2 <= temp_celsius < 2:
        my_class = 1
    # Temperatures equal or warmer than +2, but less than +15 degrees Celsius
    elif 2 <= temp_celsius < 15:
        my_class = 2
    # Temperatures equal or warmer than +15 degrees Celsius
    else:
        my_class = 3

    return my_class


def fahr_to_celsius(temp_fahrenheit):
    """
    Function to convert temperature in fahrenheit to temperature in celsius
    input: temp_fahrenheit:int | float --> temperature in fahrenheit
    output: temperature in celsius:float
    """
    # Formula for converting fhrenheit to celsis
    return (temp_fahrenheit - 32) * 5/9
