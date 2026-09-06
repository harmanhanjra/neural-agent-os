from openai import OpenAI
client = OpenAI(base_url="https://api.openrouter.ai/v1", api_key="free-default")

def agent_turn(role, msg):
    try:
        r = client.chat.completions.create(model="deepseek-v4-flash", messages=[{"role":"system","content":"Agent: "+role},{"role":"user","content":msg}], stream=False)
        return {"agent":role,"reply":r.choices[0].message.content,"usage":r.usage.total_tokens if r.usage else None}
    except Exception as e:
        return {"agent":role,"reply":"[offline] "+msg,"error":str(e)}

def run(q="hello"):
    return agent_turn("agent", q)
