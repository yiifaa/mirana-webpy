BEGIN {
	OFS = "="
	for(i = 1; i < 5; i ++) {
		items[i]["name"] = 5 "*" i
		items[i]["value"] = 5 * i
	}
	#  确定数组的长度
	len = length(items) + 1
	for(i = 1; i < 5; i ++) {
		print items[i]["name"], items[i]["value"]
		#printf("%d \t %d \n", items[i]["name"], items[i]["value"])
	}
}
