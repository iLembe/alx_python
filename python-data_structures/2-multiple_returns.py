def multiple_returns(sentence):\n    if not sentence:\n        return (0, None)\n    return (len(sentence), sentence[0])\n\n# Test cases\nresult1 = multiple_returns("Holberton")\nresult2 = multiple_returns("Holberton is so cool")\nresult3 = multiple_returns("H")\nresult4 = multiple_returns("")\n\nprint(f"Length: {result1[0]} - First character: {result1[1]}")\nprint(f"Length: {result2[0]} - First character: {result2[1]}")\nprint(f"Length: {result3[0]} - First character: {result3[1]}")\nprint(f"Length: {result4[0]} - First character: {result4[1]}")
