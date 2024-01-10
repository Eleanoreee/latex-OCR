import sys
from langchain.llms import Ollama
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler   

output_file = "generate_zephyr.txt"

llm = Ollama(base_url = "http://localhost:11434",
             model = "zephyr",
             callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))

num_interactions = 10
output_list = []

for i in range(num_interactions):
    output = llm("Only give me 10 random long and complex math expressions in latex in-line equations. All equations must be bounded by $ signs, no need for \begin.")
    output_list.append(output)

all_output = '\n'.join(output_list)

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(all_output + "\n")