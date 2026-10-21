"""Hosted Gemma client supporting multiple providers:
- Groq (default, ultra-fast inference for gemma2-9b-it)
- Google GenAI (gemma-2-9b-it, gemma-2-27b-it)
- OpenRouter / generic OpenAI-compatible API
"""

import os
from typing import List, Dict, Optional
from dotenv import load_dotenv

# Load local environment if present
load_dotenv()

SYSTEM_TEACHER_PROMPT = """You are Fluently (SpeakEasy AI), a friendly, patient, and encouraging personal English teacher.
Your mission is to help learners build confidence and fluency in English.

Key teaching rules:
1. Explain grammar and vocabulary concepts simply and conversationally.
2. Provide relatable, real-life example sentences for every concept.
3. Gently correct grammar or phrasing mistakes if noticed, showing both the correction and why it sounds more natural.
4. Keep explanations concise, bite-sized, and easy to read.
5. End responses with a quick follow-up question or practice prompt when appropriate to encourage active conversation.
6. Acknowledge that you are an AI assistant and remind learners to verify nuanced idiomatic expressions or exam-specific rules.
"""

def get_config():
    return {
        "provider": os.getenv("GEMMA_PROVIDER", "groq").lower(),
        "api_key": os.getenv("GEMMA_API_KEY", ""),
        "model": os.getenv("GEMMA_MODEL", "gemma2-9b-it"),
    }

def query_gemma(messages: List[Dict[str, str]], provider: Optional[str] = None, model: Optional[str] = None) -> str:
    """Send a list of message dicts [{'role': 'user'|'assistant', 'content': '...'}] to the hosted Gemma API."""
    cfg = get_config()
    provider = provider or cfg["provider"]
    api_key = cfg["api_key"]
    model = model or cfg["model"]

    if not api_key:
        raise ValueError(
            "GEMMA_API_KEY is not configured. Please set GEMMA_API_KEY in your .env file or environment variables."
        )

    if provider == "groq":
        from groq import Groq
        client = Groq(api_key=api_key)
        
        full_messages = [{"role": "system", "content": SYSTEM_TEACHER_PROMPT}] + messages
        response = client.chat.completions.create(
            model=model,
            messages=full_messages,
            temperature=0.7,
            max_tokens=1024,
        )
        return response.choices[0].message.content

    elif provider in ("google", "gemini"):
        from google import genai
        client = genai.Client(api_key=api_key)
        
        # Build contents from messages
        prompt_parts = [SYSTEM_TEACHER_PROMPT + "\n\n"]
        for m in messages:
            role = "Learner" if m["role"] == "user" else "Teacher"
            prompt_parts.append(f"{role}: {m['content']}")
        prompt_parts.append("Teacher: ")
        
        response = client.models.generate_content(
            model=model if "gemma" in model else "gemma-2-9b-it",
            contents="\n".join(prompt_parts)
        )
        return response.text

    elif provider == "openrouter":
        import requests
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        full_messages = [{"role": "system", "content": SYSTEM_TEACHER_PROMPT}] + messages
        payload = {
            "model": model,
            "messages": full_messages,
            "temperature": 0.7,
        }
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload, timeout=30)
        res.raise_for_status()
        data = res.json()
        return data["choices"][0]["message"]["content"]

    else:
        raise ValueError(f"Unsupported provider: '{provider}'. Supported providers: 'groq', 'google', 'openrouter'.")


if __name__ == "__main__":
    print(f"Current config: provider={get_config()['provider']}, model={get_config()['model']}")
    print("Testing client initialization...")
    try:
        reply = query_gemma([{"role": "user", "content": "Hello!"}])
        print(f"Response: {reply}")
    except ValueError as e:
        print(f"Handled expected config check: {e}")
