import seaborn
import matplotlib.pyplot as pyplot

def first_funct():
    for name in seaborn.get_dataset_names():
        if name == "car_crashes":
            data_set_name = name

    data_set = seaborn.load_dataset(data_set_name)

    seaborn.set_theme(style="darkgrid")
    pyplot.plot(data_set['alcohol'])
    pyplot.plot(data_set['speeding'])
    pyplot.show()

    seaborn.set_theme(style="darkgrid")
    pyplot.plot(data_set['not_distracted'], label='Not Distracted')
    pyplot.plot(data_set['no_previous'], label='No Previous')
    pyplot.legend()
    pyplot.show()

def second_funct():
    x = [3, 1, 3]
    y = [3, 2, 1]

    pyplot.plot(x, y, label='Line')
    pyplot.title('Line Chart')
    pyplot.legend()
    pyplot.show()

    x = [10, 20, 30, 40]
    y = [20, 30, 40, 50]

    pyplot.plot(x, y)
    pyplot.title('Simple Plot')
    pyplot.legend(['Line 1'])
    pyplot.xlabel('x-axis')
    pyplot.ylabel('y-axis')
    pyplot.show()

    # Pie Chart
    labels = ['crocodiles', 'dogs', 'snakes', 'eagles', 'whales', 'lions']
    sizes = [25, 10, 30, 10, 15, 10]
    exploder = (0, 0, 0.1, 0, 0, 0)
    pyplot.pie(sizes, labels=labels, startangle=90, shadow=True, explode=exploder)
    pyplot.legend()
    pyplot.show()

def main():
    first_funct()
    second_funct()

main()
