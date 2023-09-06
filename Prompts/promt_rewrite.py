# Input file name
input_file_name = 'p1.txt'
# Output file name
output_file_name = 'p1 nl.txt'

try:
    # Open the input file for reading
    with open(input_file_name, 'r') as input_file:
        # Read the content of the input file
        content = input_file.read()
        
        # Replace "\n" with actual newlines
        content = content.replace(r'\n', '\n')
        
        # Open the output file for writing
        with open(output_file_name, 'w') as output_file:
            # Write the modified content to the output file
            output_file.write(content)
    
    print(f"Successfully converted {input_file_name} to {output_file_name}")
except FileNotFoundError:
    print(f"File {input_file_name} not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
