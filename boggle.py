import numpy as np
bag_of_words = []

class Tree(object):
    def __init__(self, char):
        self.char = char
        self.children = []
        self.word_finish = False
        self.counter = 1
        
root = Tree('*')

def add(root, word):
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = Tree(char)
            node.children.append(new_node)
            node = new_node
    node.word_finish = True

def find(root, prefix):
    node = root
    if not root.children:
        return False , 0, False
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return False, 0, False
    return True, node.counter, node.word_finish

def isword(string):
    global root
    ###Tree Searching###
    _,counter,answer = find(root,string)
    return counter>1,answer
    ##Linear Searching###
    # for word in dictionary:
    #     if(string==word):
    #         return True
    # return False

def find_word_from(board, visited, a, b, string):
    global bag_of_words
    visited[a][b]=1
    n,m = board.shape
    string += board[a][b]
    counter, answer = isword(string.lower())
    if answer:
        bag_of_words.append(string)
    if counter:
        for row in range(a-1,a+2):
            for col in range(b-1, b+2):
                if(row>=0 and col>=0 and row < n and col < m):
                    if(visited[row][col]==0):
                        
                        find_word_from(board, np.copy(visited), row, col, string)


def findWords(board):
    global dictionary, bag_of_words
    n,m = board.shape
    string = ""
    for i in range(0,n):
        for j in range(0,m):
            find_word_from(board, np.zeros((n,m)), i, j, string)
    return np.asarray(bag_of_words)

if __name__ == "__main__":
    input_ = input("Enter Boogle Board String:  ")
    boogle_board = np.asarray([x.strip() for x in input_.split(",")])
    # boogle_board = np.asarray(["A", "C", "E", "D", "L", "U", "G", "I", "E", "F", "H", "T", "G", "A", "F", "K"])
    boogle_board = np.reshape(boogle_board, (4,4))
    dictionary = np.asarray(str(open("dictionary.txt","r").read()).split("\n"))
    for word in dictionary:
        add(root, word.lower())
    print("Boogle Board : ")
    print(boogle_board)
    print("\nList of Words:")
    print(findWords(boogle_board))