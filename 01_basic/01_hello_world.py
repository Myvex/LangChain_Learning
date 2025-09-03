# 01_hello_world.py
# 说明：LangChain OpenAI 的最小 Hello World 示例
# 运行方式：python 01_basic/01_hello_world.py

from langchain.llms import OpenAI

# 如果你已经在环境变量里配置了 OPENAI_API_KEY，可以直接省略
llm = OpenAI(openai_api_key="YOUR_OPENAI_API_KEY")

response = llm.predict(
    "What would be a good company name for a company that makes colorful socks?"
)

print("AI 给出的公司名建议：")
print(response)
