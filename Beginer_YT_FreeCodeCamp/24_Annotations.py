# Annotations

# Without annotation
def incr(n):
    return n+1

# With int annotation
# This int is ignored by IDE and python at runtime
def increment(n: int) -> int :
    return n+1

count: int =0


