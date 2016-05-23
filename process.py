import json, gzip, glob
for filename in glob.iglob('./tweets/*.txt.gz'):
    with gzip.open(filename, 'rb') as f:
        file_content = f.read()
        file_content = file_content.split('\n')
        if len(file_content) > 1:
            del file_content[-1]
            string_content = ''
            for tweet in file_content:
                string_content = string_content + tweet + '\n'
            
            with open('./tweets/all-tweets.json', 'w') as outfile:
                outfile.write(string_content)