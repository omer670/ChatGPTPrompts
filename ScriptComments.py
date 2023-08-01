import sys
import openai 

openai.api_key = "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"


def GenerateDocstring(scriptName, givenPrompt = None, pythonVersion =  3.7):
    
    # Prompt to remove comments
    with open(scriptName) as f:
        sourceCode = f.read()

    if givenPrompt is None:
        givenPrompt = "Write elaborate, high quality code comments for each function in the above script:"
    
    # Wrap the source code with hints for GPT-3
    GPTPrompt = f"# Python {pythonVersion}\n\n" \
           + sourceCode \
           + "\n# " + givenPrompt + "\n\"\"\""
   # prompt = "hello"

    # Send prompt to GPT-3
    response = openai.Completion.create(
                   model= "text-davinci-003",
                   prompt=GPTPrompt,
                   temperature=0,
                   max_tokens=1000,
                   top_p=1.0,
                   frequency_penalty=0.0,
                   presence_penalty=0.0,
                   stop=["#", "\"\"\""]
               )
    
    # Return the generated docstring
    docstring = response["choices"][0]["text"]
    return docstring



print(GenerateDocstring(sys.argv[1], sys.argv[2], 3.11))

