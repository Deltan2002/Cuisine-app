from secretKey import token
from langchain import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import os


os.environ["HUGGINGFACEHUB_API_TOKEN"] = token

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"


llm = HuggingFaceHub(
    repo_id=repo_id,
    model_kwargs={"temperature": 0.2, "max_length": 700},
    huggingfacehub_api_token=token
)

def generate_restaurant_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Please suggest a fancy name for the restaurant."


    )

    name_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_name,
        output_key="restaurant_name",
    )

    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest food items for {restaurant_name}. Return it as comma separated values."
    )

    items_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_items,
        output_key="menu_items"
    )
    
    chain = SequentialChain(
    chains = [name_chain, items_chain],
    input_variables = ["cuisine"],
    output_variables=["restaurant_name","menu_items"],
    )
    response = chain({'cuisine':cuisine})
      
    return response               

if __name__ == '__main__':
    print(generate_restaurant_name_and_items("Arabian"))