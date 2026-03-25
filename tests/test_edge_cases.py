# tests/test_edge_cases.py

from src.agent import CustomerAgent

agent = CustomerAgent()

edge_cases = [
    "",
    "ok",
    "????",
    "bhai mera order nahi aya",
    "refund pls",
]

for case in edge_cases:
    try:
        print(f"\nINPUT: {case if case else '[EMPTY]'}")
        result = agent.process(case)
        print(result)
    except Exception as e:
        print("Handled Error:", e)