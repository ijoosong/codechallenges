
#assuming that we read in the file and separated out each line into an array of lines
#for example: li = ["yahoo,ap42", "google,ap42", ....etc]

def affinity(li):
#in case you don't want to make a li, just erase li above and uncomment li below
#    li = ['yahoo,ap42', 'google,ap42', 'twitter,th174', 'google,aa314', 'yahoo,aa314', 'google,ap42', 'google,th174', 'yahoo,ai123', 'twitter,ai123', 'google,tt878']
    dictionary = {}
    for pageView in li:
        site,userId = pageView.split(',')
        if site not in dictionary:
            dictionary[site] = [userId]
        elif userId not in dictionary[site]:
            dictionary[site].append(userId)
    finalLi = []
    for key in dictionary:
        finalLi.append({key:dictionary[key]})

    #assume there is a highest affinity
    aff = [0, '', '']
    print finalLi
    for i in range(len(finalLi)):
        for j in range(i+1,len(finalLi)):
            count = 0
            [(ki,vi)] = finalLi[i].items()
            [(kj,vj)] = finalLi[j].items()
            for value in vi:
                if value in vj:
                    count += 1
            if count > aff[0]:
                aff[0],aff[1],aff[2] = count,ki,kj
    return aff[1:]
