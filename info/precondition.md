**Precondition:**

```python
0 <= len(commands) <= 30
all(re.match("\APUSH [A-Z]\Z", c) or re.match("\APOP\Z", c) for c in commands)
```