"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests
You will learn:
 - how to write to stderr
 - how to test output to the stderr and stdout
"""
import sys

"""
Standard error. – The user program writes error information to this file processing.
 Errors are returned via standard error ( STDERR ). 

 Standard output - The user program writes the usual information for this file processing. 
 The output is returned via standard output ( stdout ). 

"""


def my_precious_logger(text: str):
    l_stderr = sys.stderr
    l_stdout = sys.stdout
    if text.split()[0] == 'error:':
        l_stderr.write(text + '\n')
    else:
        l_stdout.write(text + '\n')