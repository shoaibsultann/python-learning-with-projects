# Q2: Write a program to fill in a letter template given below with name and date.

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace('<|Name|>', 'Shoaib').replace('<|Date|>','2nd June 2025'))
