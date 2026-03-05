def beautifulArray(self, n):

        res = [1]

        while len(res) < n:

            temp = []

            # build odd numbers
            for x in res:
                if 2*x - 1 <= n:
                    temp.append(2*x - 1)

            # build even numbers
            for x in res:
                if 2*x <= n:
                    temp.append(2*x)

            res = temp

        return res