#!/usr/bin/env python

import json, glob, re


#Bible content
with open('bible/eng/kjv.json') as data_file:
    data = json.load(data_file)
    for book in data:
        cd = {}
        for chapter in data[book]:
            cd[int(chapter)]=len(data[book][chapter].keys())
        ca = [None] * (len(cd.keys()))
        for i in range(len(cd.keys())):
            ca[i]= cd[i+1]
        print 'bible.put("'+book.lower()+'", new int[]{'+', '.join(str(v) for v in ca)+'})';
with open('quran/eng/pickthall.json') as data_file:
    data = json.load(data_file)
    cd = {}
    for chapter in data:
        cd[int(chapter)]=len(data[chapter].keys())-1
    ca = [None] * (len(cd.keys()))
    for i in range(len(cd.keys())):
        ca[i]= cd[i+1]
    print 'int[] quran = new int[]{'+', '.join(str(v) for v in ca)+'})';
with open('tao-te-ching/eng/tao-te-ching.json') as data_file:
    data = json.load(data_file)
    cd = {}
    for chapter in data:
        cd[int(chapter)]=len(data[chapter].keys())
    ca = [None] * (len(cd.keys()))
    for i in range(len(cd.keys())):
        ca[i]= cd[i+1]
    print 'int[] tao_te_ching = new int[]{'+', '.join(str(v) for v in ca)+'})';
