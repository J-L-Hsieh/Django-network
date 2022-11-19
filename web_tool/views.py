# -*- coding: UTF-8 -*-
from cgitb import html
from dataclasses import replace
from http.client import HTTPResponse
from operator import contains
import os,sys
from select import select
import sqlite3
import re
from re import search
from posixpath import split
from pprint import pprint
from traceback import print_tb
from urllib import response
from webbrowser import get
from web_tool.python.enrichment import enrichment_program
from web_tool.python.yeast_associated import associated_analysis
# import web_tool.python.enrichment_program


import pymysql
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from web_tool.models import Wormbase, Gene,WormbaseGenetranscriptW285,TranscriptWbidType,DiseaseAll,GeneticInteractionAll,GoCAll,GoFAll,GoPAll,PathwayAll,PhenotypeAll,PhysicalInteractionAll,ProteinDomainAll,RegulatorAll

import pandas as pd
import json
import time
''' -------------------------------分頁管理---------------------------------'''
def index(request):
    return render(request, 'index.html', locals())
def wormbase(request):
    return render(request,'wormbase.html',locals())
def pirscan(request):
    return render(request,'pirscan.html',locals())
def search(request):
    return render(request,'search.html',locals())
def browser(request):
    return render(request,'browser.html',locals())
def detail (request,pk):
    return render(request,'detail.html',locals())
def enrichment(request):
    return render(request,'enrichment.html',locals())
def domain(request,pk):
    return render(request,'domain.html',locals())
def yeast(request):
    return render(request,'yeast_browse.html',locals())
def yeast_associated_base(request):
    return render(request,'yeast_associated.html',locals())
def yeast_name_base(request):
    return render(request,'yeast_name.html',locals())
# --------------------------------------------------------------------------------------------
def ajax_wormbase(request):
    name = request.POST['wormbase_search']
    try:
        if Wormbase.objects.filter(wormbase_id = name):
            gene = Wormbase.objects.get(wormbase_id = name)

        elif Wormbase.objects.filter(sequence_name = name):
            gene = Wormbase.objects.get(sequence_name = name)

        elif Wormbase.objects.filter(gene_name = name):
            gene = Wormbase.objects.get(gene_name = name)

        elif Wormbase.objects.filter(other_name = name):
            gene = Wormbase.objects.get(other_name = name)

        wormbase_id = gene.wormbase_id
        Sequence = gene.sequence_name
        gene_name = gene.gene_name
        other_name = gene.other_name
    except:
        wormbase_id = "error"
        Sequence = ''
        gene_name = ''
        other_name = ''

    response = {
        'wormbase_id' : wormbase_id,
        'Sequence':Sequence,
        'gene_name':gene_name,
        'other_name':other_name
    }
    return JsonResponse(response)

#靜態爬蟲爬取wormbase id之json檔 並整理成table
import urllib.request as req
def ajax_data(request):
    gene_id = request.POST['gene_id']
    try:
        url = 'https://wormbase.org/rest/widget/gene/'+gene_id+'/sequences'
        request = req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        })
    except:
        url = 'https://wormbase.org/species/c_elegans/transcript/'+gene_id
        request = req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        })

    with req.urlopen(request) as response:
        dat = response.read().decode("utf-8")
    dat = json.loads(dat)
    # print(dat)
    dat =(dat['fields']['gene_models']['data']['table'])
    data =[]
    for i in range(len(dat)):
        try :
            data.append({'Transcript': dat[i]['model']['id'],'Type' : dat[i]['type'], 'Length' : dat[i]['length_unspliced'],'CDS':dat[i]['cds']})
        except:
            data.append({'Transcript': dat[i]['model'][0]['id'],'Type' : dat[i]['type'][0],'Length' : dat[i]['length_unspliced'][0],'CDS':dat[i]['cds']['text']['id']})
    response = {'data':data}
    print(data)
    return JsonResponse(response)

'''-------------------------------------------detail-------------------------------------------'''
# 靜態爬蟲
import urllib.request as req

