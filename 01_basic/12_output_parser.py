# 12_output_parser.py
# 说明：演示 LangChain 的 CommaSeparatedListOutputParser，生成并解析逗号分隔的列表
# 运行方式：python 01_basic/12_output_parser.py

from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

output_parser=CommaSeparatedListOutputParser() #按逗号分隔的列表形式返回

format_instructions=output_parser.get_format_instructions()

prompt=PromptTemplate(
    template="List five {subject} .\n {format_instructions}",
    input_variables=["subject"],
    partial_variables={"format_instructions":format_instructions}
)

chain = LLMChain(
    llm=OpenAI(openai_api_key="YOUR_OPENAI_API_KEY"),
    prompt=prompt
)

output = chain("ice cream flavors")