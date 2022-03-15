import pandas

def series(py_list):
    num_list = [3, 5, 6, 1]
    indices = ["first", "second", "third", "fourth"]
    panda_series = pandas.Series(py_list, indices)
    print(panda_series)

    return panda_series

# df is DataFrame
def df():
    # Print the data using a dictionary type object
    # people_dict = {'Name': ['Vinay', 'Kushal', 'Aman'],
    #           'Age': [22, 25, 24],
    #           'Occupation': ['Engineer', 'Doctor', 'Accountant']
    #          }
    # people_df = pandas.DataFrame(people_dict)
    # print(people_df)

    # Print the data using a list type object
    # people_lst = [[2, 'Vishal', 22],
    #               [1, 'Kushal', 25],
    #               [1, 'Aman', 24]
    #              ]
    # people_df = pandas.DataFrame(people_lst)
    # people_df.columns = ['ID', 'Name', 'Age']
    # print(people_df)

    # Reading data from a csv file and converting it into a Dataframe
    people_df = pandas.DataFrame(pandas.read_csv('csv_file.csv'))
    # print(people_df)

    # Creating a custom index
    people_df.set_index("ID", inplace=True)
    # print(people_df)

    # Sort the DataFrame by the index
    people_df.sort_index()
    # print(people_df)

    # Conditional DataFrame
    people_df.where(people_df["Age"] > 24, inplace=True)
    # print(people_df)


# series(num_list)
# df()
