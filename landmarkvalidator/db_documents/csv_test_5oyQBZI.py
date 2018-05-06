##################################################
# Slicer Fiducial Distance Calculator #
##################################################

import sys
import numpy as np
import math

# importing csv module
import csv

try:
    # csv file names
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    subjid = sys.argv[3]
    output_filename = sys.argv[4]

    print ""
    print ""
    print "-----------------------------"
    print "SEEG Trajectory Calculation"
    print "-----------------------------"
    print ""

    # 

except:
    print ""
    print ""
    print "-----------------------------"
    print "-----------------------------"
    print "SEEG Trajectory Calculation"
    print "Usage: python seeg_trajectory.py [actual] [planned] [subjid] [output]"
    print "e.g. python seeg_trajectory.py ~/Documents/actual.fcsv ~/Documents/planned.fcsv subj1 ~/Documents/output.csv"
    print "-----------------------------"
    print "-----------------------------"
    print ""
    print ""
    print "Error:"
    print ""



#########################
## Read first csv file ##
#########################

# initializing the titles and rows list
fields1 = []
data_by_rows = []

print "Reading actual trajectories file: ", filename1

with open(filename1, 'r') as csvfile1:
    # creating a csv reader object
    csvreader1 = csv.reader(csvfile1)

    # extracting field names through first row
    comment1 = csvreader1.next()
    comment2 = csvreader1.next()
    fields1 = csvreader1.next()
 
    # extracting each data row one by one
    for row1 in csvreader1:
        data_by_rows.append(row1)

##########################
## Read second csv file ##
##########################

fields2 = []
data2_by_rows = []

print "Reading planned trajectories file: ", filename2
with open(filename2, 'r') as csvfile2:
    # creating a csv reader object
    csvreader2 = csv.reader(csvfile2)

    # extracting field names through first row
    comment1 = csvreader2.next()
    comment2 = csvreader2.next()
    fields2 = csvreader2.next()
 
    # extracting each data row one by one
    for row2 in csvreader2:
        data2_by_rows.append(row2)

xvals_planned = []
yvals_planned = []
zvals_planned = []

xvals_actual = []
yvals_actual = []
zvals_actual = []

labels = []
descriptions = []
types = []
omitted = []
euclid_dist = []
radial_dist = []
radial_angle = []
line_angle = []


for each_row in data_by_rows:

    xvals_actual.append(each_row[1])
    yvals_actual.append(each_row[2])
    zvals_actual.append(each_row[3])

for each_row in data2_by_rows:
    
    xvals_planned.append(each_row[1])
    yvals_planned.append(each_row[2])
    zvals_planned.append(each_row[3])
    labels.append(each_row[11])
    descriptions.append(each_row[12])

numFid = csvreader1.line_num - 3

for i in range(0, numFid):
    if (i % 2 == 0):
        types.append('target')
    elif (i % 2 == 1):
        types.append('entry')

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

euclid_dist = [None] * numFid
radial_dist = [None] * numFid
radial_angle = [None] * numFid
line_angle = [None] * numFid
omitted = [None] * numFid

for i in range(0,numFid):
    xyz_planned = np.array([float(xvals_planned[i]), float(yvals_planned[i]), float(zvals_planned[i])])
    xyz_actual = np.array([float(xvals_actual[i]), float(yvals_actual[i]), float(zvals_actual[i])])
    euclid_dist[i] = euclidianDistanceCalc(xyz_planned, xyz_actual)

for i in range(0,numFid,2):
    xyz_planned_entry = np.array([float(xvals_planned[i+1]), float(yvals_planned[i+1]), float(zvals_planned[i+1])])
    xyz_planned_target = np.array([float(xvals_planned[i]), float(yvals_planned[i]), float(zvals_planned[i])])
    
    xyz_actual_entry = np.array([float(xvals_actual[i+1]), float(yvals_actual[i+1]), float(zvals_actual[i+1])])
    xyz_actual_target = np.array([float(xvals_actual[i]), float(yvals_actual[i]), float(zvals_actual[i])])

    radial_dist[i] = radialDistanceCalc(xyz_actual_target, xyz_planned_entry, xyz_planned_target)
    radial_dist[i+1] = radialDistanceCalc(xyz_actual_entry, xyz_planned_entry, xyz_planned_target)
    radial_angle[i] = ptLineAngleCalc(xyz_actual_target, xyz_planned_entry, xyz_planned_target)
    line_angle[i] = lineLineAngleCalc(xyz_actual_entry, xyz_actual_target, xyz_planned_entry, xyz_planned_target)

## Populate data into output rows ##

## Writing to output CSV ##
output_rows = []
output_fields = ['fid', 'subjid', 'X_planned', 'Y_planned', 'Z_planned', 'X_actual', 'Y_actual', 'Z_actual', 'label', 'description', 'type', 'omitted', 'euclid_dist', 'radial_dist', 'radial_angle', 'line_angle']
output_rows.append(output_fields)


for i in range(0,numFid):    
    output_row = [None] * numFid

    #fid
    output_row[0] = i+1

    #subjID
    output_row[1] = subjid

    #X_planned
    output_row[2] = xvals_planned[i]

    #Y_planned
    output_row[3] = yvals_planned[i]

    #Z_planned
    output_row[4] = zvals_planned[i]

    #X_actual
    output_row[5] = xvals_actual[i]

    #Y_actual
    output_row[6] = yvals_actual[i]

    #Z_actual
    output_row[7] = zvals_actual[i]

    #name
    output_row[8] = labels[i] 

    #description
    output_row[9] = descriptions[i]

    #type
    output_row[10] = types[i]

    #omitted
    output_row[11] = omitted[i]

    #euclid_dist
    output_row[12] = euclid_dist[i]

    #radial_dist
    output_row[13] = radial_dist[i]

    #radial_angle
    output_row[14] = radial_angle[i]

    #line_angle
    output_row[15] = line_angle[i]

    output_rows.append(output_row)



with open(output_filename, 'w') as out_csvfile:
    csvwriter = csv.writer(out_csvfile)
    csvwriter.writerows(output_rows)


print ""
print "Output file written to: ", output_filename
print ""
print "-----------------------------"
