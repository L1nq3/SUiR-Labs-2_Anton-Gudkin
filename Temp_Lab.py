import csv
import random as r
import xml.dom.minidom as minidom

def count_name():
    ans = 0
    with open('books-en.csv', encoding='cp1251') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in (reader):
            if len(row['Book-Title']) > 30:
                ans += 1
    print(ans)

def search():
    pattern = input('Введите автора: ')
    with open('books-en.csv', encoding='cp1251') as f:
            reader = csv.DictReader(f, delimiter=';')
            fl = True
            print('---'*20)
            for row in (reader):
                 if (pattern == row['Book-Author']) and (1997 <= int(row['Year-Of-Publication']) <= 2000):
                      fl = False
                      for key in row:
                           print(key + ' ' * (20-len(key)) + '| ' + row[key])
                      print('---'*20)  
            if fl:
                 print('Author is not founded')
                 print('---'*20) 

def bibliographic_generation():
     with open('books-en.csv', encoding='cp1251') as f:
        reader = list(csv.DictReader(f, delimiter=';'))
        rand_nums = []
        res = open('result.txt', 'w')
        for _ in range(20):
             x = r.randint(1, len(reader))
             if rand_nums.count(x) == 0:
                  rand_nums.append(x)
        n = 0  
        for i in rand_nums:
             n += 1
             if len(reader[i]['Book-Author']) >= 60 or len(reader[i]['Book-Title']) >= 100: #добавил просто чтобы не выводились книги с гигантскими названиями
                  continue
             res.writelines(f'{n}' + ' '*(3-len(str(n))) + reader[i]['Book-Author'] + ' '*(60-len(reader[i]['Book-Author'])) + reader[i]['Book-Title'] + ' '*(100-len(reader[i]['Book-Title'])) + ' | ' + reader[i]['Year-Of-Publication'] + '\n')
          #    print(reader[i]['Book-Author'] + ' '*(60-len(reader[i]['Book-Author'])) + reader[i]['Book-Title'] + ' '*(100-len(reader[i]['Book-Title'])) + ' | ' + reader[i]['Year-Of-Publication'])

def get_text(elem):
    if elem and elem.firstChild:
        return elem.firstChild.nodeValue.strip()
    return ''

def pairs_xml():
     dom = minidom.parse('currency.xml')
     val = dom.getElementsByTagName('Valute')
     result = {}
     for valute in val:
          char_nodes = valute.getElementsByTagName('CharCode')
          nom_nodes  = valute.getElementsByTagName('Nominal')
          if not char_nodes or not nom_nodes:
               continue
          key = get_text(char_nodes[0])
          num = int(get_text(nom_nodes[0]))
          result[key] = num
     for key in result:
          print(key, result[key], end = ' ')

def publisher():
     with open('books-en.csv', encoding='cp1251') as f:
          reader = list(csv.DictReader(f, delimiter=';'))
          set_publ = []
          for i in range(len(reader)):
               if set_publ.count(reader[i]['Publisher']) == 0:
                    set_publ.append(reader[i]['Publisher'])
                    print(reader[i]['Publisher'])
def downloads():
     top_nums = 20
     with open('books-en.csv', encoding='cp1251') as f:
          reader = list(csv.DictReader(f, delimiter=';'))
          rate = [0 for _ in range(top_nums)]
          name = ['' for _ in range(top_nums)]
          for i in range(len(reader)):
               candidate = reader[i]['Book-Title']
               down = int(reader[i]['Downloads'])
               for j in range(top_nums):
                    if rate[j] < down:
                         rate[j] = down
                         name[j] = candidate
                         break
          for i in range(top_nums):
               print(i+1, ' '*(3-len(str(i+1))), name[i], ' '*(100-len(name[i])), '|', rate[i])
# count_name()

# search() #Scott Turow

# bibliographic_generation()

# pairs_xml()

# publisher()
# publisher_check()

# downloads()

print('Задание №1')
count_name()
input('нажмите Enter для продолжения')
print('Задание №2')
search() #Scott Turow
input('нажмите Enter для продолжения')
print('Задание №3')
bibliographic_generation()
input('нажмите Enter для продолжения')
print('Задание №4')
pairs_xml()
print('\n')
input('нажмите Enter для продолжения')
print('Доп Задание №1')
publisher()
input('нажмите Enter для продолжения')
print('Доп Задание №2')
downloads()