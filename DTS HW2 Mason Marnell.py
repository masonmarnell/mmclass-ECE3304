#Homework 2 - Mason Marnell

# Works with any combination of array lengths.
# The numbers from the lecture example were used here since the method of input wasn't specified.


f = [1,3,6,8,2,5,9]
g = [2,5,4,3,1,6,3]

def convolution(f1, g1):
    out = []
    tempreset = []
    multiplytemp = []
    for y in range(0, (len(f1)+len(g1)-1)):
        out.append(0) # I found out that ^ always gives the right length of the array
        tempreset.append(0)
    for z1 in range(0,len(f1)): #Iterator for multiplying through.
        multiplytemp = tempreset[:] #Finally figured out the colon is how you set entire arrays equal.
        for z1a in range(0, len(g1)): #The array g is multiplied by a single index of f.
            multiplytemp[z1a+z1] = g1[z1a]*f1[z1]
        for z1b in range(0, len(g1)): #The final array is procedurally set to the temp array in the correct spot.
            out[z1b+z1] = out[z1b+z1] + multiplytemp[z1b+z1]
        #print(out)

    print(out)


convolution(f, g)