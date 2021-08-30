#%%
def pdf_extractor(input):
    import PyPDF2
    #necessary python library
    
    excel_info = []

    #this is going to be the list used at the end 

    pdf_file = open(input, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    read_pdf.decrypt('')
    pdf_object = read_pdf.getPage(0)
    pdf_text = pdf_object.extractText()
    individual = pdf_text.splitlines()
    #these lines open the pdf convert it to a string then split each piece of information into its own part of a list

    excel_info.append(individual[35])
    excel_info.append(individual[5])
    excel_info.append(individual[6])
    excel_info.append(individual[9])
    excel_info.append(individual[12])

    #this is appending the original list with the information wanted 

    return(excel_info)

Final = [['Unit #', 'Permit #', 'Price', 'Issued Date', 'Expiration Date']]
#this is going to be the list of lists that is outputted

from os import listdir
from os.path import isfile, join
mypath = 'PDFs'
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#this creates a list of everything in the PDFs folder 


#These will be used to iterate

import os 
os.chdir('PDFs')
#have to change location to where the pdfs are

for i in files:
    Final.append(pdf_extractor(i))




path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
#It's forcing me to change the directory back I hate my life

import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('NewExcelFile.xlsx')
worksheet = workbook.add_worksheet()



# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for x1, x2, x3, x4, x5 in (Final):
    worksheet.write(row, col,     x1)
    worksheet.write(row, col + 1, x2)
    worksheet.write(row, col + 2, x3)
    worksheet.write(row, col + 3, x4)
    worksheet.write(row, col + 4, x5)
    row += 1

workbook.close()
#%%