# script-version: 2.0
# Catalyst state generated using paraview version 5.11.1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [2102, 568]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [180.0, 62.5, 850.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [571.9455764053191, 609.2684572131575, 1461.9956532202646]
renderView1.CameraFocalPoint = [180.0, 62.5, 850.0]
renderView1.CameraViewUp = [-0.3396105646662453, 0.7989630942216066, -0.49630901506915065]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 235.38532239712825

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 0.500000)
layout1.AssignView(1, renderView1)
layout1.SetSize(2102, 1136)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'EAM Data Reader'
diag32_F2010eamh02010060172000nc = EAMDataReader(registrationName='diag32_F2010.eam.h0.2010-06-01-72000.nc', ConnectivityFile='/home/local/KHQ/abhi.yenpure/repositories/eam/forMovie/TEMPEST_ne30pg2.scrip.renamed.nc',
    DataFile='/home/local/KHQ/abhi.yenpure/repositories/eam/forMovie/diag32_F2010.eam.h0.2010-06-01-72000.nc')
diag32_F2010eamh02010060172000nc.a2DVariables = []
diag32_F2010eamh02010060172000nc.a3DMiddleLayerVariables = ['CLOUD', 'T', 'cnd01_AST_ACTDIAG01', 'cnd01_AST_ACTDIAG01_inc', 'cnd01_CLDLIQ_ACTDIAG01', 'cnd01_CLDLIQ_ACTDIAG01_inc', 'cnd01_NCIC_ACTDIAG01', 'cnd01_NDROPMIX_ACTDIAG01', 'cnd01_NDROPSRC_ACTDIAG01', 'cnd01_NDROPW_ACTDIAG01', 'cnd01_NPCCN_ACTDIAG01', 'cnd01_NSRCEVAP_ACTDIAG01', 'cnd01_NSRCNACT_ACTDIAG01', 'cnd01_NSRCNCLR_ACTDIAG01', 'cnd01_NSRCSHRK_ACTDIAG01', 'cnd01_QCIC_ACTDIAG01']

# find source
diag32_F2010eamh02010060172000nc_1 = FindSource('diag32_F2010.eam.h0.2010-06-01-72000.nc')

# create a new 'EAMVolumize'
eAMVolumize1 = EAMVolumize(registrationName='EAMVolumize1', Input=OutputPort(diag32_F2010eamh02010060172000nc_1,1))

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=eAMVolumize1)
clip1.ClipType = 'Box'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['CELLS', 'CLOUD']
clip1.Value = 0.5

# init the 'Box' selected for 'ClipType'
clip1.ClipType.Position = [0.0, 40.0, 700.0]
clip1.ClipType.Length = [360.0, 10.0, 300.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [180.0, 0.0, 499.3101324524089]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from clip1
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'cnd01_NCIC_ACTDIAG01'
cnd01_NCIC_ACTDIAG01TF2D = GetTransferFunction2D('cnd01_NCIC_ACTDIAG01')
cnd01_NCIC_ACTDIAG01TF2D.ScalarRangeInitialized = 1
cnd01_NCIC_ACTDIAG01TF2D.Range = [1000000.0, 50000000.0, 0.0, 1.0]

# get color transfer function/color map for 'cnd01_NCIC_ACTDIAG01'
cnd01_NCIC_ACTDIAG01LUT = GetColorTransferFunction('cnd01_NCIC_ACTDIAG01')
cnd01_NCIC_ACTDIAG01LUT.AutomaticRescaleRangeMode = 'Never'
cnd01_NCIC_ACTDIAG01LUT.TransferFunction2D = cnd01_NCIC_ACTDIAG01TF2D
cnd01_NCIC_ACTDIAG01LUT.RGBPoints = [1000000.0, 0.278431372549, 0.278431372549, 0.858823529412, 1230998.875000001, 0.0, 0.0, 0.360784313725, 3980603.2500000014, 0.0, 1.0, 1.0, 7425441.500000004, 0.0, 0.501960784314, 0.0, 10847003.999999996, 1.0, 1.0, 0.0, 28147109.99999999, 1.0, 0.380392156863, 0.0, 30661893.99999998, 0.419607843137, 0.0, 0.0, 50000000.0, 0.878431372549, 0.301960784314, 0.301960784314]
cnd01_NCIC_ACTDIAG01LUT.ColorSpace = 'RGB'
cnd01_NCIC_ACTDIAG01LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'cnd01_NCIC_ACTDIAG01'
cnd01_NCIC_ACTDIAG01PWF = GetOpacityTransferFunction('cnd01_NCIC_ACTDIAG01')
cnd01_NCIC_ACTDIAG01PWF.Points = [1000000.0, 0.0, 0.5, 0.0, 50000000.0, 1.0, 0.5, 0.0]
cnd01_NCIC_ACTDIAG01PWF.ScalarRangeInitialized = 1

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

# setup the color legend parameters for each legend in this view

# get color legend/bar for cnd01_NCIC_ACTDIAG01LUT in view renderView1
cnd01_NCIC_ACTDIAG01LUTColorBar = GetScalarBar(cnd01_NCIC_ACTDIAG01LUT, renderView1)
cnd01_NCIC_ACTDIAG01LUTColorBar.Orientation = 'Horizontal'
cnd01_NCIC_ACTDIAG01LUTColorBar.WindowLocation = 'Any Location'
cnd01_NCIC_ACTDIAG01LUTColorBar.Position = [0.5882055680760649, 0.7701492537313432]
cnd01_NCIC_ACTDIAG01LUTColorBar.Title = 'cnd01_NCIC_ACTDIAG01'
cnd01_NCIC_ACTDIAG01LUTColorBar.ComponentTitle = ''
cnd01_NCIC_ACTDIAG01LUTColorBar.ScalarBarLength = 0.32999999999999974

# set color bar visibility
cnd01_NCIC_ACTDIAG01LUTColorBar.Visibility = 1

# show color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup extractors
# ----------------------------------------------------------------

# create extractor
jPG1 = CreateExtractor('JPG', renderView1, registrationName='JPG1')
# trace defaults for the extractor.
jPG1.Trigger = 'TimeStep'

# init the 'JPG' selected for 'Writer'
jPG1.Writer.FileName = 'RenderView1_{timestep:06d}{camera}.jpg'
jPG1.Writer.ImageResolution = [2102, 568]
jPG1.Writer.Format = 'JPEG'

# ----------------------------------------------------------------
# restore active source
SetActiveSource(jPG1)
# ----------------------------------------------------------------

# ------------------------------------------------------------------------------
# Catalyst options
from paraview import catalyst
options = catalyst.Options()
options.GlobalTrigger = 'TimeStep'
options.CatalystLiveTrigger = 'TimeStep'

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    from paraview.simple import SaveExtractsUsingCatalystOptions
    # Code for non in-situ environments; if executing in post-processing
    # i.e. non-Catalyst mode, let's generate extracts using Catalyst options
    SaveExtractsUsingCatalystOptions(options)
