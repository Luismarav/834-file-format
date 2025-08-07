# 834-file-format
This script fromats 834 eligiblity files for certain vendors/clients. What is dose specifically is that any segment in the block of data between SE and ST if the block contains "AI*C" it will delete the block. 
Before I run this script I open the text file in notepad++ and I have to make it readable for me by replacing the (:) with \r\n.
Lastly before we start deleting segments we need to count how many records there are because at the end there is a total count in the (GE) line and subtract the number of how many segments there are. 
