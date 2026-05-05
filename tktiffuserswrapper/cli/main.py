from tktiffuserswrapper import config
import importlib
import sys

def main(
):
    if len( sys.argv ) < 2:
        print( "使い方: 設定モジュールパス" )
        return -1

    SETUP_MODULE_PATH = sys.argv[ 1 ]

    SETUP_MODULE = importlib.import_module( SETUP_MODULE_PATH )

    while True:
        input( "ENTERで生成を開始します" )

        config.reset()

        importlib.reload( SETUP_MODULE )

        #TODO

    return 0
