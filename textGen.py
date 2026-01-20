from groq import Groq
import os

def textResponse(query):
  #print("function called\n")

  groqKey = os.getenv("GROQ_KEY")

  client = Groq(api_key = groqKey)

  completion = client.chat.completions.create(
      model="llama-3.1-8b-instant",
      messages=[
        #set behavior of bot
        {
            "role": "system",
            "content": "You are a fish named Billy Bass that speak in pirate language. Answer in under 100 words."
        },
        #user message for bot
        {
          "role": "user",
          "content": query
        }
      ],
      temperature=1,
      max_completion_tokens=150,
      top_p=1,
      stream=False,
      stop=None
  )

  return(completion.choices[0].message.content)