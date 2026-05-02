class Solution:
    # Find first index from left that will hold water
    def find_left(self, height: List[int]) -> int:
        idx = 0
        while idx <= len(height) - 1 and height[idx] <= height[idx+1]:
            idx+=1
        return idx
    # Find first index from right that will hold water
    def find_right(self, height: List[int]) -> int:
        idx = len(height) - 1
        while idx >= 0 and height[idx] <= height[idx - 1]:
            idx-=1
        return idx
    # Find intermediate peaks
    def find_peaks(self, height: List[int]) -> List[int]:
        peaks = set()
        peaks.add(0)
        peaks.add(len(height)-1)
        cur_peak = height[0]
        for i,e in enumerate(height):
            if e >= cur_peak:
                peaks.add(i)
                cur_peak = e
        return list(peaks)
    # Convert peaks into tuples of peaks (bounds on valleys)
    def find_valleys(self, peaks: List[int]) -> List[tuple[int,int]]:
        idx = 0
        ret = []
        while idx < len(peaks) - 1:
            ret.append((peaks[idx],peaks[idx+1]))
            idx+=1
        return ret
    # Find total amount of water
    def sum_water(self, height: List[int], valleys: List[tuple[int,int]]) -> int:
        total = 0
        for (left,right) in valleys:
            min_height = min(height[left],height[right])
            for e in height[left+1:right]:
                if(min_height > e):
                    total += min_height - e
        return total
    def trap(self, height: List[int]) -> int:
        if(len(height) < 2):
            return 0
        else:
            left = self.find_left(height)
            right = self.find_right(height)
            heightt = height[left:right+1]
            peaks = self.find_peaks(heightt)
            peaks.sort()
            valleys = self.find_valleys(peaks)
            return self.sum_water(heightt,valleys)