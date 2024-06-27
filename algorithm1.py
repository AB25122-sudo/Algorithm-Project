'''
## 전역 변수부
katok = ['DaHyen', 'JunYeon', 'Tzuyu', 'Sana', 'JiHyo'] # 배열

## 메인 코드부

## 데이터 추가 (모모가 카톡 1회)
# 1단계 : 빈칸 확보
katok.append(None)
# 2단계 : 마지막 칸에 친구 대입
katok[5] = 'Momo'

## 데이터 삽입 (미나가 카톡 연속 40회 == 미나를 3등으로)
# 1단계 : 빈칸 확보
katok.append(None)
# 2단계 : 한칸씩 뒤로 이동. 3등까지..
katok[6] = katok[5] # 모모 이동
katok[5] = None
katok[5] = katok[4] # 지효 이동
katok[4] = None
katok[4] = katok[3] # 사나 이동
katok[3] = None
# 3단계 : 확보한 자리(3)에 미나 대입
katok[3] = 'Mina'

## 데이터 삭제 (사나(4등)가 카톡 차단)
# 1단계 : 데이터 삭제
katok[4] = None
# 2단계 : 한칸씩 앞으로 이동. 마지막 친구까지...
katok[4] = katok[5] # 지효 이동
katok[5] = None
katok[5] = katok[6] # 지효 이동
katok[6] = None
# 3단계 : 마지막 칸을 제거
del(katok[6])
print(katok)
'''


'''
## Function
def add_data(friend):
    kt.append(None)
    kLen = len(kt)
    kt[kLen-1] = friend
def insert_data(position, friend):
    kt.append(None)
    kLen = len(kt)
    for i in range(kLen-1,position, -1):
        kt[i] = kt[i-1]
        kt[i-1] = None
    kt[position] = friend
def delete_data(position):
    kt[position] = None
    kLen = len(kt)
    for i in range(position, kLen-1):
        kt[i] = kt[i+1]
        kt[i+1] = None
    del kt[kLen-1]

## Global
kt = []

## Main
add_data('DaHyeon')
add_data('JungYeon')
add_data('Tzuyu')
add_data('Sana')
add_data('JiHyo')
add_data('Momo')

insert_data(3, 'Mina')

delete_data(4)

print(kt)
'''

'''
def add_data(friend):
    kt.append(None)
    kLen = len(kt)
    kt[kLen-1] = friend
def insert_data(position, friend):
    kt.append(None)
    kLen = len(kt)
    for i in range(kLen-1,position, -1):
        kt[i] = kt[i-1]
        kt[i-1] = None
    kt[position] = friend
def delete_data(position):
    kt[position] = None
    kLen = len(kt)
    for i in range(position, kLen-1):
        kt[i] = kt[i+1]
        kt[i+1] = None
    del kt[kLen-1]

#
kt,select = [], -1

#
if __name__ == '__main__':
    while (select != 4):
        select = int(input('1:add\n2:insert\n3:delete\n4:quit'))
        if (select == 1):
            data = input('data: ')
            add_data(data)
            print(kt)
        elif (select==2):
            pos = int(input('insert position: '))
            data = input('data: ')
            insert_data(pos,data)
            print(kt)
        elif (select==3):
            pos = int(input('delete position: '))
            delete_data(pos)
            print(kt)
        elif (select==4):
            print(kt)
            exit
        else:
            print('input 1~4')
            continue
'''

'''
class Node():
    def __init__(self):
        self.data = None
        self.link = None

#
node1 = Node()
node1.data = 'DaHyeon'
node2 = Node()
node2.data = 'JeongYeon'
node1.link = node2
node3 = Node()
node3.data = 'Tzuyu'
node2.link = node3
node4 = Node()
node4.data = 'Sana'
node3.link = node4
node5 = Node()
node5.data = 'JiHyo'
node4.link = node5

# newNode = Node()
# newNode.data = 'Mr.Jae'
# newNode.link = node2.link
# node2.link = newNode

node2.link = node3.link
del node3

head = node1
# print(head.data, end=' ') 
# print(head.link.data, end=' ')
# print(head.link.link.data, end=' ')
# print(head.link.link.link.data, end=' ')
# # print(head.link.link.link.link.data, end=' ')
# # print(head.link.link.link.link.link.data, end=' ')

current = head
print(current.data, end=' ')
while (current.link != None):
   current = current.link 
   print(current.data, end=' ')
'''

'''
#
class Node():
    def __init__(self):
        self.data,self.link = None,None
def printNodes(start):
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()
def insertNode(findData,insertData):
    global memory,head,current,pre
    if (findData == head.data):
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return 
    current = head
    while (current.link != None):
        pre = current
        current = current.link
        if (findData == current.data):
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    node =  Node()
    node.data = insertData
    current.link = node
    memory.append(node)
def deleteNode(deleteData):
    global memory, head, current, pre
    if (head.data == deleteData):
        current = head
        head = head.link
        del (current)
        return
    current = head
    while (current.link != None):
        pre = current
        current = current.link
        if (deleteData == current.data):
            pre.link = current.link
            del(current)
            return
    print('Not exist')
def findNode(fData):
    global memory, head, current, pre
    current = head
    if (current.data == fData):
        return current
    while (current.link != None):
        current = current.link
        if (current.data == fData):
            return current
    return Node()


#
memory, head,current,pre =[], None,None,None
dataArray = ['ung'+str(i) for i in range(1,8)]

#
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)
for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

# insertNode('ung2', 'sola')
# insertNode('Mr.Jae', 'MoonByul')
# deleteNode('ung1')
# deleteNode('ung3')
# printNodes(head)

findData = 'ung3'
fNode = findNode(findData)
print(f'{fNode.data} yes!')
'''