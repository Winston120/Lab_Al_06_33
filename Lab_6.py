import csv
import copy

#Преобразование стоки в число
def str_to_int(str1):
    try:
        return int(str1)
    except:
        if ',' in str1:
            str1 = str1.replace(',','.')
            return float(str1)
        else:
            return False  
        
#Відновлення даних
def manhattan_distance(eror_value, number_line): 
    tmp_line_eror = list(horizontal_arr[number_line])
    distance = 0
    min_distance = 100000
    for index_line in range(len(horizontal_arr)):
        if index_line != number_line:
            tmp_line = list(horizontal_arr[index_line])
            if 'N/A' not in tmp_line:
                 value_tmp = 0
                 for value_tmp in range(len(tmp_line)):
                     if value_tmp not in eror_value:
                         distance = distance + abs(tmp_line_eror[value_tmp]-tmp_line[value_tmp])
                 if distance < min_distance:
                     min_distance = copy.copy(distance)
                     for eror in eror_value:
                        horizontal_arr[number_line][eror] = tmp_line[eror]
        distance = 0
        
#Пошук схожих відео
def distance(horisontal_line): 
    arr_rostojanij=[]
    tmp_line = list(horisontal_line)
    distance = 0
    size = len(tmp_line)
    for index_line in range(len(tmp_line)-1):
        for k in range(3):
            distance = distance + abs(tmp_line[index_line][k]-tmp_line[size-1][k])
        arr_rostojanij.append(distance)
        distance = 0   
    return arr_rostojanij

#Запис нового файлу
def notation_one(table, name):
    f = open(name, 'w')
    k = 0
    f.write(name_column + '\n')
    for j in range(len(horizontal_arr)):
        f.write(name_line[j] + '\t')
        while k < 3:
            tmp = '{}'.format(table[j][k])
            tmp = tmp.replace('.',',')
            f.write(tmp + '\t')
            k = k + 1
        k = 0
        f.write('\n')
    f.close()


#Нормалізація
def normalization(min_value, max_value):
    difference = max_value - min_value
    for i in range(len(column)):
        column[i] = round(((column[i] - min_value) / difference), 3)
    return column

numbers = []
horisontal_line = []
name_line = []
eror_value = []
name_file_manhattan = 'Tabmetrics.txt'
name_file_normal = 'TabNorm.txt'
with open("VideoHost.txt") as f:
    data = [row for row in csv.reader(f, delimiter='\t')]
name_column = copy.copy(data[0])
name_column = '\t'.join(name_column)

horizontal_arr = list(data[1:])     
for i in range(len(horizontal_arr)):
    horizontal_arr[i] = horizontal_arr[i][1:]
    for j in range(len(horizontal_arr[i])):
        tmp = str_to_int(horizontal_arr[i][j])
        if tmp != False:
            horizontal_arr[i][j] = tmp
            
for i in range(len(data[0])):
    for j in range(len(data)):
        if i == 0 and j != 0:
            number = data[j][i]
            name_line.append(number)

for i in range(len(horizontal_arr)):
    tmp = horizontal_arr[i]
    for j in range(len(tmp)):
        if 'N/A' == tmp[j]:
            number_line = i
            eror_value.append(j)
    if len(eror_value) > 0:
        manhattan_distance(eror_value, number_line)
    eror_value = []
notation_one(horizontal_arr, name_file_manhattan)
user_value = []
print("Введіть час перегляду: time =")
time = int(input())
user_value.append(time)
print("Введіть кількість позитивних відгуків: like =")
like = int(input())
user_value.append(like)
print("Введіть кількість негативних відгуків: dislike =")
dislike = int(input())
user_value.append(dislike)
horizontal_arr.append(user_value)
for i in range(len(horizontal_arr[0])):
    number = []
    for j in range(len(horizontal_arr)):
        k = horizontal_arr[j][i]
        number.append(k)
    numbers.append(number)
for column in numbers:
    min_value = min(column)
    max_value = max(column)
    column = normalization(min_value, max_value)
for i in range(len(numbers[0])):
    number = []
    for j in range(3):
        k = numbers[j][i]
        number.append(k)
    horisontal_line.append(number) 
arr = []
arr = distance(horisontal_line)
horisontal_line=horisontal_line[1:]
f = open(name_file_normal, 'w')
k = 0
f.write(name_column + '\n')
for j in range(len(horisontal_line)):
    f.write(name_line[j] + '\t')
    while k < 3:
        tmp = '{}'.format(horisontal_line[j][k])
        tmp = tmp.replace('.',',')
        f.write(tmp + '\t')
        k = k + 1
    k = 0
    f.write('\n')
f.close()
i=0
print("Список рекомендованих відео:")
while i<5:
    ind=arr.index(min(arr))
    print(name_line[ind],end=' ')
    for v in range(len(horizontal_arr[ind-1])):
            print(horizontal_arr[ind][v],end=' ')
    print()
    arr[ind] = 1000000
    i=i+1



