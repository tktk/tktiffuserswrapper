from unittest.mock import patch
import unittest

from tktiffuserswrapper.pnginfo import generatePngInfo

def _dummy_add_text(
    _texts,
    _KEY,
    _VALUE,
):
    _texts[ _KEY ] = _VALUE

class TestPnpInfoGeneratePngInfo( unittest.TestCase ):
    def test( _self ):
        texts = {}

        PIPELINE_ARGS = {
            "arg1": 10,
            "arg2": "20",
        }
        EXTRAS = {
            "extra1": "30",
            "extra2": 40,
        }

        with patch( "tktiffuserswrapper.pnginfo.PngInfo" ) as mockPngInfo:
            instance = mockPngInfo.return_value

            instance.add_text.side_effect = lambda _KEY, _VALUE: _dummy_add_text(
                texts,
                _KEY,
                _VALUE,
            )

            PNG_INFO = generatePngInfo(
                PIPELINE_ARGS,
                EXTRAS,
            )

            EXPECTED_TEXTS = {
                "tktiffuserswrapper.PIPELINE_ARGS.arg1": "10",
                "tktiffuserswrapper.PIPELINE_ARGS.arg2": "20",
                "tktiffuserswrapper.EXTRAS.extra1": "30",
                "tktiffuserswrapper.EXTRAS.extra2": "40",
            }
            _self.assertEqual( EXPECTED_TEXTS, texts )

if __name__ == '__main__':
    unittest.main()
