# trace generated using paraview version 5.11.1-1745-ge8c78138a6
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

import numpy as np
import math

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

LoadPlugin("/home/local/KHQ/abhi.yenpure/repositories/eam/scripts/eam_reader.py", ns=globals())
LoadPlugin("/home/local/KHQ/abhi.yenpure/repositories/eam/scripts/eam_filters.py", ns=globals())
LoadPlugin("/home/local/KHQ/abhi.yenpure/repositories/eam/scripts/eam_projection.py", ns=globals())
LoadState("/home/local/KHQ/abhi.yenpure/repositories/eam/forMovie/states/state_slice_lat_lev_rotate_layout1.pvsm")

# find source
v2_F2010_nc00_inst_macmic01eamh02010122500000nc = FindSource('v2_F2010_nc00_inst_macmic01.eam.h0.2010-12-25-00000.nc')
SetActiveSource(v2_F2010_nc00_inst_macmic01eamh02010122500000nc)
v2_F2010_nc00_inst_macmic01eamh02010122500000nc.a3DMiddleLayerVariables = ['cnd01_ALST_ACTDIAG01', 'cnd01_AST_ACTDIAG01', 'cnd01_CDMC_ACTDIAG01', 'cnd01_CDNC_ACTDIAG01', 'cnd01_RAL_ACTDIAG01', 'cnd01_REL_ACTDIAG01']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1988, 1144)

sin = math.sin
r   = math.radians
cos = math.cos

# find source
slice1 = FindSource('Slice1')
# set active source
SetActiveSource(slice1)

for i in range(1, 361): 
    # Properties modified on slice1.SliceType
    slice1.SliceType.Origin = [i, 78.25, 799.2482197458811]

    a = i
    rZmatrix = np.array([[cos(r(a)), sin(r(a)), 0, 0],
                        [-sin(r(a)), cos(r(a)), 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])
    ocam       = np.array([531.7759596581271, 4369.374717357803, 2151.6182850174414, 1.0])
    cam        = ocam.dot(rZmatrix)
    ofoc       = np.array([531.7759596581271, 0.0, 2151.6182850174414, 1.0])
    foc        = ofoc.dot(rZmatrix)
    print(cam)
    print(foc)
    '''
    # current camera placement for renderView1
    renderView1.CameraPosition = [531.7759596581271, 4369.374717357803, 2151.6182850174414]
    renderView1.CameraFocalPoint = [531.7759596581271, 0.0, 2151.6182850174414]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 338.4313507490336
    '''
    renderView1.InteractionMode = '2D'
    renderView1.CameraPosition = [cam[0], cam[1], cam[2]]
    renderView1.CameraFocalPoint = [foc[0], foc[1], foc[2]]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    #renderView1.CameraParallelScale = 338.4313507490336

    # update the view to ensure updated data information
    renderView1.Update()

    x = ('%04d' %i)
    filename = 'rotateZ' + x + '.png'
    # save screenshot
    SaveScreenshot(filename, layout1, 16, SaveAllViews=1, ImageResolution=[1988, 1144])
'''
# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1979, 1136)

# find view
renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')

# find view
renderView2 = FindViewOrCreate('RenderView2', viewtype='RenderView')

# find view
renderView4 = FindViewOrCreate('RenderView4', viewtype='RenderView')

# current camera placement for renderView1
renderView1.CameraPosition = [175.25241088867188, 3023.123900962093, 2416.484130859375]
renderView1.CameraFocalPoint = [175.25241088867188, 0.0, 2416.484130859375]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 1386.1438050807299

# current camera placement for renderView2
renderView2.CameraPosition = [175.25241088867188, 3023.123900962093, 2416.484130859375]
renderView2.CameraFocalPoint = [175.25241088867188, 0.0, 2416.484130859375]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraParallelScale = 1386.1438050807299

# current camera placement for renderView3
renderView3.CameraPosition = [175.25241088867188, 3023.123900962093, 2416.484130859375]
renderView3.CameraFocalPoint = [175.25241088867188, 0.0, 2416.484130859375]
renderView3.CameraViewUp = [0.0, 0.0, 1.0]
renderView3.CameraParallelScale = 1386.1438050807299

# current camera placement for renderView4
renderView4.CameraPosition = [175.25241088867188, 3023.123900962093, 2416.484130859375]
renderView4.CameraFocalPoint = [175.25241088867188, 0.0, 2416.484130859375]
renderView4.CameraViewUp = [0.0, 0.0, 1.0]
renderView4.CameraParallelScale = 1386.1438050807299

# save screenshot
SaveScreenshot('/home/local/KHQ/abhi.yenpure/repositories/eam/forMovie/screenshot.png', layout1, 16, SaveAllViews=1,
    ImageResolution=[1979, 1136])
'''
