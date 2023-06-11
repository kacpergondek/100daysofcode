import pandas as pd

data_path = '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
data = pd.read_csv(data_path)
fur_data = data['Primary Fur Color']

Primary_color = {}

Primary_color['Gray'] = len(fur_data[fur_data == 'Gray'])
Primary_color['Cinnamon'] = len(fur_data[fur_data == 'Cinnamon'])
Primary_color['Black'] = len(fur_data[fur_data == 'Black'])

new_data_frame = pd.DataFrame(data=Primary_color, index=[0])

new_data_frame.to_csv("Squirrel_count.csv")