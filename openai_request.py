import openai
import config
import json


def summarize_text(text_to_summarize):

    openai.api_key = config.openai_api_key
    prompt = "Produce 5 hashtags for the text below and a summary of 5 sentences or less \nDesired format:\n{{\"summary\": \"\",\n\"hashtags\": \"\"}}\n\"\"\"\nText: {}\n\"\"\"".format(text_to_summarize)
    print(prompt)
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= prompt,
    temperature=0.0,
    max_tokens=600,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    print(response)
    json_string = response['choices'][0]['text']
    
    json_response = json.loads(json_string)
    summary = json_response['summary']
    hashtags = json_response['hashtags']
    return summary, hashtags

