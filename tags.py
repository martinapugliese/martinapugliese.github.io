# lil' script to fetch all tags on posts (outside of categories ones)
# to see which ones have already been used and to which extent

import os
from collections import Counter

tags = []
filenames = [item for item in os.listdir('_posts') if '.DS_' not in item]
for filename in filenames:
    content = open('_posts/' + filename).readlines()
    for i in range(len(content)):
        if '---' in content[i] and i > 0:
            break
        else:
            line = content[i]
            if '  - ' in line and '---' not in line and '#' not in line:
                tags.append(line.replace('\n', ''))

c = Counter(tags)
print(c.most_common())
