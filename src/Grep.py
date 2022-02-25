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
from Usage import usage


def grep(args):
    searchWordArgIndex = 0
    existenceFlag = True
    if len(args) > 0 and args[0] == "-v":
        if len(args) < 3:
            usage(error="Please provide a pattern and at least one filename", tool="grep")
        existenceFlag = False
        searchWordArgIndex = 1
    else:
        if len(args) < 2:
            usage(error="Please provide a pattern and at least one filename", tool="grep")

    searchWord = args[searchWordArgIndex]
    fileNameArray = args[searchWordArgIndex + 1:]
    for i in range(len(fileNameArray)):
        # removed safeCheck
        file = open(fileNameArray[i], "r")
        readContent = file.readlines()
        for j in range(len(readContent)):
            matchLocation = readContent[j].find(searchWord)
            if not existenceFlag and matchLocation == -1:
                print(readContent[j], end="")
            elif existenceFlag and matchLocation != -1:
                print(readContent[j], end="")
        file.close()
