# 
# File:			TestFib5.py
# Description:	classic Fibonacci demonstration use of caching
# Author:		Chris Folan
#		  __                            ___       ___                       
#		 /\ \             __          /'___\     /\_ \                      
#	  ___\ \ \___   _ __ /\_\    ____/\ \__/  ___\//\ \      __      ___    
#	 /'___\ \  _ `\/\`'__\/\ \  /',__\ \ ,__\/ __`\\ \ \   /'__`\  /' _ `\  
#	/\ \__/\ \ \ \ \ \ \/ \ \ \/\__, `\ \ \_/\ \L\ \\_\ \_/\ \L\.\_/\ \/\ \ 
#	\ \____\\ \_\ \_\ \_\  \ \_\/\____/\ \_\\ \____//\____\ \__/.\_\ \_\ \_\
#	 \/____/ \/_/\/_/\/_/   \/_/\/___/  \/_/ \/___/ \/____/\/__/\/_/\/_/\/_/
#              

import datetime

def memoize(f):
    ''' simple cache decorator '''
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    

def fib(n):
    ''' classic fibonacci '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

num = 32
# -- compare fibonacci - without and with cache --
st = datetime.datetime.now()
res = fib(num)
et = datetime.datetime.now()
print ("{} => {} (without cache - duration: {})".format(num, res, et - st))

st = datetime.datetime.now()
fib = memoize(fib)
res = fib(num)
et = datetime.datetime.now()
print ("{} => {} (with cache - duration: {})".format(num, res, et - st))

