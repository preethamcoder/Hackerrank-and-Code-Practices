def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealths = []
        for i in accounts:
            wealths.append(sum(i))
        return max(wealths)
