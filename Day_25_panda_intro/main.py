import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_color = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_color = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_color, cinnamon_color, black_color]
}

hi = pandas.DataFrame(data_dict)
hi.to_csv("Fur Color Count.csv")