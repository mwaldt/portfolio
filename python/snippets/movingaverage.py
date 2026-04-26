# Program to calculate moving average
# SMAj=(1/k)∗∑(i=j−1toj+k−1) ai
# where,
#     SMAj = Simple Moving Average of jth window
#     k = size of the window
#     ai = ith element of the set of observations

array = [1, 2, 3, 7, 9]
window_size = 3

i = 0

moving_averages = []

while i < len(array) - window_size + 1:
    window = array[i : i + window_size]
    window_average = round(sum(window) / window_size, 2)
    moving_averages.append(window_average)
    i += 1

print(moving_averages)
