import numpy as np  # type: ignore
import pytest
import os
from geotiff import GeoTiff

@pytest.fixture
def tiff_file():
    filename = "dem.tif"
    dir = dir = "./tests/inputs/"
    return(os.path.join(dir, filename))

@pytest.fixture
def area_box():
    return([(138.632071411, -32.447310785), (138.644218874, -32.456979174)])


@pytest.fixture
def geoTiff(tiff_file):
    return(GeoTiff(tiff_file))

def test_read(tiff_file, area_box, geoTiff: GeoTiff):
    print("testing read tiff")
    print(f"reading: {tiff_file}")
    print(f"Using bBox: {area_box}")
    array = geoTiff.read_box(area_box)
    print("Sample array:")
    print(array)
    print(array.shape)
    assert isinstance(array, np.ndarray)


def test_int_box(area_box, geoTiff: GeoTiff):
    intBox = geoTiff.get_int_box(area_box)
    assert isinstance(intBox, tuple)
    assert len(intBox) == 2
    assert isinstance(intBox[0], tuple)
    assert isinstance(intBox[1], tuple)
    assert ((126, 144), (169, 178)) == intBox


def test_conversions(area_box, geoTiff: GeoTiff):
    b = geoTiff.get_int_box(area_box)
    geoTiff.get_wgs_84_coords(b[0][0], b[0][1])
    geoTiff.get_wgs_84_coords(b[1][0], b[1][1])
    
    
    
    print(area_box)

    bounding_box = geoTiff.get_bBox_wgs_84(area_box)
    assert area_box[0][0] <= bounding_box[0][0]
    assert area_box[0][1] >= bounding_box[0][1]
    assert area_box[1][0] >= bounding_box[1][0]
    assert area_box[1][1] <= bounding_box[1][1]

    # TODO add asserts for comapring the bBox's
    # print(geoTiff.read_box(area_box).shape)
    # print(geoTiff.tif_bBox_wgs_84)