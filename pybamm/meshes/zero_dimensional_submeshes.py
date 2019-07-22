#
# Zero dimensional submesh
#
import pybamm
import numpy as np


class SubMesh0D:
    """
    0D submesh class.
    Contains the position of the node.

    Parameters
    ----------
    position : dict
        A dictionary that contains the position of the spatial variable
    npts : dict, optional
        Number of points to be used. Included for compatibility with other meshes, but
        ignored by this mesh class
    """

    def __init__(self, position, npts=None):
        # check that only one variable passed in
        if len(position) != 1:
            raise pybamm.GeometryError("position should only contain a single variable")

        spatial_position = list(position.values())[0]
        self.nodes = np.array([spatial_position])
        self.npts = 1

    def add_ghost_meshes(self):
        # No ghost meshes to be added to this class
        pass