import unittest

from tktiffuserswrapper.tokenizer import promptIsTooLong

class TokenizerDummy:
    def __init__(
        _self,
        _test,
        MODEL_MAX_LENGTH = -1,
        RETURNS_ENCODE = None,
        RETURNS_TOKENIZE = None,
        EXPECTED_PROMPT = None,
    ):
        _self._test = _test
        _self.model_max_length = MODEL_MAX_LENGTH

        _self.RETURNS_ENCODE = RETURNS_ENCODE
        _self.RETURNS_TOKENIZE = RETURNS_TOKENIZE
        _self.EXPECTED_PROMPT = EXPECTED_PROMPT

    def encode(
        _self,
        _PROMPT,
        add_special_tokens,
    ):
        _self._test.assertEqual( _self.EXPECTED_PROMPT, _PROMPT )
        _self._test.assertTrue( add_special_tokens )

        return _self.RETURNS_ENCODE

    def tokenize(
        _self,
        _PROMPT,
    ):
        _self._test.assertEqual( _self.EXPECTED_PROMPT, _PROMPT )

        return _self.RETURNS_TOKENIZE

class TestTokenizerPromptIsTooLong( unittest.TestCase ):
    def test( _self ):
        PROMPT = "PROMPT"

        tokenizer = TokenizerDummy(
            _self,
            MODEL_MAX_LENGTH = 5,
            RETURNS_ENCODE = [ 1, 2, 3, 4, 5 ],
            EXPECTED_PROMPT = PROMPT,
        )

        TOO_LONG_TOKENS_COUNT, MODEL_MAX_LENGTH, OVERFLOW_TOKENS = promptIsTooLong(
            tokenizer,
            PROMPT,
        )

        _self.assertIsNone( TOO_LONG_TOKENS_COUNT )
        _self.assertIsNone( MODEL_MAX_LENGTH )
        _self.assertIsNone( OVERFLOW_TOKENS )

    def test_tooLong( _self ):
        PROMPT = "PROMPT"

        tokenizer = TokenizerDummy(
            _self,
            MODEL_MAX_LENGTH = 5,
            RETURNS_ENCODE = [ 1, 2, 3, 4, 5, 6 ],
            RETURNS_TOKENIZE = [ 7, 8, 9 ],
            EXPECTED_PROMPT = PROMPT,
        )

        TOO_LONG_TOKENS_COUNT, MODEL_MAX_LENGTH, OVERFLOW_TOKENS = promptIsTooLong(
            tokenizer,
            PROMPT,
        )

        _self.assertEqual( 3, TOO_LONG_TOKENS_COUNT )
        _self.assertEqual( 2, MODEL_MAX_LENGTH )
        _self.assertEqual( [ 9 ], OVERFLOW_TOKENS )

if __name__ == '__main__':
    unittest.main()
