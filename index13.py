from itertools import product

import numpy as np

arr_2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr_2d)

element = arr_2d[1,2]
print(element)

dimension = arr_2d.ndim
print(dimension)

size = arr_2d.size
print(size)

products = ['apples','oranges','tangerine','pears']

sales = [150, 200, 350, 90]

sales_series = pd.Series(sales, index=products)

total_sales = sales_series.sum()

best_selling_product = sales_series.idxmax()

highest_number = sales.series.max()

print(f"Best Selling product: {best_selling_product}")

print(total_sales)


