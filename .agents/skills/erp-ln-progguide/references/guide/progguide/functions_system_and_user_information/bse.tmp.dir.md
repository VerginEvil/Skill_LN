# bse.tmp.dir$()

## Syntax:
`function string bse.tmp.dir$( )`

## Description
This returns a string containing the name of the directory where temporary files can be created by the application. The function uses the environment variable BSE_TMP to retrieve the information. If this environment variable is not filled, *bse.tmp.dir$()* returns the string "$BSE/tmp". If the environment variable BSE is not filled, the function returns the string "/usr/tmp".

## Context
This function is implemented in the porting set and can be used in all script types.
Note  To create temporary files with a unique name in the directory BSE.TMP.DIR, use the function call [creat.tmp.file$()](../functions_directory_file_operations/creat.tmp.file.md).

## Related topics
- [System and user information overview and synopsis](overview_and_synopsis.md)
