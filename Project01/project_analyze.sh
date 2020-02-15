#!/bin/bash

#feature input

for item in $@ ; do
	if [ "$item" = "FIXME" ]; then
		> "fixme.log"
		find .. -type f -print0 | while IFS= read -r -d '' file; do
			occur=$(grep -n "#FIXME" $file | tail -n 1 | cut -d ":" -f 1)
			count=$(wc -l < $file)
			if [ "$occur" == "$count" ]; then
				filename=$(basename "$file")
				echo "$filename" >> "fixme.log"
			fi
		done
	fi
	if [ "$item" = "Checkout-Latest-Merge" ]; then
		git log --grep="merge" --abbrev-commit --oneline --graph > "gitlog.txt"
		commit=$(cat gitlog.txt | head -n 1 | cut -d " " -f 2)
		git checkout "$commit"
	fi
	if [ "$item" = "Type-Count" ]; then
		echo "Enter extension type (No Punctuation)"
		read type
		count=$(find .. -type f -name "*.$type" | wc -l)
		echo "$count"
	fi
done