def ajax_crawler(request):
    # print(request)
    search = request.POST.get('transcript')
    print(search)
    url = 'https://wormbase.org/rest/widget/transcript/{}/sequences'.format(search)

    request = req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        data = json.loads(data)

    # print(data)
    # 判斷strand

    if str(data['fields']['protein_sequence']['data']) == 'None':
        if data['fields']['spliced_sequence_context']['data']['strand'] == '+' :
        # spliced_sequence_table = gene_table(data['fields']['spliced_sequence_context']['data']['positive_strand']['sequence'])
        # spliced_sequence_table = spliced_sequence_table.to_html()

        # spliced data
            spliced_sequence = data['fields']['spliced_sequence_context']['data']['positive_strand']['sequence']
            spliced_feature = data["fields"]["spliced_sequence_context"]["data"]["positive_strand"]["features"]

        # unspliced data
            unspliced_sequence = data['fields']['unspliced_sequence_context']['data']['positive_strand']['sequence']
            unspliced_feature = data["fields"]["unspliced_sequence_context"]["data"]["positive_strand"]["features"]
            unspliced_feature_table = feature_table(data["fields"]["unspliced_sequence_context"]["data"]["positive_strand"]["features"]).to_html()

        # prorein
            cds = 'no cds'


        else:
            spliced_sequence = data['fields']['spliced_sequence_context']['data']['negative_strand']['sequence']
            spliced_feature = data["fields"]["spliced_sequence_context"]["data"]["negative_strand"]["features"]
        # unspliced data
            unspliced_sequence = data['fields']['unspliced_sequence_context']['data']['negative_strand']['sequence']
            unspliced_feature = data['fields']['unspliced_sequence_context']['data']['negative_strand']['features']
            unspliced_feature_table = feature_table(data["fields"]["unspliced_sequence_context"]["data"]["negative_strand"]["features"]).to_html()

        # prorein
            cds= 'no cds'
    else:

        if data['fields']['spliced_sequence_context']['data']['strand'] == '+' :
        # spliced_sequence_table = gene_table(data['fields']['spliced_sequence_context']['data']['positive_strand']['sequence'])
        # spliced_sequence_table = spliced_sequence_table.to_html()
        # spliced data
            spliced_sequence = data['fields']['spliced_sequence_context']['data']['positive_strand']['sequence']
            spliced_feature = data["fields"]["spliced_sequence_context"]["data"]["positive_strand"]["features"]
        # unspliced data
            unspliced_sequence = data['fields']['unspliced_sequence_context']['data']['positive_strand']['sequence']
            unspliced_feature = data["fields"]["unspliced_sequence_context"]["data"]["positive_strand"]["features"]
            unspliced_feature_table = feature_table(data["fields"]["unspliced_sequence_context"]["data"]["positive_strand"]["features"]).to_html()


        # prorein
            protein_sequence_table = protein_sequence_table.to_html()

        else:
            spliced_sequence = data['fields']['spliced_sequence_context']['data']['negative_strand']['sequence']
            spliced_feature = data["fields"]["spliced_sequence_context"]["data"]["negative_strand"]["features"]
        # unspliced data
            unspliced_sequence = data['fields']['unspliced_sequence_context']['data']['negative_strand']['sequence']
            unspliced_feature = data['fields']['unspliced_sequence_context']['data']['negative_strand']['features']
            unspliced_feature_table = feature_table(data["fields"]["unspliced_sequence_context"]["data"]["negative_strand"]["features"]).to_html()

        # prorein
            cds = data['fields']['protein_sequence']['data']['sequence']
    if cds =='no cds':
        cds_sequence = 'no cds'
        spliced_feature_table = feature_table(spliced_feature).to_html()
    else:
        cds_sequence = CDS(spliced_sequence,spliced_feature)
        spliced_feature_table = feature_table(spliced_feature).to_html()
        del spliced_feature[-1]
    spliced_feature_table = spliced_feature_table.replace('table','table id = "table_id1" class = "table table-striped table-hover"',1)
    unspliced_feature_table = unspliced_feature_table.replace('table','table id = "table_id2" class = "table table-striped table-hover" ',1)

    # print(cds)
    response={
        'spliced_feature_table' : spliced_feature_table ,
        'spliced_feature' : spliced_feature,
        'spliced_sequence':spliced_sequence,

        'unspliced_sequence' : unspliced_sequence,
        'unspliced_feature' : unspliced_feature,
        'unspliced_feature_table' : unspliced_feature_table ,

        'cds': cds,
        'cds_sequence' : cds_sequence
    }

    return JsonResponse(response)

# 製作特徵表
def feature_table(feature):
    j=1
    k=1
    _index = []
    for i in range(len(feature)):
        if feature[i]['type'] == 'exon':
            if j%2 == 1:
                feature[i]['type'] = 'exon_odd'
            elif j%2 == 0:
                feature[i]['type'] = 'exon_even'
            _index.append('Exon'+str(j))
            j = j+1
        elif feature[i]['type'] == 'intron':
            _index.append('Intron'+ str(k))
            k=k+1
        else:
            _index.append(feature[i]['type'])

    _index = pd.Series(_index)
    feature = pd.DataFrame(feature)
    # print(_index)

    # feature.drop(['type'])
    feature = feature.set_index(_index)[['start','stop']]
    feature['length'] =  feature['stop'] - feature['start'] + 1
    # print(feature)

    return feature


