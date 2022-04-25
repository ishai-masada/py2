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

# Scenario 4
def get_economy(url):
    # Read the data from the Google Spreadsheet into a Pandas DataFrame
    people_df = pandas.read_csv(url)
    # Set the index to be the ID column of the data
    people_df.set_index("ID", inplace=True)

    # Create a DataFrame with the people from the Economy Class
    people_df = people_df.where(people_df["Class"] == 'Economy').dropna()

    print(people_df)

get_economy(url)
