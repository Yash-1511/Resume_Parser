# Importing necessary libraries
import streamlit as st 
import spacy 
import fitz
import pandas as pd

# basic configuration
st.set_page_config(
    page_title='Resume_Parser'
)
st.title("Resume Parser Task")

def extract_text_from_pdf(pdf):
    """_summary_
    A helper function for reading pdf and extract text using pymupdf library
    Args:
        pdf (_type_): file
    Returns:
        text: str
    """
    document = fitz.open(pdf) # open pdf
    text = " "
    for page in document:   # read every page
        text = text + str(page.get_text()) # store text from every page in pdf
    return text

def convert_to_dataframe(result):
    """Converts the data from the `result` variable into a Pandas DataFrame."""
    data = {}

    for ent in result.ents:
        label = ent.label_
        if label not in data:
            data[label] = []
        data[label].append(ent.text)
    for label, entity_list in data.items():
        data[label] = ", ".join(entity_list)
    df = pd.DataFrame(data,index=(0,))
    return df

def main():
    # upload pdf
    pdf_file = st.file_uploader("Choose your resume",type=["pdf"])
    
    if pdf_file is not None: 
        # save into folder
        save_pdf_path = './uploads/' + pdf_file.name
        with open(save_pdf_path,"wb") as f:
            f.write(pdf_file.getbuffer()) 
        # extracting text from pdf              
        text = extract_text_from_pdf(save_pdf_path)
        
        # load our model
        model = spacy.load('./output/model-best')
        result = model(text)
        
        # extract data from result 
        df = convert_to_dataframe(result)
        st.dataframe(df,hide_index=True)      
if __name__ == "__main__":
    main()