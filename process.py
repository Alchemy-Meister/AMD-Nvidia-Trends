import json, gzip, glob
for filename in glob.iglob('./tweets/*.txt.gz'):
    with gzip.open(filename, 'rb') as f:
        file_content = f.read()
        file_content = file_content.split('\n')
        if len(file_content) > 1:
            del file_content[-1]
            string_content = '{ "tweets": ['
            for tweet in file_content:
                string_content = string_content + tweet + ','
            string_content = string_content[:-1] + ']}'
            parsed = json.loads(string_content)
            
            with open('./corpus_new/all-tweets.json', 'w') as outfile:
                outfile.write(json.dumps(parsed, indent=4, sort_keys=True))