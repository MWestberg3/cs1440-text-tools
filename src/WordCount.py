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

def wc(files):
    totalLines = 0
    totalWords = 0
    totalBytes = 0
    printedLines = ""
    if len(files) < 1:
        usage(error="Too few arguments", tool="wc")
    for i in range(len(files)):
        # removed safeCheck
        openFile = open(files[i], "r")
        readContent = openFile.readlines()
        openFile.close()

        # calculate number of lines
        numOfLines = len(readContent)
        totalLines += numOfLines

        # calculate number of characters
        numOfCharacters = 0
        for j in range(numOfLines):
            numOfCharacters += len(readContent[j])
        totalBytes += numOfCharacters

        # calculate number of words
        stringFile = "\n".join(readContent)
        wordArray = stringFile.split()
        numOfWords = len(wordArray)
        totalWords += numOfWords

        # print result
        printedLines += str(numOfLines) + "\t" + str(numOfWords) + "\t" + str(numOfCharacters) + "\t" + files[i] + "\n"

    print(printedLines[:-1])
    if len(files) > 1:
        print(str(totalLines) + "\t" + str(totalWords) + "\t" + str(totalBytes) + "\ttotal")
