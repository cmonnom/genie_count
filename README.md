# genie_count
A quick script to evaluate the number of specific mutation entries in a particular version of Genie.

A quick script (thanks Jeff) to evaluate the number of
specific mutation entries in a particular version of Genie.

Place genie data directories next to this script
Update directories, versions and genes arraya to parse
each genie directory and the list of genes you want to count

The output would be something like this:
<pre>
count for 9.0:
 - JAK2 4
 - TET2 33
count for 9.1:
 - JAK2 136
 - TET2 31
count for 10.0:
 - JAK2 166
 - TET2 40
</pre>

