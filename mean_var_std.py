import numpy as np
def calculate(list, result=None):
    if result is None:
        result = []
        result.extend(l for l in list)
        if len(result) == 9:
            print("The input is correct!")
            numbers = np.array(result)
            square = numbers.reshape((3, 3))
            mean_row = (np.mean(square, axis=0)).tolist()
            mean_column = np.mean(square, axis=1).tolist()
            mean = np.mean(square)
            variance_row = np.var(square, axis=0).tolist()
            variance_column = np.var(square, axis=1).tolist()
            variance = np.var(square)
            std_row = np.std(square, axis=0).tolist()
            std_column = np.std(square, axis=1).tolist()
            std = np.std(square)
            max_row = np.max(square, axis=0).tolist()
            max_column = np.max(square, axis=1).tolist()
            max_all = np.max(square)
            min_row = np.min(square, axis=0).tolist()
            min_column = np.min(square, axis=1).tolist()
            min_all = np.min(square)
            sum_row = np.sum(square, axis=0).tolist()
            sum_column = np.sum(square, axis=1).tolist()
            sum_all = np.sum(square)
            calculations = {
  'mean': [mean_row, mean_column, mean],
  'variance': [variance_row, variance_column, variance],
  'standard deviation': [std_row, std_column, std],
  'max': [max_row, max_column, max_all],
  'min': [min_row, min_column, min_all],
  'sum': [sum_row, sum_column, sum_all]
}
            return calculations
        else:
            raise ValueError("List must contain nine numbers.")


print(calculate([0,1,2,3,4,5,6,7,8]))
