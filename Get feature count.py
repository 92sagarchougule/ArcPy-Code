import arcpy
import pythonaddins

arcpy.env.workspace = arcpy.GetParameterAsText(0)

flist = arcpy.ListFeatureClasses()

a = 0
for i in flist:
    j = arcpy.ListFields(i)
    Message = pythonaddins.MessageBox(i + ' : ' +str(count),"Warning",3)
    if(Message == 'Yes'):
        count = arcpy.GetCount_management(i)
        a+=1
        arcpy.AddMessage(a,'Name of SHP: ',i ,'Count',count)
        for field in j:
            arcpy.AddMessage('Name of Field: ',field.name)
    else:
        arcpy.AddMessage('left out')
