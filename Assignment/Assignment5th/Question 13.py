class numbers():
    l1=[1,6,2,7,8,3,7,6,1]
    l2=[5,2,2,6,4,9,3]
    unionlist=[]
    def union12(self):
        for i in range(0,len(self.l1)):
            unionlist = []
            for j in range (0,len(self.l2)):
                if self.l1[i]!=self.l2[j]:
                    (self.unionlist).append(self.l1[i])
        print(unionlist)
   #  #find the union of two list
   #  u=l1.union(l2)
   #  print('Union of the set is:',u)
   #  #find intersection of two list
   #  i=l1.intersection(l2)
   #  print('intersection of the list is:',i)

