import memory
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


def get_Chat_respnse(prompt,memory,api_key):
    model = ChatOpenAI(
        api_key=api_key,  # Replace with your DeepSeek API key
        base_url="https://api.deepseek.com/v1",  # DeepSeek endpoint
        model="deepseek-chat",  # or "deepseek-coder"

    )
    chain = ConversationChain(llm=model,memory=memory)


    response=chain.invoke({'input': prompt})

    return response['response']
#memory=ConversationBufferMemory(return_messages=True)
#print(get_Chat_respnse('chatgpt和deepseek有什么区别',memory,'sk-d5ecfe9df3e34c1e9d2452b6e2841850'))
#print(get_Chat_respnse('我刚才问的啥来着',memory,'sk-d5ecfe9df3e34c1e9d2452b6e2841850'))