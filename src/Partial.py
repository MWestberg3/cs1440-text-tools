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


def head(args):
    if args[0] == "-n":
        header = args[1]
        newArgs = args[2:]
        for i in range(len(newArgs)):
            # perform safe Check
            safeCheck = os.access(newArgs[i], os.R_OK)
            if safeCheck:
                file = open(newArgs[i], "r")
                if len(newArgs) > 1:
                    print("\n" + f"==> {newArgs[i]} <==")
                # end if len(newArgs) > 1:
                for j in range(int(header)):
                    readContent = file.readline()
                    print(end="".join(readContent))
                # end for j in range(int(header)):
            else:
                usage(error="Invalid File", tool="head")
        # end for i in range(len(newArgs)):
    else:
        header = 10
        for i in range(len(args)):
            # perform safe Check
            safeCheck = os.access(args[i], os.R_OK)
            if safeCheck:
                file = open(args[i], "r")
                if len(args) > 1:
                    print("\n" + f"==> {args[i]} <==")
                # end if len(args) > 1:
                for j in range(int(header)):
                    readContent = file.readline()
                    print(end="".join(readContent))
                # end for j in range(int(header)):
            else:
                usage(error="Invalid File", tool="head")
        # end for i in range(len(args)):

def tail(args):                                                     	         	  
    """output the last part of files"""                             	         	  
    print("TODO: output the last part of files")                    	         	  
