class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = {}
        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
        
        builder = []
        
        if len(count) == 1 and count['1'] == 1:
            return '1'
        
        if '0' not in count:  # Check if the key '0' is not present in count
            for i in range(count['1']):
                builder.append('1')
            return "".join(builder)
        
        if count['1'] == 1:
            zeroCount = count['0']
            for i in range(zeroCount):
                builder.append('0')
            builder.append('1')
            return "".join(builder)
        
        while count['1'] > 1:
            builder.append('1')
            count['1'] -= 1
        
        while count['0'] > 0:
            if count['0'] == 0:
                break
            builder.append('0')
            count['0'] -= 1
        
        builder.append("1")
        return "".join(builder)