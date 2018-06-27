import numpy as np

np_height = np.round(np.random.normal(1.75, 0.20, 501), 2)
np_weight = np.round(np.random.normal(60.32, 15, 501), 2)
np_city = np.column_stack((np_height, np_weight))

# Average height of people in the city
avg_height = np.mean(np_city[:, 0])
print("Average height of people in the city is: ", avg_height, "mts.")

# Average weight of people in the city
avg_weight = np.mean(np_city[:, 1])
print("Average weight of people in the city is: ", avg_weight, "kg.")

# Height of middle person in the city
mid_height = np.median(np_city[:, 0])
print("Height of middle person of the city is: ", mid_height, "mts.")

# Weight of middle person in the city
mid_weight = np.median(np_city[:, 1])
print("Weight of the middle person of the city is: ", mid_weight, "kg.")

# To check how height and weight are correlated
cor = np.corrcoef(np_city[:, 0], np_city[:, 1])
print("The correlation between height and weight is: ", cor)

# To find the standard deviation of height
sd_height = np.std(np_city[:, 0])
print("The standard deviation of height is: ", sd_height)

# To find the standard deviation of weight
sd_weight = np.std(np_city[:, 1])
print("THe standard deviation of weight is: ", sd_weight)

# To find the bmi
bmi = np_weight / np_height ** 2
print("The body mass index of people in the city are: ", bmi)
