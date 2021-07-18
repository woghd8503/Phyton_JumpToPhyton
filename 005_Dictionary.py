# Dictionary
dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(dic)

a = {1: 'hi'}
print(a)
a = {'a': [1, 2, 3]}
print(a)

# Dictionary 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1, 2, 3]
print(a)

del a[1]
print(a)

# Dictionary 딕셔너리 사용하는 방법 key 사용해서 Value 얻기
grade = {'pey': 10, 'julliet': 99}
grade['pey']
print(grade['pey'])
grade['julliet']
print(grade['julliet'])

a = {1:'a', 2:'b'}
a[1]
print(a[1])
a[2]
print(a[2])

a = {'a':1, 'b':2}
a['a']
print(a['a'])
a['b']
print(a['b'])

dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
dic['name']
print(dic['name'])
dic['phone']
print(dic['phone'])
dic['birth']
print(dic['birth'])

# Dictionary 만들 때 주의할 사항
a = {1:'a', 1:'b'}
print(a)

#a = {[1,2] : 'hi'} 딕셔너리의 key 값으로 딕셔너리를 사용할 수 없음
#print(a)

# Dictionary Key 리스트 만들기(keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.keys()
print(a.keys())

#for k in a.keys():   리스트를 사용하는 것과 차이가 없지만, 리스트 고유의 append, insert, pop, remove, sort함수는 사용 불가
#    print(k)

# dict_keys 객체를 리스트로 변환하려면 다름과 같이 하면 된다.
list(a.keys())
print(list(a.keys()))

# Dictionary Value 리스트 만들기(values)
a.values()
print(a.values())

# Dictionary Key, Value 쌍 얻기(items)
a.items()
print(a.items())

# Dictionary Key:Value 쌍 모두 지우기(clear)
a.clear()
print(a)

# Dictionary Key로 Value얻기(get)
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
a.get('name')
print(a.get('name'))
a.get('phone')
print(a.get('phone'))

a = {'name:':'pey', 'phone':'0119993323', 'birth':'1118'}
print(a.get('nokey'))

a.get('foo','bar')
print(a.get('foo','bar'))

# Dictionary 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
'name' in a
print('name' in a)

'email' in a
print('email' in a)