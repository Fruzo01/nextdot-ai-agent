# 🧠 THINKING.md

## Model Choice

I chose Groq’s LLaMA 3.3 70B model because it provides strong reasoning capabilities with very fast response times on the free tier. Since the task required structured output, sentiment understanding, and explanation generation, I needed a model that could handle multiple steps reliably in a single prompt without additional chaining.

## Prompting Strategy

I designed the prompt as a clear pipeline: classification → extraction → reply → reasoning. Instead of leaving it open-ended, I enforced a strict JSON schema and added explicit rules such as avoiding "None" values, not hallucinating customer names, and ensuring all outputs are structured.

To satisfy the “think out loud” requirement, I broke reasoning into three parts: classification_reason, sentiment_reason, and tone_choice_reason. This makes the model’s decision process transparent and easier to debug.

I also included tone guidelines (e.g., apologetic for complaints, warm for feedback) so the generated replies align with the detected sentiment instead of being generic.

## Challenges Faced

One major issue was inconsistent JSON output from the model. Sometimes extra text or formatting broke parsing. I fixed this by adding a regex-based fallback to extract JSON and a retry mechanism for robustness.

Another issue was handling missing or invalid values like "None" or "N/A". I added a cleaning function to convert these into proper null values.

While running the code, I also encountered a file system error when saving outputs because the directory did not exist. I resolved this by dynamically creating the output folder using os.makedirs().

## Improvements with More Time

With more time, I would:
- Add schema validation (e.g., Pydantic) to enforce stricter JSON correctness
- Build a simple Streamlit UI for better interaction
- Improve issue_type classification with more fine-grained categories
- Add logging and monitoring for production readiness

## Final Thoughts

My goal was to build a robust and explainable pipeline rather than just a working demo. I focused on making the system reliable, structured, and easy to understand, similar to how real-world AI systems are designed.
