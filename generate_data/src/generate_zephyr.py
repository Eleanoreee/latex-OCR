import sys
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

output_file = "/Users/eleanorewu/Latex-OCR/generate_data/generate_zephyr5.txt"

llm = Ollama(base_url="http://localhost:11434",
             model="zephyr",
             callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))

num_interactions = 200
output_list = []

for i in range(num_interactions):
    output = llm("Only give me 10 random long and complex math expressions in latex in-line equations. All equations must be bounded by $ signs, no need for \begin.")
    output_list.append(output)

all_output = '\n'.join(output_list)

# Append to the existing file
with open(output_file, 'a', encoding='utf-8') as file:
    file.write(all_output + "\n")