# #tri selection
# a=[9, 8, 7, 6, 5, 4]
# for i in range(0,len(a)-1):
#     min=i
#     for j in range(i+1,len(a)):
#         if a[min]>a[j]:
#             min=j
#     if a[i]>a[min]:
#         a[i],a[min]=a[min],a[i]
# print(a)
# #tri de boule
# a=[9, 8, 7, 6, 5, 4]
# b=True
# while b:
#     b=False
#     for i in range(0,len(a)-1):
#         if a[i]>a[i+1]:
#             a[i],a[i+1]=a[i+1],a[i]
#             b=True
# print(a)
# #merge_sort
# def fusion(l1,l2):
#     if l1==[]:
#         return l2
#     if l2==[]:
#         return l1
#     if l1[0]<l2[0]:
#         return [l1[0]]+fusion(l1[1::],l2)
#     else:
#         return [l2[0]]+fusion(l1,l2[1::])
# def tri(tab):
#     if len(tab)<=1:
#         return tab
#
#     tab1=[tab[i] for i in range(len(tab)//2)]
#     tab2=[tab[i] for i in range(len(tab)//2,len(tab))]
#     return fusion(tri(tab1),tri(tab2))
# print(tri([9, 8, 7, 6, 5, 4]))
# #quick sort
# def quick_sort(l):
#     if l==[]:
#         return []
#     else:
#         n=len(l)
#         l1=[]
#         l2=[]
#         for i in range(1,n):
#             if l[i]<=l[0]:
#                 l1.append(l[i])
#             else:
#                 l2.append(l[i])
#     return quick_sort(l1)+[l[0]]+quick_sort(l2)
#
# print(quick_sort([9, 8, 7, 6, 5, 4]))
# #insertion tri
# a=[9, 8, 7, 6, 5, 4]
# for i in range(0,len(a)):
#     b=a[i]
#     j=i
#     while (j>0 and a[j-1]>b):
#         a[j]=a[j-1]
#         j=j-1
#     a[j]=b
# print(a)

