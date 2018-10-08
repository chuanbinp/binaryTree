#importing dependencies
import random

#functions related to binary tree
def randomBinaryTreeGenerator(maxCount):
    maxCounter = maxCount-1
    if maxCounter == 0:
        childNode1 = random.randint(0,9)
        parentNode = random.randint(0,9)
        childNode2 = random.randint(0,9)

        return [[childNode1],parentNode,[childNode2]]

    else:
        childNode1 = randomBinaryTreeGenerator(maxCount-1)
        childNode2 = randomBinaryTreeGenerator(maxCount-1)
        parentNode = random.randint(0,9)

        return [childNode1,parentNode,childNode2]

def numOfNodes(t):
    if len(t) == 1:
        return 1
    else:
        numOfLeftNodes = numOfNodes(t[0])
        numOfRightNodes = numOfNodes(t[2])
        return numOfLeftNodes + numOfRightNodes + 1

def sumOfNodes(t):
    if len(t) == 1:
        return t[0]
    else:
        parentNode = t[1]
        sumOfLeftNodes = sumOfNodes(t[0])
        sumOfRightNodes = sumOfNodes(t[2])
        return parentNode + sumOfLeftNodes + sumOfRightNodes

def maxNode(t):
    if len(t) == 1:
        return t[0]
    else:
        parentNode = t[1]
        maxLeftNode = maxNode(t[0])
        maxRightNode = maxNode(t[2])

        maxVal = parentNode
        if maxLeftNode > maxVal:
            maxVal = maxLeftNode
        if maxRightNode > maxVal:
            maxVal = maxRightNode

        return maxVal

def minNode(t):
    if len(t) == 1:
        return t[0]
    else:
        parentNode = t[1]
        minLeftNode = minNode(t[0])
        minRightNode = minNode(t[2])

        minVal = parentNode
        if minLeftNode < minVal:
            minVal = minLeftNode
        if minRightNode < minVal:
            minVal = minRightNode

        return minVal

def mirror(t):
    if len(t) == 1:
        return t[0]
    else:
        parentNode = t[1]
        leftNode = mirror(t[0])
        rightNode = mirror(t[2])

        return [rightNode, parentNode, leftNode]

def printTree(t, lvl):
    if len(t) == 1:
        print("  " * lvl, t[0])
    else:
        printTree(t[2], lvl+1)

        parentNode = t[1]
        print("  " * lvl, parentNode)

        printTree(t[0], lvl+1)

#Get user input for number of levels of binary tree
noOfTry = 0
treeLevels_str = input("How many levels do you want your binary tree to have?")
while noOfTry < 2:
    if treeLevels_str.isdigit():
        treeLevels_int = int(treeLevels_str)
        break
    else:
        print("Please enter an integer.")
        noOfTry+=1
        treeLevels_str = input("How many levels do you want your binary tree to have?")
else:
    print("Too many tries! BYE BYE...")

#Generate binary tree and call functions above
if treeLevels_int != None:
    tree = randomBinaryTreeGenerator(treeLevels_int)
    print("Random Binary Tree Generated in list form:", tree)
    print("Which looks like: ")
    printTree(tree,2)
    print("Number of Nodes: ", numOfNodes(tree))
    print("Highest Node is: ", maxNode(tree))
    print("Lowest Node is: ", minNode(tree))
    print("Sum of all Nodes is: ", sumOfNodes(tree))
    print("Mirror of this Tree: ", mirror(tree))
