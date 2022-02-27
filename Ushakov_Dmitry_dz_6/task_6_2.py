# *2.Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
def parse_line(line):
    lst = line.split(' ')
    return (lst[0], lst[5][1:], lst[6])


fname = "nginx_logs.txt"
print(f'Parse file {fname}')
gen = (parse_line(line) for line in open(fname, 'r'))
dict_user = {}
while True:
    try:
        new_element = next(gen)
        if new_element[0] in dict_user:
            dict_user[new_element[0]] += 1
        else:
            dict_user[new_element[0]] = 1
    except StopIteration:
        break
rate = sorted(dict_user.items(), key=lambda item: item[1], reverse=True)

print('Top 3 spammers:')
for i in range(1, 4):
    leader = rate.pop(0)
    print(f'{i}. {leader[0]} - {leader[1]} times')
