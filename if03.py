def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if b<a<c:
        return a
    if a<b<c:
        return b
    if a<c<b:
        return c
print(main(2,6,8))