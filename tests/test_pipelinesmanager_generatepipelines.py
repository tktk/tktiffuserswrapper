import unittest

from tktiffuserswrapper.pipelinesmanager import PipelinesManager

_PIPELINE_FOR_T2I = 10
_PIPELINE_FOR_I2I = 20
_PIPELINE_FOR_INPAINT = 30

class TestPipelinesManagerGeneratePipelines( unittest.TestCase ):
    def test( _self ):
        pipelinesManager = PipelinesManager()

        pipelinesManager.generatePipelines( _generatePipelines )

        _self.assertEqual( _generatePipelines, pipelinesManager._beforeGeneratePipelines )
        _self.assertEqual( _PIPELINE_FOR_T2I, pipelinesManager._pipelineForT2I )
        _self.assertEqual( _PIPELINE_FOR_I2I, pipelinesManager._pipelineForI2I )
        _self.assertEqual( _PIPELINE_FOR_INPAINT, pipelinesManager._pipelineForInpaint )

    # TODO testAlreadyGenerated
    # TODO testChangedGeneratePipelines

def _generatePipelines(
):
    return _PIPELINE_FOR_T2I, _PIPELINE_FOR_I2I, _PIPELINE_FOR_INPAINT

if __name__ == '__main__':
    unittest.main()
