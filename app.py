# Note: The openai-python library support for Azure OpenAI is in preview.
import os
from openai import AzureOpenAI
from flask import Flask, request, render_template

deployment_name = "testdeployment"
openapi_version = "2023-07-01-preview"
openapi_url = "https://oai-projects.openai.azure.com/"

client = AzureOpenAI(
    azure_endpoint=openapi_url,
    api_version=openapi_version,
    api_key=os.getenv("OPENAI_API_KEY")
)
list_of_input = ["title", "name", "tone", "creature", "environment"]

def create_completion(client, model, messages, temperature=0.7, max_tokens=800, top_p=0.95, frequency_penalty=0, presence_penalty=0, stop=None):
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop
        )
        return completion
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def app():
    if request.method == 'POST':
        prompts = [request.form[field] for field in list_of_input]
        prompts.append("; Based on the prompts here; the order of the prompt is, title,name,tone,creature,environment, can you create a story ?")
        messages = [{"role": "system", "content": prompt} for prompt in prompts]
        completion = create_completion(client, deployment_name, messages)
        if completion:
            content = completion.choices[0].message.content
            paragraphs = content.split('\n')
            #return render_template('index.html', sentiment=completion)
            return render_template('index.html', sentiment=paragraphs)
        else:
            return render_template('index.html', sentiment='An error occurred.')
    else:
        return render_template('index.html')

# Change port number, default port 5000 gives 403 error on MacOS Sonoma (Current Version: 14.2.1)
if __name__ == '__main__':
    application.run(port=8000, debug=True)
