# UNUSABLE CODE
# Cannot install Pandas due to a lack of space. Following code is for the discussion
# post purpose only

import pandas

titanic = pandas.read_excel("titanic.xls")
titanic.describe()
names, ages = titatic.loc[:, 'name'], titatic.loc[:, 'age']
print(f'Ages: {ages} \n Names: {names}')
