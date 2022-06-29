#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.8.0 with dump python functionality
###

import salome
import SMESH, SALOMEDS, GEOM
from salome.smesh import smeshBuilder
from salome.geom import geomBuilder
import salome_notebook

from parametric_values import test_list, component_to_test, max_size_range

salome.salome_init()

notebook = salome_notebook.NoteBook()


def generate_mesh_with_salome(
    med_mesh_filename,
    lipb_size=0.01,
    structure_size=0.01,
    baffle_plate_size=0.01,
    tungsten_size=0.01,
    bz_pipe_1_1_size=0.01,
    bz_pipe_1_2_size=0.01,
    bz_pipe_1_3_size=0.01,
    bz_pipe_2_1_size=0.01,
    bz_pipe_2_2_size=0.01,
    bz_pipe_2_3_size=0.01,
    bz_pipe_2_4_size=0.01,
    bz_pipe_3_1_size=0.01,
    bz_pipe_3_2_size=0.01,
    bz_pipe_3_3_size=0.01,
    bz_pipe_3_4_size=0.01,
):
    """creates a mesh using salome 9.8.0 in the WCLL model

    Args:
        lipb_size (float, optional): the maximum mesh cell size in the lipb
        structure_size (float, optional): the maximum mesh cell size in the structure
        baffle_plate_size (float, optional): the maximum mesh cell size in the baffle_plate
        tungsten_size (float, optional): the maximum mesh cell size in the tungsten
        bz_pipe_1_1_size (float, optional): the maximum mesh cell size in the bz_pipe_1_1
        bz_pipe_1_2_size (float, optional): the maximum mesh cell size in the bz_pipe_1_2
        bz_pipe_1_3_size (float, optional): the maximum mesh cell size in the bz_pipe_1_3
        bz_pipe_2_1_size (float, optional): the maximum mesh cell size in the bz_pipe_2_1
        bz_pipe_2_2_size (float, optional): the maximum mesh cell size in the bz_pipe_2_2
        bz_pipe_2_3_size (float, optional): the maximum mesh cell size in the bz_pipe_2_3
        bz_pipe_2_4_size (float, optional): the maximum mesh cell size in the bz_pipe_2_4
        bz_pipe_3_1_size (float, optional): the maximum mesh cell size in the bz_pipe_3_1
        bz_pipe_3_2_size (float, optional): the maximum mesh cell size in the bz_pipe_3_2
        bz_pipe_3_3_size (float, optional): the maximum mesh cell size in the bz_pipe_3_3
        bz_pipe_3_4_size (float, optional): the maximum mesh cell size in the bz_pipe_3_4

    Returns:
        [.med file]: the mesh file in .med format

    """
    ### GEOM component
    geompy = geomBuilder.New()

    O = geompy.MakeVertex(0, 0, 0)
    OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
    OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
    OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
    [Body1, Steel_SOLID] = geompy.ImportSTEP(
        "../data/meshes/CAD_files/WCLL ver 4/sym/Component1.step",
        False,
        True,
    )
    [Body1_1, Steel_SOLID_1] = geompy.ImportSTEP(
        "../data/meshes/CAD_files/WCLL ver 4/sym/Component10.step",
        False,
        True,
    )
    [Body1_2, Steel_SOLID_2] = geompy.ImportSTEP(
        "../data/meshes/CAD_files/WCLL ver 4/sym/Component11.step",
        False,
        True,
    )
    [Body1_3, Steel_SOLID_3] = geompy.ImportSTEP(
        "../data/meshes/CAD_files/WCLL ver 4/sym/Component12.step",
        False,
        True,
    )
    [Body1_4, Steel_SOLID_4] = geompy.ImportSTEP(
        "../data/meshes/CAD_files/WCLL ver 4/sym/Component13.step",
        False,
        True,
    )
    [Body1_5, Steel_SOLID_5] = geompy.ImportSTEP(
        "../data/meshes/CAD_files/WCLL ver 4/sym/Component14.step",
        False,
        True,
    )
    [Body1_6, Steel_SOLID_6] = geompy.ImportSTEP(
        "../data/meshes/CAD_files/WCLL ver 4/sym/Component15.step",
        False,
        True,
    )
    [Body1_7, Steel_SOLID_7] = geompy.ImportSTEP(
        "../data/meshes/CAD_files/WCLL ver 4/sym/Component2.step",
        False,
        True,
    )
    [Body1_8, Steel_SOLID_8] = geompy.ImportSTEP(
        "../data/meshes/CAD_files/WCLL ver 4/sym/Component3.step",
        False,
        True,
    )
    [Body1_9, Steel_SOLID_9] = geompy.ImportSTEP(
        "../data/meshes/CAD_files/WCLL ver 4/sym/Component4.step",
        False,
        True,
    )
    [Body1_10, Steel_SOLID_10] = geompy.ImportSTEP(
        "../data/meshes/CAD_files/WCLL ver 4/sym/Component5.step",
        False,
        True,
    )
    [Body1_11, Steel_SOLID_11] = geompy.ImportSTEP(
        "../data/meshes/CAD_files/WCLL ver 4/sym/Component6.step",
        False,
        True,
    )
    [Body1_12, Steel_SOLID_12] = geompy.ImportSTEP(
        "../data/meshes/CAD_files/WCLL ver 4/sym/Component7.step",
        False,
        True,
    )
    [Body1_13, Steel_SOLID_13] = geompy.ImportSTEP(
        "../data/meshes/CAD_files/WCLL ver 4/sym/Component8.step",
        False,
        True,
    )
    [Body1_14, Steel_SOLID_14] = geompy.ImportSTEP(
        "../data/meshes/CAD_files/WCLL ver 4/sym/Component9.step",
        False,
        True,
    )
    WCLL_3D = geompy.MakePartition(
        [
            Body1,
            Body1_1,
            Body1_2,
            Body1_3,
            Body1_4,
            Body1_5,
            Body1_6,
            Body1_7,
            Body1_8,
            Body1_9,
            Body1_10,
            Body1_11,
            Body1_12,
            Body1_13,
            Body1_14,
        ],
        [],
        [],
        [],
        geompy.ShapeType["SOLID"],
        0,
        [],
        0,
    )
    slicer = geompy.MakeFaceHW(10, 10, 1)
    central_z_position = geompy.MakeTranslation(slicer, 0, 0, 0.058)
    WCLL_2D = geompy.MakeCommonList([WCLL_3D, central_z_position], True)
    lipb = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["FACE"])
    geompy.UnionIDs(lipb, [115])
    structure = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["FACE"])
    geompy.UnionIDs(structure, [2])
    baffle_plate = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["FACE"])
    geompy.UnionIDs(baffle_plate, [105])
    tungsten = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["FACE"])
    geompy.UnionIDs(tungsten, [98])
    bz_pipe_1_1 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["FACE"])
    geompy.UnionIDs(bz_pipe_1_1, [63])
    bz_pipe_1_2 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["FACE"])
    geompy.UnionIDs(bz_pipe_1_2, [155])
    bz_pipe_1_3 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["FACE"])
    geompy.UnionIDs(bz_pipe_1_3, [145])
    bz_pipe_2_1 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["FACE"])
    geompy.UnionIDs(bz_pipe_2_1, [140])
    bz_pipe_2_2 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["FACE"])
    geompy.UnionIDs(bz_pipe_2_2, [150])
    bz_pipe_2_3 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["FACE"])
    geompy.UnionIDs(bz_pipe_2_3, [56])
    bz_pipe_2_4 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["FACE"])
    geompy.UnionIDs(bz_pipe_2_4, [160])
    bz_pipe_3_1 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["FACE"])
    geompy.UnionIDs(bz_pipe_3_1, [84])
    bz_pipe_3_2 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["FACE"])
    geompy.UnionIDs(bz_pipe_3_2, [91])
    bz_pipe_3_3 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["FACE"])
    geompy.UnionIDs(bz_pipe_3_3, [77])
    bz_pipe_3_4 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["FACE"])
    geompy.UnionIDs(bz_pipe_3_4, [70])
    inlet = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(inlet, [117])
    outlet = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(outlet, [118])
    plasma_facing_wall = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(plasma_facing_wall, [104])
    fw_coolant_interface_1_1 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(fw_coolant_interface_1_1, [28, 24, 26, 21])
    fw_coolant_interface_1_2 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(fw_coolant_interface_1_2, [35, 33, 37, 30])
    fw_coolant_interface_1_3 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(fw_coolant_interface_1_3, [42, 46, 44, 39])
    fw_coolant_interface_1_4 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(fw_coolant_interface_1_4, [53, 48, 51, 55])
    bz_coolant_interface_1_1 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(bz_coolant_interface_1_1, [68])
    bz_coolant_interface_1_2 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(bz_coolant_interface_1_2, [158])
    bz_coolant_interface_1_3 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(bz_coolant_interface_1_3, [148])
    bz_coolant_interface_2_1 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(bz_coolant_interface_2_1, [143])
    bz_coolant_interface_2_2 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(bz_coolant_interface_2_2, [153])
    bz_coolant_interface_2_3 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(bz_coolant_interface_2_3, [61])
    bz_coolant_interface_2_4 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(bz_coolant_interface_2_4, [163])
    bz_coolant_interface_3_1 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(bz_coolant_interface_3_1, [89])
    bz_coolant_interface_3_2 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(bz_coolant_interface_3_2, [96])
    bz_coolant_interface_3_3 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(bz_coolant_interface_3_3, [82])
    bz_coolant_interface_3_4 = geompy.CreateGroup(WCLL_2D, geompy.ShapeType["EDGE"])
    geompy.UnionIDs(bz_coolant_interface_3_4, [75])
    [
        lipb,
        structure,
        baffle_plate,
        tungsten,
        bz_pipe_1_1,
        bz_pipe_1_2,
        bz_pipe_1_3,
        bz_pipe_2_1,
        bz_pipe_2_2,
        bz_pipe_2_3,
        bz_pipe_2_4,
        bz_pipe_3_1,
        bz_pipe_3_2,
        bz_pipe_3_3,
        bz_pipe_3_4,
        inlet,
        outlet,
        plasma_facing_wall,
        fw_coolant_interface_1_1,
        fw_coolant_interface_1_2,
        fw_coolant_interface_1_3,
        fw_coolant_interface_1_4,
        bz_coolant_interface_1_1,
        bz_coolant_interface_1_2,
        bz_coolant_interface_1_3,
        bz_coolant_interface_2_1,
        bz_coolant_interface_2_2,
        bz_coolant_interface_2_3,
        bz_coolant_interface_2_4,
        bz_coolant_interface_3_1,
        bz_coolant_interface_3_2,
        bz_coolant_interface_3_3,
        bz_coolant_interface_3_4,
    ] = geompy.GetExistingSubObjects(WCLL_2D, False)
    geompy.addToStudy(O, "O")
    geompy.addToStudy(OX, "OX")
    geompy.addToStudy(OY, "OY")
    geompy.addToStudy(OZ, "OZ")
    geompy.addToStudy(Body1, "Body1")
    geompy.addToStudyInFather(Body1, Steel_SOLID, "Steel_SOLID")
    geompy.addToStudy(Body1_1, "Body1")
    geompy.addToStudyInFather(Body1_1, Steel_SOLID_1, "Steel_SOLID")
    geompy.addToStudy(Body1_2, "Body1")
    geompy.addToStudyInFather(Body1_2, Steel_SOLID_2, "Steel_SOLID")
    geompy.addToStudy(Body1_3, "Body1")
    geompy.addToStudyInFather(Body1_3, Steel_SOLID_3, "Steel_SOLID")
    geompy.addToStudy(Body1_4, "Body1")
    geompy.addToStudyInFather(Body1_4, Steel_SOLID_4, "Steel_SOLID")
    geompy.addToStudy(Body1_5, "Body1")
    geompy.addToStudyInFather(Body1_5, Steel_SOLID_5, "Steel_SOLID")
    geompy.addToStudy(Body1_6, "Body1")
    geompy.addToStudyInFather(Body1_6, Steel_SOLID_6, "Steel_SOLID")
    geompy.addToStudy(Body1_7, "Body1")
    geompy.addToStudyInFather(Body1_7, Steel_SOLID_7, "Steel_SOLID")
    geompy.addToStudy(Body1_8, "Body1")
    geompy.addToStudyInFather(Body1_8, Steel_SOLID_8, "Steel_SOLID")
    geompy.addToStudy(Body1_9, "Body1")
    geompy.addToStudyInFather(Body1_9, Steel_SOLID_9, "Steel_SOLID")
    geompy.addToStudy(Body1_10, "Body1")
    geompy.addToStudyInFather(Body1_10, Steel_SOLID_10, "Steel_SOLID")
    geompy.addToStudy(Body1_11, "Body1")
    geompy.addToStudyInFather(Body1_11, Steel_SOLID_11, "Steel_SOLID")
    geompy.addToStudy(Body1_12, "Body1")
    geompy.addToStudyInFather(Body1_12, Steel_SOLID_12, "Steel_SOLID")
    geompy.addToStudy(Body1_13, "Body1")
    geompy.addToStudyInFather(Body1_13, Steel_SOLID_13, "Steel_SOLID")
    geompy.addToStudy(Body1_14, "Body1")
    geompy.addToStudyInFather(Body1_14, Steel_SOLID_14, "Steel_SOLID")
    geompy.addToStudy(WCLL_3D, "WCLL_3D")
    geompy.addToStudy(slicer, "slicer")
    geompy.addToStudy(central_z_position, "central_z_position")
    geompy.addToStudy(WCLL_2D, "WCLL_2D")
    geompy.addToStudyInFather(WCLL_2D, lipb, "lipb")
    geompy.addToStudyInFather(WCLL_2D, structure, "structure")
    geompy.addToStudyInFather(WCLL_2D, baffle_plate, "baffle_plate")
    geompy.addToStudyInFather(WCLL_2D, tungsten, "tungsten")
    geompy.addToStudyInFather(WCLL_2D, bz_pipe_1_1, "bz_pipe_1_1")
    geompy.addToStudyInFather(WCLL_2D, bz_pipe_1_2, "bz_pipe_1_2")
    geompy.addToStudyInFather(WCLL_2D, bz_pipe_1_3, "bz_pipe_1_3")
    geompy.addToStudyInFather(WCLL_2D, bz_pipe_2_1, "bz_pipe_2_1")
    geompy.addToStudyInFather(WCLL_2D, bz_pipe_2_2, "bz_pipe_2_2")
    geompy.addToStudyInFather(WCLL_2D, bz_pipe_2_3, "bz_pipe_2_3")
    geompy.addToStudyInFather(WCLL_2D, bz_pipe_2_4, "bz_pipe_2_4")
    geompy.addToStudyInFather(WCLL_2D, bz_pipe_3_1, "bz_pipe_3_1")
    geompy.addToStudyInFather(WCLL_2D, bz_pipe_3_2, "bz_pipe_3_2")
    geompy.addToStudyInFather(WCLL_2D, bz_pipe_3_3, "bz_pipe_3_3")
    geompy.addToStudyInFather(WCLL_2D, bz_pipe_3_4, "bz_pipe_3_4")
    geompy.addToStudyInFather(WCLL_2D, inlet, "inlet")
    geompy.addToStudyInFather(WCLL_2D, outlet, "outlet")
    geompy.addToStudyInFather(WCLL_2D, plasma_facing_wall, "plasma_facing_wall")
    geompy.addToStudyInFather(
        WCLL_2D, fw_coolant_interface_1_1, "fw_coolant_interface_1_1"
    )
    geompy.addToStudyInFather(
        WCLL_2D, fw_coolant_interface_1_2, "fw_coolant_interface_1_2"
    )
    geompy.addToStudyInFather(
        WCLL_2D, fw_coolant_interface_1_3, "fw_coolant_interface_1_3"
    )
    geompy.addToStudyInFather(
        WCLL_2D, fw_coolant_interface_1_4, "fw_coolant_interface_1_4"
    )
    geompy.addToStudyInFather(
        WCLL_2D, bz_coolant_interface_1_1, "bz_coolant_interface_1_1"
    )
    geompy.addToStudyInFather(
        WCLL_2D, bz_coolant_interface_1_2, "bz_coolant_interface_1_2"
    )
    geompy.addToStudyInFather(
        WCLL_2D, bz_coolant_interface_1_3, "bz_coolant_interface_1_3"
    )
    geompy.addToStudyInFather(
        WCLL_2D, bz_coolant_interface_2_1, "bz_coolant_interface_2_1"
    )
    geompy.addToStudyInFather(
        WCLL_2D, bz_coolant_interface_2_2, "bz_coolant_interface_2_2"
    )
    geompy.addToStudyInFather(
        WCLL_2D, bz_coolant_interface_2_3, "bz_coolant_interface_2_3"
    )
    geompy.addToStudyInFather(
        WCLL_2D, bz_coolant_interface_2_4, "bz_coolant_interface_2_4"
    )
    geompy.addToStudyInFather(
        WCLL_2D, bz_coolant_interface_3_1, "bz_coolant_interface_3_1"
    )
    geompy.addToStudyInFather(
        WCLL_2D, bz_coolant_interface_3_2, "bz_coolant_interface_3_2"
    )
    geompy.addToStudyInFather(
        WCLL_2D, bz_coolant_interface_3_3, "bz_coolant_interface_3_3"
    )
    geompy.addToStudyInFather(
        WCLL_2D, bz_coolant_interface_3_4, "bz_coolant_interface_3_4"
    )

    ### SMESH component

    smesh = smeshBuilder.New()
    # smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
    # multiples meshes built in parallel, complex and numerous mesh edition (performance)

    Mesh_2D = smesh.Mesh(WCLL_2D)
    NETGEN_1D_2D = Mesh_2D.Triangle(algo=smeshBuilder.NETGEN_1D2D)
    lipb_1 = Mesh_2D.GroupOnGeom(lipb, "lipb", SMESH.FACE)
    structure_1 = Mesh_2D.GroupOnGeom(structure, "structure", SMESH.FACE)
    baffle_plate_1 = Mesh_2D.GroupOnGeom(baffle_plate, "baffle_plate", SMESH.FACE)
    tungsten_1 = Mesh_2D.GroupOnGeom(tungsten, "tungsten", SMESH.FACE)
    bz_pipe_1_1_1 = Mesh_2D.GroupOnGeom(bz_pipe_1_1, "bz_pipe_1_1", SMESH.FACE)
    bz_pipe_1_2_1 = Mesh_2D.GroupOnGeom(bz_pipe_1_2, "bz_pipe_1_2", SMESH.FACE)
    bz_pipe_1_3_1 = Mesh_2D.GroupOnGeom(bz_pipe_1_3, "bz_pipe_1_3", SMESH.FACE)
    bz_pipe_2_1_1 = Mesh_2D.GroupOnGeom(bz_pipe_2_1, "bz_pipe_2_1", SMESH.FACE)
    bz_pipe_2_2_1 = Mesh_2D.GroupOnGeom(bz_pipe_2_2, "bz_pipe_2_2", SMESH.FACE)
    bz_pipe_2_3_1 = Mesh_2D.GroupOnGeom(bz_pipe_2_3, "bz_pipe_2_3", SMESH.FACE)
    bz_pipe_2_4_1 = Mesh_2D.GroupOnGeom(bz_pipe_2_4, "bz_pipe_2_4", SMESH.FACE)
    bz_pipe_3_1_1 = Mesh_2D.GroupOnGeom(bz_pipe_3_1, "bz_pipe_3_1", SMESH.FACE)
    bz_pipe_3_2_1 = Mesh_2D.GroupOnGeom(bz_pipe_3_2, "bz_pipe_3_2", SMESH.FACE)
    bz_pipe_3_3_1 = Mesh_2D.GroupOnGeom(bz_pipe_3_3, "bz_pipe_3_3", SMESH.FACE)
    bz_pipe_3_4_1 = Mesh_2D.GroupOnGeom(bz_pipe_3_4, "bz_pipe_3_4", SMESH.FACE)
    inlet_1 = Mesh_2D.GroupOnGeom(inlet, "inlet", SMESH.EDGE)
    outlet_1 = Mesh_2D.GroupOnGeom(outlet, "outlet", SMESH.EDGE)
    plasma_facing_wall_1 = Mesh_2D.GroupOnGeom(
        plasma_facing_wall, "plasma_facing_wall", SMESH.EDGE
    )
    fw_coolant_interface_1_1_1 = Mesh_2D.GroupOnGeom(
        fw_coolant_interface_1_1, "fw_coolant_interface_1_1", SMESH.EDGE
    )
    fw_coolant_interface_1_2_1 = Mesh_2D.GroupOnGeom(
        fw_coolant_interface_1_2, "fw_coolant_interface_1_2", SMESH.EDGE
    )
    fw_coolant_interface_1_3_1 = Mesh_2D.GroupOnGeom(
        fw_coolant_interface_1_3, "fw_coolant_interface_1_3", SMESH.EDGE
    )
    fw_coolant_interface_1_4_1 = Mesh_2D.GroupOnGeom(
        fw_coolant_interface_1_4, "fw_coolant_interface_1_4", SMESH.EDGE
    )
    bz_coolant_interface_1_1_1 = Mesh_2D.GroupOnGeom(
        bz_coolant_interface_1_1, "bz_coolant_interface_1_1", SMESH.EDGE
    )
    bz_coolant_interface_1_2_1 = Mesh_2D.GroupOnGeom(
        bz_coolant_interface_1_2, "bz_coolant_interface_1_2", SMESH.EDGE
    )
    bz_coolant_interface_1_3_1 = Mesh_2D.GroupOnGeom(
        bz_coolant_interface_1_3, "bz_coolant_interface_1_3", SMESH.EDGE
    )
    bz_coolant_interface_2_1_1 = Mesh_2D.GroupOnGeom(
        bz_coolant_interface_2_1, "bz_coolant_interface_2_1", SMESH.EDGE
    )
    bz_coolant_interface_2_2_1 = Mesh_2D.GroupOnGeom(
        bz_coolant_interface_2_2, "bz_coolant_interface_2_2", SMESH.EDGE
    )
    bz_coolant_interface_2_3_1 = Mesh_2D.GroupOnGeom(
        bz_coolant_interface_2_3, "bz_coolant_interface_2_3", SMESH.EDGE
    )
    bz_coolant_interface_2_4_1 = Mesh_2D.GroupOnGeom(
        bz_coolant_interface_2_4, "bz_coolant_interface_2_4", SMESH.EDGE
    )
    bz_coolant_interface_3_1_1 = Mesh_2D.GroupOnGeom(
        bz_coolant_interface_3_1, "bz_coolant_interface_3_1", SMESH.EDGE
    )
    bz_coolant_interface_3_2_1 = Mesh_2D.GroupOnGeom(
        bz_coolant_interface_3_2, "bz_coolant_interface_3_2", SMESH.EDGE
    )
    bz_coolant_interface_3_3_1 = Mesh_2D.GroupOnGeom(
        bz_coolant_interface_3_3, "bz_coolant_interface_3_3", SMESH.EDGE
    )
    bz_coolant_interface_3_4_1 = Mesh_2D.GroupOnGeom(
        bz_coolant_interface_3_4, "bz_coolant_interface_3_4", SMESH.EDGE
    )
    isDone = Mesh_2D.Compute()
    [
        lipb_1,
        structure_1,
        baffle_plate_1,
        tungsten_1,
        bz_pipe_1_1_1,
        bz_pipe_1_2_1,
        bz_pipe_1_3_1,
        bz_pipe_2_1_1,
        bz_pipe_2_2_1,
        bz_pipe_2_3_1,
        bz_pipe_2_4_1,
        bz_pipe_3_1_1,
        bz_pipe_3_2_1,
        bz_pipe_3_3_1,
        bz_pipe_3_4_1,
        inlet_1,
        outlet_1,
        plasma_facing_wall_1,
        fw_coolant_interface_1_1_1,
        fw_coolant_interface_1_2_1,
        fw_coolant_interface_1_3_1,
        fw_coolant_interface_1_4_1,
        bz_coolant_interface_1_1_1,
        bz_coolant_interface_1_2_1,
        bz_coolant_interface_1_3_1,
        bz_coolant_interface_2_1_1,
        bz_coolant_interface_2_2_1,
        bz_coolant_interface_2_3_1,
        bz_coolant_interface_2_4_1,
        bz_coolant_interface_3_1_1,
        bz_coolant_interface_3_2_1,
        bz_coolant_interface_3_3_1,
        bz_coolant_interface_3_4_1,
    ] = Mesh_2D.GetGroups()
    NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
    NETGEN_2D_Parameters_1.SetMaxSize(0.002)
    NETGEN_2D_Parameters_1.SetMinSize(0.001)
    NETGEN_2D_Parameters_1.SetSecondOrder(0)
    NETGEN_2D_Parameters_1.SetOptimize(1)
    NETGEN_2D_Parameters_1.SetFineness(2)
    NETGEN_2D_Parameters_1.SetChordalError(-1)
    NETGEN_2D_Parameters_1.SetChordalErrorEnabled(0)
    NETGEN_2D_Parameters_1.SetUseSurfaceCurvature(1)
    NETGEN_2D_Parameters_1.SetFuseEdges(1)
    NETGEN_2D_Parameters_1.SetUseDelauney(0)
    NETGEN_2D_Parameters_1.SetQuadAllowed(0)
    NETGEN_2D_Parameters_1.SetLocalSizeOnShape(lipb, lipb_size)
    NETGEN_2D_Parameters_1.SetLocalSizeOnShape(structure, structure_size)
    NETGEN_2D_Parameters_1.SetLocalSizeOnShape(baffle_plate, baffle_plate_size)
    NETGEN_2D_Parameters_1.SetLocalSizeOnShape(tungsten, tungsten_size)
    NETGEN_2D_Parameters_1.SetLocalSizeOnShape(bz_pipe_1_1, bz_pipe_1_1_size)
    NETGEN_2D_Parameters_1.SetLocalSizeOnShape(bz_pipe_1_2, bz_pipe_1_2_size)
    NETGEN_2D_Parameters_1.SetLocalSizeOnShape(bz_pipe_1_3, bz_pipe_1_3_size)
    NETGEN_2D_Parameters_1.SetLocalSizeOnShape(bz_pipe_2_1, bz_pipe_2_1_size)
    NETGEN_2D_Parameters_1.SetLocalSizeOnShape(bz_pipe_2_2, bz_pipe_2_2_size)
    NETGEN_2D_Parameters_1.SetLocalSizeOnShape(bz_pipe_2_3, bz_pipe_2_3_size)
    NETGEN_2D_Parameters_1.SetLocalSizeOnShape(bz_pipe_2_4, bz_pipe_2_4_size)
    NETGEN_2D_Parameters_1.SetLocalSizeOnShape(bz_pipe_3_1, bz_pipe_3_1_size)
    NETGEN_2D_Parameters_1.SetLocalSizeOnShape(bz_pipe_3_2, bz_pipe_3_2_size)
    NETGEN_2D_Parameters_1.SetLocalSizeOnShape(bz_pipe_3_3, bz_pipe_3_3_size)
    NETGEN_2D_Parameters_1.SetLocalSizeOnShape(bz_pipe_3_4, bz_pipe_3_4_size)
    NETGEN_2D_Parameters_1.SetWorstElemMeasure(35)
    NETGEN_2D_Parameters_1.SetCheckChartBoundary(64)
    isDone = Mesh_2D.Compute()

    ## Set names of Mesh objects
    smesh.SetName(bz_pipe_2_3_1, "bz_pipe_2_3")
    smesh.SetName(bz_pipe_2_4_1, "bz_pipe_2_4")
    smesh.SetName(bz_pipe_3_1_1, "bz_pipe_3_1")
    smesh.SetName(bz_pipe_3_2_1, "bz_pipe_3_2")
    smesh.SetName(bz_pipe_3_3_1, "bz_pipe_3_3")
    smesh.SetName(bz_pipe_3_4_1, "bz_pipe_3_4")
    smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), "NETGEN 1D-2D")
    smesh.SetName(bz_pipe_2_2_1, "bz_pipe_2_2")
    smesh.SetName(bz_pipe_2_1_1, "bz_pipe_2_1")
    smesh.SetName(lipb_1, "lipb")
    smesh.SetName(bz_coolant_interface_3_4_1, "bz_coolant_interface_3_4")
    smesh.SetName(baffle_plate_1, "baffle_plate")
    smesh.SetName(structure_1, "structure")
    smesh.SetName(bz_pipe_1_1_1, "bz_pipe_1_1")
    smesh.SetName(tungsten_1, "tungsten")
    smesh.SetName(bz_coolant_interface_1_1_1, "bz_coolant_interface_1_1")
    smesh.SetName(bz_pipe_1_3_1, "bz_pipe_1_3")
    smesh.SetName(bz_coolant_interface_1_2_1, "bz_coolant_interface_1_2")
    smesh.SetName(bz_pipe_1_2_1, "bz_pipe_1_2")
    smesh.SetName(bz_coolant_interface_2_1_1, "bz_coolant_interface_2_1")
    smesh.SetName(bz_coolant_interface_1_3_1, "bz_coolant_interface_1_3")
    smesh.SetName(bz_coolant_interface_2_3_1, "bz_coolant_interface_2_3")
    smesh.SetName(bz_coolant_interface_2_2_1, "bz_coolant_interface_2_2")
    smesh.SetName(bz_coolant_interface_3_1_1, "bz_coolant_interface_3_1")
    smesh.SetName(bz_coolant_interface_2_4_1, "bz_coolant_interface_2_4")
    smesh.SetName(Mesh_2D.GetMesh(), "Mesh_2D")
    smesh.SetName(bz_coolant_interface_3_3_1, "bz_coolant_interface_3_3")
    smesh.SetName(bz_coolant_interface_3_2_1, "bz_coolant_interface_3_2")
    smesh.SetName(inlet_1, "inlet")
    smesh.SetName(outlet_1, "outlet")
    smesh.SetName(plasma_facing_wall_1, "plasma_facing_wall")
    smesh.SetName(fw_coolant_interface_1_1_1, "fw_coolant_interface_1_1")
    smesh.SetName(fw_coolant_interface_1_2_1, "fw_coolant_interface_1_2")
    smesh.SetName(fw_coolant_interface_1_3_1, "fw_coolant_interface_1_3")
    smesh.SetName(fw_coolant_interface_1_4_1, "fw_coolant_interface_1_4")
    smesh.SetName(NETGEN_2D_Parameters_1, "NETGEN 2D Parameters_1")

    try:
        Mesh_2D.ExportMED(
            med_mesh_filename,
            auto_groups=0,
            version=41,
            overwrite=1,
            meshPart=None,
            autoDimension=1,
        )
        pass
    except:
        print("ExportMED() failed. Invalid file name?")

    if salome.sg.hasDesktop():
        salome.sg.updateObjBrowser()


