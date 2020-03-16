import os
import pandas as pd

refs = 'my_text_file'
folder = 'folder_for_abstracts/'
prefix = 'xxx'


def convert_medline(refs):
    with open(refs) as data_file:
        block = ""
        found = False
        x = 0
        for line in data_file:
            if found:
                block += line
                if line.startswith("AID") or line.startswith("PST"):
                    x = x + 1
                    found = False
                    with open(folder + prefix + str(x) + ".txt", "w") as file:
                        file.write(block)
                        block = ""
            else:
                if line.startswith("PMID"):
                    found = True
                    block += line



all = []

def extract_info_abstract(folder):
    abstracts = [os.path.join(folder, f) for f in os.listdir(folder)]
    for abstract in abstracts:
        dict = {'PMID': 1234, 'Date': 1234, 'MESH tags':'empty'}
        mesh = []
        with open(abstract) as f:
            content = f.readlines()
            for line in content:
                if line.startswith('PMID'):
                    dict['PMID'] = line[5:]
                elif line.startswith('MH  -'):
                    mesh.append(line[5:])
                elif line.startswith('DP'):
                    dict['Date'] = line[5:]
            dict['MESH tags'] = mesh
        all.append(dict.copy())
        df = pd.DataFrame(all)
    print(df)
    df.to_csv('file_name.csv', encoding='utf-8', index=False)


