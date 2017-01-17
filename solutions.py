# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import collections
def question1(s,t):
    len_s= len(s)
    len_t= len(t)
    Link_list_t = Linked_list(t[0])
    for i in range(1,len_t):
        Link_list_t.append(t[i])
    for i in range(len_s):
        for j in range(len_t):
            if s[i]==t[j]:
                output=check_ana(s[i:],Link_list_t)
                if output == 1:
                    return True
                else:
                    return False
        

def check_ana(s,t):
    len_s=len(s)
    for i in range(len_s):
        t.search_and_delete(s[i])
        if t.empty() == 1:
            return 1
    return 0

class Node(object):
    def __init__ (self,value):
        self.value = value
        self.next = None
class Linked_list(object):
    def __init__ (self,head):
        self.head= Node(head) 
        self.last = self.head
    def append(self,value):
        second_last = self.last
        second_last.next=Node(value)
        self.last= second_last.next
    def search_and_delete(self,search_term):
        current=self.head
        next_in_list=current.next
        if current.value==search_term:
            self.delete(None,current)
            print "head is same"
            self.print_list()
        else:
            while next_in_list != None:
                if (next_in_list.value == search_term):
                    """ error in this block. The idea is correct
                    but delete function is not reducing nodes even though it
                    written correctly. It is probably because we are not removing 
                    in the tree. Look how tree is implemented in udacity"""
                    self.delete(current,next_in_list) 
                    print "after_head"
                    self.print_list()
                else:
                    """ error in this block. The idea is correct
                    but delete function is not reducing nodes even though it
                    written correctly. It is probably because we are not removing 
                    in the tree. Look how tree is implemented in udacity"""
                    two_ahead_in_list = next_in_list.next
                    current = next_in_list
                    next_in_list=two_ahead_in_list
    def empty(self):
        if self.head==None:
            return 1
        else:
            return 0

    def delete(self,a,b):
        if a == None:
            """This block is working"""
            print "a none b value",b.value
            self.head = self.head.next
        elif b.next == None:
            """ error in this block. The idea is correct
            but delete function is not reducing nodes even though it
            written correctly. It is probably because we are not removing 
            in the tree. Look how tree is implemented in udacity"""
            print "B none a value",b.value
            self.last=a
            a.next=None
        else:
            """ error in this block. The idea is correct
            but delete function is not reducing nodes even though it
            written correctly. It is probably because we are not removing 
            in the tree. Look how tree is implemented in udacity"""
            print "within delete loop", a.value
            print "within delete loop", b.value
            a.next=b.next
    def print_list(self):
        print self.head.value," "
        first=self.head
        while first.next!=None:
            print first.next.value," "
            first=first.next

def question2(s):
    len_s = len(s)
    dict_pal=dict()
    for i in range(len_s):
        for j in range(i+1,len_s+1):
            reverse_str=reverse_string(s[i:j])
            if reverse_str == s[i:j]:
                if len(s[i:j]) not in dict_pal:
                    dict_pal[len(s[i:j])]=s[i:j]
    return dict_pal[max(dict_pal.keys(),key=int)]
def reverse_string(s):
    len_s=len(s)
    new_string=""
    for i in range(len_s):
        new_string +=s[len_s-i-1]
    return new_string

def question3(Graph):
    list_vnn=dict()
##    list_vnn[0]=[]
    for Node1 in Graph.keys():
##        list_vnn[0].append(Node1)
        for (Node2,weight) in Graph[Node1]:
            if weight not in list_vnn:
                list_vnn[weight]=[]
            list_vnn[weight].append((Node1,Node2))
    weight_descending_order=sorted(list_vnn.keys())
    minimum_spanning_tree=dict()
    for weights in weight_descending_order:
        for list_of_nodes in list_vnn[weights]:
            minimum_spanning_tree = minimum_spanning_tree_create(minimum_spanning_tree, list_of_nodes[0],list_of_nodes[1],weights)
    return minimum_spanning_tree.values()[0]

def minimum_spanning_tree_create(minimum_spanning_tree,vertice1,vertice2,weights):
    if not minimum_spanning_tree:
        minimum_spanning_tree={1:{vertice1:[(vertice2,weights)],vertice2:[(vertice1,weights)]}}
    else:
        tree1 =0
        tree2 =0
        for trees in minimum_spanning_tree.keys():
            for vertices in minimum_spanning_tree[trees]:
                if vertices == vertice1:
                    tree1 = trees
                if vertices == vertice2:
                    tree2 = trees
        if tree1 != tree2 :
            if tree1==0:
                minimum_spanning_tree[tree2][vertice2].append((vertice1,weights))                
                minimum_spanning_tree[tree2][vertice1] = [(vertice2,weights)]                
            elif tree2==0:
                minimum_spanning_tree[tree1][vertice1].append((vertice2,weights))                
                minimum_spanning_tree[tree1][vertice2] = [(vertice1,weights)]                
            else:                
                index = max(minimum_spanning_tree.keys())+1
                minimum_spanning_tree[index]= dict(minimum_spanning_tree[tree1].items() +minimum_spanning_tree[tree2].items())
                minimum_spanning_tree[index][vertice1].append((vertice2,weights))
                minimum_spanning_tree[index][vertice2].append((vertice2,weights))
                minimum_spanning_tree.pop(tree1)
                minimum_spanning_tree.pop(tree2)
        elif tree1 == 0 and tree2 == 0:
            index=max(minimum_spanning_tree.keys())+1
            minimum_spanning_tree[index]={vertice1:[(vertice2,weights)],vertice2:[(vertice1,weights)]}
    return minimum_spanning_tree
class Node1(object):
  def __init__(self, data):
    self.data = data
    self.next = None
def question5(ll,m):
    q = collections.deque(ll.data)
    n = ll.next
    while n != None:
        q.append(n.data)
        n=n.next
    for i in range(m-1):
        q.pop()
    return q.pop()
"""print question1("prateek","rp")"""
"""print question2("quasi")"""
Graph1 = {'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
Graph2 = {'A': [('B', 2)],
 'B': [('A', 2), ('C', 5),('E',4)], 
 'C': [('B', 5),('D',3)],
 'D': [('C',3),('E',2)],
  'E':[('F',7),('B',4)]}
def question4(T,r,n1,n2):
    return check_ancestor(T,r,n1,n2)

def check_ancestor(T,r,n1,n2):
    if (n1>r and r>n2) or (n1<r and r<n2):
        return r
    first_i = -1
    second_i = -1
    for i in len(T[r]):
        if T[r][i]==1 and first_i !=-1 and second_i !=1:
            first_i=i
        if T[r][i]==1 and first_i >-1 and second_i !=1:
            second_i=i
    if (n1>r and n2>r):
        return check_ancestor(T,second_i,n1,n2)
    if (n1<r and n2<r):
        return check_ancestor(T,first_i,n1,n2)

question3(Graph2)
a = Node1('a')
b = Node1('b')
a.next = b
c = Node1('c')
b.next = c
d = Node1('d')
c.next = d
e = Node1('e')
d.next = e
f = Node1('f')
e.next = f
g = Node1('g')
f.next = g
h = Node1('h')
g.next = h
i = Node1('i')
h.next = i
j = Node1('j')
i.next = j


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
print question5(a,3)
