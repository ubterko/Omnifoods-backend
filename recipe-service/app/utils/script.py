with open("seed.txt",'r') as f:
    text = f.read()
    text = text.replace("\n\n","\n")
    writer = open("seed.txt",'w') 
    writer.write(text)