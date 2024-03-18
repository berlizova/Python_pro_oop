from datetime import timedelta, datetime


def date_range(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)


def convert_to_datetime(date_str):
    try:
        # Attempt to parse the date using multiple formats
        return datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        try:
            # Attempt to parse the date with different separator formats
            for separator in ['-', '/', ' ', '.']:
                date_str = date_str.replace(separator, '-')
            return datetime.strptime(date_str, "%d-%m-%Y")
        except ValueError as e:
            raise ValueError("Invalid date format") from e


# Inputs
start_date_str = input("Enter the start date (DD-MM-YYYY): ")
end_date_str = input("Enter the end date (DD-MM-YYYY): ")

try:
    start_date = convert_to_datetime(start_date_str)
    end_date = convert_to_datetime(end_date_str)
    if start_date > end_date:
        raise ValueError("Start date cannot be greater than end date.")
except ValueError as e:
    print(f"Error: {e}")
else:
    print("Sequence of dates:")
    for date in date_range(start_date, end_date):
        print(date.strftime("%d-%m-%Y"))
