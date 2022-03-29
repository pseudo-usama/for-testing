names = ['ahmad', 'asif' , 'faisell' , 'kazmi']
names = ['shamsuddin', 'shams', 'zia']

def isSorted(names):
    return all(names[i] < names[i+1] for i in range(len(names)-1))

print(isSorted(names))

