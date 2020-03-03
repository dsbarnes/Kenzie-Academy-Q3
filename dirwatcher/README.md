## Backend--Dirwatcher--Assignment!
The `dirwatcher.py` program will continually search within all files in the directory
for a 'magic' string which is provided as a command line argument.  

Use:  
`dirwatcher ['dir']['magic_string']['interval']['suffex']`

| Arg              | Description                                                                      |
| ---------------- | -------------------------------------------------------------------------------- |
| ['dir]           | An argument that specifies the directory to watch. (required)                    |
| ['magic_string'] | The string to search for in the text. (required)                                 |
| ['interval']     | An argument that controls the polling interval.                                  |
| ['suffex']       | An argument that filters for a file extension to search such as `.txt` or `.log` |


If the magic string is found in a file, output a log message indicating which file and line number.

### More Directions:
Once a magic text occurrence has been logged, 
it should not be logged again unless
it appears in the file as another subsequent line entry later on.  
(Or perhaps if it appears in another file??)

Files in the monitored directory may be added or deleted 
or appended at any time by other processes. 

Your program should log a message when new files appear 
or other previously watched files disappear. 

Assume that files will only be changed by appending to them.  
You don't have to continually re-check sections of a file that you have already checked.

Your program should terminate itself by catching  
SIGTERM or SIGINT (be sure to log a termination message).  

**NOTE:** that handling OS signals and polling the directory that is being watched are two separate functions of your program.  
You won't be getting an OS signal when files are created or deleted.  

Use all best-practices that have been taught so far: docstrings, PEP8, unit tests, clean and readable code and meaningful commit messages.  

Include a startup and shutdown banner in your logs and report the total runtime (uptime) within your shutdown log banner.  
