import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp): 
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):   # DONE!
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    x = datetime.fromisoformat(iso_string)
    # print(x.strftime("%A %d %B %Y"))
    return x.strftime("%A %d %B %Y")
    
    """
    %A Weekday, full version Wednesday
    %d Day of month 31
    %B Month name, full version December
    %Y Year, full version 2018
    """

def convert_f_to_c(temp_in_farenheit): # DONE
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_c_float = ((float(temp_in_farenheit) - 32) * (5/9))
    rounded_temp = round(temp_in_c_float,1)
    return rounded_temp


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    #def calculate_mean(a, b):
        #total = a + b
        #mean = total / 2
    
    #return mean
    #print(calculate_mean(3, 4))2

    total = 0

    for list_item in weather_data:
        total += float(list_item)

    mean_value = total / len(weather_data)
    
    return mean_value 

#print(calculate_mean([51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43])) (to run the test while working in waether.py to determine what's being printed)

def load_data_from_csv(csv_file):   # DONE
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    
    weather_data = []   
    with open(csv_file) as csv_file:   # you can name csv_file anything
        reader = csv.reader(csv_file)
        for line in reader:
            if line != []:
                weather_data.append(line)

    weather_data_integer = weather_data[1:] # deletes 1st row from the tests (contains headings in string format)/data/example csv files
    
    for daily_data_format    in weather_data_integer:
        daily_data_format[1] = int(daily_data_format[1]) # daily_data_format refers to the presentation of each line: (datetime_str, min_int, max_int)
        daily_data_format[2] = int(daily_data_format[2])

    return weather_data_integer


def find_min(weather_data): #[34,25, 18, 57, 69]
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list.
    """

    if weather_data == []:
        return ()
    else:
        min_value = weather_data[0]
        index = 0
        min_index = 0

        for num in weather_data:
            if float(num) <= float(min_value):
                min_value = float(num)
                min_index = index

            index += 1
        
    return (min_value, min_index)
        

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """

    if weather_data == []:
        return ()
    else:
        max_value = weather_data[0]
        index = 0
        max_index = 0

        for num in weather_data:
            if float(num) >= float(max_value):
                max_value = float(num)
                max_index = index

            index += 1
        
    return (max_value, max_index)
    

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.

    My Notes:
    The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
    The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
    The average low this week is 12.2°C.
    The average high this week is 17.8°C.
    """
    
    list_min = []
    for list_all_mins in weather_data:
        list_min.append(list_all_mins[1])

    list_max = []
    for list_all_max in weather_data:
        list_max.append(list_all_max[2])

    low_average = (calculate_mean(list_min))
    high_average = (calculate_mean(list_max))

    min_value, min_index = find_min(list_min)
    max_value, max_index = find_max(list_max)

    result = ""
    no_of_rows = len(weather_data)
    result = result + str(no_of_rows) + " Day Overview\n"
    result = result + "  The lowest temperature will be " 
    result = result + f"{format_temperature(convert_f_to_c(min_value))}"
    result = result + ", and will occur on "
    result = result + f"{convert_date(weather_data[min_index][0])}.\n"
    
    result = result + "  The highest temperature will be " 
    result = result + f"{format_temperature(convert_f_to_c(max_value))}"
    result = result + ", and will occur on "
    result = result + f"{convert_date(weather_data[max_index][0])}.\n"

    result = result + "  The average low this week is "
    result = result + f"{format_temperature(convert_f_to_c(low_average))}.\n"

    result = result + "  The average high this week is "
    result = result + f"{format_temperature(convert_f_to_c(high_average))}.\n"

    return result
#Note: the below is added to see what information is printed when I run the weather.py.
# print(generate_summary([      
#             ["2021-07-02T07:00:00+08:00", 49, 67],
#             ["2021-07-03T07:00:00+08:00", 57, 68],
#             ["2021-07-04T07:00:00+08:00", 56, 62],
#             ["2021-07-05T07:00:00+08:00", 55, 61],
#             ["2021-07-06T07:00:00+08:00", 53, 62]
#         ]))

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    
    My Notes:
    row refers to each input(unformatted) line; sections of the each row e.g.
    date,min,max
    2021-07-02T07:00:00+08:00,49,67
    2021-07-03T07:00:00+08:00,57,68
    2021-07-04T07:00:00+08:00,56,62
    2021-07-05T07:00:00+08:00,55,61
    2021-07-06T07:00:00+08:00,53,62
    [0                         ,1,2] (sections of the list seperated by commas)
    """

    result = "" # this represents output to be produced in string format

    for row in weather_data: 
        result = result + "---- "
        result = result + f"{convert_date(row[0])}"
        result = result + " ----\n"
        
        result = result + "  Minimum Temperature: "
        result = result + f"{format_temperature(convert_f_to_c(row[1]))}"  + "\n"
        
        result = result + "  Maximum Temperature: "
        result = result + f"{format_temperature(convert_f_to_c(row[2]))}" + "\n"
        
        result = result + "\n"
    
    return result
