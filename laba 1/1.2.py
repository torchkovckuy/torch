def find_combinations(candidates, target):
    candidates.sort()
    result = []

    def find(start, combination, sum_comb):
        if sum_comb == target:
            result.append(combination.copy())
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            if sum_comb + candidates[i] > target:
                continue

            combination.append(candidates[i])
            find(i + 1, combination, sum_comb + candidates[i])
            combination.pop()
    find(0, [], 0)
    return result
print(find_combinations([2,5,2,1,2], 5))
print(find_combinations([10,1,2,7,6,1,5], 8))