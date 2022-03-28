#####################################################################################
#
# Name:   Ishai Masada
#
# Date:   3/28/22
#
# Purpose:  Use Seaborn and Matplotlib to create plots
#
# Functions:       first_funct, second_funct
#
# Update:   None
#
#####################################################################################
import seaborn
import scipy
import matplotlib.pyplot as pyplot


#####################################################################################
#
# Function Name:  first_funct
#
# Date:           3/28/22
#
# Purpose:       Create several different plots
#
# Who called:           main function
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def first_funct():
    # Get the car crashes data set name
    for name in seaborn.get_dataset_names():
        if name == "car_crashes":
            data_set_name = name

    # Retrieve the correct dataset with the car crashes dataset name
    data_set = seaborn.load_dataset(data_set_name)

    # Set the theme
    seaborn.set_theme(style="darkgrid")

    # Plot a line using the alcohol data
    pyplot.plot(data_set['alcohol'])

    # Plot a line using the speeding data
    pyplot.plot(data_set['speeding'])
    pyplot.show()

    # Set the theme
    seaborn.set_theme(style="darkgrid")

    # Plot a line using the not distracted data with a label
    pyplot.plot(data_set['not_distracted'], label='Not Distracted')

    # Plot a line using the no previous data with a label
    pyplot.plot(data_set['no_previous'], label='No Previous')

    # Add a legend
    pyplot.legend()
    pyplot.show()

#####################################################################################
#
# Function Name:  second_funct
#
# Date:           3/28/22
#
# Purpose:       Create several different plots
#
# Who called:           main function
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def second_funct():
    # Initialize x and y values
    x = [3, 1, 3]
    y = [3, 2, 1]

    # Create a plot using the x and y values with a label
    pyplot.plot(x, y, label='Line')

    # Add a title
    pyplot.title('Line Chart')

    # Add a legend
    pyplot.legend()
    pyplot.show()

    # Initialize x and y values
    x = [10, 20, 30, 40]
    y = [20, 30, 40, 50]

    # Create a plot using the x and y values with a label
    pyplot.plot(x, y)

    # Add a title
    pyplot.title('Simple Plot')

    # Add a legend
    pyplot.legend(['Line 1'])

    # Add an x-axis label
    pyplot.xlabel('x-axis')

    # Add a y-axis label
    pyplot.ylabel('y-axis')
    pyplot.show()

    # Pie Chart

    # Create a list of labels
    labels = ['crocodiles', 'dogs', 'snakes', 'eagles', 'whales', 'lions']

    # Create a list of percentages for each label
    sizes = [25, 10, 30, 10, 15, 10]

    # Designate one label to separate
    exploder = (0, 0, 0.1, 0, 0, 0)

    # Create a plot using the pie method
    pyplot.pie(sizes, labels=labels, startangle=90, shadow=True, explode=exploder)

    # Add a legend
    pyplot.legend()
    pyplot.show()

#####################################################################################
#
# Function Name:  main
#
# Date:           3/28/22
#
# Purpose:       Call all functions
#
# Who called:           None
#
# Functions:             first_funct, second_funct
#
# Update:                 None
#
#####################################################################################
def main():
    # Call both functions
    first_funct()
    second_funct()

main()
