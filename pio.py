def printPostorder(start, end, preorder, pIndex, d):
    if start > end:
        return pIndex
    value = preorder[pIndex]
    pIndex = pIndex + 1
    if start == end:
        print(value, end=' ')
        return pIndex
    i = d[value]
    pIndex = printPostorder(start, i - 1, preorder, pIndex, d)
    pIndex = printPostorder(i + 1, end, preorder, pIndex, d)
    print(value, end=' ')
    return pIndex
def findPostorder(inorder, preorder):
    d = {}
    for i, e in enumerate(inorder):
        d[e] = i
    pIndex = 0
    print('Postorder traversal is ', end='')
    printPostorder(0, len(inorder) - 1, preorder, pIndex, d) 
inorder = [4, 2, 1, 7, 5, 8, 3, 6]
preorder = [1, 2, 4, 3, 5, 7, 8, 6]
findPostorder(inorder, preorder)
