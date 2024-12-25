def calculate_area(width, length):
    area = width * length
    print(area)

square_area = [20, 40]

calculate_area(square_area[0], square_area[1])

calculate_area(*square_area)