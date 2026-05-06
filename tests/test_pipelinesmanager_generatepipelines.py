import unittest

from tktiffuserswrapper.pipelinesmanager import PipelinesManager

_PIPELINE_FOR_TEXT2IMAGE = 10
_PIPELINE_FOR_IMAGE2IMAGE = 20
_PIPELINE_FOR_INPAINT = 30

_BEFORE_PIPELINE_FOR_TEXT2IMAGE = 40
_BEFORE_PIPELINE_FOR_IMAGE2IMAGE = 50
_BEFORE_PIPELINE_FOR_INPAINT = 60

def _generatePipelinesDummy(
):
    return _PIPELINE_FOR_TEXT2IMAGE, _PIPELINE_FOR_IMAGE2IMAGE, _PIPELINE_FOR_INPAINT

class TestPipelinesManagerGeneratePipelines( unittest.TestCase ):
    def test( _self ):
        pipelinesManager = PipelinesManager()

        pipelinesManager.generatePipelines( _generatePipelinesDummy )

        _self.assertEqual( _generatePipelinesDummy, pipelinesManager._beforeGeneratePipelines )
        _self.assertEqual( _PIPELINE_FOR_TEXT2IMAGE, pipelinesManager._pipelineForText2Image )
        _self.assertEqual( _PIPELINE_FOR_IMAGE2IMAGE, pipelinesManager._pipelineForImage2Image )
        _self.assertEqual( _PIPELINE_FOR_INPAINT, pipelinesManager._pipelineForInpaint )

    def test_alreadyGenerated( _self ):
        pipelinesManager = PipelinesManager()

        pipelinesManager._beforeGeneratePipelines = _generatePipelinesDummy
        pipelinesManager._pipelineForText2Image = _BEFORE_PIPELINE_FOR_TEXT2IMAGE
        pipelinesManager._pipelineForImage2Image = _BEFORE_PIPELINE_FOR_IMAGE2IMAGE
        pipelinesManager._pipelineForInpaint = _BEFORE_PIPELINE_FOR_INPAINT

        pipelinesManager.generatePipelines( _generatePipelinesDummy )

        _self.assertEqual( _BEFORE_PIPELINE_FOR_TEXT2IMAGE, pipelinesManager._pipelineForText2Image )
        _self.assertEqual( _BEFORE_PIPELINE_FOR_IMAGE2IMAGE, pipelinesManager._pipelineForImage2Image )
        _self.assertEqual( _BEFORE_PIPELINE_FOR_INPAINT, pipelinesManager._pipelineForInpaint )

    def test_changedGeneratePipelines( _self ):
        pipelinesManager = PipelinesManager()

        pipelinesManager._beforeGeneratePipelines = lambda _: 70

        pipelinesManager.generatePipelines( _generatePipelinesDummy )

        _self.assertEqual( _generatePipelinesDummy, pipelinesManager._beforeGeneratePipelines )
        _self.assertEqual( _PIPELINE_FOR_TEXT2IMAGE, pipelinesManager._pipelineForText2Image )
        _self.assertEqual( _PIPELINE_FOR_IMAGE2IMAGE, pipelinesManager._pipelineForImage2Image )
        _self.assertEqual( _PIPELINE_FOR_INPAINT, pipelinesManager._pipelineForInpaint )

if __name__ == '__main__':
    unittest.main()
