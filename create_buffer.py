# -*- coding: utf-8 -*-
"""
Created on Sun May  3 13:06:55 2020

@author: Naomi
"""

# This script runs the Buffer tool. The user supplies the input
#  and output paths, and the buffer distance.
 
import arcpy
arcpy.env.overwriteOutput = True
 
try:
     # Get the input parameters for the Buffer tool
     inPath = arcpy.GetParameterAsText(0)
     outPath = arcpy.GetParameterAsText(1)
     bufferDistance = arcpy.GetParameterAsText(2)
 
     # Run the Buffer tool
     arcpy.Buffer_analysis(inPath, outPath, bufferDistance)
 
     # Report a success message    
     arcpy.AddMessage("All done!")
 
except:
     # Report an error messages
     arcpy.AddError("Could not complete the buffer")
 
     # Report any error messages that the Buffer tool might have generated    
     arcpy.AddMessage(arcpy.GetMessages())