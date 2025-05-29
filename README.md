# Optimization-and-Manufacturing-of-Front-landing-Gear-for-a-15-25-Kg-Class-Unmanned-Aerial-Vehicle

Landing Gear Analysis Workflow
==============================

This repository shows how to run FEA in ANSYS, post-process via ridge regression, visualize results, and compute optimal design parameters.

Files
-----
- `Landing_Gear.wbpj`  
- `analysis 01 landing gear.csv`        ← FEA export (400 points)  
- `regression analysis.py`              ← Ridge regression script  
- `landing gear regression 2.xlsx`      ← Regression output  
- `multiplot.py`                        ← Plotting script  
- `SVD.py`                              ← LQR/SVD-based parameter solver  
- `README.txt`                          ← This file  

Requirements
------------
- ANSYS Workbench (2020 R2 or later)  
- Python 3.8+ with:
    - numpy
    - pandas
    - scikit-learn
    - matplotlib
    - openpyxl  

Steps
-----

1. **FEA in ANSYS Workbench**  
   - Open `Landing_Gear.wbpj`.  
   - Set up the parameter study (400 datapoints over your chosen inputs).  
   - After solution, export the result table to CSV:
     ```
     analysis 01 landing gear.csv
     ```

2. **Ridge Regression**  
   - Make sure `analysis 01 landing gear.csv` is in this folder.  
   - Edit the file path at the top of `regression analysis.py` if needed.  
   - Run:
     ```
     python "regression analysis.py"
     ```
   - This reads `landing gear regression 2.xlsx`, fits ridge models to each output, and prints polynomial equations.  
   - It also writes its fitted coefficients and metrics into:
     ```
     landing gear regression 2.xlsx
     ```

3. **Plot Regression Results**  
   - Place `landing gear regression 2.xlsx` alongside `multiplot.py`.  
   - Run:
     ```
     python multiplot.py
     ```
   - The script will generate comparison plots (actual vs. predicted, residuals, etc.).

4. **Optimal Parameters via SVD/LQR**  
   - Edit the workbook path inside `SVD.py` (currently points to `Book1.xlsx`).  
   - Ensure your input data file (e.g. `Book1.xlsx`) is in place.  
   - Run:
     ```
     python SVD.py
     ```
   - This computes the pseudoinverse solution (or LQR-style R matrix) and writes results back into the Excel file.

Notes
-----
- All scripts assume files are in the same directory—adjust paths if you reorganize.  
- Regression and SVD scripts overwrite existing Excel workbooks—back up if needed.  
- For alternative weighting in the SVD/LQR step, modify cost or tolerance parameters inside `SVD.py`.
