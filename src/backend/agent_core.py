# Agent OS — core orchestration (real logic)
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.openrouter.ai/v1", api_key="free-default")

def agent_turn(role, message):
    r = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[{"role":"system","content":"Agent OS specialist profile: "+role}, {"role":"user","content":message}],
        stream=False
    )
    return {"agent": role, "reply": r.choices[0].message.content, "usage": r.usage.total_tokens if r.usage else None}
