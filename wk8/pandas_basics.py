import pandas

num_list = [3, 5, 6, 1]
def series(py_list):
    indices = ["first", "second", "third", "fourth"]
    panda_series = pandas.Series(py_list, indices)
    print(panda_series, '\n')

    return panda_series

# df is DataFrame
def df():
    # Print the data using a dictionary type object
    people_dict = {'Name': ['Vinay', 'Kushal', 'Aman'],
              'Age': [22, 25, 24],
              'Occupation': ['Engineer', 'Doctor', 'Accountant']
             }
    people_df = pandas.DataFrame(people_dict)
    print(people_df, '\n')

    # # Print the data using a list type object
    people_lst = [[2, 'Vishal', 22],
                  [1, 'Kushal', 25],
                  [1, 'Aman', 24]
                 ]
    people_df = pandas.DataFrame(data=people_lst, columns=['ID', 'Name', 'Age'])
    print(people_df, '\n')

    # Reading data from a csv file and converting it into a Dataframe
    people_df = pandas.DataFrame(pandas.read_csv('csv_file.csv'))
    print(people_df, '\n')

    # # Creating a custom index
    people_df.set_index("ID")
    print(people_df, '\n')

    # # Sort the DataFrame by the index
    people_df.sort_index()
    print(people_df, '\n')

    # # Conditional DataFrame
    # people_df.where(people_df["Age"] > 24, inplace=True)
    # print(people_df)


series(num_list)
df()
