# Problem Link: https://leetcode.com/problems/min-stack/
class MinStack:

    def __init__(self):
        self.cont = []
        self.mins = []

    def push(self, val: int) -> None:
        if len(self.cont) == 0 or val < self.mins[-1]:
            self.cont.append(val)
            self.mins.append(val)
        else:
            self.cont.append(val)
            self.mins.append(self.mins[-1])

    def pop(self) -> None:
        del self.cont[-1]
        del self.mins[-1]

    def top(self) -> int:
        return self.cont[-1]

    def getMin(self) -> int:
        return self.mins[-1]


if __name__ == '__main__':
    st = MinStack()
    print(st.push(-2))
    print(st.push(0))
    print(st.push(-3))
    print(st.getMin())
    print(st.pop())
    print(st.top())
    print(st.getMin())
