import unittest

import tktiffuserswrapper as tw
import inspect

class TestReset( unittest.TestCase ):
    def test_reset( _self ):
        tw.reset()

        _self.assertIsNone( tw.GENERATE_PIPELINES )
        _self.assertEqual( 1, tw.GENERATION_COUNT )
        _self.assertIsNone( tw.GENERATE_PIPELINE_ARGS )
        _self.assertDictEqual( {}, tw.PNG_INFO_EXTRAS )
        _self.assertEqual( "output", tw.OUTPUT_PATH_PREFIX )

        _self.assertTrue( callable( tw.POST_PROCESS ) )
        SIGNATURE = inspect.signature( tw.POST_PROCESS )
        _self.assertEqual( 1, len( SIGNATURE.parameters ) )

if __name__ == '__main__':
    unittest.main()
