#!/usr/bin/env python
# Author Rishab Shah rishah@bu.edu
# Author Prateek Mehta pmehta59@bu.edu

import sys,re
import json
    
    
while(1):
    #f = open ( 'puzzles.txt' , 'r')
    #l = (f.read().split("\n") )
    #print(len(l))
    #count = 0
    #print('this is sparta',argvv[1])\
    try:
        l=input()
        list_mat = [""]
        #print(i)
        words = json.loads(l)['grid']
        
        for j in words:
            list_mat.append(j)
        
        list_mat.append(','.join(str(x) for x in json.loads(l)['lengths']))
#        print(list_mat)
        argvv=list_mat.copy()
        #            print (list_mat)
        
        #argvv = ['','LA','ST','4']
        #argvv = ['',"hos", "equ", "era",'3,6']
        #argvv = ['',"yeho", "slnl", "onca", "nnab",'5,5,6']
        #argvv = ['','vanmo','ipveo','toarr','tsmed','miipb','4,7,7,7']
        #argvv = ['','OIHOYEDH','MSOTTTKO','DEPSPCTA','RSOGICOR', 'ACPNRRSP','OBLRAEOA','PBLOATIN','CULCIHCT','8,4,6,7,6,6,5,4,5,8,5']
        
        
        #clock = time.clock if sys.platform == 'win32' else time.time
        
        #allgrids = {}
        gridsolutions = {}
        
        #
        # Temporary test function.
#        #
#        def trim_dictionary2(length,grid):
#            jgrid = ''.join(grid).replace(' ','')
#            dictionaries[length] = []
#        
#            c1 = [0]*26
#            for i in range(len(jgrid)):
#                pos = ord(jgrid[i])-ord('A')
#                c1[pos] = c1[pos] + 1
#        
#            for k in range(len(fulldictionary[length])):
#                c2 = [0]*26
#                for i in range(length):
#                    pos = ord(fulldictionary[length][k][i])-ord('A')
#                    c2[pos] = c2[pos] + 1
#        
#                j = 0
#                stillOK = True
#                while j<26 and stillOK:
#                    if c2[j]<=c2[j]:
#                        j = j + 1
#                    else:
#                        stillOK = False
#        
#                if stillOK:
#                    dictionaries[length].append(fulldictionary[length][k])
#        
#        
#        #
#        # Temporary test function.
#        #
#        def trim_dictionary(length,grid):
#            alphabet = "".join([x for x in set("".join(grid)) if x!=" "])
#            usable = re.compile('[' + alphabet + ']{%d,}$' % length, re.I).match
#            dictionaries[length] = [x for x in fulldictionary[length] if usable(x)]
#        
        
        #
        # Save the dictionary into a tree structure.
        #
        def plant_word_tree(dictionary):
            tree = {}
            for word in dictionary:
                branch = tree
                for letter in word:
                    if letter not in branch:
                        branch[letter] = {}
                    branch = branch[letter]
            return tree
        
        
        #
        # Find word number 'iword' in the current grid.
        #
        def find_word1d(iword,grid1d,nrow,ncol):
        #    trim_dictionary2(lengths[iword],grid)
        #    refgrids[iword] = grid1d
            if grid1d in gridsolutions:
                return gridsolutions[grid1d]
            else:
                onesolutions = {}
                gridsolutions[grid1d] = {}
                for i0 in range(nrow*ncol):
                    if grid1d[i0]==" ":
                        continue
                    newsolutions = gridwalk1d(i0,grid1d,nrow,ncol,grid1d[i0],((i0),),iword,tree[lengths[iword]][grid1d[i0]])
                    #print(grid1d)
                    onesolutions = merge_dicts(onesolutions,newsolutions)
                    for key in newsolutions:
        #                onesolutions[key] = newsolutions[key]
                        gridsolutions[grid1d][key] = newsolutions[key]
        #            print iword,i0,grid1d
        #            print mysolution
        #            print
        #            solution[iword] = "."*lengths[iword]
                return onesolutions
        
        
        #
        # Walk through the grid starting from i0 and look for matching words
        # of the right length.
        #
        #@profile
        def gridwalk1d(i0,grid1d,nrow,ncol,start,visited,iword,branch):
        #    print "\r"+"-".join(solution),
            onesolution = {}
            for i in neighbors1d[i0]:
        #        if i in visited or grid1d[i]==" ":
        #        if i in visited or grid1d[i] not in branch:
        #            continue
        #
                if grid1d[i] in branch and i not in visited:
                    word = start + grid1d[i]
                    if len(word) == lengths[iword]:
        #
        # Good! We have an exact match for the desired word length. Save it as
        # intermediate solution. If this is the last word we need, then append the
        # intermediate solution to the global list of solutions.
        #
        
        #
        # Problem here: for a given grid, if there are two or more ways to form the
        # same word, only the last one gets saved in the onesolution dict. This is not
        # good if an earlier way leads to a possible solution.
        #
                        if word not in onesolution:
                            onesolution[word] = {}
        #                onesolution[word+"%02d" % i] = {}
                        solution[iword] = word
                        if iword==len(lengths)-1:
                            jsolution = " ".join(solution)
        #                    for refgrid in refgrids:
        #                        if jsolution not in allgrids[refgrid]:
        #                            allgrids[refgrid].append(jsolution)
                            if jsolution not in jsolutions:
                                solutions.append(list(solution))
                                jsolutions.append(jsolution)
