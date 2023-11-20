from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    """以下の料理のレシピを考えてください。
                                      
料理名: {dish}"""
)

result = prompt.format(dish="カレー")
print(result)
