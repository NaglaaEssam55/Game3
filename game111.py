lst=[1,2,3,4,5,6,7,8,9]
sum1=0
sum2=0
nums1=[]
nums2=[]
for i in lst:
    x=int(input("Enter Player1:"))
    while x<=0 or x>9 or lst[x-1]==-1:
            x=int(input('Enter player1:'))
           
    nums1.append(x)     
    lst[(x)-1]=(-1)
    print (lst)
    if len(nums1)==3:
        sum1=nums1[0]+nums1[1]+nums1[2]
        if sum1==15 : 
            print("player1 is winner")
            break
    if len(nums1)==4:
        sum1=nums1[0]+nums1[1]+nums1[2]
        sum11=nums1[0]+nums1[1]+nums1[3]
        sum111=nums1[1]+nums1[2]+nums1[3]
        sum1111=nums1[0]+nums1[2]+nums1[3]
        if sum1==15 or sum11==15 or sum111==15 or sum1111==15:
            print ("player1 is winner")
            break
    if len(nums1)==5:
        sum1=nums1[2]+nums1[3]+nums1[4]
        sum11=nums1[0]+nums1[3]+nums1[4]
        sum111=nums1[1]+nums1[3]+nums1[4]
        sum1111=nums1[1]+nums1[2]+nums1[4]
        if sum1==15 or sum11==15 or sum111==15 or sum1111==15:
            print ("player1 is winner")
            break
        else : 
           print("draw")
           break 
    y=int(input("Enter player2:"))
    while y<=0 or y>9 or lst[y-1]==-1:
            y=int (input("Enter player2:"))      
    nums2.append(y)
    lst[(y)-1]=(-1)
    print (lst)
    if len(nums2)==3:
        sum2=nums2[0]+nums2[1]+nums2[2]
        if sum2==15:
            print ("player2 is winner")
            break
    if len(nums2)==4:
        sum2=nums2[0]+nums2[1]+nums2[2]
        sum22=nums2[0]+nums2[1]+nums2[3]
        sum222=nums2[1]+nums2[2]+nums2[3]
        sum2222=nums2[0]+nums2[2]+nums2[3]          
        if sum2==15 or sum22==15 or sum222==15 or sum2222==15:
            print ("player2 is winner")
            break
      
  
