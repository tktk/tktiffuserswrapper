class PipelinesManager:
    def __init__( _self ):
        _self._beforeGeneratePipelines = None
        _self._pipelineForT2I = None
        _self._pipelineForI2I = None
        _self._pipelineForInpaint = None

    def generatePipelines(
        _self,
        _GENERATE_PIPELINES,
    ):
        _self._pipelineForT2I, _self._pipelineForI2I, _self._pipelineForInpaint = _GENERATE_PIPELINES()

        _self._beforeGeneratePipelines = _GENERATE_PIPELINES
