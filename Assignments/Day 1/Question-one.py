def find_leap_year(year):
    '''
    function to determine if an year is a leap year.
    returns a boolean true if its a leap year and false if it isn't.
    '''
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    return False

while True:
    '''
    A while loop for outputing if a year is leap year or not.
    It calls the function above indorder to know if a year ia a leap year or not
    '''
    year = int(input("Enter a year"))
    if year == 0:
        break
    if find_leap_year(year):
        print(f"{year} is a leap year.")
    else: 
        print(f"{year} is not leap year")
