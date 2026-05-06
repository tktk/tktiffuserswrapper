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
        tw.reset()

        _self.assertIsNone( tw.GENERATE_PIPELINES )
        _self.assertEqual( 1, tw.GENERATION_COUNT )
        _self.assertIsNone( tw.GENERATE_PIPELINE_ARGS )

        _self._assertCallable(
            tw.GET_TOKENIZERS,
            1,
        )
        _self._assertCallable(
            tw.GET_PROMPT_KEYS,
            0,
        )

        _self.assertDictEqual( {}, tw.PNG_INFO_EXTRAS )
        _self.assertEqual( "output", tw.OUTPUT_PATH_PREFIX )

        _self._assertCallable(
            tw.POST_PROCESS,
            1,
        )

if __name__ == '__main__':
    unittest.main()
