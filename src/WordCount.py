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


def wc(files):
    amtFiles = len(files)
    numOfLines = 0
    numOfCharacters = 0
    if amtFiles == 1:
        safeCheck = os.access(files[0], os.R_OK)
        if safeCheck:
            openFile = open(files[0], "r")
            readContent = openFile.readlines()
            for i in range(len(readContent)):
                numOfLines += 1
            stringFile = "".join(readContent)
            wordArray = stringFile.split()
            numOfWords = len(wordArray)
            # print result
            print(str(numOfLines) + "    " + str(numOfWords))
