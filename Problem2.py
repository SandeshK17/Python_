letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 
name = input("Emter Your name:")
print(letter.replace("<|Name|>",name).replace("<|Date|>","15/05/2025"))