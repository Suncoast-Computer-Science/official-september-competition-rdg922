# September Programming Competition

Official Suncoast Programming Competition!

## How to submit problems

Each problem has a filename, make sure to name your file for that problem as so

## Checking your problems

When you push your changes to github it will show you in the actions tab the status for each problem
You MUST get the points for each question in order to actually complete the problem. Points are not reflective of your score.

## Goodbye!

*Filename:* goodbye.py

Problem: Say goodbye to the user, taking in their name as a string!

Example Input: 

```
Bob
```

Example Output:

```
Goodbye Bob!
```

## Cookie

*Filename:* cookie.py

Problem: Sam has *x* cookies. Bob has *y* cookies. Sam gives Bob all her cookies. How many does Bob have after Sam gives Bob her cookies?

Example Input: 

```
1
2
```

Example Output:

```
3
```

## Numbers:

*Filename:* numbers.py

You will be given an integer *n*. Print "True" if *n* is within 10 of 100 (including +10 and -10) and "False" if it is not.

Example Input 1:

```
110
```

Example Output 1:

```
True
```

Example Input 2:

```
211
```

Example Output 2:

```
False
```


## Data Length

*Filename:* data.py

Problem: A company is collecting data on how many families plan on attendeing an event. The company wants to data store about how many people are attending their event but they may not have enough room to store the number if it is to long. The average family attending is a family of 5. Given the number of familys attending return the length of the number of people attending.

Example Input:

```
392
```

Example Output:

```
4
```

## Swapping

*Filename:* swapping.py

Problem: John has a database of names, but due to a glitch, John's names are bugged and have the last and first letter swapped! For integer *tc* names, swap the last and first letters of names

Example Input:
```
3
boR
tohiR
yancN
```

Example Output:

```
Rob
Rohit
Nancy
```

Example Input 2:

```
1
Bruh
```

Example Output 2:

```
hruB
```

## Crossword

*Filename:* crossword.py

Problem: Felipe wants to know if he can the combination of a prefix and a word will fit in his crossword puzzle. You will be given two strings, a prefix and a word, and you wil be given the length of the correct answer. If the word is the correct length, return the word (body following the prefix). The order you will recieve the prefix and word body will not be consistent. If the word does not fit return "False". Tip: The prefix will always be shorter than the body.

Example Input 1:

```
value
de
7
```

Example Output 1:

```
devalue
```

Example Input 2:

```
dis
appear
8
```

Example Output 2:

```
False
```

## Laser Tag

*Filename:* laser.py

Problem: A laser tag company wants a program that will retern a games team scores ordered. The first number inputed will be how many people played there is always an even number of players. Then each players socre will be inputed. Each team is grouped together so the first and second palyer would be on a team, the third and frouth player will be on a team, and so on. You should out put the team scores in an list ordered from least to greatest.

Example Input:

```
8
48
53
24
36
62
23
45
57
```

Example Output:

```
[60, 85, 101, 102]
```

## Diamonds

*Filename:* diamonds.py

Problem: A student is bored in class and is trying to make diamond shapes out of asterics. The student wants the diamonds to be symetrical and vary in size. Your input will be how many diamonds you should output (it will always be and odd amount). You should output teh amount of diomands requested with a space between each one. The middle diamond should be the largest and the first and last diamonds should be the smallest. Your output should be symmetrical.

Example Input 1:

```
7
```
Example Output 1:

```
*
 
 *
***
 *
 
  *
 ***
*****
 ***
  *
 
   *
  ***
 *****
*******
 *****
  ***
   *
 
  *
 ***
*****
 ***
  *
 
 *
***
 *
 
*
```

Example Input 2:

```
3
```

Example Output 2:

```
*
 
 *
***
 *
 
*
```

## Parenthesis:

*Filename:* parenthesis.py

Problem: Sally's daughter wrote a mess or open and close parenthesis and is asking if the string is valid. For *tc* number of strings, check if they are valid and print "True" or "False". A valid string is one that opens and closes properly.

Example Input 1:

```
4
()
(()())
())(()
)(
```

Example Output 1:

```
True
True
False
False
```

Example Input 2:

```
2
)
(
```

Example Output 2:

```
False
False
```