if __name__ == "__main__":
    # generate_mesh_with_salome(med_mesh_filename="Mesh_2D.med")
    n = 0
    for list in test_list:
        n += 1
        if component_to_test == "lipb":
            size = list[0]
        elif component_to_test == "structure":
            size = list[1]
        elif component_to_test == "baffle":
            size = list[2]
        elif component_to_test == "tungsten":
            size = list[3]
        elif component_to_test == "pipes":
            size = list[4]
        elif component_to_test == "everything":
            size = list[0]
        elif component_to_test == "lipb_2.2e-3_everything_else":
            size = list[1]
        elif component_to_test == "everything_optimised_1" or "everything_optimised_5":
            size = list[-1]

        print(
            "meshing for size = {:.1e}, iteration {} of {}".format(
                size, n, len(max_size_range)
            )
        )
        med_mesh_filename = (
            "../data/meshes/mesh_study/med_files/{}_max_size_{:.1e}.med".format(
                component_to_test, size
            )
        )
        lipb_size = list[0]
        structure_size = list[1]
        baffle_plate_size = list[2]
        tungsten_size = list[3]
        bz_pipe_1_1_size = list[4]
        bz_pipe_1_2_size = list[5]
        bz_pipe_1_3_size = list[6]
        bz_pipe_2_1_size = list[7]
        bz_pipe_2_2_size = list[8]
        bz_pipe_2_3_size = list[9]
        bz_pipe_2_4_size = list[10]
        bz_pipe_3_1_size = list[11]
        bz_pipe_3_2_size = list[12]
        bz_pipe_3_3_size = list[13]
        bz_pipe_3_4_size = list[14]

        generate_mesh_with_salome(
            med_mesh_filename=med_mesh_filename,
            lipb_size=lipb_size,
            structure_size=structure_size,
            baffle_plate_size=baffle_plate_size,
            tungsten_size=tungsten_size,
            bz_pipe_1_1_size=bz_pipe_1_1_size,
            bz_pipe_1_2_size=bz_pipe_1_2_size,
            bz_pipe_1_3_size=bz_pipe_1_3_size,
            bz_pipe_2_1_size=bz_pipe_2_1_size,
            bz_pipe_2_2_size=bz_pipe_2_2_size,
            bz_pipe_2_3_size=bz_pipe_2_3_size,
            bz_pipe_2_4_size=bz_pipe_2_4_size,
            bz_pipe_3_1_size=bz_pipe_3_1_size,
            bz_pipe_3_2_size=bz_pipe_3_2_size,
            bz_pipe_3_3_size=bz_pipe_3_3_size,
            bz_pipe_3_4_size=bz_pipe_3_4_size,
        )
        print("done")
