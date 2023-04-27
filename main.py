triplets = []

with open('docs_gettext/youtube.pot', 'r', encoding='UTF-8') as f:
    lines = f.readlines()

    # Iterate over each line of the file
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Check if it's the start of a new message definition
        if line.startswith('#:'):
            comment = line[2:].strip()
            msgid = ''
            msgstr = ''

            # Look for the msgid and msgstr lines
            while i < len(lines) - 1:
                i += 1
                if lines[i].startswith('msgid "'):
                    msgid = lines[i].strip()[7:-1]
                elif lines[i].startswith('msgstr "'):
                    msgstr = lines[i].strip()[8:-1]
                    break
            
            # Append the triplet if both msgid and msgstr are nonempty
            if msgid:
                triplets.append([comment, msgid, msgstr])

        i += 1
        
# print(triplets)

import openai
import time
openai.api_key = "anything"
openai.api_base ="https://free.churchless.tech/v1"

def translate_text(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"请将以下英文翻译成中文:\n{text}",
        max_tokens=2048
    )

    translate_text = response.choices[0].text.strip()
    return translate_text

for t in triplets:
    t[2]=translate_text(t[1])
    time.sleep(1)
    

import csv
filename = 'output.csv'
with open(filename, 'w', newline='', encoding='UTF-8') as f:
    writer = csv.writer(f)
    
    # Write the header row
    # writer.writerow(fieldnames)

    # Write each triplet as a row in the CSV file
    for triplet in triplets:
        writer.writerow(triplet)