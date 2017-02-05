# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import collections

print "############################# Question 1 #####################################################"

def question1(s,t):
    len_s=len(s) ## Finding the length of the string
    len_t=len(t) ## Finding the length of the anagram 
    for i in range(len_s-len_t+1): ### Searching on string till len(string)- len(anagram). This is done because we have to find the anagram of len(angaram)
        output = check_ana(s[i:],t) ## Function which gives if the anagram is not
        if output == True: ## The output is true then return true
            return True
    return False ## Return false if none of the output is true

def check_ana(s,t): ## Checks for anagram
    len_t = len(t) 
    ana_t=t
    for i in range(len_t): ## checks for string for only for length of anagram 
        done = 0
        for j in range(len_t-i):### it loops within the anagram
            if done==0: #### checks the for a single letter in string with single letter in anagram
                if s[i]==ana_t[j]: 
                    ana_t=ana_t.replace(s[i],'',1) #### If there is a match then as linklist it removes the them
                    done=1
    if ana_t=="":
        return True
    else:
        return False
    
print "Question1 s= prateek t=tar", question1('prateek','tar')
print "Question1 s= prateek t=eet", question1('prateek','eet')
print "Question1 s= prateek t=ra", question1('prateek','ra')

print "############################# Question 2 #####################################################"

def question2(s): ## Find if there are palindrome in the string
    len_s = len(s) ###Lenght of the string
    dict_pal=dict() ### Create a dictionary
    for i in range(len_s): #### For the length of the string
        for j in range(i+1,len_s+1): #### Finding all possible strings in the combination
            reverse_str=reverse_string(s[i:j]) ####  Finding a reverse string
            if reverse_str == s[i:j]: #### If there is a match 
                if len(s[i:j]) not in dict_pal: ### There is no other string of same size then 
                    dict_pal[len(s[i:j])]=s[i:j] #store it the dictionary
    return dict_pal[max(dict_pal.keys(),key=int)]  ### return the largest value in the dictionary
def reverse_string(s): ### This is the function to create a reverse string
    len_s=len(s)
    new_string=""
    for i in range(len_s):
        new_string +=s[len_s-i-1]
    return new_string

print question2("quasi")
print question2("abracadabra")
print question2("aba")

print "############################# Question 3 #####################################################"

def question3(Graph): ### Input a graph
    list_vnn=dict()  ### Create a dictionary
    for Node1 in Graph.keys(): ### This loop creates a dictionary of weights as key and nodes which it connects in a tuple in a list. 
        for (Node2,weight) in Graph[Node1]: 
            if weight not in list_vnn:
                list_vnn[weight]=[]
            list_vnn[weight].append((Node1,Node2))
    weight_descending_order=sorted(list_vnn.keys()) ### The keys are sorted in dictionary
    minimum_spanning_tree=dict() ## Empty dictionary for minimum spanning tree is created
    for weights in weight_descending_order: ## In reverse order with smallest weight node first, we select edges and start creating trees. Initially multiple trees are created but they get connected till the end to make one tree
        for list_of_nodes in list_vnn[weights]:
            minimum_spanning_tree = minimum_spanning_tree_create(minimum_spanning_tree, list_of_nodes[0],list_of_nodes[1],weights) ## Minimum spanning tree function 
    return minimum_spanning_tree.values()[0]

