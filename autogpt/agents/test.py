import ast
import json

def extract_dict_from_response(response_content: str):
    # response content comes from OpenAI as a Python `str(content_dict)`, literal_eval reverses this
    try:
        return ast.literal_eval(response_content)
    except BaseException as e:
        # TODO: How to raise an error here without causing the program to exit?
        return {}
    
if __name__ == '__main__':
        raw_response = '''
{
"thoughts": {
"text": "To fulfill the goal of understanding how messages are constructed and how memory is used, I should start by analyzing the messages provided in this conversation.",
"reasoning": "Analyzing the messages will help me gain insights into the structure and content of messages, as well as how information is stored and retrieved within the conversation.",
"plan": "1. Analyze the content and structure of the messages.\\n2. Identify patterns in message construction and memory usage.\\n3. Summarize my findings to convey to the user.",
"criticism": "I need to be thorough in my analysis and ensure I extract relevant information about message construction and memory usage.",
"speak": "I will begin by analyzing the messages in this conversation to better understand how they are constructed and how memory is used."
},
"command": {
"name": "analyze_messages",
"args": {}
}
}
'''
        #with open("llm_response.txt", "w") as outfile:
        #        outfile.write(raw_response)
        with open('llm_response.json', 'r') as openfile:
                # Reading from json file
                reload = openfile.read()
        assistant_reply_dict = extract_dict_from_response(reload)
        '''with open("llm_response.json", "w") as outfile:
                json.dump(json_file, outfile)

        with open('llm_response.json', 'r') as openfile:
                # Reading from json file
                json_object = json.load(openfile)
        print(json_object)'''
        #assistant_reply_dict = extract_dict_from_response(raw_response)
        print(assistant_reply_dict)