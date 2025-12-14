# Dec 1 2025
##### [link to problem](https://adventofcode.com/2025/day/1)
##### The first problem of the year, not a particularly difficult problem but I think a good start in terms of being interesting. You have a lock and a set of instuctions to extract the password.
## Part 1
##### Given your instructions and with a tumbler starting at 50, how many times does it land on 0? 
##### Relatively simple problem, lets start with parsing, all I did was take the list of instuctions and turn each into a pair of direction and value as to be easier to work with later. Next I just add or subtract based on direction and take the remainder by 100, if 0 add to the count and we're done.
## Part 2
##### Apparently we actually need to know how many times we even just pass 0, including instructions up to 1000, still not too complex, for insructions greater than 99 floor divide by 100 and add to our count, than take the remainder by 100 and apply to the position, if greater than 100 or less than 0 add 1 to the count and sub or add 100 respectfully.
## Thoughts
##### A interesting if simple problem, great for day 1 and here's to 11 more great days