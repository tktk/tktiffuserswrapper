class PipelinesManager:
    def __init__( _self ):
        _self._beforeGeneratePipelines = None
        _self._pipelineForText2Image = None
        _self._pipelineForImage2Image = None
        _self._pipelineForInpaint = None

    def generatePipelines(
        _self,
        _GENERATE_PIPELINES,
    ):
        if _self._beforeGeneratePipelines is not None and _self._beforeGeneratePipelines.__code__ == _GENERATE_PIPELINES.__code__:
            return

        _self._pipelineForText2Image, _self._pipelineForImage2Image, _self._pipelineForInpaint = _GENERATE_PIPELINES()

        _self._beforeGeneratePipelines = _GENERATE_PIPELINES
