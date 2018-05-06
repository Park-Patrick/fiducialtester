# -*- coding: utf-8 -*-
"""
Created on Sat May  5 14:33:12 2018

@author: Spiny
"""
from csv_test import import_csv

filename1 = "./uploads/UHF_MEAN_no_outliers.fcsv"
filename2 = "./uploads/UHF_T1_JL2122flipped_1_20180505.fcsv"

xyz_planned, xyz_actual, euclid_dist = import_csv(filename1, filename2)

euclid_values = []
euclid_fiducials = []

for i in euclid_dist:
    if i > 0:
        euclid_values.append(i)

for i in range(len(euclid_values)):
    euclid_fiducials.append(euclid_dist.index(euclid_values[i]))

p1 = xyz_actual[:,0]
p2 = xyz_actual[:,1]
p3 = xyz_actual[:,2]

v1 = p3 - p1
v2 = p2 - p1

cp = np.cross(v1, v2)
a, b, c = cp

d = np.dot(cp, p3)
d = -d

# Assuming that the fiducials and corresponding anatomy are fixed
mid_fiducials = [0, 1, 2, 3, 4, 9, 10, 13, 18, 19]
right_fiducials = [5, 7, 11, 14, 16, 20, 22, 24, 26, 28, 30]
left_fiducials = [6, 8, 12, 15, 17, 21, 23, 25, 27, 29, 31]

# Plane equation formula
def plane_calc(x, y, z):
    plane_eq = a*x + b*y + c*z + d
    return plane_eq

right_coor = []
left_coor = []
right_vals = []
left_vals = []
error_right = []
error_left = []
fidinderror_right = []
fidinderror_left = []
fiderror_right = []
fiderror_left = []
newright = []
newleft = []

for i in right_fiducials:
    right_coor.append(xyz_planned[:,i])
    
for i in range(len(right_coor)):
    right_vals.append(plane_calc(right_coor[i][0], right_coor[i][1], right_coor[i][2]))
  
for i in right_vals:
    if i > 0:
        error_right.append(i)
        
for i in range(len(error_right)):
    fidinderror_right.append(right_vals.index(error_right[i]))
    
for i in fidinderror_right:
    fiderror_right.append(right_fiducials[i])

newright = [x+1 for x in fiderror_right]

for i in left_fiducials:
    left_coor.append(xyz_planned[:,i])
    
for i in range(len(left_coor)):
    left_vals.append(plane_calc(left_coor[i][0], left_coor[i][1], left_coor[i][2]))
        
for i in left_vals:
    if i < 0:
        error_left.append(i)
        
for i in range(len(error_left)):
    fidinderror_left.append(left_vals.index(error_left[i]))
    
for i in fidinderror_left:
    fiderror_left.append(left_fiducials[i])

newleft = [x+1 for x in fiderror_left]

del i

print("Right side fiducial errors: {}".format(newright))
print("Left side fiducial errors: {}".format(newleft))

