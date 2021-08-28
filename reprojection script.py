# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:04:57 2020

@author: Naomi
"""

# This script re-projects the vector datasets in a target folder

import arcpy

# Create path variables
TargetFolder = arcpy.GetParameterAsText(0)
Target = arcpy.GetParameterAsText(1)

# Get a list of all the feature classes in target folder 
arcpy.env.workspace = TargetFolder
arcpy.env.overwriteOutput = True

Fc_list = arcpy.ListFeatureClasses()

#print("Running script Reproject Data in Folder " + TargetFolder)

try:
    final = []
    # Loop through the feature classes in target folder
    for fc in Fc_list:
        
        #Describe the Spatial reference for each feature class in target folder
        desc = arcpy.Describe(fc)
        fcSR = desc.SpatialReference
        
        #Describe the Spatial reference for target feature class
        descTarget = arcpy.Describe(Target)
        TargetSR = descTarget.SpatialReference
        
        #Loop through all feature classes with a different spatial reference
        if fcSR.Name != TargetSR.Name:
            rootName = fc.replace(".shp", "")
            
            # Perform the re-projection
            outPath = TargetFolder +  "\\" +rootName + "_projected.shp"
            arcpy.Project_management(fc, outPath, TargetSR)
            
            final.append(fc)
            
    arcpy.AddMessage("Re-projection complete for {}".format(",".join(str(fc) for fc in final)))
#    print("Completed script Reproject Data in Folder " + TargetFolder)
   

except:
    arcpy.AddError("Could not reproject")
#    print("Could not reproject")
