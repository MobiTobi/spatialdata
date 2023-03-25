from importlib.metadata import version

__version__ = version("spatialdata")

# Forcing usage of shapely 2.0 by geopandas
# https://geopandas.org/en/stable/getting_started/install.html#using-the-optional-pygeos-dependency
from ._compat import _check_geopandas_using_shapely

_check_geopandas_using_shapely()


__all__ = [
    "models",
    "transformations",
    "dataloader",
    "concatenate",
    "rasterize",
    "transform",
    "bounding_box_query",
    "SpatialData",
    "read_zarr",
    "unpad_raster",
    "multiscale_spatial_image_from_data_tree",
    "iterate_pyramid_levels",
]

from spatialdata import dataloader, models, transformations
from spatialdata._core.concatenate import concatenate
from spatialdata._core.operations.rasterize import rasterize
from spatialdata._core.operations.transform import transform
from spatialdata._core.query.spatial_query import bounding_box_query
from spatialdata._core.spatialdata import SpatialData
from spatialdata._io.io_zarr import read_zarr
from spatialdata._utils import (
    iterate_pyramid_levels,
    multiscale_spatial_image_from_data_tree,
    unpad_raster,
)

from .models._utils import get_axis_names