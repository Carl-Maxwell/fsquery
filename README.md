fsquery
=======

A simple script to let you jump around the file system a little faster

fsquery is a filesytem search program, like locate, except fsquery is supposed 
to search the filesytem in real time (locate requires running updatedb each 
time before use if your filesystem has changes - my files change regularly 
so locate doesn't work well for me). Currently fsquery is _very_ slow.

fsquery was inspired by jquery (css selectors really), it allows you to send
in queries for files, for example:
"components/ functions.php"
would search for any files named functions.php that have a parent folder called 
components

in future I would like to extend the queries to allow selecting files by their 
contents

I designed fsquery for my own use, this sort of query is very useful for me
due to the particular layout of files that I interact with, I have lots
of files and folders with similar names and it's useful to be able to query
through them to quickly find the ones I'm looking for.

For example, commands of the form
vim `fsquery --first components/ images/ somefile.php`
or
cd `fsquery --first components/ images/`
save me some typing when searching for stuff

in these cases I could probably leave out the images/ parts of the queries and they 
would still work. It's much shorter than remembering & typing out the whole path

(actually I have aliased f to fsquery, so they're a few characters shorter)
