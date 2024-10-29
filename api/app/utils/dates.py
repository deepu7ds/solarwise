from datetime import datetime


# DO NOT CHANGE THIS
__from = 1979
# This can change to the current year by the operator
__to = 2024

__valid_year_range = range(__from, __to + 1)


def get_valid_year_range():
    return __valid_year_range


def is_valid_date(date_string):
    """
    checks if a given date is valid in YYYY-MM-DD format
    """
    try:
        # Attempt to create a datetime object with the given string
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        # If it raises a ValueError, the date is not valid
        return False


def is_valid_year(year: int):
    """
    checks if the given year is within the valid range
    """
    return year in __valid_date_range


def get_month(month_number: int):
    """
    Converts the month number to the month name
    """
    date = datetime(1900, month_number, 1)
    return date.strftime("%B")


def get_current_year():
    date = datetime.now()
    return date.strftime("%Y")


"""
Tests
"""
if __name__ == "__main__":

    # The current year test
    print("year: ", get_current_year())