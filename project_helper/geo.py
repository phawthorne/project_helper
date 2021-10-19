from osgeo import gdal


def transfer_color_table(src_raster, dst_raster, src_band_num=1, dst_band_num=1):
    """
    Copy a color table from `src_raster` to `dst_raster`
    """
    src_ds = gdal.OpenEx(src_raster)
    src_band = src_ds.GetRasterBand(src_band_num)
    cinterp = src_band.GetRasterColorInterpretation()
    ctable = src_band.GetRasterColorTable().Clone()
    
    ds = gdal.OpenEx(dst_raster, 1)
    band = ds.GetRasterBand(dst_band_num)
    band.SetRasterColorInterpretation(cinterp)
    band.SetRasterColorTable(ctable)
    
    src_band = None
    src_ds = None

    band = None
    ds = None
