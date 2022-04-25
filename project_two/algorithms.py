# Import Pandas
import pandas

# Import Numpy
import numpy

# Import Matplotlib
import matplotlib.pyplot as matplotlib

# Store the url of the Cars Google Spreadsheet into a variable
part_1_url = 'https://docs.google.com/spreadsheets/d/1OntrAAivWeLHR35wRHg5EY5e-O-CmY16MUMzroV3JYY/edit#gid=0'

# Store the url of the Passenger  Google Spreadsheet into a variable
part_2_url = 'https://docs.google.com/spreadsheets/d/101XWuT7vCf2AqMMKWFx3_pR1B1ec8CvmOkqEGVjgQgU/edit#gid=0'

# Replace the necessart parts of both URLs
url_1 = part_1_url.replace('/edit#gid=', '/export?format=csv&gid=')
url_2 = part_2_url.replace('/edit#gid=', '/export?format=csv&gid=')

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

# Scenario 2
def get_car_by_make(url):
    # Read the data from the Google Spreadsheet into a Pandas DataFrame
    cars_df = pandas.read_csv(url)
    # Set the index to be the ID column of the data
    cars_df.set_index("ID", inplace=True)

    # Initialize an empty DataFrame as a placeholder for the desired cars
    desired_cars = pandas.DataFrame()

    # Establish the make of the desired cars
    desired_make = "Lamborghini"
    print(f"The desired make: {desired_make}")

    # Iterate over the rows of the data
    for idx, row in cars_df.iterrows():
        # Check of the make of the car is equal to the desired make
        if row["Make"] == desired_make:
            # Set the DataFrame equal to the appended value
            desired_cars = desired_cars.append(row)

    # Reset the indices of the data
    desired_cars.reset_index(drop=True, inplace=True)
    print(desired_cars)

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

# Scenario 4
def get_economy(url):
    # Read the data from the Google Spreadsheet into a Pandas DataFrame
    people_df = pandas.read_csv(url)
    # Set the index to be the ID column of the data
    people_df.set_index("ID", inplace=True)

    # Create a DataFrame with the people from the Economy Class
    people_df = people_df.where(people_df["Class"] == 'Economy').dropna()

    return people_df

# Scenario 5
def ages(url):
    # Read the data from the Google Spreadsheet into a Pandas DataFrame
    people_df = pandas.read_csv(url)
    # Set the index to be the ID column of the data
    people_df.set_index("ID", inplace=True)

    # Initialize lists to store the ages of the males and females
    x_males = []
    x_females = []

    # Iterate over the rows of the data
    for idx, row in people_df.iterrows():
        # Check if the column is for Males
        if row["Gender"] == "Male":
            # Add the age to the male ages list
            x_males.append(row["Age"])
        # Check if the column is for Females
        elif row["Gender"] == "Female":
            # Add the age to the female ages list
            x_females.append(row["Age"])

    # Create the subplots structured as 1 row by 2 columns
    fig, (ax0, ax1) = matplotlib.subplots(1, 2)

    # Create the first histogram for the males
    ax0.hist(x_males, rwidth=1)
    # Set the x-label
    ax0.set_xlabel("Age")
    # Set the y-label
    ax0.set_ylabel("Count")
    # Set the title of the plot
    ax0.set_title("Male Passenger Distribution")

    # Create the second histogram for the females
    ax1.hist(x_females, rwidth=0.5)
    # Set the x-label
    ax1.set_xlabel("Age")
    # Set the y-label
    ax1.set_ylabel("Count")
    # Set the title of the plot
    ax1.set_title("Female Passenger Distribution")

    # Arange the default layout for the figure
    fig.tight_layout()

    # Display the figure
    matplotlib.show()
