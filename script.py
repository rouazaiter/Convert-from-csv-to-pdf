from fpdf import FPDF, HTMLMixin
from string import Template
from jinja2 import Template, Environment, FileSystemLoader
import pandas as pd 

class PDF(FPDF, HTMLMixin):
    pass


data = pd.read_csv('C:/Users/lenovo/Desktop/s/output.csv')
print(data)

# Parcourir les lignes du DataFrame
for index, row in data.iterrows():
    firstname = row['firstname']
    lastname = row['lastname']
    position = row['position']
    company = row['company']    
    print("First Name:",firstname)
    print("Last Name:", lastname)
    print("Position:", position)
    print("Company:", company)
'''
for x in data:
    print("First Name:", x.firstname)
    print("Last Name:", x.lastname)
    print("Position:", x.position)
    print("Company:", x.company)
    print()  '''
    
env = Environment(loader=FileSystemLoader('C:\\Users\\lenovo\\Desktop\\s'))
template = env.get_template('template.html')
    

pdf = PDF()

#env = Environment(loader=FileSystemLoader('C:/Users/lenovo/Desktop/s/template.html'))
#template = env.from_string(template_content)


for index, row in data.iterrows():
    row_data = ', '.join(str(cell) for cell in row)
    pdf.add_page()
    #pdf.set_font('Arial', 'B', 12)
    #pdf.multi_cell(0, 10, row_data)
    html = template.render(row)
    pdf.write_html(html)

    #template_content = file.read()
    
#html = template.render(data=row)

    
pdf.output('C:/Users/lenovo/Desktop/s/output.pdf')




