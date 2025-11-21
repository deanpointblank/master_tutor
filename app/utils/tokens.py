from typing import Optional

import tiktoken


def count_tokens(text: str, model: str = "gpt-4o") -> int:
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")

    return len(encoding.encode(text))


def estimate_cost(
    input_tokens: int,
    output_tokens: int,
    model: str = "gpt-4o",
) -> float:
    pricing: dict[str, tuple[float, float]] = {
        "gpt-4o": (0.0025, 0.01),
        "gpt-4o-mini": (0.00015, 0.0006),
        "claude-sonnet-4-20250514": (0.003, 0.015),
        "claude-opus-4-20250514": (0.015, 0.075),
        "gemini-2.0-flash-exp": (0.0, 0.0),
    }

    input_price, output_price = pricing.get(model, (0.0, 0.0))
    input_cost = (input_tokens / 1000) * input_price
    output_cost = (output_tokens / 1000) * output_price

    return input_cost + output_cost
