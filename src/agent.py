# src/agent.py

import os
import json
import re
import time
from typing import Dict, Any
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("GROQ_API_KEY not found. Add it to .env file.")

client = Groq(api_key=API_KEY)


class CustomerAgent:
    def __init__(self, model: str = "llama-3.3-70b-versatile"):
        self.model = model

    def _validate_input(self, text: str) -> str:
        if not text or not text.strip():
            raise ValueError("Input message is empty.")
        return text.strip()

    def _build_prompt(self, message: str) -> str:
        return f"""
You are an AI customer support agent.

Analyze the message and return STRICT JSON.

Message:
\"\"\"{message}\"\"\"

Tasks:
1. Classify intent (complaint / query / feedback / request)
2. Detect sentiment (positive / neutral / negative / urgent)

3. Extract structured fields:
   - customer_name (ONLY if explicitly mentioned, else null)
   - issue_type (choose specific: payment_issue / delayed_delivery / access_issue / product_query / feature_request / general)
   - urgency_level (Low / Medium / High / Critical)
   - recommended_action (clear and actionable)

4. Generate a professional reply matching sentiment:
   - complaint → apologetic, accountable, urgent
   - query → helpful, informative
   - feedback → appreciative, warm

5. THINK OUT LOUD:
   Provide structured reasoning:
   - classification_reason
   - sentiment_reason
   - tone_choice_reason

STRICT OUTPUT RULES:
- Return ONLY valid JSON
- No extra text
- Do NOT return "None", "N/A"
- Use null for missing values
- Do NOT hallucinate names

Output format:
{{
  "intent": "...",
  "sentiment": "...",
  "extracted": {{
    "customer_name": null,
    "issue_type": "...",
    "urgency_level": "...",
    "recommended_action": "..."
  }},
  "reply": "...",
  "reasoning": {{
    "classification_reason": "...",
    "sentiment_reason": "...",
    "tone_choice_reason": "..."
  }}
}}
"""

    def _clean_nulls(self, data: Dict[str, Any]) -> Dict[str, Any]:
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = self._clean_nulls(value)
            elif isinstance(value, str) and value.strip().lower() in ["none", "n/a", "null", ""]:
                data[key] = None
        return data

    def _parse_json_with_retry(self, raw: str, retries=2) -> Dict[str, Any]:
        for _ in range(retries):
            try:
                return json.loads(raw)
            except:
                match = re.search(r"\{.*\}", raw, re.DOTALL)
                if match:
                    try:
                        return json.loads(match.group())
                    except:
                        pass
            time.sleep(0.5)

        raise ValueError(f"Invalid JSON:\n{raw}")

    def process(self, message: str) -> Dict[str, Any]:
        message = self._validate_input(message)
        prompt = self._build_prompt(message)

        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Return ONLY valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        raw = response.choices[0].message.content
        print("\n[DEBUG OUTPUT]\n", raw)

        parsed = self._parse_json_with_retry(raw)
        parsed = self._clean_nulls(parsed)

        return parsed