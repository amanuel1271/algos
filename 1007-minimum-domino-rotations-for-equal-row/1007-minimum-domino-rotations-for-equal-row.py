class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        def moves_to_make_equi(arr1,arr2):
            count_freq = Counter(arr1)
            num_with_max_freq = []
            max_freq = max(count_freq.values())
            
            for num in range(1,7):
                if count_freq[num] == max_freq:
                    num_with_max_freq.append(num)
            
            min_swaps = math.inf
            for num in num_with_max_freq:
                is_possible = True
                swap_cnt = 0
                for i in range(len(arr1)):
                    if arr1[i] == num:
                        continue
                    if arr2[i] != num: #can't swap
                        is_possible = False
                        break
                    swap_cnt += 1
                    
                if is_possible:
                    min_swaps = min(min_swaps,swap_cnt)
                    
            return min_swaps
                        
                        
        
        res = min(moves_to_make_equi(tops,bottoms),moves_to_make_equi(bottoms,tops))
        return res if res != math.inf else -1
        