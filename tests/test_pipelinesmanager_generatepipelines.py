import unittest

from tktiffuserswrapper.pipelinesmanager import PipelinesManager

_PIPELINE_FOR_TEXT2IMAGE = 10
_PIPELINE_FOR_IMAGE2IMAGE = 20
_PIPELINE_FOR_INPAINT = 30

class TestPipelinesManagerGeneratePipelines( unittest.TestCase ):
    def test( _self ):
        pipelinesManager = PipelinesManager()

        pipelinesManager.generatePipelines( _generatePipelines )

        _self.assertEqual( _generatePipelines, pipelinesManager._beforeGeneratePipelines )
        _self.assertEqual( _PIPELINE_FOR_TEXT2IMAGE, pipelinesManager._pipelineForText2Image )
        _self.assertEqual( _PIPELINE_FOR_IMAGE2IMAGE, pipelinesManager._pipelineForImage2Image )
        _self.assertEqual( _PIPELINE_FOR_INPAINT, pipelinesManager._pipelineForInpaint )

    # TODO testAlreadyGenerated
    # TODO testChangedGeneratePipelines

def _generatePipelines(
):
    return _PIPELINE_FOR_TEXT2IMAGE, _PIPELINE_FOR_IMAGE2IMAGE, _PIPELINE_FOR_INPAINT

if __name__ == '__main__':
    unittest.main()
