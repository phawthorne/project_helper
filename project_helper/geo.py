from osgeo import gdal


def transfer_color_table(src_raster, dst_raster, src_band_num=1, dst_band_num=1):
    """
    Copy a color table from `src_raster` to `dst_raster`
    
    Parameters:
    -----------
    src_raster : str or Path
        Path to the source raster file
    dst_raster : str or Path
        Path to the destination raster file
    src_band_num : int, default=1
        Band number to read from the source raster
    dst_band_num : int, default=1
        Band number to write to in the destination raster
        
    Raises:
    -------
    RuntimeError
        If there's an issue opening the raster files or accessing the bands
    """
    try:
        src_ds = gdal.OpenEx(str(src_raster))
        if src_ds is None:
            raise RuntimeError(f"Could not open source raster: {src_raster}")
            
        src_band = src_ds.GetRasterBand(src_band_num)
        if src_band is None:
            raise RuntimeError(f"Could not get band {src_band_num} from source raster")
            
        cinterp = src_band.GetRasterColorInterpretation()
        ctable = src_band.GetRasterColorTable()
        
        if ctable is None:
            raise RuntimeError(f"Source raster band has no color table")
            
        ctable = ctable.Clone()
        
        ds = gdal.OpenEx(str(dst_raster), 1)  # 1 = update mode
        if ds is None:
            raise RuntimeError(f"Could not open destination raster for writing: {dst_raster}")
            
        band = ds.GetRasterBand(dst_band_num)
        if band is None:
            raise RuntimeError(f"Could not get band {dst_band_num} from destination raster")
            
        band.SetRasterColorInterpretation(cinterp)
        band.SetRasterColorTable(ctable)
    finally:
        # Clean up resources
        src_band = None
        src_ds = None
        band = None
        ds = None
