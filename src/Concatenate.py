#                         ~                                         	         	  
#                        (o)<  DuckieCorp Software License          	         	  
#                   .____//                                         	         	  
#                    \ <' )   Copyright (c) 2022 Erik Falor         	         	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	  
#                                                                   	         	  
# Permission is NOT granted, to any person who is NEITHER an employee NOR     	  
# customer of DuckieCorp, to deal in the Software without restriction,        	  
# including without limitation the rights to use, copy, modify, merge,        	  
# publish, distribute, sublicense, and/or sell copies of the Software, and to 	  
# permit persons to whom the Software is furnished to do so, subject to the   	  
# following conditions:                                             	         	  
#                                                                   	         	  
# The above copyright notice and this permission notice shall be included in  	  
# all copies or substantial portions of the Software.               	         	  
#                                                                   	         	  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    	  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 	  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      	  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     	  
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS	  
# IN THE SOFTWARE.
import os
from Usage import usage

def cat(args):
    amtArgs = len(args)
    if len(args) < 1:
        usage(error="Too few arguments", tool="cat")
    for i in range(amtArgs):
        safeCheck = os.access(args[i], os.R_OK)
        if safeCheck:
            file = open(args[i], "r")
            readContent = file.readlines()
            print(end="".join(readContent))
            file.close()
        else:
            usage(error=f"Invalid File {args[i]}", tool="cat")

def tac(args):
    amtArgs = len(args)
    if len(args) < 1:
        usage(error="Too few arguments", tool="tac")
    for i in range(amtArgs):
        safeCheck = os.access(args[i], os.R_OK)
        if safeCheck:
            file = open(args[i], "r")
            readContent = file.readlines()
            reverseFile = readContent[::-1]
            print(end="".join(reverseFile))
            file.close()
        else:
            usage(error=f"Invalid File {args[i]}", tool="tac")
