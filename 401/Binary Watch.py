# /usr/bin/python
# coding: utf-8


class Solution:

    def getSums(self, nums, start, num, results):
        if num == 0:
            results.append(start)
        elif nums:
            for idx, _num in enumerate(nums):
                self.getSums(nums[idx+1:], start + _num, num-1, results)

    def readBinaryWatchHour(self, num):
        hour = [8, 4, 2, 1]
        results = []
        self.getSums(hour, 0, num, results)
        return results

    def readBinaryWatchMinute(self, num):
        minute = [32, 16, 8, 4, 2, 1]
        results = []
        self.getSums(minute, 0, num, results)
        return results

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        results = []
        for i in range(num+1):
            if i < 4 and num - i < 6:
                hours = self.readBinaryWatchHour(i)
                minutes = self.readBinaryWatchMinute(num-i)
                for hour in hours:
                    for minute in minutes:
                        if hour < 12 and minute < 60:
                            time = str(hour) + ":" + str(minute) if minute > 9 else str(hour) + ':0' + str(minute)
                            results.append(time)
        return results


print(Solution().readBinaryWatch(2))