def CDS(spliced_sequence,spliced_feature_withcds):
    start = ''
    stop =''
    for i in range(len(spliced_feature_withcds)-1):
        if(spliced_feature_withcds[i]['start'] == spliced_feature_withcds[i+1]['start']):
            if(spliced_feature_withcds[i]['type'] == 'five_prime_UTR'):
                start = spliced_feature_withcds[i]['stop']+1
            else:
                start = spliced_feature_withcds[i+1]['stop']+1

        if(spliced_feature_withcds[i]['stop'] == spliced_feature_withcds[i+1]['stop']):
            if(spliced_feature_withcds[i]['type']) == 'three_prime_UTR':
                stop = spliced_feature_withcds[i]['start']-1
            else:
                stop = spliced_feature_withcds[i+1]['start']-1
    if start == '' :
        start = spliced_feature_withcds[0]['start']
    if stop  == '' :
        stop = spliced_feature_withcds [-1]['stop']
    cds = spliced_sequence[start-1:stop-3]

    spliced_feature_withcds.append({'type':'cds','start':start,'stop':stop})
    return cds

'''-----------------------------------------pirscan------------------------------------------'''
def PirScan (request):
    search = request.POST.get('search')
    print(search)
    url = 'https://wormbase.org/rest/widget/transcript/{}/sequences'.format(search)

    request = req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        data = json.loads(data)

    # print(data)
    # 判斷strand

    if str(data['fields']['protein_sequence']['data']) == 'None':
        if data['fields']['spliced_sequence_context']['data']['strand'] == '+' :
        # spliced data
            spliced_sequence = data['fields']['spliced_sequence_context']['data']['positive_strand']['sequence']
        else:
            spliced_sequence = data['fields']['spliced_sequence_context']['data']['negative_strand']['sequence']
    else:
        if data['fields']['spliced_sequence_context']['data']['strand'] == '+' :
            spliced_sequence = data['fields']['spliced_sequence_context']['data']['positive_strand']['sequence']
        else:
            spliced_sequence = data['fields']['spliced_sequence_context']['data']['negative_strand']['sequence']

    with open('../pirScan/inputSeq.fa','w') as in1:
        in1.write(search+'\n')
        in1.write(spliced_sequence)

    os.chdir('../pirScan/')
    os.system('python piTarPrediction.py inputSeq.fa ce none [0,2,2,3,6]')

    with open('output/piRNA_targeting_sites.json','r') as output:
        output = json.load(output)
    name = output['name']
    result=[]
    for i in range(len(output['newout'])):
        result.append({'piRNA':output['newout'][i][0],'target':output['newout'][i][1],'score':output['newout'][i][14],'position':output['newout'][i][3],'pairing':output['newout'][i][9]+'<br>'+output['newout'][i][10]})

    response = {'result':result,'name':name}
    return  JsonResponse(response)
'''---------------------------------------search mode----------------------------------------'''
def mode1(request):

    search = request.POST.get('search1')

    name = request.POST.get('search1')
    if TranscriptWbidType.objects.filter(transcript = name):
        gene = TranscriptWbidType.objects.get(transcript = name)
        name = gene.wormbase_id

    try:
        if WormbaseGenetranscriptW285.objects.filter(wormbase_id = name):
            gene = WormbaseGenetranscriptW285.objects.get(wormbase_id = name)
        wormbase_id = gene.wormbase_id
        Sequence = gene.sequence_name
        gene_name = gene.gene_name
        other_name = gene.other_name
        transcript = gene.transcript
        gene_type = gene.type
        # else:
    except:
        wormbase_id = "error"
        Sequence = ''
        gene_name = ''
        other_name = ''
        transcript = ''
        gene_type = ''
    index1 = TranscriptWbidType.objects.filter(wormbase_id = name)
    transcript = str(transcript).replace('[','').replace(']','').replace("'",'').replace(' ','').split(',')
    gene_type = str(gene_type).replace('[','').replace(']','').replace("'",'').split(',')
    table2_data = []
    for i in range(len(transcript)):
        table2_data.append({'transcript':transcript[i],"gene_type":gene_type[i]})
    print(table2_data)

    response = {
        'search':search,
        'wormbase_id' : wormbase_id,
        'Sequence':Sequence,
        'gene_name':gene_name,
        'other_name':other_name,
        'table2_data':table2_data,
    }
    print(response)
    return  JsonResponse(response)
