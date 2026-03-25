# src/main.py

import os
import json
from agent import CustomerAgent
from utils import pretty_print

# Sample Inputs (Required)
inputs = {
    "A": """i ordered the premium plan 3 weeks ago and STILL havent received any confirmation email or access. this is absolutely ridiculous. i paid Rs 4999 and nobody has responded to my 4 emails. if this isnt fixed today im disputing the charge with my bank. my name is Rohan Mehta and my order id is ORD-8821.""",

    "B": """hi I saw your AI tool on linkedin and I am curious how it works for small businesses? like do you guys offer any free trial or something? also can it work with whatsapp? just exploring options for now nothing urgent.""",

    "C": """Just wanted to say the onboarding session last Tuesday was really well done. Priya from your team was super helpful and patient. The tool is working great so far. Looking forward to the advanced features you mentioned. Keep it up!"""
}


def run_pipeline():
    # 🔥 Ensure outputs directory exists (IMPORTANT FIX)
    os.makedirs("outputs", exist_ok=True)

    agent = CustomerAgent()
    results = {}

    for key, text in inputs.items():
        try:
            print(f"\n🔄 Processing input {key}...")

            result = agent.process(text)
            results[key] = result

            file_path = f"outputs/output_{key}.json"

            with open(file_path, "w") as f:
                json.dump(result, f, indent=2)

            print(f"✅ Saved: {file_path}")

        except Exception as e:
            print(f"❌ Error in {key}: {e}")

    return results


def interactive_mode(agent):
    print("\n💬 Interactive Mode (type 'exit' to quit)")

    while True:
        user_input = input("\nEnter message: ")

        if user_input.lower() == "exit":
            print("👋 Exiting interactive mode.")
            break

        try:
            result = agent.process(user_input)
            pretty_print(result)
        except Exception as e:
            print("❌ Error:", e)


if __name__ == "__main__":
    print("🚀 Running pipeline on sample inputs...")

    results = run_pipeline()

    print("\n🎯 Starting interactive mode...")
    agent = CustomerAgent()
    interactive_mode(agent)