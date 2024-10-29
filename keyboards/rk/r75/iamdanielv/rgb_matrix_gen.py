import json

number_of_rows = 6
cols = [14, 15, 15, 14, 14, 9]  # in order of rows

calculated_matrix = []

for row_position in range(number_of_rows):
    for col_position in range(cols[row_position]):
        number_of_cols = cols[row_position]

        x = 224 / (number_of_cols - 1) * col_position
        y = 64 / (number_of_rows - 1) * row_position
        calculated_matrix.append(
            {
                "matrix": [row_position, col_position],
                "x": int(x),
                "y": int(y),
                "flags": 4,
            }
        )

for i in calculated_matrix:
    print(json.dumps(i) + ",")
