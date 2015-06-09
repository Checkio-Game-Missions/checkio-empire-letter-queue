We will emulate the queue process with letters. You are given a sequence of commands:

- "PUSH X" -- enqueue **X**, where **X** is a letter in uppercase.
- "POP" -- dequeue the front position. if the queue is empty, then do nothing.

The queue can only contain letters.

You should process all commands and assemble letters 
which remain in the queue in one word from the front to the back of the queue.

`["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]`

| Command | Queue | Note
|:-------:|:-----:|:----:
| PUSH A  | A     | Added "A" in the empty queue
| POP     |       | Removed "A"
| POP     |       | The queue is empty already
| PUSH Z  | Z     |
| PUSH D  | ZD    |
| PUSH O  | ZDO   |
| POP     | DO    |
| PUSH T  | DOT   | The result
