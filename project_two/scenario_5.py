# Import Pandas
import pandas

# Import Numpy
import numpy

# Import Matplotlib
import matplotlib.pyplot as matplotlib

# Store the url of the Passenger  Google Spreadsheet into a variable
raw_url = 'https://docs.google.com/spreadsheets/d/101XWuT7vCf2AqMMKWFx3_pR1B1ec8CvmOkqEGVjgQgU/edit#gid=0'

# Replace the necessart parts of both URLs
url = raw_url.replace('/edit#gid=', '/export?format=csv&gid=')

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

ages(url)
