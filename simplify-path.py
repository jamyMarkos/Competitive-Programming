class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = ['/']
        list_ = path.split('/')

        while '' in list_:
            list_.remove('')
        
        print(list_)

        for str_ in list_:
            if str_ == '.':
                continue
            elif str_ == '..':
                path_stack = path_stack[:-2]
            else:
                if not path_stack:
                    path_stack.append('/')
                path_stack.append(str_)
                path_stack.append('/')


        while path_stack and path_stack[-1] == '/':
            path_stack.pop()

        return '/' if not path_stack else ''.join(path_stack)