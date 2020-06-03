# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 10:55:44 2020

@author: Naomi
"""

# Data extraction script
# This script uses selections and cursors to process some data from a "raw" format into 
# More specialized datasets for a specific mapping purpose.
# It retrieves all current players born in a particular country (say, Sweden) broken down by position. 

import arcpy
arcpy.env.workspace = " "
arcpy.env.overwriteOutput = True

# Define relevant feature classes
fcRosters = arcpy.GetParameterAsText(0)
fcCountries = arcpy.GetParameterAsText(1)

# Define a country
countryName = arcpy.GetParameterAsText(2)
countryQuery = "CNTRY_NAME = '" + countryName + "'"

try:
    # make an attribute selection to select a country
    arcpy.MakeFeatureLayer_management(fcCountries, "SelectedCountry", countryQuery)
    arcpy.MakeFeatureLayer_management(fcRosters, "SelectedPlayers")
    
    # Use a spatial selection to grab all the players that fall within this country
    arcpy.SelectLayerByLocation_management("SelectedPlayers", "CONTAINED_BY", "SelectedCountry")
    
    # Makes a separate shapefile for each of the three forward positions
    # (center, right wing, and left wing) from the player roster
    arcpy.MakeFeatureLayer_management("SelectedPlayers", "Center", "position = 'C'")
    arcpy.CopyFeatures_management("Center", "/Centers.shp" )
    
    arcpy.MakeFeatureLayer_management("SelectedPlayers", "RightWing", "position = 'RW'")
    arcpy.CopyFeatures_management("RightWing", "/RightWing.shp")
    
    arcpy.MakeFeatureLayer_management("SelectedPlayers", "LeftWing", "position = 'LW'")
    arcpy.CopyFeatures_management("LeftWing", "/LeftWing.shp")
    
except:
    arcpy.AddError("Could not make feature layers")
    
try:
    # Add fields for height in cm and weight in kgs to the new shapefiles
    fieldName1 = "weight_kg"
    fieldName2 = "weight"
    fieldName3 = "height_cm"
    fieldName4 = "height"
    for fc in ("Centers.shp", "RightWing.shp", "LeftWing.shp"):
        arcpy.AddField_management(fc, fieldName1, "TEXT")
        arcpy.AddField_management(fc, fieldName3, "TEXT")
        # Update new fields using an update cursor
        with arcpy.da.UpdateCursor(fc,(fieldName1, fieldName2, fieldName3, fieldName4)) as cursor:
            for row in cursor:
                #Update weight_kg field
                row[0] = (row[1]) * 0.453592
                # Convert feet and inches to cm
                height_ft = row[3].split("' ")
                feet = int(height_ft[0])
                inch = int(height_ft[1].replace('"',''))
                height_cm = ((feet*12) + inch) * 2.54  
                # Update height_cm field
                row[2] = height_cm
                cursor.updateRow(row)

finally:
    # Delete feature layers and cursor
    arcpy.Delete_management("SelectedCountry")
    arcpy.Delete_management("SelectedPlayers")
    del row, cursor 

arcpy.AddMessage("Complete!")
