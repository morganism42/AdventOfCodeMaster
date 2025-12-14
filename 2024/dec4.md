# Dec 4
###### [link to problem](https://adventofcode.com/2024/day/4)
###### Today's problem was about taking a grid of letters and finding the word ```XMAS``` in it. I can be horizontal vertical diagonal or even backwards.
## Part 1
###### Parsing was easy, simply took the data and split it by newlines. Finding the word itself is a trickier problem, there are a few methods you could use, for the horizontal and vertical you could use a regex and rotate the grid for half, which I tried and ended up being both ugly to look at and aroudn 30 lines of code, and couldn't even find diagonals. the other 2 methods I thought of involve finding the first letter of the word.
##### Method 1  (the bad one)
###### after finding the first letter you could have a recursive function that simply checks in a direction and when it finds the final letter it returns true, if it finds the edge or a wrong letter it returns false.
```py
def find_word(grid, word, x, y, dx, dy):
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return False
    if grid[x][y] != word[0]:
        return False
    if len(word) == 1:
        return True
    return find_word(grid, word[1:], x+dx, y+dy, dx, dy)
# then you would call this function for every direction represented by tuples in the form (dx, dy)
directions = ((1, 0), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1), (0, -1), (-1, 0))
if letter == 'X':
    for direction in directions:
        if find_word(grid, 'MAS', x, y, direction[0], direction[1]):
            answer += 1
```
###### heres an example of this function, I don't like it though it does have a certain attraction for the part of me that loves recursive functions, I did originally solve using this kind of function but it was much worse than this.
##### Method 2 (the good one)(kinda)
###### This method is much simpler, you simply iterate through the grid until you find the first letter, then in one large if statement you check every position for the rest of the word at once, where the kinda comes in is that I didn't feel like making sure I was far enough from an edge.
```py
if letter == 'X':
    for direction in ((1, 0), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1), (0, -1), (-1, 0)):
        try: # probably not best practice but in this scenario it has no downsides
		    if data[x + dx][y + dy] == 'M' and data[x + 2 * dx][y + 2 * dy] == 'A' and data[x + 3 * dx][y + 3 * dy] == 'S':
			    answer += 1
        except:
			pass
```
###### I like this method a lot, its much simpler and easier to understand at a glance in my opinin, also I commited a little bit of a code crime by using a try except block to catch out of bounds errors, but in Advent of Code there is an element of speed involved to try and get in the top 100, not that I've even breached the top 1000 yet.

###### Anyways thanks for reading this, I'd say you can find me at ... but I don't actually have any social media platforms to find me on, and I'm not putting my discord account here where it can be scraped, not that I probably haven't done that inside some discord bot that I have message me when it generates errors.