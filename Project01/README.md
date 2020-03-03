# CS1XA3 Project 01 
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
FIXME checks for all files in the repo that has "#FIXME" in the last line of the file. It then compiles the file names of all such files into CS1XA3/Project01/fixme.log.

**Execution:** 
To execute, we execute the script followed by FIXME.

`./CS1XA3/Project01/project_analyze.sh FIXME`

Note that a fixme.log file will always be created even if nothing is found, however it will be an empty file.

**References:** 
 - [StackOverFlow](https://stackoverflow.com/questions/965053/extract-filename-and-extension-in-bash)

## Feature 02: Checkout-Latest-Merge

**Description:**
Checkout-Latest-Merge searches through all the commits made in the repo and finds the most recent commit containing the word "merge". It is case sensitive. The code works by finding all commits with the word "merge" in its message. It will then compile them into a file called gitlog.txt. The code then takes the most recent commit ie first line and then checks out that git automatically. If the file is empty, ie. there are no commits with "merge" in it's message. It will do nothing and will perform `git checkout`. 

**Execution:**
For execution, similar to before, we execute with:

`./CS1XA3/Project01/project_analyze.sh Checkout-Latest-Merge`

The output will either automatically switch you to the commit found or in the current working stage as before.

**References:** None used.

## Feature 03: Type-Count

**Description:**
Type-Count will find all files in the repo with the extension provided by the user once prompted. It will return how many files were found with that extension in the repo.

**Execution:**
For execution, run the script using:

`./CS1XA3/Project01/project_analyze.sh Type-Count`

Once prompted with `Enter extension type (No Punctuation)`, user will type file extension they are looking for. The format of the extension should be just the extension with no punctuation (i.e. "txt", "pdf", etc.). If the user input following the prompt does not follow this format or is a format that doesn't exist in repo, the output will result in 0.

**References**: None used.

## Feature 04: File Size List

**Description:**
File Size List will go through all file in the repo and return the file name along with the file size in human readable format, ie. megabytes, kilobytes, etc.

**Execution:**
We execute with:

'./CS1XA3/Project01/project_analyze.sh File-Size-List'

The output will be all files and their sizes listed next to them.

**References:** None used. 

## Feature 05: Find Tag

**Description:**
Find Tag will prompt for a Tag word. It will then search through all files in the repo and look for the tag word. A file called Tag.log will be created in Project01 and the file name and all lines where the tag was found will be listed underneath the file name in the log.
Note if tag is given but there are no files containing the tag word, a log will still be created but will have no contents in it.

**Execution:**
We excecute with 

'./CS1XA3/Project01/project_analyze.sh Find-Tag'

**References:** None used.

## Feature 06: Backup-Delete/Restore
**Description:** 
Backup-Delete/Restore will have 2 possible prompts, either Backup or Restore. If Backup is prompted then an empty directory called backup will be created. If such a directoy already exists then it is emptied of its contents. Finding all files with .tmp extension, it copies these files into the backup directory deleting them from their original locations. Their original locations are logged into a filed called restore.log. If Restore is selected then all files are moved back into their original locations and the backup is emptied of it's contents. If Restore is the prompt but no restore.log file exists, an error message will be thrown back to the user.

**Execution:**
Execute with:
'./CS1XA3/Project01/project_analyze.sh Backup-Delete/Restore'

When prompted users will enter either:
"Backup" or "Restore"

**References:**
[StackExchange](https://unix.stackexchange.com/questions/481152/remove-files-files-from-subdirectories-in-directory?rq=1)
[AskUbuntu](askubuntu.com/questions/444551/get-absolute-path-of-files-using-find-command)


## Custom Feature 01: File-Changes

**Description:** 
This feature will take on one of 2 user inputs when prompted for a `Tag` which can be either `Accessed` or `Modified`.

If Tag is Accessed:
- The feature will find all files in the repo accessed within the date and time range and add these file names to Accessed.txt

If Tag is Modified:
- The feature will find all files in the repo modified within the date and time rage and these file names to Modified.txt

**Execution:** 
Like other features' execution, the user will execute the code followed by argument `File-Changes`:

`./CS1XA3/Project01/project_analyze.sh File-Changes`  

This feature will take on one of 2 user inputs when prompted for a `Tag` which can be either `Accessed` or `Modified`.                                                                  If user prompts Accessed or Modified:                                                                                                                                                  
 - User will then be prompted again for a `Date Range`. The user can then input `All` or `"MM/DD/YYYY"` where MM is number of the month and DD is the day of month and YYYY is the year..               
 - User will again be prompted for a `Time Range`. The user can again input `All` or `HH:MM-HH:MM"` where HH:MM is using military time. 

**References:**
-[StackExchange](https://unix.stackexchange.com/questions/84381/how-to-compare-two-dates-in-a-shell)
-[StackExchange](https://unix.stackexchange.com/questions/395933/how-to-check-if-the-current-time-is-between-2300-and-0630)

## Custom Feature 02: Organize

**Description:**
The user will be prompted with 2 options of `Files` or `Directories`

If Files is prompted:
 - create a new directory CS1XA3/Project01/Important-$USER
 - copy all files in repo which has "important" in file name or within file contents into this directory
 - rename all remaining files with the "Not-Needed: 'oldfilename'"

If Directories is prompted:
 - for all directories not called private, check all directory names for "Dumb" 
 - create a directory called Trash can and move all of these directories
 - prompt again with `Do you want to delete Dumb Directories these files?`
 - if yes, delete them from their original location

**Execution:**

We execute with:

`./CS1XA3/Project01/project_analyze.sh Organize`

Once prompted with `What do you want to organize?`, type "Directories" or "Files"
If prompt chosen is "Directories", user will be asked:
 `Do you want to delete Dumb Directories?`
User will give "YES" or "NO" as input. 

**References:**	None Used
