def get_y_vals(data):
    """
    Takes user input to extract table data in list form.
    Length of inclusive start and exclusive end MUST be 6 (i.e. start: 6, end: 11, row: 1).  
    
    :param
    """
    start = int(input("Y value start(inclusive): "))
    end = int(input("Y value end(exclusive): "))
    row = int(input("Row: "))
    return table.iloc [row, start-1:end].tolist() 


def mean(array):
    """This is to get the mean of an array"""
    return sum(array) / len(array)


def linear_coefficients(X, Y):
    """
    Returns m, b used for the equation Y = mX + b.
    
    Parameters:
    X (Array): an array of floats used as the X Values
    Y (Array): an array of floats used as the Y values
    
    Output:
    
    Equation: https://www.statisticshowto.datasciencecentral.com/probability-and
    """
    n_count = len(X)

    m = ((n_count * sum(X * Y)) - (sum(X) * sum(Y))) / ((n_count * sum(X ** 2)) - (sum(X) ** 2))
    b = ((sum(Y) * sum(X**2)) - (sum(X) * sum(X * Y))) / ((n_count * sum(X ** 2)) - (sum(X) ** 2))    
    return m, b


def predict(m, b, x):
    """Generates predicted values."""
    return m * x + b


def r2_score(pred_y, true_y):
    """
    Finds the r2 score
    Equation pulled from http://brokerstir.com/r-squared-value-explained/
    """
    RSS = sum((true_y - pred_y) ** 2)
    TSS = sum((true_y - mean(true_y)) ** 2)
    return (1 - RSS) / (TSS)