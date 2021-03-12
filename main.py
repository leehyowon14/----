#어절처리
def isin(t,a): #리스트 안 내용 검사(에러안나게하기위해 index사용 안함)
    if t in a:
        return True
    else:
        return False

nounf = open('noun.txt', 'r', encoding='UTF8')  #명사사전

data = nounf.readlines()
t = []
for line in data:
    t += line.split( )
#print(len(t))
#print(t)
nounf.close()

josahadaf = open('josahada.txt', 'r', encoding = 'UTF8') #조사, 용언사전
data = josahadaf.readlines()
jh = []
for line in data:
    jh += line.split( )
#print(len(jh))
#print(jh)
josahadaf.close()

sent = input('문장 입력:')
st = sent.split( )
#print(st)
n = len(st)
a = []
for k in range(0, n):
    if isin(st[k], t): #명사
        a.append(st[k])
    else:
        kn = len(st[k])
        for j in range(0, kn):
            if isin(st[k][:j], t) and isin(st[k][j:], jh): #명사 + 조사, 용언
                a.append(st[k][:j])
            elif isin(st[k][:j], t) and isin(st[k][j:], t): #명사 + 명사
                a.append(st[k][:j] + st[k][j:])

print(a)
