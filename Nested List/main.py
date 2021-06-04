if __name__ == '__main__':
    
    # N is number of students
    N = int(input())

    # templist will hold data of each student for short time
    tempList = [0,0]

    #this is the main list which is nested
    list1 = []

    #this is the list of name(s) that have required grade
    names = []
    # for loop to input data of students
    for i in range (0,N):
        
        tempList[0] = input().strip()   #name stores in 0th index of tempList
        tempList[1] = float(input().strip())   #grade is stored at 1st index

        list1.append(tempList)          #append the whole list as one item into main list
        
        tempList = [0,0]                #reset the tempList so the data isn't duplicated

    #extract the grades in a separate list  
    grades = []
    for j in range (0,N):
        grades.append(list1[j][1])
    
    grades.sort()   #sort the grades in reverse order

    # using for loop to find the second lowest grade since
    #the list is in reverse order the second lowest grade
    #will be on second index and if there are more than one
    #lowest value then "2nd lowest" will be on 3rd index or later

    for k in range (1,N):
        if grades[k] > grades[k-1]:
            secondLowest = grades[k]    #if second lowest is found hold it
            break
        else:
            continue

    #Since the second lowest is found now we have to find name(s) against it.

    for l in range (0,N):
        if list1[l][1] == secondLowest: #if this name has the required grade extract it
            names.append(list1[l][0])   #this is the list of required name(s)

    names.sort()    #sort the names alphabetically
    
    #loop to print all names in the list
    for m in range (0,len(names)):
        print(names[m]) 