def pascal_triangle(n):
    # Return an empty list if n <= 0
    if n <= 0:
        return []
    
    triangle = [[1]]  # The first row of Pascal's triangle is always [1]

    # Generate each row of Pascal's triangle
    for i in range(1, n):
        prev_row = triangle[-1]  # Get the last row from the triangle
        new_row = [1]  # Start each row with 1
        # Fill in the middle elements of the new row
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # End each row with 1
        triangle.append(new_row)  # Add the new row to the triangle

    return triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

