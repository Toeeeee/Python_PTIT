p=[0]*100005
r=[0]*100005
for i in range(100005):
	p[i]=i 
	r[i]=0
def tim(x):
	if p[x]!=x: p[x]=tim(p[x])
	return p[x]
def join(a,b):
	a=tim(a)
	b=tim(b)
	if a==b: return
	if r[a]==r[b]: r[a]+=1
	if r[a]<r[b]: p[a]=b
	else: p[b]=a
t=int(input())
while t>0:
	t-=1
	a,b,c=[int(i) for i in input().split()]
	if c==1: join(a,b)
	else:
		a=tim(a)
		b=tim(b)
		if a==b:
			print(1)
		else: print(0)