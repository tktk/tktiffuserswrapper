import unittest

from tktiffuserswrapper.pipelinesmanager import PipelinesManager

_PIPELINE_FOR_TEXT2IMAGE = 10
_PIPELINE_FOR_IMAGE2IMAGE = 20
_PIPELINE_FOR_INPAINT = 30

class TestPipelinesManagerGetSuitablePipeline( unittest.TestCase ):
    def _test(
        _self,
        _PIPELINE_ARGS,
        _EXPECTED_PIPELINE,
        _EXPECTED_PIPELINE_PREFIX,
    ):
        pipelinesManager = PipelinesManager()

        pipelinesManager._pipelineForText2Image = _PIPELINE_FOR_TEXT2IMAGE
        pipelinesManager._pipelineForImage2Image = _PIPELINE_FOR_IMAGE2IMAGE
        pipelinesManager._pipelineForInpaint = _PIPELINE_FOR_INPAINT

        PIPELINE, PIPELINE_PREFIX = pipelinesManager.getSuitablePipeline( _PIPELINE_ARGS )
        _self.assertEqual( _EXPECTED_PIPELINE, PIPELINE )
        _self.assertEqual( _EXPECTED_PIPELINE_PREFIX, PIPELINE_PREFIX )

    def testText2Image( _self ):
        _self._test(
            {
                "mask_image": 40,
            },
            _PIPELINE_FOR_TEXT2IMAGE,
            "t2i",
        )

    # TODO testImage2Image
    # TODO testInpaint

if __name__ == '__main__':
    unittest.main()