'''---------------------------------------browser type----------------------------------------'''
def browser_type(request):
    data = dict(request.POST)
    data = data['checkboxvalue[]']
    sql = str(data).replace('[','(').replace(']',')')
    print(sql)

    try:
        conn = sqlite3.connect('db.sqlite3')
        db_cursor = conn.cursor()
        select = f"""SELECT Wormbase_id,transcript,type FROM transcript_wbid_type
                            WHERE type IN %s;"""
        print(select)
        print(sql)
        db_cursor.execute(select % sql)
        data = db_cursor.fetchall()
    finally:
        conn.close()
    table =[]
    for i in range(len(data)):
        table.append({'Wormbase ID':data[i][0],'transcript':data[i][1],'type':data[i][2]})

    response = {'table':table}
    return JsonResponse(response)
''' ------------------------------------------------------enrichment-----------------------------------------------------------------'''
@csrf_exempt
def enrichment_analysis(request):
    input_list = request.POST.get('input_name')
    # input_list = input_list.replace('\n',',').replace(' ','').replace(',','').split('\r')
    type_input = request.POST.get('type')
    p = request.POST.get('p')
    # print(p)
    result = enrichment_program(input_list,type_input,p)
    all_table =result[1]
    result = result[0]
    response = {'result':result,'all_table':all_table}
    print(all_table)
    return JsonResponse(response)

    '''------------------------------------------------------yeast_browser------------------------------------------------------------------'''
def yeast_browser(request):
    table_name = request.POST.get('first_feature')
    table_column = request.POST.get('other_feature')[:-1]
    table_column = 'SELECT '+ table_name+ ',' + table_column
    table_name = 'FROM '+ table_name +'_all'
    print(table_column)
    print(table_name)
    try:
        connect = sqlite3.connect('db.sqlite3')
        select = table_column + ' ' + table_name
        table = pd.read_sql('%s' %select, connect)
    finally:
        connect.close()
    table = table.fillna('-')
    detail_column = ['-']*len(table)
    table['Detail'] = detail_column
    table = table.to_html(table_id='result_table',index= None,classes="table table-striped table-bordered")
    # print(table)
    response = {'table':table}
    return JsonResponse(response)

'''------------------------------------主物種與其他物種的關係數量---------------------------------'''
def yeast_associated(request):
    # print(request)
    table_name = request.POST.get('table_name')
    row_name = request.POST.get('row_name')

    try:
        connect = sqlite3.connect('db.sqlite3')
        select = 'SELECT * FROM ' + table_name +'_all WHERE '+table_name +" IN ('" +row_name +"')"
        print(select)
        table = pd.read_sql('%s' %select, connect)
    finally:
        connect.close()
    '''---------------------刪除不必要的欄位------------------------'''
    associated_table = table.dropna(axis='columns')
    all_tables = associated_analysis(associated_table)
    associated_table = associated_table.drop(['count','SystematicName'],axis=1)
    #拿出column name
    associated_table = associated_table.to_html(table_id='associated_table',index= None,classes="table table-striped table-bordered")
    response={'associated_table':associated_table , 'all_tables':all_tables}
    return JsonResponse(response)
'''------------------------------------------------------------------------------------------'''
def yeast_name(request):
    first_feature = request.POST.get('first_feature')
    second_feature = request.POST.get('second_feature')
    first_feature = first_feature.split(':')
    second_feature = second_feature.split(':')
    # print(first_feature)
    try:
        connect = sqlite3.connect('db.sqlite3')
        for  i in range(2):
            if i == 1:
                select = 'SELECT count,SystematicName FROM ' + first_feature[0] +'_all WHERE '+first_feature[0] +" IN ('" +first_feature[1] +"')"
                first_table = pd.read_sql('%s' %select, connect)
                print(select)

            select = 'SELECT count,SystematicName FROM ' + second_feature[0] +'_all WHERE '+second_feature[0] +" IN ('" +second_feature[1] +"')"
            second_table = pd.read_sql('%s' %select, connect)
    finally:
        connect.close()

    first_names = eval(first_table.iat[0,1])
    second_names = eval(second_table.iat[0,1])
    print(type(len(second_names)))
    first_name_table = pd.DataFrame(list(zip(first_names,['true']*len(first_names))),columns=['all','%s'%first_feature[1]])
    second_name_table = pd.DataFrame(list(zip(second_names,['true']*len(second_names))),columns=['all','%s'%second_feature[1]])
    df_merge = pd.merge(first_name_table,second_name_table,how="outer")
    df_merge = df_merge.fillna('false').to_html(table_id='both_name_table',index=None,classes='table table-striped table-bordered')

    response = {'df_merge':df_merge}
    return JsonResponse(response)