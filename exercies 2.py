colors = []

while True:
    color = input("Enter a color (or press q to quit): ")
    if color == "q":
        break
    colors.append(color)

stop_value = len(colors)

for i in range(stop_value):
    print(colors[i])
