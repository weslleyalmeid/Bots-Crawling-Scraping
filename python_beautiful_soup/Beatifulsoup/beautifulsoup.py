from bs4 import BeautifulSoup


with open('arquivo.html', 'r') as f:
    # soup = BeautifulSoup(f, 'lxml')
    soup = BeautifulSoup(f, 'html5lib')

''' 019 Acessando tags HTML '''
tag = soup.title
print(tag)
print(tag.name)

''' 020 Acessando os atributos das tags '''
print(soup.p['class'])
print(soup.p.attrs)
print(soup.a['href'])
print(soup.a.get('href'))

''' 021 Extraindo texto do conteúdo HTML '''
print(soup.prettify())

# obtém o texto sem as tags
print(soup.get_text())

# obtém o texto da tag
print(soup.p.get_text())

''' 022 Navegando usando as tags HTML '''
with open('arquivo02.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

print(soup.title)
print(soup.head.title)
print(soup.a)
print(soup.td)

print(soup.td.attrs)

''' 023 Navegando nos filhos - Parte 1 '''
type(soup.table.contents)
soup.table.contents
len(soup.table.contents)

soup.table.contents[1].span
soup.table.contents[1].span.string


for child in soup.table.contents:
    if child.name == 'tr':
        print(child)
        print('\n')

for child in soup.footer.children:
    print(child)

for child in soup.footer.p.children:
    if child.name == 'a':
        print(child.get('href'))

print(len(list(soup.children)))
print(len(list(soup.descendants)))

''' 024 Navegando nos filhos - Parte 2 '''
from bs4.element import NavigableString, Tag

for tag in soup.descendants:
    if isinstance(tag, NavigableString):
        print(tag)
    else:
        print(tag.name)

for tag in soup.descendants:
    if isinstance(tag, Tag):
        print(tag)

#? diferença entre strings e stripped
#* deixa todos os caracteres ativo, tipo \n \t e afins
for string in soup.aside.strings:
    print(repr(string))

#* remove os caracteres  
for string in soup.aside.stripped_strings:
    print(repr(string))

''' 025 Navegando nos pais '''
tag_title = soup.title
print(tag_title)
print(tag_title.parent)

print(soup.td.parent)
print(soup.td.parent.parent)


for pai in soup.p.parents:
    print(pai.name)

''' 026 Navegando nos irmãos '''
print(soup.td.parent)
print(soup.td.next_sibling)
print(soup.td.next_sibling.next_sibling)

for sibling in soup.p.next_siblings:
    print(repr(sibling))

for sibling in soup.p.previous_siblings:
    print(repr(sibling))

'''  027 Navegando entre os elementos '''  
from bs4 import BeautifulSoup
from bs4.element import Tag

with open('./arquivo03.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

print(soup.div.next_element.next_element)
print(soup.li.previous_element.previous_element)

for element in soup.ul.next_elements:
    if isinstance(element, Tag):
        print(element)

for element in soup.li.previous_elements:
    if isinstance(element, Tag):
        print(element)

''' 028 Buscando elementos com find '''
from bs4 import BeautifulSoup

with open('./arquivo04.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

tag  = soup.find('li')
print(tag)

tag = soup.find(string = 'bear')
print(tag)

tag = soup.find(id = 'primaryconsumers')
print(tag)

tag = soup.find(attrs= {'class':'primaryconsumerlist'})
print(tag)

tag = soup.find(class_= 'primaryconsumerlist')
print(tag)

tag = soup.find('ul', attrs={'id':'parent_producers'})
print(tag)

tag = soup.ul.li.find('li')
print(tag)

''' 029 Buscando elementos com find_all '''
from bs4 import BeautifulSoup

with open('arquivo03.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

tag_list = soup.find_all('ul')
print(tag_list)

tag_list = soup.find_all(['ul', 'div'])
print(tag_list)

tag_list = soup.find_all('ul', limit= 2)
print(tag_list)

tag_list = soup.find_all(string= 'rabbit')
print(tag_list)

tag_list = soup.find_all(string= True)
print(tag_list)

tag_list = soup.find_all(string= ['rabbit', 'bear'])
print(tag_list)

tag_list = soup.find_all(class_= ['producerlist', 'primaryconsumerlist'])
print(tag_list)

tag_list = soup.ul.find_all('div')
print(tag_list)

tag_list = soup.find_all('div', class_= 'name')
print(tag_list)


''' 030 Buscando elementos com find_parent e find_parents '''
from bs4 import BeautifulSoup

with open('arquivo04.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')
'''
# * Procura só para baixo
find
 find_all 
# * Verífica o pai do nó
find_parent
find_parents
'''
     
primaryconsumers = soup.find_all(class_= 'primaryconsumerlist')
primaryconsumer = primaryconsumers[0]
print(primaryconsumer)

parent_ul = primaryconsumer.find_parents('ul')
print(parent_ul)

parent_ul = primaryconsumer.find_parent('ul')
print(parent_ul)

''' 031 Buscando irmãos '''
from bs4 import BeautifulSoup

with open('arquivo03.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

'''
# * busca irmão para baixo
find_next_sibling
# * busca irmão para cima
find_previous_sibling
'''

producers = soup.find(id='producers')
next_sibling = producers.find_next_sibling()
print(next_sibling)

producers = soup.find(id='producers')
next_siblings = producers.find_next_siblings()
print(next_siblings)

producers = soup.find(id='quaternaryconsumers')
previous_sibling = producers.find_previous_sibling()
print(previous_sibling)

producers = soup.find(id='quaternaryconsumers')
previous_siblings = producers.find_previous_siblings()
print(previous_siblings)

''' 032 Buscando o próximo elemento e o anterior '''
from bs4 import BeautifulSoup

with open('arquivo03.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')

producers = soup.find(id='producers')
tag_next = producers.find_next()
print(tag_next)

producers = soup.find(id='producers')
tag_next = producers.find_all_next()
print(tag_next)

producers = soup.find(id='quaternaryconsumers')
tag_previous = producers.find_previous()
print(tag_previous)

producers = soup.find(id='quaternaryconsumers')
tag_previous = producers.find_all_previous()
print(tag_previous)