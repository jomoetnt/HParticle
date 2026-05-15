import io

subpagePaths = {'jeffHome.html': 'index.html', 'jeffArticles.html': 'articles/index.html'}
tokenPaths = {r'{jeffHeader}': 'header.html'}

subpageTexts = {}
tokenTexts = {}

# read token files
for tokenPath in list(tokenPaths.values()):
    with open(tokenPath, 'r', encoding='utf-8') as tokenFile:
        tokenTexts[tokenPath] = tokenFile.read()

# read input files and make replacements
for pagePath in list(subpagePaths.keys()):
    with open(pagePath, 'r', encoding='utf-8') as pageFile:
        subpageTexts[pagePath] = pageFile.read()
        for token in list(tokenTexts.keys()):
            subpageTexts[pagePath] = subpageTexts[pagePath].replace(token, tokenTexts[token])

# write output files
for pagePath in list(subpageTexts.keys()):
    with open(subpagePaths[pagePath], 'w', encoding='utf-8') as pageFile:
        pageFile.write(subpageTexts[pagePath])