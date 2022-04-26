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

# Scenario 2
def get_cars_by_make(url):
    # Read the data from the Google Spreadsheet into a Pandas DataFrame
    cars_df = pandas.read_csv(url)
    # Set the index to be the ID column of the data
    cars_df.set_index("ID", inplace=True)

    # Initialize an empty DataFrame as a placeholder for the desired cars
    desired_cars = pandas.DataFrame()

    # Establish the make of the desired cars
    desired_make = "Lamborghini"

    print(cars_df)

    print(f"\nThe desired make: {desired_make}")

    # Iterate over the rows of the data
    for idx, row in cars_df.iterrows():
        # Check of the make of the car is equal to the desired make
        if row["Make"] == desired_make:
            # Set the DataFrame equal to the appended value
            desired_cars = desired_cars.append(row)

    # Reset the indices of the data
    desired_cars.reset_index(drop=True, inplace=True)
    print('\n', desired_cars)

get_cars_by_make(url)
