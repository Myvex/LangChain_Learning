# 14_structure_output_parser.py
# 说明：演示 LangChain 的 StructureOutputParser，返回 JSON 结构化答案
# 运行方式：python 01_basic/14_structure_output_parser.py

from langchain.output_parsers import (
    StructureOutputParser,ResponseSchema
)
from langchain.prompts import(
    PromptTemplate,ChatPromptTemplate,HumanMessagePromptTemplate
)
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

response_schemas= [
    ResponseSchema(
        name="answer",
        description="answer to the user's quesition"
    ),
    ResponseSchema(
        name="source",
        description=(
            "source used to answer the user's question,"
            "should be a website"
        )
    )
]

output_parser = StructureOutputParser.from_response_schemas(response_schemas)

format_instructions = output_parser.get_format_instructions()

prompt = PromptTemplate(
    template=(
        "answer the users question as best as possible.\n"
        "{format_instructions}\n{question}"
    ),
    input_variables=["question"],
    partial_variables={
        "format_instructions":format_instructions
    }
)

model=OpenAI(openai_api_key="")
_input=prompt.format_prompt(quesition="what's the capital of france?")
output = model(_input.to_string())
output_parser.parse(output)

chat_model=ChatOpenAI(openai_api_key="")

prompt=ChatPromptTemplate(
    message=[
        HumanMessagePromptTemplate.from_template(
            "answer the users question as best as possible.\n"
            "{format_instructions}\n{question}"
        )
    ],
    input_variables=["question"],
    partial_variables={
        "format_instuctions":format_instructions
    }
)
_input = prompt.format_prompt(quesition="what's the capital of france?")
output = chat_model(_input.to_messages())
output_parser.parse(output.content)