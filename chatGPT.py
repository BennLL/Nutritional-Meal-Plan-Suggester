import openai
openai.api_key = "" #Enter your own api key

def act_as(user_prompt):
    system_prompt = 'act as a nutrition specialist and provide a meal plan after details have been given'

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        temperature=0.8,
        max_tokens=2000,  
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )

    assistant_response = completion.choices[0].message.content

    return assistant_response


