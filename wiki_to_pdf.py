import pdfkit
import glob
import os

config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
filelist = glob.glob(r'*.md')

for filename in filelist:
    body = open(filename, 'r', encoding='utf-8').read()

    body = body.replace('</<', '<')
    body = body.replace('<hr/>', '')

    header = '''<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    </head>
    <style>
      pre {
        font-size: 15px;
        border-bottom: solid;
        border-bottom-width: 1px;
      }

      pre:last-child {
        border-bottom: none;
      }

      table {
        border-collapse: collapse;
      }

      tr {
        border: solid;
        border-width: 1px 1px;
      }

      th {
        font-weight: bold;
        font-size: 20px;
      }

      td, th {
        font-size: 20px;
        border: solid;
        border-width: 1px;
      }
    </style>
    <body>'''

    name = filename.replace(".md", "")

    tail = '''
    </body>
    </html>'''

    full_html = header + "<h1>" + name + "</h1><br>" + body + tail

    html_file = open(name + ".html", "w", encoding='utf-8')
    html_file.write(full_html)
    html_file.close()
    pdfkit.from_file(name + '.html', name + '.pdf', configuration=config)
    os.remove(name + '.html')