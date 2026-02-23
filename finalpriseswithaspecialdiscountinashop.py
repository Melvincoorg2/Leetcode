def finalPrices(self, prices):

        n = len(prices)
        result = prices[:]   # copy original prices
        stack = []           # store indices

        for i in range(n):

            # If current price is <= price at stack top
            while stack and prices[i] <= prices[stack[-1]]:

                index = stack.pop()
                result[index] -= prices[i]

            stack.append(i)

        return result