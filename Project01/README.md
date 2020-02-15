# CS 1XA3 Project 01 
#### Nithusha Sivakumar | sivakumn | 400088188

## Usage

First execute the script from project root (~/CS1XA3/Project01):

	`chmod +x CS1XA3/Project01/project_analyze.sh`

To use features, run script followed by arguments:

	`./CS1XA3/Project01/project_analyze.sh arg1 arg2 arg3 ...`

Possible arguments:

| Argument | Feature |
| -------- | ------- |
| **arg1** | `FIXME` |
| **arg2** | `Checkout-Latest-Merge` |
| **arg3** | `Type-Count` |

Arguments should be EXACTLY outlined as one of the above, else nothing will occur. Can add multiple arguments at once but arguments will be taken in order and executed in order typed.

## Feature 01: FIXME

**Description:**
FIXME checks for all files in the repo that has "#FIXME" in the last line of the file. It them compiles the file names of all such files into CS1XA3/Project01/fixme.log.

**Execution:** 
To execute, we execute the script followed by FIXME.
	`./CS1XA3/Project01/project_analyze.sh FIXME'
Note that a fixme.log file will always be created even if nothing is found, however it will be an empty file.

**Reference:** 
 - [StackOverFlow](https://stackoverflow.com/questions/965053/extract-filename-and-extension-in-bash)

## Feature 02: Checkout-Latest-Merge

**Description:**
Checkout-Latest-Merge searches through all the commits made in the repo and finds the most recent commit containing the word "merge". It is case sensitive. The code works by finding all commits with the word "merge" in its message. It will then compile them into a file called gitlog.txt. The code then takes the most recent commit ie first line and then checks out that git automatically. If the file is empty, ie. there are no commits with "merge" in it's message. It will do nothing and will perform `git checkout`. 

**Execution:**
For execution, similar to before, we execute with:
	`./CS1XA3/Project01/project_analyze.sh Checkout-Latest-Merge'
The output will either automatically switch you to the commit found or in the current working stage as before.

**Reference:** None used.

## Feature 03: Type-Count

**Description:**
Type-Count will find all files in the repo with the extension provided by the user once prompted. It will return how many files were found with that extension in the repo.

**Execution:**
For execution, run the script using:
	`./CS1XA3/Project01/project_analyze.sh Type-Count'
Once prompted with `Enter extension type (No Punctuation), user will type file extension they are looking for. The format of the extension should be just the extension with no punctuation (i.e. "txt", "pdf", etc.). If the user input following the prompt does not follow this format or is a format that doesn't exist in repo, the output will result in 0.

**Reference**: None used.

## Custom Feature 01: Date Accessed and Date Last Modified:

**Description:** 
This feature will take on one of 2 user inputs when prompted for a `Tag` which can be either `Accessed` or `Modified`.

If Tag is Accessed:
- The feature will find all files in the repo accessed within the date and time range and add these file names to Accessed.txt

If Tag is Modified:
- The feature will find all files in the repo modified within the date and time rage and these file names to Modified.txt

**Execution:** 
Like other features' execution user will execute the code followed by argument `File-Changes`:
	`./CS1XA3/Project01/project_analyze.sh File-Changes'  
This feature will take on one of 2 user inputs when prompted for a `Tag` which can be either `Accessed` or `Modified`.                                                                  If user prompts Accessed or Modified:                                                                                                                                                  
 - User will then be prompted again for a `Date Range`. The user can then prompt `All` or `"MMM DD" where MMM is first 3 letters of the month and DD is the day of month.               
 - User will again be prompted for a `Time Range`. The user can again prompt `All` or `HH:MM-HH:MM" where HH:MM is using military time. 

## Custom Feature 02: 

**Description:**
The user will be prompted with 2 options of `Files` or `Directories`

If Files is prompted:
-create a new directory CS1XA3/Project01/Important-$USER
-copy all files in repo which has "important" in file name or within file contents into this directory
-rename all remaining files with the name + "Not Needed"

If Directories is prompted:
-for all directories not called private, check all directory names for "Dumb" 
-create a directory called Trash can and move all of these directories
-prompt again with `Do you want to delete Dumb Directories these files?`
-if yes, delete them from their original location

**Execution:**

We execute with:
	`./CS1XA3/Project01/project_analyze.sh Organize'
Once prompted with `What do you want to organize?`, type "Directories" or "Files"
If prompt chosen is "Directories", user will be asked `Do you want to delete Dumb Directories?`. User will give "YES" or "NO" as input. 

**Reference:**	
