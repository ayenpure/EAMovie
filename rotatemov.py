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

LoadState("/home/local/KHQ/abhi.yenpure/repositories/eam/forMovie/state_slice_lat_lev_rotate1.pvsm")

# find source
v2_F2010_nc00_inst_macmic01eamh02010122500000nc = FindSource('v2_F2010_nc00_inst_macmic01.eam.h0.2010-12-25-00000.nc')

# Properties modified on v2_F2010_nc00_inst_macmic01eamh02010122500000nc
v2_F2010_nc00_inst_macmic01eamh02010122500000nc.a3DMiddleLayerVariables = ['cnd01_AST_ACTDIAG01', 'cnd01_CDMC_ACTDIAG01', 'cnd01_CDNC_ACTDIAG01', 'cnd01_RAL_ACTDIAG01', 'cnd01_REL_ACTDIAG01']


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
    b       = np.array([0.0, 5355.648401112309, 2416.484130859375, 1.0])
    cam = b.dot(rZmatrix)
    print(cam)

    renderView1.CameraPosition = [cam[0], cam[1], cam[2]]
    renderView1.CameraFocalPoint = [0.0, 0.0, 2416.484130859375]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraViewAngle = 15.88385994876174
    renderView1.CameraParallelScale = 1386.1438050807299

    # update the view to ensure updated data information
    renderView1.Update()

    x = ('%04d' %i)
    filename = 'rotateZ' + x + '.png'
    # save screenshot
    SaveScreenshot(filename, renderView1, 16, ImageResolution=[1988, 1144])
