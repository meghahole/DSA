

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        lens1 =len(str1)
        lens2 =len(str2)
        op_strg = ""
        
        if str1+str2 != str2+str1 :
            return ""
            
        def gcd(lens1 , lens2):
            minnum = min(lens1,lens2)
            
            for i in range(minnum,0,-1):
                if lens1 % i ==0 and lens2 % i ==0:
                    print(i)
                    return i
            return 1

        """ for i in range(mintras):
            if str1[i] == str2[i]:
                op_strg = op_strg + str1[i]
                print(op_strg)
                continue
                
            else:
                break """
        #print(op_strg)
        
        return str1[:gcd(len(str1),len(str2))   ]

s = Solution()

#s.gcdOfStrings("ABCABC","ABC")
s.gcdOfStrings("ABABAB","ABAB")