def minimum_spanning_tree_create(minimum_spanning_tree,vertice1,vertice2,weights): ## input to function is minimum_spanning_tree which gets added. It contains two nodes and the weight of the edge between the node
    if not minimum_spanning_tree: ### Create a minimum spanning tree if there is none and mark it with 1
        minimum_spanning_tree={1:{vertice1:[(vertice2,weights)],vertice2:[(vertice1,weights)]}}
    else:
        tree1 =0
        tree2 =0
        for trees in minimum_spanning_tree.keys(): ### We have to find two trees which have the node1 and node2. If there is only tree then we are creating a circular tree.
            for vertices in minimum_spanning_tree[trees]:
                if vertices == vertice1:
                    tree1 = trees
                if vertices == vertice2:
                    tree2 = trees
        if tree1 != tree2 : ## check If there are two trees with vertices then you it is not a circular tree
            if tree1==0: ## if one the tree is empty then create a tree 
                minimum_spanning_tree[tree2][vertice2].append((vertice1,weights))                
                minimum_spanning_tree[tree2][vertice1] = [(vertice2,weights)]                
            elif tree2==0:
                minimum_spanning_tree[tree1][vertice1].append((vertice2,weights))                
                minimum_spanning_tree[tree1][vertice2] = [(vertice1,weights)]                
            else: ## check if two different trees are found and the edge connects two trees then connect the trees and create one and store it. Remove the original tree
                index = max(minimum_spanning_tree.keys())+1
                minimum_spanning_tree[index]= dict(minimum_spanning_tree[tree1].items() +minimum_spanning_tree[tree2].items())
                minimum_spanning_tree[index][vertice1].append((vertice2,weights))
                minimum_spanning_tree[index][vertice2].append((vertice2,weights))
                minimum_spanning_tree.pop(tree1)
                minimum_spanning_tree.pop(tree2)
        elif tree1 == 0 and tree2 == 0: ## If there is no tree with the two nodes then create a new tree
            index=max(minimum_spanning_tree.keys())+1
            minimum_spanning_tree[index]={vertice1:[(vertice2,weights)],vertice2:[(vertice1,weights)]}
    return minimum_spanning_tree

Graph1 = {'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
Graph2 = {'A': [('B', 2)],
 'B': [('A', 2), ('C', 5),('E',4)], 
 'C': [('B', 5),('D',3)],
 'D': [('C',3),('E',2)],
  'E':[('F',7),('B',4)]}
Graph3 = {'A': [('B', 2)],
 'B': [('A', 2)]}

       
print question3(Graph1)
print question3(Graph2)
print question3(Graph3)

print "############################# Question 5 #####################################################"
    

class Node1(object):
    ### This class creates a element in link list.
  def __init__(self, data):
    self.data = data
    self.next = None
def question5(ll,m): ## This function finds the nth element from the end of the linked list.
    q = collections.deque(ll.data) ## This function puts the first element of the linked list in the queue
    n = ll.next  ## This function moves to the next element
    while n != None: ## Till we reach the last element
        q.append(n.data) ## We add elements in the queue 
        n=n.next ### We move on to the next element in the queue
    for i in range(m-1): ## This step is removing elements from the queue
        q.pop() 
    return q.pop() ## Return the nth element of the queue


a = Node1('a')
b = Node1('b')
h = Node1('h')
i = Node1('i')
j = Node1('j')
c = Node1('c')
d = Node1('d')
e = Node1('e')
f = Node1('f')
g = Node1('g')

a.next = f
f.next = g
h.next = i
i.next = j
b.next = c
c.next = d
d.next = e

print question5(a,3)
print question5(d,1)
print question5(h,2)


print "############################# Question 4 #####################################################"

def question4(T,r,n1,n2):  ## This function passes value to the check ancestor function
    return check_ancestor(T,r,n1,n2)

def check_ancestor(T,r,n1,n2):
    if (n1>r and r>n2) or (n1<r and r<n2): ## Checks for the condition which decides that r is the common ancestor
        return r ## Returns the value r
    first_i = -1 ## Setting first_i to a negative value. It is the left chld
    second_i = -1 ## Setting second_i to a negative value. It is the right child
    for i in len(T[r]):  ## These steps are to derive the left or the right child from the node r)
        if T[r][i]==1 and first_i !=-1 and second_i !=1:
            first_i=i
        if T[r][i]==1 and first_i >-1 and second_i !=1:
            second_i=i
    if (n1>r and n2>r): #checks for the condition for selecting the right child
        return check_ancestor(T,second_i,n1,n2)
    if (n1<r and n2<r): #checks for the condtion for selecting the left child.
        return check_ancestor(T,first_i,n1,n2)



z = [[0,1,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [1,0,0,0,1],
   [0,0,0,0,0]]

k = [[0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]]

print question4(z,3,4,1)
print question4(k,1,2,4)