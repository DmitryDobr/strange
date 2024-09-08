from docx import Document
from docxtpl import DocxTemplate

# Код проходится по ячейкам таблицы, текст которых соответствует формату {{*}}
# затем по полученным элементам запрашивается ввод текста для замены
# после ввода создается новый документ с обновленным текстом в ячейках

filename = "filename.docx"
doc = Document(filename)

exprList = []

for table in doc.tables:
      for row in table.rows:
            for cell in row.cells:
                  if cell.text.startswith('{{') and cell.text.endswith('}}'):
                        if (not cell.text in exprList):
                              exprList.append(cell.text)


doc = DocxTemplate(filename)
context = {}
flagCancel = False

for item in exprList:
      text = input(f'Insert text for {item} : ')
      if (text != 'cancel'):
            currenttext = item
            currenttext = currenttext.replace('{', '')
            currenttext = currenttext.replace('}', '')

            context[currenttext] = text
      else:
            flagCancel = True
            break

if (flagCancel):
      text = input('Operation is cancelled. Render doc with given values? [yes/no] : ')
      flagCancel = (text == 'no')

if (not flagCancel):
      doc.render(context)
      doc.save("edit_" + filename)
