#! /bin/awk -f
BEGIN {
	RS = "\n\n"
	FS = "\n"
	num = 1
	print "姓名", "年龄"
}

#
{
	split($1, name, "：")
	split($2, age, "：")
	num += 1
	print name[2], age[2]
}
#
END {
	print "总计", num "人"
}