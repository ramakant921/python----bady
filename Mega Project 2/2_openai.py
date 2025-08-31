from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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"
)


command = '''
[20:59, 26/8/2025] Saurabh 2: Bas missing you
[21:00, 26/8/2025] 🙂: then you are gay
[21:00, 26/8/2025] Saurabh 2: Nope
[21:00, 26/8/2025] Saurabh 2: I am straight
[21:00, 26/8/2025] Saurabh 2: I can send you the proof
[21:00, 26/8/2025] 🙂: accpet it bro i have no problem
[21:01, 26/8/2025] 🙂: i don't need any proof
[21:01, 26/8/2025] 🙂: you can be anyone became anyone it's your choice     
🙏
[21:02, 26/8/2025] 🙂: how's your preparation goin ?
[21:02, 26/8/2025] Saurabh 2: Fucked up
[21:02, 26/8/2025] 🙂: dayum
[21:03, 26/8/2025] 🙂: chal bye😘😘
[21:15, 26/8/2025] Saurabh 2: Bye 💋💋💋💋💋
'''


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Ramakant who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Ramakant"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)