# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

* A detailed written description of the problem this program aims to solve.
  * The program we are supposed to design essentially rewrites basic functions that are found in a unix system such as: cat, tac, cut, paste, grep, head, tail, sort, and wordcount(wc).
    * Cat concatenates two files together. (Doesn't create a new file)
    * Tac concatenates two files together, but backwards (last line first, first line last)
    * Cut returns only first section as separated by a comma
    * Paste merges lines of a file, separating with a comma
    * Grep searches a file, and returns a file matching a pattern the user inputs (similar to a search bar)
    * Head prints out the first 10 lines of a file. Can be customized with -n
    * Tail prints out the last 10 lines of a file, but can also be customized with -n
    * Sort - sorts lines based on ASCII values
    * WC - counts and returns the amount of characters, lines, words (as separated by white space) and the input for the file
      * several files input are separated by newlines of output
* Describe what a *good* solution looks like.
    * List what you already know how to do.
      * Access files
      * Concatenate strings
      * Print line-by-line files
      * Create and access arrays
      * Access modules
      * Remove pieces from strings
      * Converting ASCII characters
    * Point out any challenges that you can foresee.
      * I am still not very great at accessing arrays
      * sys.args is still foreign to me


## Phase 1: System Analysis *(10%)*

**Deliver:**

* List all of the data that is used by the program, making note of where it comes from.
  * The program will use file inputs, and create arrays. The files accessed will come from any file according to the user.
  * ASCII values?
* Explain what form the output will take.
  * The output will be a string. There should be no floating numbers. Strictly String.
* Describe what algorithms and formulae will be used (but don't write them yet).
  * String concatenates


## Phase 2: Design *(30%)*

**Deliver:**

* Function signatures that include:
    * cat(args)
      * concatenate files and prints
    * tac(args)
      * concatenate files and print in reverse
    * cut(args)
      * removes sections from each line of files(things following a comma)
    * paste(args)
      * merge lines of files, separated by commas
    * grep(args)
      * print lines that match user imputed patters
    * head(args)
      * output first part of files (first 10 lines)
    * tail(args)
      * output the last part of files (last 10 lines)
    * sort(args)
      * sort lines of text files according to ASCII values
    * wc(files)
      * print how many lines, words, and byte counts for each file (and return at end of line which file was used)
* Pseudocode that captures how each function works.
  * cat(args):
    * assign amtArgs = len(args)
        * for i loop range amtArgs
          * run safeCheck
            * file = open args[i]
            * readContent = file.readlines()
            * print(end=""".join(readContent))
            * close file
  
  * tac(args):
    * assign amtArgs = len(args)
      * for i loop range amtArgs
        * run safeCheck
          * file = open args[i]
          * assign readContent to file.readlines
          * print array backwards using slicing
          * close file
  
  * cut(args):
    * set standard column numbers array to 0
    * create a new array
    * if the first args is '-f' and there are a total of 3 or more args, and the first item aftert -f is a digit:
      * split the number given by commas
      * set the standard column numbers array to an empty array
      * for k loop in the length of the amount of numbers you have describing the columns
        * the column number is going to be whatever the first value is in the array, but converted to integer
        * then append that number to the column number, and subtract it by one to make the one based input to a zero based array
      * sort the array (ensuring order of column number doesn't matter)
      * name of files array begins with whatever comes after the digit
    * if there is no -f, and there are more than 1 args
      * your file name array is just the args
    * DEAL WITH ERROR HANDLING
    * begin concatenating files to open here:
    * create an empty array for every file we open
    * for i loop in the range of file name array
      * run safe check
        * open file
        * read and add it to the every file array
        * close the file
    * strip out the files '\n' operator, ensuring each column stays on the same line
    * begin extracting the specified columns
    * for j loop in the range of everyfilearray
      * assign a variable (oneLine) to the first line part of the everyFileArray
      * create an empty string to concatenate to
      * separate each column by splitting the line with a ','
      * for loop in the range of the column numbers
        * if there is something to be printed on the line, concatenate a comma
        * hen concatenate the column to the printed line
      * print out the printedLine
  
  * paste(args):
    * create empty array
    * for i loop in range of file name array
      * safe check
        * open file
        * append file lines to empty array
    * set variable to false
    * number of files that are closed is 0
    * while loop as long as NOT true:
      * begin with empty string
      * for j loop so in he range of empty array (line 121)
        * create empty string
        * so long as the file array (line 121) is not None
          * append one line to empty string
          * if there is an empty line, close the file and return the file as None
        * if the files are not closed
          * print one line at a time and strip the \n
          * if there is still more to print after the line, print a comma
* concatenate first column to first row of each file
  
      * head(args):
        * if statement for if there is a "-n"
          * figure out the header value
          * splice to only have the files to open
          * for loop in range of the new args
            * safe check
              * open the file
              * for loop in range of the header
                * print a single line
        * elif there is NO "-n"
          * header will be defaulted to 10
          * for loop in range of args
            * safe check
              * open the file
              * for loop in range of 10
                * print a single line

      * wc(args):
        * determine amount of files
        * set variable for numberOfLines = 0
        * set variable for numberOfCharacters = 0
        * if there is only one argument run:
          * safe check
            * open file by lines
            * assign opened file to variable (readContent)
            * for i loop in the range of new variable
              * add one to the numberOfLines variable
            * convert readContent to string
            * split string by white space
            * assign numOfCharacters to the sum characters in wordArray
            * print numberOfLines, numberOfWords, numberOfCharacters, and file name
            * 
        * else if there is more than one:
        * otherwise:

        * grep(args):
          * create a variable specifying the location of the word in array(searchWordArgIndex)
          * check if there is a '-v' flag
          * if there IS a '-v', the new word to search for is at location 1 in array not 0
        * the word to look for is specified at the location (searchWordArgIndex)
        * the files are all located AFTER the searchWordArgIndex
        * for loop in length of fileNameArray
          * safe check
            * open file
            * read the file
            * for loop in length of the file line
              * if there is not a '-v' and there was record of the searched word in line, then print the line
              * but if there is a '-v' and there was NO record of the searched word in line, the print the line
              * 

        * tail(args):
          * if statement for if there is a "-n"
            * figure out 'tailer' value
            * splice to only have files to open
            * for loop in range of the new files
              * safe check
                * open the file
                * reverse the file
                * only take the 'tailer' value
                * reverse back
                * print one line in 'tailer' at a time
          * otherwise:
            * set tailer to 10
            * run for i loop in range of args
              * safe check
                * open file
                * reverse file
                * take tailer value but last 10
                * print tail
                * close file

  * sort(args)
    * determine the length of args
    * begin array for every file
    * for i loop (length of args)
      * safe check
        * open file
        * read content
        * add to array for every file
        * close file
    * sort array for every file
    * print


## Phase 3: Implementation *(15%)*

**Deliver:**

*   (More or less) working code.
*   Note any relevant and interesting events that happened while you wrote the code.
    * I learned a lot more about accessing files, and showing usage errors. I learned how to utilize for loops, arrays, and while loops better, and being more efficient with if statements.


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    * There were VERY MANY test cases. Some specific ones are:
      * sort() - passed
      * cat() - passed
      * tac() - passed
      * grep() - ran the -v command, and had trouble isolating the word because I was using the index(), but then ran the find, and was able to locate the word.
      * header() - ran data/words200
        * passed
      * tail() - data/words200
        * failed, adjusted to put word in reverse (similar to tac) then I took the first files (according to the tailer value), then reversed it back, and it worked.
      * wc() - data/words200
        * failed - the byte count would not take into account the \n.
        * passed - ended up using a for loop to iterate through each line and adding one to a character counter variable.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.


## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 6: Maintenance

**Deliver:**

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    * What parts of your program are sloppily written and hard to understand?
        * Are there parts of your program which you aren't quite sure how/why they work?
          * At this point, I understand how it works. During the coding process, there were several lines of code I just experimented with, and then it worked, but I didn't know how or why. But now I understand exactly what my code is doing.
        * If a bug is reported in a few months, how long would it take you to find the cause?
          * I think it would take me roughly an hour to find it, if that. I know my program pretty well, and can follow it easily.
    * Will your documentation make sense to...
        * ...anybody besides yourself?
          * I honestly think it's a little rushed, and it changed so much, that much of the documentation was updated after the program was completed.
        * ...yourself in six month's time?
          * I think I will, but mostly bits and pieces.
    * How easy will it be to add a new feature to this program in a year?
      * I think it would be pretty easy, simply because of the modules and the separation of each feature.
    * Will your program continue to work after upgrading...
        * ...your computer's hardware?
          * most definitely
        * ...the operating system?
          * yes
        * ...to the next version of Python?
          * unless they change some key features, it should be able to function for quite some time.
*   Fill out the Assignment Reflection on Canvas.
