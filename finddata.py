# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a query selection
QuerySelect(QueryString='((cnd01_NCIC_ACTDIAG01 > 1e5) & (cnd01_NCIC_ACTDIAG01 < 1e7))', FieldType='CELL', InsideOut=0)

# find source
clip1 = FindSource('Clip1')

# create a new 'Extract Selection'
extractSelection1 = ExtractSelection(registrationName='ExtractSelection1', Input=clip1)

# set active source
SetActiveSource(extractSelection1)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
extractSelection1Display = Show(extractSelection1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'cnd01_NCIC_ACTDIAG01'
cnd01_NCIC_ACTDIAG01LUT = GetColorTransferFunction('cnd01_NCIC_ACTDIAG01')

# get opacity transfer function/opacity map for 'cnd01_NCIC_ACTDIAG01'
cnd01_NCIC_ACTDIAG01PWF = GetOpacityTransferFunction('cnd01_NCIC_ACTDIAG01')

# trace defaults for the display properties.
extractSelection1Display.Representation = 'Surface'
extractSelection1Display.ColorArrayName = ['CELLS', 'cnd01_NCIC_ACTDIAG01']
extractSelection1Display.LookupTable = cnd01_NCIC_ACTDIAG01LUT
extractSelection1Display.SelectTCoordArray = 'None'
extractSelection1Display.SelectNormalArray = 'None'
extractSelection1Display.SelectTangentArray = 'None'
extractSelection1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSelection1Display.SelectOrientationVectors = 'None'
extractSelection1Display.ScaleFactor = 36.0
extractSelection1Display.SelectScaleArray = 'None'
extractSelection1Display.GlyphType = 'Arrow'
extractSelection1Display.GlyphTableIndexArray = 'None'
extractSelection1Display.GaussianRadius = 1.8
extractSelection1Display.SetScaleArray = [None, '']
extractSelection1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSelection1Display.OpacityArray = [None, '']
extractSelection1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSelection1Display.DataAxesGrid = 'GridAxesRepresentation'
extractSelection1Display.PolarAxes = 'PolarAxesRepresentation'
extractSelection1Display.ScalarOpacityFunction = cnd01_NCIC_ACTDIAG01PWF
extractSelection1Display.ScalarOpacityUnitDistance = 28.366884442981373
extractSelection1Display.OpacityArrayName = ['CELLS', 'AREL']
extractSelection1Display.SelectInputVectors = [None, '']
extractSelection1Display.WriteLog = ''

# show color bar/color legend
extractSelection1Display.SetScalarBarVisibility(renderView1, True)

# get 2D transfer function for 'cnd01_NCIC_ACTDIAG01'
cnd01_NCIC_ACTDIAG01TF2D = GetTransferFunction2D('cnd01_NCIC_ACTDIAG01')

# hide data in view
Hide(clip1, renderView1)

# set active source
SetActiveSource(clip1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=clip1.ClipType)

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['CELLS', 'cnd01_NCIC_ACTDIAG01']
clip1Display.LookupTable = cnd01_NCIC_ACTDIAG01LUT
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'None'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 49.91863070393533
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.GaussianRadius = 2.4959315351967666
clip1Display.SetScaleArray = [None, '']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = [None, '']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = cnd01_NCIC_ACTDIAG01PWF
clip1Display.ScalarOpacityUnitDistance = 6.426124626883379
clip1Display.OpacityArrayName = ['CELLS', 'CLOUD']
clip1Display.SelectInputVectors = [None, '']
clip1Display.WriteLog = ''

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(clip1, renderView1)

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(clip1, renderView1)

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on clip1Display
clip1Display.Opacity = 0.5

# Properties modified on clip1Display
clip1Display.Opacity = 0.25

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1358, 1136)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [571.9455764053191, 609.2684572131575, 1461.9956532202646]
renderView1.CameraFocalPoint = [180.0, 62.5, 850.0]
renderView1.CameraViewUp = [-0.3396105646662453, 0.7989630942216066, -0.49630901506915065]
renderView1.CameraParallelScale = 235.38532239712825

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
