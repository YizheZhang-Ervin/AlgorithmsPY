from DataStructure.stack import Stack
from DataStructure.tree.binarytree import BinaryTree, postordereval


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        # 如果是左括号，当前节点添加左子节点，新节点设为当前节点
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        # 如果是数字，赋值给当前节点，其父节点设为当前节点
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        # 如果是运算符，赋给当前节点，并给当前节点加右子节点，新节点设为当前节点
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        # 如果是右括号，父节点设为当前节点
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


if __name__ == '__main__':
    pt = buildParseTree("( ( 10 + 5 ) * 3 )")
    print(postordereval(pt))
