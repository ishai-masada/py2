import pandas

def series():
    num_list = [3, 5, 6, 1]
    indices = ["first", "second", "third", "fourth"]

    # Python list to a Pandas Series
    panda_series = pandas.Series(num_list, indices)
    print("Series of numbers\n", panda_series, '\n')

    # Dates from 3/1/22 to 3/12/22
    dates = ["5/1/22", "5/2/22", "5/3/22", "5/4/22", "5/5/22","5/6/22", "5/7/22",
             "5/8/22", "5/9/22", "5/10/22", "5/11/22", "5/12/22"]
    indices = [num for num in range(1, 13)]
    panda_series = pandas.Series(dates, indices)
    print("Series with dates from May 1 to May 12\n", panda_series, '\n')

# df is DataFrame
def df():
    # Print the data using a dictionary type object
    people_dict = {'Name': ['Vinay', 'Kushal', 'Aman'],
              'Age': [22, 25, 24],
              'Occupation': ['Engineer', 'Doctor', 'Accountant']
             }
    people_df = pandas.DataFrame(people_dict)
    print("DataFrame using a dictionary\n", people_df, '\n')

    # Print the data using a list type object
    people_lst = [[2, 'Vishal', 22],
                  [1, 'Kushal', 25],
                  [1, 'Aman', 24]
                 ]
    people_df = pandas.DataFrame(data=people_lst, columns=['ID', 'Name', 'Age'])
    print("DataFrame using a list object\n", people_df, '\n')

    # Reading data from a csv file and converting it into a Dataframe
    people_df = pandas.DataFrame(pandas.read_csv('csv_file.csv'))
    print("DataFrame using data from a csv file\n", people_df, '\n')

    # # Creating a custom index
    people_df.set_index("ID", inplace=True)
    print("DataFrame using the \'ID\' column as the index\n", people_df, '\n')

    # # Sort the DataFrame by the index
    people_df.sort_values(['ID'], inplace=True, ascending=False)
    print("DataFrame sorted by descending index\n", people_df, '\n')

    # # Conditional DataFrame
    people_df.where(people_df["Age"] > 24, inplace=True)
    print("DataFrame with a condition\n", people_df)


series()
df()
