# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:35:40 2020

@author: Naomi
"""

# Opens a feature class from a geodatabase and prints the spatial reference
import arcpy

featureClass = "D:/GIS/Geog485/GEOG485/GEOG485.gdb/us_cities_Buffer1"

# Describe the feature class and get its spatial reference
desc = arcpy.Describe(featureClass)
spatialRef = desc.spatialReference

# Print the spatial reference name
print(spatialRef.Name)
#name = spatialRef.Name
#print("The spatial reference type of " + featureClass + " is " + name)