# trace generated using paraview version 5.11.1-1745-ge8c78138a6
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11
import numpy as np
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

LoadPlugin("/home/local/KHQ/abhi.yenpure/repositories/eam/scripts/eam_reader.py", ns=globals())
LoadPlugin("/home/local/KHQ/abhi.yenpure/repositories/eam/scripts/eam_filters.py", ns=globals())
LoadPlugin("/home/local/KHQ/abhi.yenpure/repositories/eam/scripts/eam_projection.py", ns=globals())
LoadState("/home/local/KHQ/abhi.yenpure/repositories/eam/forMovie/states/state_slice_lat_lev_rotate_layout1.pvsm")

v2_F2010_nc00_inst_macmic01eamh02010122500000nc = FindSource('v2_F2010_nc00_inst_macmic01.eam.h0.2010-12-25-00000.nc')
SetActiveSource(v2_F2010_nc00_inst_macmic01eamh02010122500000nc)
v2_F2010_nc00_inst_macmic01eamh02010122500000nc.a3DMiddleLayerVariables = ['cnd01_ALST_ACTDIAG01', 'cnd01_AST_ACTDIAG01', 'cnd01_CDMC_ACTDIAG01', 'cnd01_CDNC_ACTDIAG01', 'cnd01_RAL_ACTDIAG01', 'cnd01_REL_ACTDIAG01']

# find source
eAMVTSSphere1 = FindSource('EAMVTSSphere1')
# set active source
SetActiveSource(eAMVTSSphere1)
cnd01_AST_ACTDIAG01LUT = GetColorTransferFunction('cnd01_AST_ACTDIAG01')
cnd01_AST_ACTDIAG01PWF = GetOpacityTransferFunction('cnd01_AST_ACTDIAG01')
cnd01_AST_ACTDIAG01TF2D = GetTransferFunction2D('cnd01_AST_ACTDIAG01')

from os import listdir
from os.path import isfile, join

presetsDir = '/home/local/KHQ/abhi.yenpure/repositories/eam/ScientificColourMaps8_ParaView'
presetnames = np.array([f for f in listdir(presetsDir) if isfile(join(presetsDir, f))])
presetpaths = np.array([join(presetsDir, f) for f in presetnames]) 

renderView1 = GetActiveViewOrCreate('RenderView')
# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [531.7759596581271, 4369.374717357803, 2151.6182850174414]
renderView1.CameraFocalPoint = [531.7759596581271, 0.0, 2151.6182850174414]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 338.4313507490336

eAMVTSSphere1Display = GetDisplayProperties(eAMVTSSphere1, view=renderView1)

layout1 = GetLayout()
layout1.SetSize(1988, 1144)

for (fname, fpath) in zip(presetnames, presetpaths):
    name = fname.split('_')[0]
    print(name)

    ImportPresets(filename=fpath, location=16)
    cnd01_AST_ACTDIAG01LUT.ApplyPreset(name, True)
    # save screenshot
    SaveScreenshot(join('/home/local/KHQ/abhi.yenpure/repositories/eam/forMovie/', name + '.png'), renderView1, 16, ImageResolution=[1988, 1144])
    # invert the transfer function
    cnd01_AST_ACTDIAG01LUT.InvertTransferFunction()
    SaveScreenshot(join('/home/local/KHQ/abhi.yenpure/repositories/eam/forMovie/', name + '_inv.png'), renderView1, 16, ImageResolution=[1988, 1144])
