# 12.8 LAB: Words in a range (lists)

## Description
This program reads words from a file and determines whether each word falls within a specified alphabetical range.

## How it works
1. The program takes three inputs:
   - A filename containing words (one per line)
   - A lower bound string
   - An upper bound string

2. It reads all words from the specified file

3. For each word, it checks if the word is alphabetically between the lower and upper bounds (inclusive)

4. It outputs whether each word is "in range" or "not in range"

## Input Format
```
filename.txt
lower_bound
upper_bound
```

## Output Format
For each word in the file:
```
word - in range
```
or
```
word - not in range
```

## Example
If the file `words.txt` contains:
```
apple
banana
cherry
grape
```

And the inputs are:
```
words.txt
banana
grape
```

The output would be:
```
apple - not in range
banana - in range
cherry - in range
grape - in range
```

## Implementation Notes
- Uses string comparison for alphabetical ordering
- Reads the entire file into memory as a list
- Strips whitespace from each word before comparison
- Range comparison is inclusive (both bounds are included)
