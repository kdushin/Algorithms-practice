class Stack:

    @staticmethod
    def push(s, element):
        assert isinstance(s, list)
        s.append(element)

    @staticmethod
    def pop(s):
        assert isinstance(s, list)
        if Stack.stack_empty(s):
            raise OverflowError
        else:
            ret = s[-1]
            s.remove(s[-1])
            return ret

    @staticmethod
    def stack_empty(s):
        assert isinstance(s, list)
        if s[-1] == 0:
            return True
        else:
            return False
