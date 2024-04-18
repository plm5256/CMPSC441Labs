import shutil
import asyncio
import argparse
from nltk.tokenize import sent_tokenize
import math
import re
from collections import Counter

import ollama

WORD = re.compile(r"\w+")

#Get the cosine distance between the input and embeddings
def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

#Turn a string into a vector for comparison
def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


async def speak(speaker, content):
  if speaker:
    p = await asyncio.create_subprocess_exec(speaker, content)
    await p.communicate()

#Driver Code
async def main():

  #Turn a paragraph into a list of sentences
  text = "Grab a paragraph of text. Create a list of sentences from the paragraph. Build a map of sentence embeddings to the sentence text using ollama embeddings function call. Ask a question taking input from the console. Calculate the top 3 sentences in your paragraph that are most similar to the input text from the console based on cosine distance between the embeddings of the sentences and the input text."
  sentences = sent_tokenize(text) #Use the nltk lib to break paragraph into a list of sentences

  #Use the embeddings function for each sentence in the list
  for i in sentences:
    ollama.embeddings(model='mistral',prompt= sentences[i])


  parser = argparse.ArgumentParser()
  parser.add_argument('--speak', default=False, action='store_true')
  args = parser.parse_args()

  speaker = None
  if not args.speak:
    ...
  elif say := shutil.which('say'):
    speaker = say
  elif (espeak := shutil.which('espeak')) or (espeak := shutil.which('espeak-ng')):
    speaker = espeak

  client = ollama.AsyncClient()

  messages = []

  
  while True:
    if content_in := input('>>> '): #Get User Input
      messages.append({'role': 'user', 'content': content_in})  #Add input to messages

      #Compare input to sentences
      similar = {0,0,0}
      v1 = text_to_vector(content_in) #Turn input into vector

      #Find cosine distance
      for i in sentences:
        v2 = text_to_vector(sentences[i]) #Turn sentences into vectors
        cos = get_cosine(v1,v2) #Get cosine
        if cos > similar[0]: #Grab the greatest match
          #Update the list of the three best matches
          similar[2] = similar[1] 
          similar[1] = similar[0]
          similar[0] = cos
          

      content_out = ''
      message = {'role': 'assistant', 'content': ''}
      async for response in await client.chat(model='mistral', messages=messages, stream=True):
        if response['done']:
          messages.append(message)

        content = response['message']['content']
        print(content, end='', flush=True)

        #Print out the top 3 matching sentences
        for i in similar:
          print("Number "+ (i + 1) +": " + similar[i])

        content_out += content
        if content in ['.', '!', '?', '\n']:
          await speak(speaker, content_out)
          content_out = ''

        message['content'] += content

      if content_out:
        await speak(speaker, content_out)
      print()


try:
  asyncio.run(main())
except (KeyboardInterrupt, EOFError):
  ...
