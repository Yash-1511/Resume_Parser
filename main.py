import spacy
import sys,fitz 
import pandas as pd 
nlp = spacy.load('./output/model-best')
fname = "./yashnewresume.pdf"
doc = fitz.open(fname)

text = " "
for page in doc:
  text = text+str(page.get_text())
  
doc = nlp(text)
# df = pd.DataFrame(columns=[ent.label_ for ent in doc.ents])
# print(df)
# for ent in doc.ents:
#   print(ent.text," - ",ent.label_)
data = {}

for ent in doc.ents:
    label = ent.label_
    if label not in data:
        data[label] = []
    data[label].append(ent.text)
    
# max_length = max(len(entity_list) for entity_list in data.values())

# # Extend the entity lists to the maximum length with None
# for entity_list in data.values():
#     entity_list.extend([None] * (max_length - len(entity_list)))
# Create comma-separated strings for each label
for label, entity_list in data.items():
    data[label] = ", ".join(entity_list)
df = pd.DataFrame(data,index=(0,))
print(df)
# print(data)