GENERATE_PIPELINES = None
GENERATION_COUNT = None
GENERATE_PIPELINE_ARGS = None
GET_PROMPT_AND_TOKENIZER_LIST_FOR_CHECK = None
MANUAL_SEED = None
PNG_INFO_EXTRAS = None
OUTPUT_PATH_PREFIX = None
POST_PROCESS = None

def _getPromptAndTokenizerListForCheck(
    _,
):
    return []

def _postProcess(
    _,
):
    pass

def reset(
):
    global GENERATE_PIPELINES
    global GENERATION_COUNT
    global GENERATE_PIPELINE_ARGS
    global GET_PROMPT_AND_TOKENIZER_LIST_FOR_CHECK
    global MANUAL_SEED
    global PNG_INFO_EXTRAS
    global OUTPUT_PATH_PREFIX
    global POST_PROCESS

    GENERATE_PIPELINES = None
    GENERATION_COUNT = 1
    GENERATE_PIPELINE_ARGS = None
    GET_PROMPT_AND_TOKENIZER_LIST_FOR_CHECK = _getPromptAndTokenizerListForCheck
    MANUAL_SEED = None
    PNG_INFO_EXTRAS = {}
    OUTPUT_PATH_PREFIX = "output"
    POST_PROCESS = _postProcess
