import docx2txt
import io
import fitz


def extract_text_from_pdf(pdf):
    """_summary_
    A helper function for reading pdf and extract text using pymupdf library
    Args:
        pdf (_type_): file
    Returns:
        text: str
    """
    document = fitz.open(pdf)  # open pdf
    text = " "
    for page in document:   # read every page
        text = text + str(page.get_text())  # store text from every page in pdf
    return text


def extract_text_from_docx(doc_path):
    try:
        temp = docx2txt.process(doc_path)
        text = [line.replace('\t', ' ') for line in temp.split('\n') if line]
        return ' '.join(text)
    except KeyError:
        return ' '


def extract_text_from_doc(doc_path):
    '''
    Helper function to extract plain text from .doc files

    :param doc_path: path to .doc file to be extracted
    :return: string of extracted text
    '''
    try:
        try:
            import textract
        except ImportError:
            return ' '
        text = textract.process(doc_path).decode('utf-8')
        return text
    except KeyError:
        return ' '


def extract_text(file_path, extension):
    '''
    Wrapper function to detect the file extension and call text
    extraction function accordingly

    :param file_path: path of file of which text is to be extracted
    :param extension: extension of file `file_name`
    '''
    text = ''
    if extension == 'pdf':
        text = extract_text_from_pdf(file_path)
    elif extension == 'docx':
        text = extract_text_from_docx(file_path)
    elif extension == 'doc':
        text = extract_text_from_doc(file_path)
    return text
 
