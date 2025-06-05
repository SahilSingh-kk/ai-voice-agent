from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load LLM (phi-2) — CPU-safe config
model_name = "microsoft/phi-2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Evaluate mode for inference
model.eval()

# Load pipeline
llm_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Build dynamic sales-focused prompt
def build_sales_prompt(user_input):
    return f"""
You are Ava, an AI assistant for Agyle Studio — a creative digital agency.

Agyle Studio provides:
- Brand design & strategy
- Video production & animation
- Web design & development
- Digital marketing & analytics

We've worked with clients like:
- Electronics Bazaar (eCommerce platform + performance marketing)
- Grow Gully (motion-first branding with animation)
- TeamedUp (web & mobile platform design)
- Slo Mo Club (content marketing for slow fashion)

Instructions:
1. Understand what the user is asking.
2. Explain how Agyle Studio can help with services relevant to their query.
3. Refer to real examples where helpful (but naturally, not forcefully).
4. Be friendly, professional, and human — not robotic.
5. End your message by offering to schedule a meeting or continue the conversation.

User said:
\"{user_input}\"

Now speak as if you're on a live call.
"""

# Generate a response
def ask_llm(user_input):
    prompt = build_sales_prompt(user_input)
    try:
        result = llm_pipeline(prompt, max_new_tokens=200, temperature=0.7)
        print("🧠 LLM raw output:", result)

        full_text = result[0]["generated_text"]

        # Basic extraction logic
        if f'"{user_input}"' in full_text:
            reply = full_text.split(f'"{user_input}"')[-1].strip()
        else:
            reply = full_text.strip()

        return reply

    except Exception as e:
        print("🔥 LLM error:", e)
        return "Sorry, there was an issue generating the response. Please try again."
