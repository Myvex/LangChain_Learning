# 05_zero_agent.py
# 说明：Zero‑Shot React Agent 示例，使用 SerpAPI 与 LLM‑Math
# 运行方式：python 01_basic/05_zero_agent.py

import os
os.environ["OPENAI_API_KEY"] = ""      # 填写你的 OpenAI API Key
os.environ["SERPAPI_API_KEY"] = ""     # 填写你的 SerpAPI Key

from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(temperature=0)

# 加载工具
tools = load_tools(["serpapi", "llm-math"], llm=chat)

# 初始化 Agent
agent = initialize_agent(
    tools,
    chat,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 运行示例
response = agent.run(
    "What will be the weather in ShangHai in three days from now on?"
)
print(response)