#                                print(jsolution)
        #
        # If this is not the last word, then update the grid and look for the next word.
        # Afterwards, resume with the original grid.
        #
                        if iword < len(lengths)-1:
                            oldgrid1d = grid1d
                            grid1d = update_grid1d(grid1d,nrow,ncol,visited+((i),))
        #                    if grid1d in allgrids:
        #                        allgrids[grid1d] = allgrids[grid1d]+1
        ##                        aap = 1
        ##                        if len(allgrids[grid1d])>0:
        ##                            print grid1d,allgrids[grid1d][0]
        ##                            print grid1d,(allgrids[grid1d][0].split("-"))[iword+1]
        #                    else:
        #                        allgrids[grid1d] = 1
        ##                        allgrids[grid1d] = []
        ##                    print grid1d[i]
                            onesolution[word] = merge_dicts(onesolution[word],find_word1d(iword+1,grid1d,nrow,ncol))
                            grid1d = oldgrid1d
        #                    trim_dictionary2(lengths[iword],grid)
        #
        # If we found a partial match, then continue looking for a match of the desired
        # word length.
        #
                    else:
                        newsolution = gridwalk1d(i,grid1d,nrow,ncol,word,visited+((i),),iword,branch[grid1d[i]])
                        onesolution = merge_dicts(onesolution,newsolution)
        #                if "VAMPIRES" in newsolution and "VAMPIRES" in onesolution:
        #                    aap=1
        #                for key in newsolution:
        #                    onesolution[key] = newsolution[key]
        #
        # End of function.
        #
            return onesolution
        
        
        #
        # Update the grid: replace the letters from the most recent match with spaces,
        # and allow the remaining letters to settle to the bottom of the grid.
        #
        def update_grid1d(grid1d,nrow,ncol,visited):
            for i in visited:
                grid1d = grid1d[:i]+" "+grid1d[i+1:]
            grid2d = [[letter for letter in row] for row in re.findall(".{%d}"%ncol,grid1d)]
            for icol in range(ncol):
                column = "".join([grid2d[irow][icol] for irow in range(nrow-1,-1,-1)])
                column = column.replace(" ","")
                column = column + " "*(nrow-len(column))
                for irow in range(nrow):
                    grid2d[irow][icol] = column[nrow-1-irow]
            return "".join(["".join(row) for row in grid2d])
        
        
        #
        # Create an array of neighbors for each grid cell.
        #
        def make_neighbors1d(grid1d,nrow,ncol):
            neighbors1d = [[] for letter in grid1d]
            for i in range(nrow*ncol):
                irow = i//ncol
                icol = i%ncol
                if icol<ncol-1:
                    neighbors1d[i].append(i+1) #right
                    if irow>0:
                        neighbors1d[i].append(i-ncol+1) #right up
                    if irow<nrow-1:
                        neighbors1d[i].append(i+ncol+1) #right down
                if icol>0:
                    neighbors1d[i].append(i-1) #left
                    if irow>0:
                        neighbors1d[i].append(i-ncol-1) #left up
                    if irow<nrow-1:
                        neighbors1d[i].append(i+ncol-1) #left down
                if irow>0:
                    neighbors1d[i].append(i-ncol) #up
                if irow<nrow-1:
                    neighbors1d[i].append(i+ncol) #down
            return neighbors1d
        
        
        def merge_dicts(a, b, path=None):
            "merges b into a"
            if path is None: path = []
            for key in b:
                if key in a:
                    if isinstance(a[key], dict) and isinstance(b[key], dict):
                        merge_dicts(a[key], b[key], path + [str(key)])
                    elif a[key] == b[key]:
                        pass # same leaf value
#                    else:
#                        raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
                else:
                    a[key] = b[key]
            return a
        
        
        def myprint(d,i,max,prefix):
            for k, v in d.items():
                if i==max:
#                    if max>1:
                    print(prefix+" "+k)
