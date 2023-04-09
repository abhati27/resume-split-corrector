import argparse
import os
import PyPDF2

# Define command-line arguments
parser = argparse.ArgumentParser(description='Extract the first page of a PDF file and save it to a new file.')
parser.add_argument('input_file', type=str, help='Name of the input PDF file in the Downloads directory')
parser.add_argument('output_file', type=str, help='Name of the output PDF file on the Desktop')
args = parser.parse_args()

# Set the full path of the input PDF file
downloads_dir = os.path.expanduser('~/Downloads')
input_file = os.path.join(downloads_dir, args.input_file)

# Check if input file exists
if not os.path.exists(input_file):
    print('Error: Input file does not exist')
    exit()

# Set the full path of the output PDF file
desktop_dir = os.path.expanduser('~/Desktop/resume')
output_file = os.path.join(desktop_dir, args.output_file)

# Open the input PDF file
with open(input_file, 'rb') as input_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(input_file)

    # Extract the first page of the PDF file
    first_page = pdf_reader.pages[0]

    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Add the first page to the PDF writer object
    pdf_writer.add_page(first_page)

    # Write the PDF writer object to a new file
    with open(output_file, 'wb') as output_file:
        pdf_writer.write(output_file)

print('First page extracted and saved to', output_file)
