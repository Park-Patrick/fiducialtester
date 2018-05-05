# -*- coding: utf-8 -*-
"""
Created on Sat May  5 14:33:12 2018

@author: Spiny
"""
from csv_test import import_csv

filename1 = "D:/brainhack2018/fiducialtester/webapp/uploads/UHF_MEAN.fcsv"
filename2 = "D:/brainhack2018/fiducialtester/webapp/uploads/UHF_MEAN_no_outliers.fcsv"

xyz_planned, xyz_actual, euclid_dist = import_csv(filename1, filename2)