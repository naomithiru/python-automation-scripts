# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:15:58 2020

@author: Naomi
"""

# This script uses map algebra to find values
# in an elevation raster greater than 3500 (meters)

import arcpy

# import arcpy.sa map algebra sub-module
from arcpy.sa import *

# Specify an input raster
inRaster = "D:/GIS/Geog485/Lesson1/Lesson1Data/foxlake"
cutoffElevation = 3500

# Check out the Spatial Analyst extension
arcpy.CheckOutExtension("Spatial")

#Make map algebra expression and save the resulting raster
outRaster = Raster(inRaster) > cutoffElevation
outRaster.save("D:/GIS/Geog485/Lesson1/foxlake_hi_10")

# Check in the Spatial Analyst extension now that you're done
arcpy.CheckInExtension("Spatial")
