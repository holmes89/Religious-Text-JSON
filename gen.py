#!/usr/bin/env python

import json, glob, re

p = re.compile(ur'([\w-]+)\/\w+\/([\w-]+)')
c = []
#Bible content
for filename in glob.glob('bible/eng/*'):
    name = re.findall(p, filename)[0];
    relbook = name[0];
    version = name[1]
    with open(filename) as data_file:
        print(filename)
        data = json.load(data_file)
        for book in data:
            for chapter in data[book]:
                for verse in data[book][chapter]:
                    content = data[book][chapter][verse]
                    obj = {}
                    obj['religiousText']=relbook
                    obj['version']=version
                    obj['book'] = book.lower()
                    obj['chapterTitle'] = ""
                    obj['chapter']=int(chapter)
                    obj['verse']=int(verse)
                    obj['content']=content
                    c.append(obj)
#Quran
for filename in glob.glob('quran/eng/*'):
    name = re.findall(p, filename)[0];
    relbook = name[0];
    version = name[1]
    with open(filename) as data_file:
        data = json.load(data_file)
        for chapter in data:
            for verse in data[chapter]:
                if verse=='name':
                    continue
                content = data[chapter][verse]
                chapter_name = data[chapter]['name']
                obj = {}
                obj['religiousText']=relbook
                obj['book'] = ""
                obj['version']=version
                obj['chapterTitle'] = chapter_name.lower()
                obj['chapter']=int(chapter)
                obj['verse']=int(verse)
                obj['content']=content
                c.append(obj)
#Tao
for filename in glob.glob('tao-te-ching/eng/*'):
    name = re.findall(p, filename)[0];
    relbook = name[0];
    version = name[1]
    with open(filename) as data_file:
        data = json.load(data_file)
        for chapter in data:
            for verse in data[chapter]:
                content = data[chapter][verse]
                obj = {}
                obj['religiousText']=relbook
                obj['book'] = ""
                obj['version']=version
                obj['chapterTitle'] = ""
                obj['chapter']=int(chapter)
                obj['verse']=int(verse)
                obj['content']=content
                c.append(obj)

#Write to file
with open("allTexts.json", "a+") as f:
    f.write("[")
    for obj in c:
        json.dump(obj, f)
        f.write(",\n")
    f.write("]")
