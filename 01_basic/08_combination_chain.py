# 08_combination_chain.py
# 说明：RunnableMap 多步链示例，演示如何在 LangChain 中串联多条子链
# 运行方式：python 01_basic/08_combination_chain.py

from langchain.schema.runnable import RunnableMap
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

# 1️⃣ 初始化 LLM（请填入你的 OpenAI API Key）
model = ChatOpenAI(openai_api_key="YOUR_OPENAI_API_KEY")

prompt1 =
    ChatPromptTemplate.from_template("generate a random color")

prompt2 = 
    ChatPromptTemplate.from_template("What is a fruit of color {color}")

prompt3 = 
    ChatPromptTemplate.from_template("What is country's flag that has the color : {color}")

prompt4 = 
    ChatPromptTemplate.from_template("What is color of {fruit} and {country}")

# 2️⃣ 子链：生成随机颜色
chain1 = prompt1 | model | StrOutputParser()

chain2 = RunnableMap(steps=({"color":chain1}) | 
    {"fruit":prompt2 | model | StrOutputParser(),
    "country":promp3 | model | StrOutputParser(),
    } | prompt4 )

chain2.invoke({})

# 完整执行流程
# invoke：chain2.invoke({})
# 传入空字典 {}（此例中不需要任何外部输入）。
# 执行顺序：
# Step 1：chain1 → 产生 color。
# Step 2：并行执行 fruit 与 country 两个子链，使用同一个 color。
# Step 3：把 fruit 与 country 作为输入，执行 prompt4，得到最终字符串。
# 返回：chain2.invoke 最终返回 prompt4 的输出字符串。

