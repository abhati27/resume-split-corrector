# resume-split-corrector

PDF Splitter is a Python script that extracts the first page of a PDF file and saves it to a new file. The script uses the PyPDF2 library to manipulate PDF files.

# Setup
1. Have python installed on your computer. pip install PyPDF2 library on your computer

    that can be done like this on the terminal:

    pip install PyPDF2

2. Enter the following code into the new document:
    
    #!/bin/bash

    python /path/to/your/python/script.py "$@"

    save it as pdf_splitter.sh

3. move the file to bin folder in your computer so that it can be accessed from anywhere. this can be done by:

    sudo cp pdf_splitter /usr/local/bin

4. Make the pdf_splitter script executable by running the following command:

    sudo chmod +x /usr/local/bin/pdf_splitter

# Usage

the now-made shell app can be commanded like this:
    
    ./pdf_spliter.sh "Curriculum_Vitae_Latex (5).pdf" "test.pdf"

    from anywhere on your computer

    
