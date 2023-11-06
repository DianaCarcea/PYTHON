# Ex1 - simulates a Stack
class Stack:
    def __init__(self):
        self._elems = []
        self._vf = 0

    def push(self, elem):
        self._elems.append(elem)
        self._vf += 1

    def pop(self):
        if self._vf != 0:
            self._vf -= 1
            val = self._elems[self._vf]
            self._elems = self._elems[:-1]
            return val
        else:
            return None

    def peek(self):
        if self._vf != 0:
            return self._elems[self._vf - 1]
        else:
            return None

    def is_empty(self):
        return self._vf == 0

    def size(self):
        return self._vf

    def clear(self):
        self._elems = []
        self._vf = 0

    def __getitem__(self, index):
        if 0 <= index < len(self._elems):
            return self._elems[index]
        else:
            raise IndexError("Index in afara intervalului!")

    def __str__(self):
        return f"MyStack: {self._elems}"

    def __repr__(self):
        return f"MyStack({self._elems})"


# Ex2 - simulates a Queue
class Queue:
    def __init__(self):
        self._elems = []
        self._front = 0
        self._rear = 0

    def push(self, elem):
        self._elems.append(elem)
        self._rear += 1

    def pop(self):
        if self._front != self._rear:
            val = self._elems[self._front]
            self._front += 1
            return val
        else:
            return None

    def peek(self):
        if self._front != self._rear:
            return self._elems[self._front]
        else:
            return None

    def peek_last(self):
        if self._front != self._rear:
            return self._elems[self._rear]
        else:
            return None

    def is_empty(self):
        return self._front == self._rear

    def size(self):
        return self._rear - self._front

    def clear(self):
        self._elems = []
        self._front = 0
        self._rear = 0

    def __getitem__(self, index):
        if 0 <= index < self.size():
            return self._elems[self._front + index]
        else:
            raise IndexError("Index in afara intervalului!")

    def __str__(self):
        return f"MyQueue: {self._elems[self._front:self._rear]}"

    def __repr__(self):
        return f"MyQueue({self._elems[self._front:self._rear]})"


# Ex3 - simulates a Matrix
class Matrix:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._elems = [[0] * cols for _ in range(rows)]

    def get_elems(self, i, j):
        if i in range(self._rows) and j in range(self._cols):
            return self._elems[i][j]
        else:
            raise IndexError("Index in afara intervalului!")

    def get_rows(self):
        return self._rows

    def get_cols(self):
        return self._cols

    def set(self, i, j, val):
        if i in range(self._rows) and j in range(self._cols):
            self._elems[i][j] = val
        else:
            raise IndexError("Index in afara intervalului!")

    def transpose(self):
        matrix_trans = Matrix(self._cols, self._rows)
        for i in range(self._rows):
            for j in range(self._cols):
                matrix_trans._elems[j][i] = self._elems[i][j]

        return matrix_trans

    def multiply(self, matrix2):
        if self._cols != matrix2.get_rows():
            raise ValueError("Dimensiuni incompatibile pentru inmultirea matricelor!")

        result = Matrix(self._rows, matrix2.get_cols())
        for i in range(self._rows):
            for j in range(matrix2.get_cols()):
                for k in range(self._cols):
                    result._elems[i][j] += self._elems[i][k] * matrix2.get_elems(k, j)

        return result

    def addition(self, matrix2):
        if self._rows != matrix2.get_rows() or self._cols != matrix2.get_cols():
            raise ValueError("Dimensiuni incompatibile pentru adunarea matricelor!")

        result = Matrix(self._rows, self._cols)
        for i in range(self._rows):
            for j in range(self._cols):
                result._elems[i][j] = self._elems[i][j] + matrix2.get_elems(i, j)
        return result

    def op_transform(self, func_lambda):
        for i in range(self._rows):
            for j in range(self._cols):
                try:
                    self._elems[i][j] = func_lambda(self._elems[i][j])
                except Exception as e:
                    print(f"S-a întâlnit excepția: {e}")

    def __str__(self):
        result = ""
        for i in range(self._rows):
            for j in range(self._cols):
                result += str(self._elems[i][j]) + " "
            result += "\n"
        return result


if __name__ == '__main__':
    # Ex1
    print("\n-------------Ex1--------------")
    stack = Stack()
    stack.push(2)
    stack.push(4)
    stack.push(6)
    print(stack)

    print("Peek:", stack.peek())
    elem_stack = 8
    stack.push(elem_stack)
    print("Push:", elem_stack)
    print(stack)
    print("Pop:", stack.pop())
    print(stack)

    for index in range(stack.size()):
        print(f"Elementul {index}:", stack[index])

    #Ex2
    print("\n-------------Ex2--------------")
    queue = Queue()
    queue.push(1)
    queue.push(3)
    queue.push(5)

    print(queue)
    print("Peek:", queue.peek())
    elem_queue = 7
    queue.push(elem_queue)
    print("Push:", elem_queue)
    print(queue)
    print("Pop:", queue.pop())
    print(queue)

    for index in range(queue.size()):
        print(f"Elementul {index}:", queue[index])

    #Ex3
    print("\n-------------Ex3--------------")
    matrix = Matrix(2, 3)

    matrix.set(0, 0, 1)
    matrix.set(0, 1, 2)
    matrix.set(0, 2, 3)

    matrix.set(1, 0, 4)
    matrix.set(1, 1, 5)
    matrix.set(1, 2, 6)

    print("Matrix:")
    print(matrix)

    matrix_trans = matrix.transpose()
    print("Matrix transpose:")
    print(matrix_trans)

    print("Multiplying the matrix by the transpose:")
    result = matrix.multiply(matrix_trans)
    print(result)

    matrix2 = Matrix(2, 3)

    matrix2.set(0, 0, 1)
    matrix2.set(0, 1, 2)
    matrix2.set(0, 2, 3)

    matrix2.set(1, 0, 4)
    matrix2.set(1, 1, 5)
    matrix2.set(1, 2, 6)

    print("Adding the matrix to the matrix2:")
    result = matrix.addition(matrix2)
    print(result)

    print("Modification of elements:")
    matrix.op_transform(lambda e: e*5)
    print(matrix)
