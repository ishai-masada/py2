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

# Scenario 1
def get_most_expensive(url):
    # Initialize three placeholder variables for the name, make, and cost of the desired car
    most_expensive_name = "Name"
    most_expensive_make = "Make"
    highest_cost = 0

    # Read the data from the Google Spreadsheet into a Pandas DataFrame
    cars_df = pandas.read_csv(url)

    # Set the index to be the ID column of the data
    cars_df.set_index("ID", inplace=True)

    # Sort the data by price in ascending order
    cars_df.sort_values(by=['Price'], ascending=False, inplace=True)

    # Iterate over the rows of the data
    for idx, row in cars_df.iterrows():
        # Set the Cost variable to the car's Cost
        highest_cost = row["Price"]
        # Set the Name variable to the car's Name
        most_expensive_name = row["Name"]
        # Set the Make variable to the car's Make
        most_expensive_make = row["Make"]

        break

    # Display the data of the most expensive car
    print(f'Most expensive car: {most_expensive_make} {most_expensive_name} - ${highest_cost}')

get_most_expensive(url)
