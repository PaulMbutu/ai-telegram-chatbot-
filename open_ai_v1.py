import openai
"""
openai.api_key = ""                                                                                   # Replace with your OpenAI API key

prompt = input("Ask me anything")
model = "text-davinci-002"
response = openai.Completion.create(
  engine=model,
  prompt=prompt,
  max_tokens=50
)
generated_text = response.choices[0].text
print(generated_text)
"""

# If theres an error check on yourchat gpt subscription. The first month is free to use the api



def chat():

            openai.api_key = ""                                                                                                   # supply your API key however you choose

            message = {"role":"user", "content": input("This is the beginning of your chat with AI. [To exit, send \"###\".]\n\nYou:")};

            conversation = [{"role": "system", "content": "DIRECTIVE_FOR_gpt-3.5-turbo"}]                                          #add system message sets response tone

            while(message["content"]!="###"):
                conversation.append(message)
                completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation)
                response={completion.choices[0].message.content}
                message["content"] = input(f"\nBig Morio: {completion.choices[0].message.content} \nYou:")
                
                print(response)
                
                conversation.append(completion.choices[0].message)
#chat()
def reply_once():

                openai.api_key = "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" # supply your API key however you choose

                #message = {"role":"user", "content": input("This is the beginning of your chat with AI. [To exit, send \"###\".]\n\nYou:")};
                message= {"role":"user", "content":"what is gold"}
                conversation = [{"role": "system", "content": "DIRECTIVE_FOR_gpt-3.5-turbo"}]#add system message sets response tone
                conversation.append(message)
                completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation)
                response={completion.choices[0].message.content}
                
                print(response)
                
                conversation.append(completion.choices[0].message)
reply_once()

