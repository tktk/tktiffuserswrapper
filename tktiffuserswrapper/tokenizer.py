def promptIsTooLong(
    _tokenizer,
    _PROMPT,
):
    TOKEN_IDS = _tokenizer.encode(
        _PROMPT,
        add_special_tokens = True,
    )
    TOKEN_IDS_LENGTH = len( TOKEN_IDS )
    MODEL_MAX_LENGTH = _tokenizer.model_max_length

    if TOKEN_IDS_LENGTH > MODEL_MAX_LENGTH:
        TOKENS = _tokenizer.tokenize( _PROMPT )
        TOKENS_LENGTH = len( TOKENS )
        MODEL_MAX_LENGTH_EFFECTIVE = MODEL_MAX_LENGTH - ( TOKEN_IDS_LENGTH - TOKENS_LENGTH )

        return TOKENS_LENGTH, MODEL_MAX_LENGTH_EFFECTIVE, TOKENS[ MODEL_MAX_LENGTH_EFFECTIVE : ]

    return None, None, None
