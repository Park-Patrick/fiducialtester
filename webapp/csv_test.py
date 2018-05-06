##################################################
# Slicer Fiducial Distance Calculator #
##################################################

import numpy as np
import math
import csv

##################
## Calculations ##
##################

#Euclidean distance calculation
    #Euclidean distance
def euclidianDistanceCalc(xyz_planned, xyz_actual):
    plan_act_diff = xyz_planned - xyz_actual
    euc_dist = math.sqrt(sum(plan_act_diff**2))
    return euc_dist

#Radial distance calculation
    #point to line distance

def radialDistanceCalc(pt, xyz_entry, xyz_target):
    x1_minus_pt = pt - xyz_entry
    x2_minus_x1 = xyz_target - xyz_entry

    sumsq_x1_minus_pt = sum(x1_minus_pt * x1_minus_pt)
    sumsq_x2_minus_x1 = sum(x2_minus_x1 * x2_minus_x1)

    mydotprod = np.dot(x1_minus_pt, x2_minus_x1)

    dist3d = np.sqrt((sumsq_x1_minus_pt * sumsq_x2_minus_x1 - (mydotprod * mydotprod))/sumsq_x2_minus_x1)
    return dist3d

#Radial angle calculation
    #point to line angle
def ptLineAngleCalc(pt, x_entry, x_target):
    x1_minus_pt = pt - x_entry
    x2_minus_x1 = x_target - x_entry

    sumsq_x1_minus_pt = sum(x1_minus_pt**2)
    sumsq_x2_minus_x1 = sum(x2_minus_x1**2)

    mydotprod = np.dot(x1_minus_pt, x2_minus_x1) # sum of products of elements

    rad_angle = math.acos(mydotprod/(np.sqrt(sumsq_x1_minus_pt)*np.sqrt(sumsq_x2_minus_x1)))
    deg_angle = math.degrees(rad_angle)
    return deg_angle

#Line angle calculation
    #line to line angle
def lineLineAngleCalc(a_entry, a_target, b_entry, b_target):
    vectorA = a_target - a_entry
    vectorB = b_target - b_entry

    sumsq_vectorA = sum(vectorA**2)
    sumsq_vectorB = sum(vectorB**2)

    mydotprod = sum(vectorA*vectorB)

    rad_angle = math.acos(mydotprod/(np.sqrt(sumsq_vectorA)*np.sqrt(sumsq_vectorB)))
    deg_angle = math.degrees(rad_angle)
    return deg_angle

def import_csv(filename1, filename2):
    #########################
    ## Read first csv file ##
    #########################

    # initializing the titles and rows list
    fields1 = []
    data_by_rows = []

    with open(filename1, 'r') as csvfile1:
        # creating a csv reader object
        csvreader1 = csv.reader(csvfile1)

        # extracting field names through first row
        comment1 = next(csvreader1)
        comment2 = next(csvreader1)
        fields1 = next(csvreader1)

        # extracting each data row one by one
        for row1 in csvreader1:
            data_by_rows.append(row1)

    ##########################
    ## Read second csv file ##
    ##########################

    fields2 = []
    data2_by_rows = []

    with open(filename2, 'r') as csvfile2:
        # creating a csv reader object
        csvreader2 = csv.reader(csvfile2)

        # extracting field names through first row
        comment1 = next(csvreader2)
        comment2 = next(csvreader2)
        fields2 = next(csvreader2)

        # extracting each data row one by one
        for row2 in csvreader2:
            data2_by_rows.append(row2)

    xvals_planned = []
    yvals_planned = []
    zvals_planned = []
    xvals_actual = []
    yvals_actual = []
    zvals_actual = []

    for each_row in data_by_rows:
        xvals_actual.append(each_row[1])
        yvals_actual.append(each_row[2])
        zvals_actual.append(each_row[3])

    for each_row in data2_by_rows:
        xvals_planned.append(each_row[1])
        yvals_planned.append(each_row[2])
        zvals_planned.append(each_row[3])

    numFid = csvreader1.line_num - 3

    errors = np.zeros([4,numFid])
    xyz_planned = np.zeros([3,numFid])
    xyz_actual = np.zeros([3,numFid])

    for i in range(0,numFid):
        xyz_planned[:,i] = np.array([float(xvals_planned[i]), float(yvals_planned[i]), float(zvals_planned[i])])
        xyz_actual[:,i] = np.array([float(xvals_actual[i]), float(yvals_actual[i]), float(zvals_actual[i])])
        errors[0:2, i] = xyz_actual[:,i] - xyz_planned[:,i]
        errors[3,i] = euclidianDistanceCalc(xyz_planned[:,i], xyz_actual[:,i])

    return xyz_planned, xyz_actual, errors
