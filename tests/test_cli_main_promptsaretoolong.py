from unittest.mock import MagicMock
from unittest.mock import patch
import unittest

from tktiffuserswrapper.cli.main import _promptsAreTooLong

callCount = 0

class TestCliMainPromptsAreTooLong( unittest.TestCase ):
    def _test(
        _self,
        _RETURNS_PROMPT_IS_TOO_LONG_LIST,
        _EXPECTED,
    ):
        global callCount

        callCount = 0

        with patch( "tktiffuserswrapper.cli.main.promptIsTooLong" ) as mockPromptIsTooLong:
            def _promptIsTooLongDummy(
                _tokenizer,
                _PROMPT,
            ):
                global callCount

                RESULT = _RETURNS_PROMPT_IS_TOO_LONG_LIST[ callCount ]

                callCount += 1

                return RESULT, 10, 20

            mockPromptIsTooLong.side_effect = _promptIsTooLongDummy

            _self.assertEqual(
                _EXPECTED,
                _promptsAreTooLong(
                    {
                        "prompt": (
                            "tokeniler1",
                            "prompt1",
                        ),
                        "prompt_2": (
                            "tokeniler2",
                            "prompt2",
                        ),
                        "negative_prompt": (
                            "tokeniler1",
                            "negativePrompt1",
                        ),
                        "negative_prompt_2": (
                            "tokeniler2",
                            "negativePrompt2",
                        ),
                    }
                ),
            )

    def test( _self ):
        _self._test(
            [
                None,
                None,
                None,
                None,
            ],
            False,
        )

    def testTooLong( _self ):
        _self._test(
            [
                None,
                None,
                30,
                None,
            ],
            True,
        )

if __name__ == '__main__':
    unittest.main()
