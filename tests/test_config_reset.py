import unittest

from tktiffuserswrapper import config
import inspect

class TestConfigReset( unittest.TestCase ):
    def test_config_reset( _self ):
        config.reset()

        _self.assertIsNone( config.GENERATE_PIPELINES )
        _self.assertEqual( 1, config.GENERATION_COUNT )
        _self.assertIsNone( config.GENERATE_PIPELINE_ARGS )
        _self.assertDictEqual( {}, config.PNG_INFO_EXTRAS )
        _self.assertEqual( "output", config.OUTPUT_PATH_PREFIX )

        _self.assertTrue( callable( config.POST_PROCESS ) )
        SIGNATURE = inspect.signature( config.POST_PROCESS )
        _self.assertEqual( 1, len( SIGNATURE.parameters ) )

if __name__ == '__main__':
    unittest.main()
