class prefix(object):
    def longest_common_prefix(self,strs):
        prefix = strs[0]
        for i in range(1,len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
        return prefix

new_prefix = prefix()
result = new_prefix.longest_common_prefix(['abcd','ab','a'])
print(result)