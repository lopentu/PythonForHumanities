# Week 7: Define functions
def count_distinct_characters(intext):
    # Week 3: Variables    
    sketch = []

    # Week 6: Looping
    for ch in intext:

        # Week 4: Conditionals
        if ch not in sketch:
            sketch.append(ch)
        else:
            pass
            
    n_element = len(sketch)
    n_character = len(intext)

    print(">>" + intext)
    print("這句話共有%d個字，用了%d個不同的字：" % (n_character, n_element))
    print(sketch)

# Week 8: Organize codes with functions
count_distinct_characters("尋尋覓覓冷冷清清淒淒慘慘戚戚")
count_distinct_characters("輕輕的我走了正如我輕輕的來")

