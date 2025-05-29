import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import itertools

def x_directional_deformation_max(length_of_rectangle, width, Thickness, radius, angular_vertical_LENG):
    return (0.1216 +
            0.0001*length_of_rectangle**-2 +
            0.0007*length_of_rectangle**-1 +
            0.0114*length_of_rectangle**1 -
            0.0001*length_of_rectangle**2 +
            0.0001*width**-2 +
            0.0008*width**-1 -
            0.0135*width**1 +
            0.0001*width**2 +
            0.0238*Thickness**-2 +
            0.0283*Thickness**-1 -
            0.0605*Thickness**1 +
            0.0036*Thickness**2 -
            0.0000*radius**-2 -
            0.0000*radius**-1 +
            0.0019*radius**1 -
            0.0000*radius**2 -
            0.0000*angular_vertical_LENG**-2 -
            0.0000*angular_vertical_LENG**-1 +
            0.0017*angular_vertical_LENG**1 -
            0.0000*angular_vertical_LENG**2) * 0.01

def y_directional_deformation_max(length_of_rectangle, width, Thickness, radius, angular_vertical_LENG):
    return (-1093.8055 +
            0.0013*length_of_rectangle**-2 +
            0.0066*length_of_rectangle**-1 +
            13.4884*length_of_rectangle**1 -
            0.1454*length_of_rectangle**2 +
            0.0028*width**-2 +
            0.0317*width**-1 -
            3.2511*width**1 +
            0.0227*width**2 +
            11.7055*Thickness**-2 +
            16.1720*Thickness**-1 -
            72.8821*Thickness**1 +
            4.9452*Thickness**2 +
            0.0000*radius**-2 +
            0.0016*radius**-1 -
            5.5748*radius**1 +
            0.0199*radius**2 -
            0.0000*angular_vertical_LENG**-2 -
            0.0025*angular_vertical_LENG**-1 +
            18.6689*angular_vertical_LENG**1 -
            0.0572*angular_vertical_LENG**2) * 0.1

def equivalent_elastic_strain_max(length_of_rectangle, width, Thickness, radius, angular_vertical_LENG):
    return (0.1303 +
            0.0000*length_of_rectangle**-2 +
            0.0000*length_of_rectangle**-1 +
            0.0048*length_of_rectangle**1 -
            0.0001*length_of_rectangle**2 +
            0.0000*width**-2 +
            0.0000*width**-1 -
            0.0051*width**1 +
            0.0000*width**2 +
            0.0135*Thickness**-2 +
            0.0184*Thickness**-1 -
            0.0807*Thickness**1 +
            0.0063*Thickness**2 -
            0.0000*radius**-2 -
            0.0000*radius**-1 -
            0.0000*radius**1 +
            0.0000*radius**2 -
            0.0000*angular_vertical_LENG**-2 -
            0.0000*angular_vertical_LENG**-1 +
            0.0021*angular_vertical_LENG**1 -
            0.0000*angular_vertical_LENG**2) * 0.01

def equivalent_stress_max(length_of_rectangle, width, Thickness, radius, angular_vertical_LENG):
    return (260.6846 +
            0.0026*length_of_rectangle**-2 +
            0.0222*length_of_rectangle**-1 +
            9.5784*length_of_rectangle**1 -
            0.1012*length_of_rectangle**2 +
            0.0043*width**-2 +
            0.0517*width**-1 -
            10.1273*width**1 +
            0.0850*width**2 +
            26.9058*Thickness**-2 +
            36.8584*Thickness**-1 -
            161.4989*Thickness**1 +
            12.5371*Thickness**2 -
            0.0000*radius**-2 -
            0.0002*radius**-1 -
            0.0988*radius**1 +
            0.0047*radius**2 -
            0.0000*angular_vertical_LENG**-2 -
            0.0006*angular_vertical_LENG**-1 +
            4.1899*angular_vertical_LENG**1 -
            0.0137*angular_vertical_LENG**2)

def maximum_shear_stress_max(length_of_rectangle, width, Thickness, radius, angular_vertical_LENG):
    return (133.9739 +
            0.0013*length_of_rectangle**-2 +
            0.0113*length_of_rectangle**-1 +
            4.8041*length_of_rectangle**1 -
            0.0507*length_of_rectangle**2 +
            0.0022*width**-2 +
            0.0262*width**-1 -
            5.1213*width**1 +
            0.0430*width**2 +
            13.4962*Thickness**-2 +
            18.4993*Thickness**-1 -
            81.2115*Thickness**1 +
            6.3270*Thickness**2 -
            0.0000*radius**-2 -
            0.0001*radius**-1 -
            0.0770*radius**1 +
            0.0025*radius**2 -
            0.0000*angular_vertical_LENG**-2 -
            0.0003*angular_vertical_LENG**-1 +
            2.0945*angular_vertical_LENG**1 -
            0.0069*angular_vertical_LENG**2)

