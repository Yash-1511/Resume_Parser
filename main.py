import streamlit as st
import spacy
from utils import extract_text
from multiprocessing import Pool
import multiprocessing as mp
import os
# Basic configuration
st.set_page_config(page_title='Resume_Parser')
st.title("Resume Parser Task")


def convert_to_dataframe(result):
    """Converts the data from the `result` variable into a dictionary."""
    data = {}
    for ent in result.ents:
        if ent.label_ not in data.keys():
            data[ent.label_] = [ent.text]
        else:
            data[ent.label_].append(ent.text)

    for key in data.keys():
        data[key] = list(set(data[key]))

    return data


def process_resume(resume_path):
    """Processes a single resume and returns the extracted data."""
    ext = resume_path.split(".")[-1]
    text = extract_text(resume_path, ext)
    model = spacy.load("en_resume_pipeline")
    result = model(text)
    data = convert_to_dataframe(result)
    return data


def main():
    # Sidebar option for choosing single or multiple PDFs
    option = st.sidebar.radio("Select Option", ("Single PDF", "Multiple PDFs"))
    os.makedirs("uploads",exist_ok=True)
    if option == "Single PDF":
        # Upload single resume PDF
        resume_file = st.file_uploader("Choose your resume", type=["pdf", "docx"])
        
        if resume_file is not None:
            # Save the resume into a folder
            save_resume_path = './uploads/' + resume_file.name
            with open(save_resume_path, "wb") as f:
                f.write(resume_file.getbuffer())
            
            # Process the single resume
            data = process_resume(save_resume_path)

            # Display data using Streamlit components
            st.header('Personal Information')
            for key, val in data.items():
                st.subheader(str(key))
                st.write(val)

    elif option == "Multiple PDFs":
        # Upload multiple resume PDFs
        resume_files = st.file_uploader("Choose your resumes", type=["pdf", "docx"], accept_multiple_files=True)
        
        if resume_files is not None:
            # Save the resumes into a folder
            save_resume_paths = []
            for resume_file in resume_files:
                save_resume_path = './uploads/' + resume_file.name
                with open(save_resume_path, "wb") as f:
                    f.write(resume_file.getbuffer())
                save_resume_paths.append(save_resume_path)

            # Process the resumes using multiprocessing
            pool = Pool(mp.cpu_count())
            results = [pool.apply_async(process_resume,args=(x,)) for x in save_resume_paths]
            results = [p.get() for p in results]
            
            for i, data in enumerate(results):
                st.header(f'Resume {i+1} - Personal Information')
                for key, val in data.items():
                    st.subheader(str(key))
                    st.write(val)


if __name__ == "__main__":
    main()
