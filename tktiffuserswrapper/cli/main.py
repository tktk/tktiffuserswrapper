from tktiffuserswrapper.pipelinesmanager import PipelinesManager
from tktiffuserswrapper.pnginfo import generatePngInfo
from tktiffuserswrapper.tokenizer import promptIsTooLong
from datetime import datetime
import tktiffuserswrapper as tw
import importlib
import sys

def _promptsAreTooLong(
    _TOKENIZER_AND_PROMPT_MAP,
    _PIPELINE_ARGS,
):
    #TODO
    return False
    tooLong = False

    for PROMPT_KEY, tokenizerAndPrompt in _TOKENIZER_AND_PROMPT_MAP.items():
        tokenizer, PROMPT = tokenizerAndPrompt

        TOO_LONG_TOKENS, MODEL_MAX_LENGTH, OVERFLOW_TOKENS = promptIsTooLong(
            tokenizer,
            PROMPT,
        )

        if TOO_LONG_TOKENS is not None:
            tooLong = True

            print( f"{PROMPT_KEY}が長すぎます（{TOO_LONG_TOKENS}/{MODEL_MAX_LENGTH}トークン。{OVERFLOW_TOKENS}が溢れています）。" )

    return tooLong

def _generateOutputPath(
    _PREFIX,
    _PIPELINE_TYPE,
):
    #TODO
    return ""
    NOW = datetime.now()

    TIMESTAMP = NOW.strftime( "%Y%m%d%H%M%S_%f" )

    return f"{_PREFIX}_{_PIPELINE_TYPE}_{TIMESTAMP}.png"

def main(
):
    if len( sys.argv ) < 2:
        print( "使い方: 設定モジュールパス" )
        return -1

    SETUP_MODULE_PATH = sys.argv[ 1 ]

    SETUP_MODULE = importlib.import_module( SETUP_MODULE_PATH )

    pipelinesManager = PipelinesManager()

    while True:
        input( "ENTERで生成を開始します" )

        tw.reset()

        importlib.reload( SETUP_MODULE )

        pipelinesManager.generatePipelines( tw.GENERATE_PIPELINES )

        for _ in range( tw.GENERATION_COUNT ):
            PIPELINE_ARGS = tw.GENERATE_PIPELINE_ARGS()

            pipeline, PIPELINE_TYPE = pipelinesManager.getSuitablePipeline( PIPELINE_ARGS )
            if "t2i" in PIPELINE_TYPE:
                print( "text2image用パイプラインを使用します" )
            elif "i2i" in PIPELINE_TYPE:
                print( "image2image用パイプラインを使用します" )
            else:
                print( "inpaint用パイプラインを使用します" )

            if _promptsAreTooLong(
                tw.GET_TOKENIZER_AND_PROMPT_MAP_FOR_CHECK( pipeline ),
                PIPELINE_ARGS,
            ) == True:
                continue

            PNG_INFO = generatePngInfo(
                PIPELINE_ARGS,
                tw.PNG_INFO_EXTRAS,
            )

            OUTPUT_PATH = _generateOutputPath(
                tw.OUTPUT_PATH_PREFIX,
                PIPELINE_TYPE,
            )

            IMAGES = pipeline( **PIPELINE_ARGS ).images

            IMAGES[ 0 ].save(
                OUTPUT_PATH,
                pnginfo = PNG_INFO,
            )

            print( f"{OUTPUT_PATH}を生成しました" )

            tw.POST_PROCESS( OUTPUT_PATH )

    return 0
