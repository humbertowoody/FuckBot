#!/bin/bash
# Script to download names DB.

# You need curl.
#sudo apt-get install curl


echo "This script will Download all the names used by the Bot"
echo "It isn't needed at all as they are provided with the folder but, just in case"
echo 
echo "Enjoy it! The output will be Names1.txt (To keep Names.txt <- Original File Provided)"

curl http://www2.census.gov/topics/genealogy/1990surnames/dist.all.last | \
	awk '{print $1}' >> Names1.txt

echo "Finished! They aren't sorted."