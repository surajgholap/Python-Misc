import docx

# To access the document demo.docx through docum var
docum = docx.Document('demo.docx')
# To print the first paragraph 
print(docum.paragraph[0].text)
sec_paragraph = docum.paragraph[1].text
# runs function is used to address different styled
# parts of the paragraph
print(sec_paragraph.runs[0].text)
# runs can be used to change the text style and the text too
sec_paragraph.runs[1].underline 
# To save the document
docum.save('new_docum.docx')