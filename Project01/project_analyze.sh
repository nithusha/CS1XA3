#!/bin/bash

#feature input

for item in $@ ; do
	if [ "$item" = "FIXME" ]; then
		> "fixme.log"
		find .. -type f -not -path '*/\.git/*' -print0 | while IFS= read -r -d '' file; do
			occur=$(grep -n "#FIXME" $file | tail -n 1 | cut -d ":" -f 1)
			count=$(wc -l < $file)
			if [ "$occur" == "$count" ]; then
				echo "$file" >> "fixme.log"
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
	if [ "$item" = "File-Size-List" ]; then
		find .. -type f -print0 | while IFS= read -r -d '' file; do
			size=$(ls -sort -lh $file | cut -d " " -f 5)
			name=$(ls -sort -lh $file | cut -d " " -f 9)
			echo "File Size: $size, File Name: $name"
		done
	fi
	if [ "$item" = "Find-Tag" ]; then
		echo "Enter Tag word"
		read tag
		> "$tag.log"
		find .. -type f -name "*.py*" -print0 | while IFS= read -r -d '' file; do
			if grep -q "#$tag" $file; then
				filename=$(grep -H "#$tag" $file | cut -d ":" -f 1)
				line=$(grep -H "#$tag" $file | cut -d ":" -f 2)
				echo "Filename is: $filename" >> "$tag.log"
				echo "$line" >> "$tag.log"
			fi
		done
	fi
	if [ "$item" = "Backup-Delete/Restore" ]; then
		echo "Which command: Backup or Restore? Enter prompt as typed in question"
		read command
		if [ "$command" == "Backup" ]; then
			if [ ! -d "backup" ]; then
				mkdir backup
			elif [ -d "backup" ]; then
				find "backup" ! -type d -exec rm -f {} +

			fi
			> "restore.log"
			DIR="$(pwd)"
			ParentDir="$(dirname $DIR)"
			find "$ParentDir" -type f -name "*.tmp*" -print0 | while IFS= read -r -d '' file; do
				mv "$file" "$DIR/backup"
				echo "$file" >> "restore.log"
			done
		fi
		if [ "$command" == "Restore" ]; then
			if [ ! -f "restore.log" ]; then
				echo "Error: restore.log not found"
				exit 1
			elif [ -f "restore.log" ]; then
				for line in $(cat restore.log) ; do
					filename=$(basename "$line")
					cd backup
					mv "$filename" "$line"
					cd ..
				done
			fi
		fi
	fi
	if [ "$item" = "File-Changes" ]; then
		echo "Accessed or Modified"
		read Tag
		echo "Date Range? Please write in the format of MM/DD/YYYY or ALL"
		read daterange
		echo "Time Range? Please write in the format of HH:MM-HH:MM or ALL?"
		read timerange
		format=""
		if [ "$Tag" == "Accessed" ]; then
			format+="x"
		elif [ "$Tag" == "Modified" ]; then
			format+="y"
		fi
		>"$Tag.txt"
		if [ "$daterange" == "ALL" ]; then
			if [ "$timerange" == "ALL" ]; then
				echo "Dates: ALL and Times: ALL" >> "$Tag.txt"
					find .. -type f -not -path '*/\.git/*' -print0 | while IFS= read -r -d '' file; do
					tstamp=$(stat --format=%"$format" $file)
					echo "$file : $tstamp" >> "$Tag.txt"
				done
			else
				start=$(echo $timerange | cut -d "-" -f 1)
				end=$(echo $timerange | cut -d "-" -f 2)
				echo "Dates: ALL and Time: $start - $end" >> "$Tag.txt"
				find .. -type f -not -path '*/\.git/*' -print0 | while IFS= read -r -d '' file; do
					tstamp=$(stat --format=%"$format" $file | cut -d " " -f 2)
					fstamp=$(stat --format=%"$format" $file)
					if [[ "$tstamp" > "$start" ]]  && [[ "$tstamp" < "$end" ]]; then
						echo "$file : $fstamp" >> "$Tag.txt"
					fi
				done
			fi
		else
			drange=$(date -d "$daterange" +%s)
			echo "$drange"
			if [ "$timerange" == "ALL" ]; then
				echo "Dates: $drange and Time: ALL" >> "$Tag.txt"
				find .. -type f -not -path '*/\.git/*' -print0 | while IFS= read -r -d '' file; do
					tstamp=$(stat --format=%"$format" $file | cut -d " " -f 1)
					stamp=$(date -d "$tstamp" +%s)
					fstamp=$(stat --format=%"$format" $file)
					if [ "$drange" -eq "$stamp" ]; then
						echo "$file : $fstamp" >> "Tag.txt"
					fi
				done
			else
				start=$(echo $timerange | cut -d "-" -f 1)
				end=$(echo $timerange | cut -d "-" -f 2)
				echo "Dates: $drange and Times: $start - $end" >> "$Tag.txt"
				find .. -type f -not -path '*/\.git/*' -print0 | while IFS= read -r -d '' file; do
					fstamp=$(stat --format=%"$format" $file)
					dstamp=$(echo $fstamp | cut -d " " -f 1)
					Dstamp=$(date -d "$dstamp" +%s)
					tstamp=$(echo $fstamp | cut -d " " -f 2)
					if [ "$Dstamp" -eq "$drange" ]; then
						if [[ "$tstamp" > "$start" ]] && [[ "$tstamp" < "$end" ]]; then
							echo "$file : $fstamp" >> "$Tag.txt"
						fi
					fi
				done
			fi
		fi
	fi
	if [ "$item" == "Organize" ]; then
		echo "What do you want to organize? Files or Directories?"
		read object
		DIR="$(pwd)"
		ParentDir="$(dirname $DIR)"
		if [ "$object" == "Files" ]; then
			if [ ! -d "Important-$USER" ]; then
				mkdir "Important-$USER"
			elif [ -d "Important-$USER" ]; then
				find "Important-$USER" ! -type d -exec rm -f {} +
			fi
			find "$ParentDir" -type f -name "important" -not -path '*/\.git/*' -print0 | while IFS= read -r -d '' file; do
				mv "$file" "$DIR/Impotant-$USER"
			done
			find "$ParentDir" -type f -not -path '*/\.git/*' -print0 | while IFS= read -r -d '' file; do
				if  grep -q "Important" $file; then
					mv "$file" "$DIR/Important-$USER"
				fi
			done
			for file in "$ParentDir"/*; do
				filename=$(basename "$file")
				dirname=$(dirname "$file")
				mv "$file" "$dirname/Not-Needed:$filename"
			done
		fi
		if [ "$object" == "Directories" ]; then
			if [ ! -d "Trash" ]; then
				mkdir "Trash"
			elif [ -d "Trash" ]; then
				find "Trash" ! -type d -exec rm -f {} +
			fi
			find "$ParentDir" -type d -name "Dumb" -and ! -name "private" -print0 | while IFS= read -r -d '' file; do
				cp  "$file" "$DIR/Trash"
			done
			echo "Do you want to delete Dumb Directories?"
			read answer
			if [ "$answer" == "yes" ]; then
				find "$ParentDir" -type d -name "Dumb" -and ! -name "private" -print0 | while IFS= read -r -d '' file; do
					rm -r "$file"
				done
			fi
		fi
	fi
done
