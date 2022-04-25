# Import Pandas
import pandas

# Import Numpy
import numpy

# Import Matplotlib
import matplotlib.pyplot as matplotlib

# Store the url of the Cars Google Spreadsheet into a variable
raw_url = 'https://docs.google.com/spreadsheets/d/1OntrAAivWeLHR35wRHg5EY5e-O-CmY16MUMzroV3JYY/edit#gid=0'

# Replace the necessart parts of both URLs
url = raw_url.replace('/edit#gid=', '/export?format=csv&gid=')

# Scenario 3
def get_expensive_power(url):
    # Read the data from the Google Spreadsheet into a Pandas DataFrame
    cars_df = pandas.read_csv(url)

    # Set the index to be the ID column of the data
    cars_df.set_index("ID", inplace=True)

    # Sort the data by price in ascending order
    cars_df.sort_values(by=['Price'], ascending=False, inplace=True)

    # Reset the indices of the data
    cars_df.reset_index(drop=True, inplace=True)

    # Initialize an empty DataFrame as a placeholder for the desired cars
    desired_cars = pandas.DataFrame()

    # Initialize a count variable
    count = 0

    # Iterate over the data to get the first five rows of the DataFrame
    for idx, row in cars_df.iterrows():
        # Set the DataFrame equal to the appended value
        desired_cars = desired_cars.append(row)

        # Increment the count variable
        count += 1

        # Check if the count variable is less than 4
        if count > 4:
            break

    # Display the information of the five cars aranged by price
    print(f'Top five cars sorted by price: \n', desired_cars)

    # Sort the data by Horsepower in ascending order
    desired_cars.sort_values(by=['Horsepower'], ascending=False, inplace=True)

    # Reset the indices of the data
    desired_cars.reset_index(drop=True, inplace=True)

    # Display the information of the five cars aranged by Horsepower
    print(f'\nSorted by Horsepower: \n', desired_cars)

get_expensive_power(url)
