##################################################################
######################## include.py   ############################
##################################################################
##### ekate - Enhanced KRATOS for Advanced Tunnel Enineering #####
##### copyright by CIMNE, Barcelona, Spain                   #####
#####          and Institute for Structural Mechanics, RUB   #####
##### all rights reserved                                    #####
##################################################################
##################################################################
##################################################################
##################################################################
import sys
import os
kratos_root_path=os.environ['KRATOS_ROOT_PATH']
##################################################################
##################################################################
#importing Kratos modules
from KratosMultiphysics import *
from KratosMultiphysics.IsogeometricApplication import *
kernel = Kernel()   #defining kernel

nurbs_fespace_library = NURBSFESpaceLibrary()
grid_util = ControlGridUtility()
multipatch_util = MultiPatchUtility()
mpatch = MultiPatch2D()

fes1 = nurbs_fespace_library.CreateRectangularFESpace(3, 3)
ctrl_grid_1 = grid_util.CreateRectangularControlPointGrid(0.0, 0.0, fes1.Number(0), fes1.Number(1), 1.0, 1.0)
patch1_ptr = multipatch_util.CreatePatchPointer(1, fes1)
patch1 = patch1_ptr.GetReference()
patch1.CreateControlPointGridFunction(ctrl_grid_1)
#print(patch1)
multipatch_util.ExportGeo(patch1, "patch1.txt")

fes2 = nurbs_fespace_library.CreateRectangularFESpace(3, 3)
ctrl_grid_2 = grid_util.CreateRectangularControlPointGrid(1.0, 0.0, fes1.Number(0), fes1.Number(1), 2.0, 1.0)
patch2_ptr = multipatch_util.CreatePatchPointer(2, fes2)
patch2 = patch2_ptr.GetReference()
patch2.CreateControlPointGridFunction(ctrl_grid_2)
#print(patch2)
multipatch_util.ExportGeo(patch2, "patch2.txt")

mpatch.AddPatch(patch1)
mpatch.AddPatch(patch2)
mpatch.ResetId()
mpatch.MakeNeighbor(patch1, BoundarySide.Right, patch2, BoundarySide.Left)
print(mpatch)

print("############REFINEMENT###############")
multipatch_refine_util = MultiPatchRefinementUtility()
multipatch_refine_util.InsertKnots(patch1_ptr, [[0.5], [0.5]])
#patch1 = patch1_ptr.GetReference()
#patch2 = patch2_ptr.GetReference()
#print("############RESULTS###############")
multipatch_util.ExportGlvis(mpatch, "mpatch.mesh")

system_size = mpatch.Enumerate()
print("system_size:", system_size)
print(mpatch)

#################RESULTS#####################(Validated with Matlab)
##>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<
##-------------Begin MultiPatchInfo-------------
##MultiPatch overview: Number of patches = 2
##MultiPatch details:
##-------------Begin PatchInfo-------------
##Patch2D, Id = 1, Add = 0x24416d0
##-------------Begin FESpaceInfo-------------
##NURBSFESpace2D, Add = 0x2440f90, n = ( 5 5), p = ( 3 3)
## knot vector 0: 0 0 0 0 0.5 1 1 1 1
## knot vector 1: 0 0 0 0 0.5 1 1 1 1
##-------------End FESpaceInfo-------------
##Grid CONTROL_POINT: [5, 5]
## Data:
## (
##  ( (0, 0, 0, 1) (0, 0.166667, 0, 1) (0, 0.5, 0, 1) (0, 0.833333, 0, 1) (0, 1, 0, 1))
##  ( (0.166667, 0, 0, 1) (0.166667, 0.166667, 0, 1) (0.166667, 0.5, 0, 1) (0.166667, 0.833333, 0, 1) (0.166667, 1, 0, 1))
##  ( (0.5, 0, 0, 1) (0.5, 0.166667, 0, 1) (0.5, 0.5, 0, 1) (0.5, 0.833333, 0, 1) (0.5, 1, 0, 1))
##  ( (0.833333, 0, 0, 1) (0.833333, 0.166667, 0, 1) (0.833333, 0.5, 0, 1) (0.833333, 0.833333, 0, 1) (0.833333, 1, 0, 1))
##  ( (1, 0, 0, 1) (1, 0.166667, 0, 1) (1, 0.5, 0, 1) (1, 0.833333, 0, 1) (1, 1, 0, 1))
## )
##Neighbors =  right:2
##-------------End PatchInfo-------------
##-------------Begin PatchInfo-------------
##Patch2D, Id = 2, Add = 0x2440e20
##-------------Begin FESpaceInfo-------------
##NURBSFESpace2D, Add = 0x24ca0a0, n = ( 4 5), p = ( 3 3)
## knot vector 0: 0 0 0 0 1 1 1 1
## knot vector 1: 0 0 0 0 0.5 1 1 1 1
##-------------End FESpaceInfo-------------
##Grid CONTROL_POINT: [4, 5]
## Data:
## (
##  ( (1, 0, 0, 1) (1, 0.166667, 0, 1) (1, 0.5, 0, 1) (1, 0.833333, 0, 1) (1, 1, 0, 1))
##  ( (1.33333, 0, 0, 1) (1.33333, 0.166667, 0, 1) (1.33333, 0.5, 0, 1) (1.33333, 0.833333, 0, 1) (1.33333, 1, 0, 1))
##  ( (1.66667, 0, 0, 1) (1.66667, 0.166667, 0, 1) (1.66667, 0.5, 0, 1) (1.66667, 0.833333, 0, 1) (1.66667, 1, 0, 1))
##  ( (2, 0, 0, 1) (2, 0.166667, 0, 1) (2, 0.5, 0, 1) (2, 0.833333, 0, 1) (2, 1, 0, 1))
## )
##Neighbors =  left:1
##-------------End PatchInfo-------------
##-------------End MultiPatchInfo-------------
##>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<

