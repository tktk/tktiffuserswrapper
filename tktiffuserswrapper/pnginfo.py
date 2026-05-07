from PIL.PngImagePlugin import PngInfo

def _addTextToPngInfo(
    _pngInfo,
    _KEY,
    _VALUE,
):
    _pngInfo.add_text(
        f"tktiffuserswrapper.{_KEY}",
        str( _VALUE ),
    )

def generatePngInfo(
    _PIPELINE_ARGS,
    _EXTRAS,
):
    pngInfo = PngInfo()

    for ( KEY, VALUE ) in _PIPELINE_ARGS.items():
        _addTextToPngInfo(
            pngInfo,
            f"PIPELINE_ARGS.{KEY}",
            VALUE,
        )

    for ( KEY, VALUE ) in _EXTRAS.items():
        _addTextToPngInfo(
            pngInfo,
            f"EXTRAS.{KEY}",
            VALUE,
        )

    return pngInfo
