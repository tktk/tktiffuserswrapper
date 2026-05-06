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

    def getSuitablePipeline(
        _self,
        _PIPELINE_ARGS,
    ):
        _PIPELINE_ARGS_KEY_IMAGE = "image"
        _PIPELINE_ARGS_KEY_MASK_IMAGE = "mask_image"

        _PIPELINE_PREFIX_TEXT2IMAGE = "t2i"
        _PIPELINE_PREFIX_IMAGE2IMAGE = "i2i"
        _PIPELINE_PREFIX_INPAINT = "inpaint"

        if _PIPELINE_ARGS_KEY_IMAGE in _PIPELINE_ARGS:
            if _PIPELINE_ARGS_KEY_MASK_IMAGE in _PIPELINE_ARGS:
                return _self._pipelineForInpaint, _PIPELINE_PREFIX_INPAINT
            else:
                return _self._pipelineForImage2Image, _PIPELINE_PREFIX_IMAGE2IMAGE

        return _self._pipelineForText2Image, _PIPELINE_PREFIX_TEXT2IMAGE
