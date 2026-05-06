import unittest

import tktiffuserswrapper as tw
import inspect

class TestReset( unittest.TestCase ):
    def _assertCallable(
        _self,
        _CALLABLE,
        _EXPECTED_PARAMTERS_COUNT,
    ):
        _self.assertTrue( callable( _CALLABLE ) )
        SIGNATURE = inspect.signature( _CALLABLE )
        _self.assertEqual( _EXPECTED_PARAMTERS_COUNT, len( SIGNATURE.parameters ) )

    def test( _self ):
        tw.GENERATE_PIPELINES = 10
        tw.GENERATION_COUNT = 20
        tw.GENERATE_PIPELINE_ARGS = 30
        tw.MANUAL_SEED = 60
        tw.PNG_INFO_EXTRAS = { "": 70 }
        tw.OUTPUT_PATH_PREFIX = 80
        tw.POST_PROCESS = 90

        tw.reset()

        _self.assertIsNone( tw.GENERATE_PIPELINES )
        _self.assertEqual( 1, tw.GENERATION_COUNT )
        _self.assertIsNone( tw.GENERATE_PIPELINE_ARGS )
        _self._assertCallable(
            tw.GET_TOKENIZER_AND_PROMPT_MAP_FOR_CHECK,
            1,
        )
        _self.assertIsNone( tw.MANUAL_SEED )
        _self.assertEqual( {}, tw.PNG_INFO_EXTRAS )
        _self.assertEqual( "output", tw.OUTPUT_PATH_PREFIX )
        _self._assertCallable(
            tw.POST_PROCESS,
            1,
        )

if __name__ == '__main__':
    unittest.main()