#                    else:
#                        print(prefix+k)
                elif len(v)>0:
                    if i==1:
                        foo = k
                    else:
                        foo = prefix+" "+k
                    myprint(v,i+1,max,foo)
        
        
        #
        # Main function. Read the grid and word lengths either from command-line
        # arguments or ask the user to supply the information.
        #
        #print()
        #print("========================")
        #print("    WORDBRAIN SOLVER")
        #print()
        #print("     by Ruud Visser")
        #print(" <ruudvisser@gmail.com>")
        #print("========================")
        #print()
        grid = []
        narg = len(argvv)
        if narg > 1 and not argvv[1].isdigit():
            for i in range(1,narg):
                if argvv[i][0].isdigit():
                    nrow = i-1
                    break
            grid = [row for row in argvv[1:nrow+1]]
            list_p = []
            j=0
            while j<len(grid[0]):
                for i in grid:
                    list_p.append(i[j])
                j+=1
                
            ncol = len(grid[0])
            lengths = [int(x) for x in re.findall("\w",argvv[nrow+1])]
#        else:
#            print("Please enter the grid (one line of letters per row)")
#            print("followed by the requested word lengths.")
#            print()
#            print("For example:")
#            print("LSE\nLID\nLOD\n4,5")
#            print()
#            while True:
#                foo = input()
#                if not foo[0].isdigit():
#                    grid.append(foo)
#                else:
#                    ncol = len(grid[0])
#                    nrow = len(grid)
#                    lengths = [int(x) for x in re.findall("\w",foo)]
#                    break
        nwords = len(lengths)
        grid1d = ''.join(list_p)
        
        #refgrids = ["."*(ncol*nrow) for length in lengths]
        #
        # Run some basic sanity checks.
        #
        for row in grid:
            if len(row) != ncol:
                print("ERROR: all rows must have the same number of letters")
                sys.exit()
        if sum(lengths) != nrow*ncol:
            print("ERROR: sum of word lengths inconsistent with grid size")
            print("       %d %d" % (sum(lengths),nrow*ncol))
            sys.exit()
        if sum(lengths) == 1:
            print("ERROR: the grid must contain at least two letters")
            sys.exit()
        #
        # Create an array of neighbors for each grid cell.
        #
        neighbors1d = make_neighbors1d(grid1d,nrow,ncol)
        #
        # Print introductory message.
        #
#        print(" "+" "*(ncol+2))
#        for row in grid:
#            print("| "+row+" |")
#        print(" "+" "*(ncol+2))
#        print()
        #
#        foo = '' if nwords==1 else 's'
#        print("Looking for %d word%s with the following letter count%s: " % (nwords,foo,foo))
#        print(" ".join(["%d" % i for i in lengths]))
#        print("\nPossible solutions:")
        #print
        #foo = ""
        #for i in range(nwords):
        #    for j in range(lengths[i]):
        #        foo = foo+"%d" % (j+1)
        #    if i<nwords-1:
        #        foo = foo+" "
        #print foo
        #
        # Read in the English dictionary generated at http://dictionary.aspell.net.
        # Split the list into sublists according to word length.
        #
        maxlength = 8
        with open('large_word_list.txt') as file:
            data = [line.strip('\n') for line in file]
        data[:]=[x for x in data if x != '']
        fulldictionary = [line.strip() for line in data if line[0] != "#"]
        fulldictionary.sort()
        dictionaries = [sorted([line.strip() for line in data if line[0] != "#" and len(line)==length]) for length in range(maxlength+1)]
        #dictionaries = [[] for length in range(maxlength+1)]
        #
        tree = []
        for dictionary in dictionaries:
            tree.append(plant_word_tree(dictionary))
        #
        # Solve the puzzle.
        #
        solution = ["" for length in lengths]
        #solution = ["."*length for length in lengths]
        solutions = []
        jsolutions = []
        #allgrids[grid1d] = []
        #find_word(0,grid)
        #start_time = clock()
        globalsolution = find_word1d(0,grid1d,nrow,ncol)
#        gs = globalsolution
        #elapsed_time = clock() - start_time
        #
        # Print the results.
        #
        #print("\nElapsed time: %d seconds" % elapsed_time)
#        print()
#        if False:
#            if len(solutions)==0:
#                print("Sorry, no solutions found. This can have several reasons:")
#                print("   1. there is a typo in the input you provided;")
#                print("   2. the dictionary used by this solver is incomplete;")
#                print("or 3. there is a bug in this solver.")
#                print("If you think the problem is #2 or #3, then please contact")
#                print("the author at ruudvisser@gmail.com")
#            else:
##                foo = '' if len(solutions)==1 else 's'
##                print('Found %d possible solution%s:' % (len(solutions),foo))
#                for solution in solutions:
#                    print('   '.join(solution))
#                print('.')
#        else:
        myprint(globalsolution,1,len(lengths),"")
        print('.')
    except:
        sys.exit(0)