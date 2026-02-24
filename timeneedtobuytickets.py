def timeRequiredToBuy(self, tickets, k):

        target = tickets[k]
        total_time = 0

        for i in range(len(tickets)):

            if i <= k:
                total_time += min(tickets[i], target)
            else:
                total_time += min(tickets[i], target - 1)

        return total_time