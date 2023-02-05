counter = 0
numsdict={}
numsdict["00"] = 7
numsdict["000"] = 8
numsdict["and"] = 3
numsdict[0] = 0
numsdict[1] = 3
numsdict[2] = 3
numsdict[3] = 5
numsdict[4] = 4
numsdict[5] = 4
numsdict[6] = 3
numsdict[7] = 5
numsdict[8] = 5
numsdict[9] = 4
numsdict[10] = 3
numsdict[11] = 6
numsdict[12] = 6
numsdict[13] = 8
numsdict[14] = 8
numsdict[15] = 7
numsdict[16] = 7
numsdict[17] = 9
numsdict[18] = 8
numsdict[19] = 8
numsdict[20] = 6
numsdict[30] = 6
numsdict[40] = 5
numsdict[50] = 5
numsdict[60] = 5
numsdict[70] = 7
numsdict[80] = 6
numsdict[90] = 6

#1 to 20
for hundreds in range(10):
    hundredshundreds = hundreds * 100
    if hundreds >0:
        numsdict[hundredshundreds] = numsdict[hundreds] + numsdict["00"]
        counter += numsdict[hundredshundreds]
        hndrd = numsdict[hundredshundreds] + numsdict["and"]
    else:
        hndrd = 0

    for i in range(1,20):
        counter+=hndrd + numsdict[i]

    for tens in range(2,10):
        tenstens = tens * 10

        #20 to 29
        for units in range(10):
            numsdict[tenstens+units] = numsdict[tenstens] + numsdict[units]
            counter +=hndrd + numsdict[tenstens+units]

counter +=numsdict[1] + numsdict["000"]
print(numsdict)
print(counter)