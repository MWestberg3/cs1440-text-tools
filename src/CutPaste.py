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

def cut(args):
    columnNumbers = [0]
    fileNameArray = []
    if len(args) < 1:
        usage(error="Too few arguments", tool="cut")

    if (args[0] != "-f") and len(args) < 1:
        usage(error="Too few arguments", tool="cut")

    if (args[0] == "-f") and len(args) < 3:
        usage(error="A comma-separated field specification is required", tool="cut")

    if args[0] == "-f":
        columnNumbersString = args[1].split(",")
        # adjust to zero-based array
        for k in range(len(columnNumbersString)):
            if not columnNumbersString[k].isdigit():
                usage(error="A comma-separated field specification is required", tool="cut")

    if (args[0] == "-f") and (len(args) >= 3):
        columnNumbersString = args[1].split(",")
        columnNumbers = []
        # adjust to zero-based array
        for k in range(len(columnNumbersString)):
            columnNumber = int(columnNumbersString[k])
            columnNumbers.append(columnNumber - 1)
        columnNumbers.sort()
        fileNameArray = args[2:]
    elif (args[0] != "-f") and (len(args) >= 1):
        fileNameArray = args
        # handle errors...



    # concatenate files
    everyFileArray = []
    for i in range(len(fileNameArray)):
        # removed safeCheck
        file = open(fileNameArray[i], "r")
        readContent = file.readlines()
        everyFileArray.extend(readContent)
        file.close()

    for stripFileIndex in range(len(everyFileArray)):
        everyFileArray[stripFileIndex] = everyFileArray[stripFileIndex].rstrip("\n")

    # extracting specified columns
    for j in range(len(everyFileArray)):
        oneLine = everyFileArray[j]
        printedLine = ""
        separatedColumns = oneLine.split(",")
        for column in range(len(columnNumbers)):
            if column >= 1:
                printedLine += ","
            #if statement to verify if the column exists
            if columnNumbers[column] < len(separatedColumns):
                printedLine += separatedColumns[columnNumbers[column]]

        print(printedLine)



def paste(args):                                                    	         	  
    """merge lines of files"""
    fileNameArray = args
    fileHandleArray = []

    for i in range(len(fileNameArray)):
        # removed safeCheck
        file = open(fileNameArray[i], "r")
        fileHandleArray.append(file)

    # loop through reading the files
    emptyLine = False
    numberFilesClosed = 0
    while not emptyLine:
        printedLine = ""
        for j in range(len(fileHandleArray)):
            readOneLine = ""

            if fileHandleArray[j] is not None:
                readOneLine = fileHandleArray[j].readline()
                if readOneLine == "":
                    fileHandleArray[j].close()
                    fileHandleArray[j] = None
                    numberFilesClosed += 1

            if numberFilesClosed != len(fileHandleArray):
                readOneLine = readOneLine.rstrip("\n")
                if j >= 1:
                    printedLine += ","
                printedLine += readOneLine

        if numberFilesClosed != len(fileHandleArray):
            print(printedLine)
        else:
            emptyLine = True