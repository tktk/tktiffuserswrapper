class PipelinesManager:
    def __init__( _self ):
        _self._beforeGeneratePipelines = 10 # TODO
        _self._pipelineForT2I = None
        _self._pipelineForI2I = None
        _self._pipelineForInpaint = None