def total_deformation_max(length_of_rectangle, width, Thickness, radius, angular_vertical_LENG):
    return (-20.3090 +
            0.0004*length_of_rectangle**-2 +
            0.0026*length_of_rectangle**-1 +
            2.3563*length_of_rectangle**1 -
            0.0252*length_of_rectangle**2 +
            0.0007*width**-2 +
            0.0086*width**-1 -
            1.6393*width**1 +
            0.0148*width**2 +
            4.5662*Thickness**-2 +
            6.2239*Thickness**-1 -
            26.8075*Thickness**1 +
            2.1846*Thickness**2 +
            0.0000*radius**-2 +
            0.0001*radius**-1 -
            0.5018*radius**1 +
            0.0026*radius**2 -
            0.0000*angular_vertical_LENG**-2 -
            0.0002*angular_vertical_LENG**-1 +
            1.4876*angular_vertical_LENG**1 -
            0.0047*angular_vertical_LENG**2)

def mass(length_of_rectangle, width, Thickness, radius, angular_vertical_LENG):
    return (2.7629 -
            0.0001*length_of_rectangle**-2 -
            0.0007*length_of_rectangle**-1 -
            0.0027*length_of_rectangle**1 +
            0.0000*length_of_rectangle**2 -
            0.0001*width**-2 -
            0.0008*width**-1 +
            0.0282*width**1 -
            0.0001*width**2 +
            0.0253*Thickness**-2 +
            0.0172*Thickness**-1 +
            0.1801*Thickness**1 -
            0.0003*Thickness**2 +
            0.0000*radius**-2 +
            0.0000*radius**-1 -
            0.0319*radius**1 +
            0.0001*radius**2 +
            0.0000*angular_vertical_LENG**-2 +
            0.0000*angular_vertical_LENG**-1 -
            0.0263*angular_vertical_LENG**1 +
            0.0001*angular_vertical_LENG**2)


# Generate all variable pairs (10 combinations)
var_pairs = list(itertools.combinations([0,1,2,3,4], 2))  # Zero-based indices
var_labels = ['length_of_rectangle', 'width', 'Thickness', 'radius', 'angular_vertical_LENG']
fixed_values = [45, 50 , 5, 105	,145]  # Default values for non-plotted variables
fig = plt.figure(figsize=(20, 15))


value = input("what do you wanna plot:  ")

if value == 'def x':
    inserted_function = x_directional_deformation_max
    cmap1 = 'plasma'
    
elif value == 'def y':
    inserted_function = y_directional_deformation_max
    cmap1 = 'viridis'
    
elif value == 'elastic strain':
    inserted_function = equivalent_elastic_strain_max
    cmap1 = 'inferno'
    
elif value == 'stress':
    inserted_function = equivalent_stress_max
    cmap1 = 'magma'
    
elif value == 'shear stress':
    inserted_function = maximum_shear_stress_max
    cmap1 = 'cividis'
    
elif value == 'deformation':
    inserted_function = total_deformation_max
    cmap1 = 'rainbow'
       
elif value == 'mass':
    inserted_function = mass
    cmap1 = 'Greys'
    
else:
    print('wrong argument please run again')

for idx, (i, j) in enumerate(var_pairs, 1):
    # Create grid for current pair
    
    if i == 0:
        low_val_x = 40
        high_val_x = 55
        Division = 50
        
    if i == 1:
        low_val_x = 35
        high_val_x = 55
        Division = 50
        
    if i == 2:
        low_val_x = 3
        high_val_x = 7
        Division = 20
        
    if i == 3:
        low_val_x = 90
        high_val_x = 110
        Division = 20
    
    if i == 4:
        low_val_x = 145
        high_val_x = 155
        Division = 20
        
    if j == 0:
        low_val_y = 40
        high_val_y = 55
        Division = 50
        
    if j == 1:
        low_val_y = 35
        high_val_y = 55
        Division = 50
        
    if j == 2:
        low_val_y = 3
        high_val_y = 7
        Division = 20
        
    if j == 3:
        low_val_y = 90
        high_val_y = 110
        Division = 20
    
    if j == 4:
        low_val_y = 145
        high_val_y = 155
        Division = 20
        
    x = np.linspace(low_val_x, high_val_x, Division)
    y = np.linspace(low_val_y, high_val_y, Division)
    X, Y = np.meshgrid(x, y)
    
    # Prepare all arguments with fixed values
    args = np.array(fixed_values, dtype=object)
    args[i] = X
    args[j] = Y
    
    # Calculate Z values
    Z = inserted_function(*args)
    
    # Create 3D subplot
    ax = fig.add_subplot(3, 4, idx, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap=cmap1, edgecolor='none')
    ax.set_xlabel(var_labels[i])
    ax.set_ylabel(var_labels[j])
    ax.set_zlabel(value)
    #ax.set_title(f'{var_labels[i]} vs {var_labels[j]}')
    fig.colorbar(surf, ax=ax, shrink=0.5)

plt.tight_layout()
plt.show()
