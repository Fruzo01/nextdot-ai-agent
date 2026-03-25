# src/utils.py

import textwrap


def format_paragraph(text: str, width: int = 70) -> str:
    return textwrap.fill(text, width=width)


def bullet_points(text: str) -> str:
    sentences = text.split(". ")
    return "\n".join([f"• {s.strip()}" for s in sentences if s.strip()])


def pretty_print(result: dict):
    print("\n================ RESPONSE ================")
    print(f"Intent    : {result['intent']}")
    print(f"Sentiment : {result['sentiment']}")

    print("\n--- Extracted Info ---")
    for k, v in result["extracted"].items():
        print(f"{k:<20}: {v}")

    print("\n--- Reply ---")
    print(format_paragraph(result["reply"]))

    print("\n--- Reasoning ---")
    for k, v in result["reasoning"].items():
        print(f"{k}: {format_paragraph(v)}")

    print("==========================================\n")