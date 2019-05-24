# Boggle-Word-Game

Boggle is a word game that is played on a 4x4 board with 16 letter tiles. The goal is to find as many words as possible. 
You are given a [dictionary](https://gist.github.com/monarch0111/bfd0c289c4aba000359b5386fedc7d96) (contains all the valid english word) and a board as string in format `A, C, E, D, L, U, G, I, E, F, H, T, G, A, F, K`

Above board can be shown in below format as 4x4

```
A C E D
L U G I 
E F H T
G A F K
```

Constraints while finding the word:
 - One cell if visited, cannot be repeated for a single word. Can be used while finding another word.
 - Movement is allowed in vertical, diagonal and horizontal directions

You need to implement a method `findWords` which accepts a parameter board(comma seperated string) and return an Array of words.

You are free to use any programming language / framework you want to.
