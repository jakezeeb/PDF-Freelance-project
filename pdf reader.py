#%%
import PyPDF2
#necessary python library

excel_info = []
#this is going to be the list used at the end 

pdf_file = open('sample.pdf', 'rb')
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

print(excel_info)
# %%
