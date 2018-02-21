import urllib.request
import json
import datetime

cdate = datetime.datetime.now()

NUMS = []
for i in range(0, 10):
    n = input('Dwse arithmo:')
    NUMS.append(int(n))

print(NUMS[:])
print('\n')

d = datetime.datetime.today().day


def check(pin1, pin2):
    s = 0
    for i in pin1:
        if i in pin2:
            s += 1
    return s


nums_epituxias = []
hmeres = []
for i in range(int(d)):
    cdate = cdate - datetime.timedelta(days=1)
    mera = cdate.strftime("%d-%m-%Y")
    hmeres.append(mera)
    url = 'http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json' % mera
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    data = json.loads(data)
    klhrwseis = data['draws']['draw']
    epituxies = []
    for k in klhrwseis:
        res = k['results']
        epituxies.append(check(NUMS, res))
    n = 0
    for i in range(180):
        if epituxies[i] > 4:
            n += 1

    nums_epituxias.append(n)
    print('apotelesmata', mera)
    print(epituxies[:])
    print('\n')

max_nums = max(nums_epituxias)
a = nums_epituxias.index(max(nums_epituxias))

print('Oi perissoteres epituxies sas einai', max_nums, 'thn hmera', hmeres[a])
