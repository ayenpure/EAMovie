# state file generated using paraview version 5.11.1
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


# Load necessary plugins
LoadPlugin("/home/local/KHQ/abhi.yenpure/repositories/eam/scripts/eam_reader.py", ns=globals())
LoadPlugin("/home/local/KHQ/abhi.yenpure/repositories/eam/scripts/eam_filters.py", ns=globals())

# Load state to set-up data
LoadState('/home/local/KHQ/abhi.yenpure/repositories/eam/forMovie/state_diag32_06-01-72000--X.pvsm')

# Find source from the loaded state to force loading selected variables
diag32_F2010eamh02010060172000nc = FindSource('diag32_F2010.eam.h0.2010-06-01-72000.nc')
SetActiveSource(diag32_F2010eamh02010060172000nc)
diag32_F2010eamh02010060172000nc.a3DMiddleLayerVariables = ['AREI', 'CLOUD', 'T', 'cnd01_AST_ACTDIAG01', 'cnd01_AST_ACTDIAG01_inc', 'cnd01_CLDLIQ_ACTDIAG01', 'cnd01_CLDLIQ_ACTDIAG01_inc', 'cnd01_NCIC_ACTDIAG01', 'cnd01_NDROPMIX_ACTDIAG01', 'cnd01_NDROPSRC_ACTDIAG01', 'cnd01_NDROPW_ACTDIAG01', 'cnd01_NPCCN_ACTDIAG01', 'cnd01_NSRCEVAP_ACTDIAG01', 'cnd01_NSRCNACT_ACTDIAG01', 'cnd01_NSRCNCLR_ACTDIAG01', 'cnd01_NSRCSHRK_ACTDIAG01', 'cnd01_QCIC_ACTDIAG01']

# Find the two render views
renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')
renderView2 = FindViewOrCreate('RenderView2', viewtype='RenderView')
# set active view
SetActiveView(renderView1)

clip1 = FindSource('Clip1')
SetActiveSource(clip1)

# Set the opacity for the Clip display and the selection mesh for View 1 (top)
clip1Display = GetDisplayProperties(clip1, view=renderView1)
clip1Display.Opacity = 0.25
clip1Display.SelectionOpacity = 0.125

# Set the opacity for the Clip display and the selection mesh for View 2 (bottom)
clip2Display = GetDisplayProperties(clip1, view=renderView2)
clip2Display.Opacity = 0.25
clip2Display.SelectionOpacity = 0.125

# Query selection for the specified variable
QuerySelect(QueryString='((cnd01_NCIC_ACTDIAG01 > 1e5) & (cnd01_NCIC_ACTDIAG01 < 1e7))', FieldType='CELL', InsideOut=0)

# Extract the cells and display them explicitly for better visibility
extractSelection1 = ExtractSelection(registrationName='ExtractSelection1', Input=clip1)
extractSelection1Display = Show(extractSelection1, renderView1, 'UnstructuredGridRepresentation')
extractSelection2Display = Show(extractSelection1, renderView2, 'UnstructuredGridRepresentation')
SetActiveSource(extractSelection1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

layout1 = GetLayout()
layout1.SetSize(2102, 1136)

# Loop over the Y length of box to export images

lengthX = 0
while lengthX <= 360:
    clip1.ClipType.Length = [lengthX, 45.0, 300.0]
    renderView1.Update()    
    renderView2.Update()
    # save screenshot
    x = ('%04d' %lengthX)
    filename = 'clipX' + x + '.png'
    SaveScreenshot(filename, layout1, SaveAllViews=1,
        ImageResolution=[2102, 1136])
    lengthX = lengthX+1 
exit()
