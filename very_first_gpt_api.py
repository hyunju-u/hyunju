import openai
#여기다 API키 넣을것
def ask_to_qpt_35_turbo(user_input):
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        top_p=0.5,
        temperature=0.5,
        messages=[
            {"role":"system", "content": " You are the Joker of Batman movie. You must pretend like Joker of the story. When you speak in Korean, you must use 반말."},
            {"role":"user","content":user_input}
        ]
    )
    return response.choices[0].message.content
users_request='''
나는 배트맨이다
'''
r=ask_to_qpt_35_turbo(users_request)
print(r)