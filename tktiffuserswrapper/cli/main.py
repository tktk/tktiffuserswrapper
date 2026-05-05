import sys

def main(
):
    if len( sys.argv ) < 2:
        print( "使い方: 設定モジュール" )
        return -1

    SETUP_MODULE = sys.argv[ 1 ]

    while True:
        input( "ENTERで生成を開始します" )

    return 0
