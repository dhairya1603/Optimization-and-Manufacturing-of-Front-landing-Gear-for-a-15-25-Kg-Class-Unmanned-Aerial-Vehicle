import numpy as np
import openpyxl
from numpy.linalg import pinv

filepath = r"C:\Users\Dhairya D\Downloads\Book1.xlsx"
# Load the workbook and select the worksheet
wb = openpyxl.load_workbook(filepath)
ws = wb.active  # or wb['SheetName'] for a specific sheet

def svd_pseudoinverse(M, tol=1e-15):
    # M: matrix to invert
    U, S, Vt = np.linalg.svd(M, full_matrices=False)
    # Reciprocal of non-zero singular values
    S_inv = np.array([1/s if s > tol else 0 for s in S])
    # Construct pseudoinverse
    M_pinv = Vt.T @ np.diag(S_inv) @ U.T
    return M_pinv

def solve_for_A_svd(K, x):
    x = np.asarray(x).reshape(-1, 1)
    n = x.shape[0]
    xxT_vec = np.outer(x, x).flatten(order='F')  # Column-major
    # The system is: K = m^T a, where m = vec(xxT), a = vec(A)
    M = xxT_vec.reshape(1, -1)  # Shape (1, n^2)
    # Use SVD pseudoinverse to solve for a
    M_pinv = svd_pseudoinverse(M)
    a = M_pinv @ np.array([K])
    A = a.reshape(n, n, order='F')
    return A

# Given values
K = 0.654
x = [5.77, 0.0014**(-1), 130.13, 0.8955, 40, 100**(-1), 4]


A_estimated = solve_for_A_svd(K, x)
print("Estimated A:\n", A_estimated)

# Verify: Should be close to 100
#x = np.array(x).reshape(-1, 1)
#print("x^T A x =", float(x.T @ A_estimated @ x))

# Iterate over each row, assuming data starts from the first row
for row in ws.iter_rows(min_row=2, max_col=8):  # Adjust min_row if you have headers
    # Extract the first 7 elements as a vector
    vector = [cell.value for cell in row[:7]]
    # Ensure all elements are numbers (skip row if not)
    if all(isinstance(x, (int, float)) for x in vector):
        # Calculate magnitude using numpy
        #vector = np.array(vector).reshape(-1, 1)
        magnitude = np.linalg.multi_dot([np.transpose(vector), A_estimated, vector]) # ||x|| = sqrt(x1^2 + ... + x7^2)[2]
        #print(magnitude)
        # Write the magnitude to the 8th column
        row[7].value = magnitude # 8th cell (index 7)
        print('done')
    else:
        row[7].value = None  # Or handle non-numeric rows as needed

# Save the updated workbook
wb.save(filepath)