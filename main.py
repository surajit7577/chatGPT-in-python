import openai

openai.api_key = "YOUR OPENAI API KEY"  # Replace with your OpenAI API key
while True:
  prompt = input("enter topic: ")

  completions = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=2048,
      n=1,
      stop=None,
      temperature=0.7,
  )

  essay = completions.choices[0].text
  print(essay)

  if prompt == "exit":
    break
