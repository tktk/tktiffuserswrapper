from unittest.mock import MagicMock
from unittest.mock import patch
import unittest

from tktiffuserswrapper.cli.main import _generateOutputPath

class TestCliMainGenerateOutputPath( unittest.TestCase ):
    def test( _self ):
        with patch( "tktiffuserswrapper.cli.main.datetime" ) as mockDatatime:
            mockStrftime = MagicMock()

            mockStrftime.strftime.return_value = "TIMESTAMP"

            mockDatatime.now.return_value = mockStrftime

            OUTPUT_PATH = _generateOutputPath(
                "PREFIX",
                "PIPELINE_TYPE",
            )

            _self.assertEqual( "PREFIX_PIPELINE_TYPE_TIMESTAMP.png", OUTPUT_PATH )

if __name__ == '__main__':
    unittest.main()
