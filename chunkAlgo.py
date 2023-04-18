import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "philschmid/bart-large-cnn-samsum"
tokenizer = AutoTokenizer.from_pretrained(model_name)

input_file = "formattedData.txt"
filename_tmp = os.path.basename(input_file)
# love this line
# filename = filename_tmp[:filename_tmp.rindex('.')]

# Open input file for reading
with open(input_file, "r") as input_file:
        # Initialize output file counter and buffer
        output_file_counter = 1
        buffer = []
        token_counter = 0
        for line in input_file:
            # Tokenize line
            encoded_line = tokenizer.encode(line.strip(), add_special_tokens=True)
            # Split encoded line into chunks of 950 tokens or less
            for i in range(0, len(encoded_line), 950):
                chunk = encoded_line[i:i+950]
                buffer.extend(chunk)
                token_counter += len(chunk)
                # If buffer size exceeds 950 tokens, write buffer to output file
                if token_counter > 950:
                    output_file_path = f"politico_{output_file_counter}.txt"
                    with open(output_file_path, "w") as output_file:
                        output_file.write("".join(tokenizer.decode(token, add_special_tokens=True) for token in buffer))
                    # Reset buffer and token counter
                    buffer = []
                    token_counter = 0
        # Write remaining tokens to output file
        if len(buffer) > 0:
            output_file_counter += 1
            output_file_path = f"politico_{output_file_counter}.txt"
            with open(output_file_path, "w") as output_file:
                output_file.write("".join(tokenizer.decode(token, add_special_tokens=True) for token in buffer))