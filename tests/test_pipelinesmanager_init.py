import unittest

from tktiffuserswrapper.pipelinesmanager import PipelinesManager

class TestPipelinesManagerInit( unittest.TestCase ):
    def test_pipelinesmanager_init( _self ):
        PIPELINES_MANAGER = PipelinesManager()

        _self.assertIsNone( PIPELINES_MANAGER._beforeGeneratePipelines )

if __name__ == '__main__':
    unittest.main()
