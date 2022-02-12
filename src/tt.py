#!/usr/bin/env python                                               	         	  

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

import sys                                                          	         	  

from Concatenate import cat, tac                                    	         	  
from CutPaste import cut, paste                                     	         	  
from Grep import grep                                               	         	  
from Partial import head, tail                                      	         	  
from Sorting import sort                                            	         	  
from WordCount import wc                                            	         	  
from Usage import usage                                             	         	  


if len(sys.argv) < 2:                                               	         	  
    usage()                                                         	         	  
    sys.exit(1)                                                     	         	  
else:
    if sys.argv[1] == "cat":
        cat(sys.argv[2:])
    elif sys.argv[1] == "tac":
        tac(sys.argv[2:])
    elif sys.argv[1] == "grep":
        grep(sys.argv[2:])
    elif sys.argv[1] == "paste":
        paste(sys.argv[2:])
    elif sys.argv[1] == "cut":
        cut(sys.argv[2:])
    elif sys.argv[1] == "head":
        head(sys.argv[2:])
    elif sys.argv[1] == "tail":
        tail(sys.argv[2:])
    elif sys.argv[1] == "sort":
        sort(sys.argv[2:])
    elif sys.argv[1] == "wc":
        wc(sys.argv[2:])
    else:
        print("No such tool exists ya dummy")
        sys.exit(1)