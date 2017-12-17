#! /bin/awk -f
BEGIN {
	num = 1
	print "Hello, World!"
}
#	pattern
{
	num += 1
}

# end
END {
	printf("%d Lines!", num)
}
