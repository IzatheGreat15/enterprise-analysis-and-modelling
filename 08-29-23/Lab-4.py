import numpy as np

# Function to input a 3x3 matrix from the user
def input_matrix():
    matrix = []
    print("Enter the elements of the 3x3 matrix:")
    for i in range(3):
        row = []
        for j in range(3):
            element = float(input(f"Enter element at position ({i}, {j}): "))
            row.append(element)
        matrix.append(row)
    return matrix

# Function to input coefficients from the user
def input_coefficients(degree):
    # empty
    poly = np.array([])

    for i in range(degree + 1):
        coefficient = float(input(f"Enter coefficient for x^{i}: "))
        poly = np.append(poly, coefficient)
    
    return poly

def number_one():
    matrix = input_matrix()

    # Convert the 2D list into a numpy array
    np_matrix = np.array(matrix)

    print("Matrix:")
    print(np_matrix)

    # a.) Print the diagonal of the matrix
    diagonal = np.diag(np_matrix)
    print("Diagonal elements:", diagonal)

    # b.) Print the inverse of the matrix
    try:
        inverse = np.linalg.inv(np_matrix)
        print("Inverse matrix:")
        print(inverse)
    except np.linalg.LinAlgError:
        print("The matrix is singular and doesn't have an inverse.")

    # c.) Print the determinant of the matrix
    determinant = np.linalg.det(np_matrix)
    print("Determinant:", determinant)

def number_two():
    degree = int(input("Enter the degree: "))
    print(degree)

    poly = input_coefficients(degree)

    # a.) Print the roots of the polynomial
    roots = np.roots(poly)
    print("The roots are: ", roots)

    # b.) Print the derivative of the polynomial
    derivative = np.polyder(poly)
    print("The coefficients of the derivative are: ", derivative)

    # c.) Print the integration of the polynomial
    integration = np.polyint(poly)
    print("The coefficients of the integral are: ", integration)

def number_three():
    vectorA = input_matrix()
    vectorB = input_matrix()

    # a.) Print the dot product of the two vectors
    dot = np.dot(vectorA, vectorB)
    print("Dot product: \n", dot)

    # b.) Print the cross product of the two vectors
    cross = np.cross(vectorA, vectorB)
    print("Cross Product: \n", cross)

    # c.) Print the magnitude of the cross product
    magnitude = np.linalg.norm(cross)
    print("Magnitude of the Cross Product: \n", magnitude)

def number_four():
    array = []

    # input 10 floating points
    for i in range(10):
        x = float(input(f"Enter a floating-point number: "))
        array = np.append(array, x)
    
    # a.) Print the mean
    mean = array.mean()
    print("Mean of the array: ", mean)

    # b.) Print all elements that are greater than 2
    arrayGreaterThan2 = array[array > 2]
    print("Elements that are greater than 2: ", arrayGreaterThan2)

    # c.) Print the first five highest values in descending order
    descendingOrder = sorted(array, reverse=True)
    slicedArray = descendingOrder[:5]
    print(slicedArray)
    




# Main function
def main():
    # number_one()  
    # number_two()  
    # number_three()
    number_four()

if __name__ == "__main__":
    main()