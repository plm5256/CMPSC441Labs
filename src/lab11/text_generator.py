from transformers import pipeline

#This function uses AI text generation freom given context
#Ideally the player would ask for information about something, and the function will create filler dialogue/information about the requested thing
def generateText(context):
    #Call pipeline function
    gen = pipeline('text-generation', model ='EleutherAI/gpt-neo-2.7B')

    #Generate text
    # context = "There are many goblins in the next city." (An example of a prompt given by the player)
    output = generator(context, max_length=50, do_sample=True, temperature=0.9)

    #Write output to a text file
    with open('dl.txt', 'w') as f:
            f.write(str(output))

# Example used in testing: context = "Deep Learning is a sub-field of Artificial Intelligence."
# Output received: "Deep Learning is a sub-field of Artificial Intelligence. It was an early and widely recognized topic in learning theory, and has received quite a lot of attention over the years.
# The term artificial intellgence is quite often used to desribe a system or machine that can be."