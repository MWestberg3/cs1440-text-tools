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
  
  * tac(args):
    * assign amtArgs = len(args)
      * for i loop range amtArgs
        * run safeCheck
          * file = open args[i]
          * assign readContent to file.readlines
          * print array backwards using slicing
  
  * cut(args):
  
  * paste(args):
    * assign amtArgs = len(args)
    * create multidimensional array (empty string?)
    * for i loop range amtArgs
      * run safeCheck
        * open file
        * assign variable to file.readlines
        * assign to a new array for each iteration i
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
    * 


## Phase 3: Implementation *(15%)*

**Deliver:**

*   (More or less) working code.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
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
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   Fill out the Assignment Reflection on Canvas.
