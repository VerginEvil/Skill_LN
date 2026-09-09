# tiext.pcs0001.project.pcs.skip.close

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProjectPCS
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2184-2185

```baan
Syntax: long tiext.pcs0001.project.pcs.skip.close(
ref             boolean          o.skip.close,
ref             string           o.message() )
Usage:        Expl:   This function is called in the process of Closing Projects:
- Main Projects and Structures
- Sub Projects
- Single Projects
To decide if the process must be skipped for a specific Closing
Project Type.
A message may be returned, to present information about the
decision to the user.
When this function is called all fields of tables:
- General Project Data (tipcs020)
- Project Details (tipcs030)
are current.
Pre:    NA
Post:   NA
Input:  NA
Output: o.skip.close            - decision result wherein
o.message               - message, multibyte - max 300 characters
Return: 0                       - success
DALHOOKERROR            - error
```
