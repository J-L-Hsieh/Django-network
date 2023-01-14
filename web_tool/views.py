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
from web_tool.python.yeast_network import network
from web_tool.python.yeast_modal import modal

from .wormbase import wormbase_crawler,wormbase_searching
# import web_tool.python.enrichment_program

from operator import itemgetter

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from web_tool.models import Wormbase, Gene,WormbaseGenetranscriptW285,TranscriptWbidType,FinalResultWt1HrdeipWs285AllWithIdtype

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
    return render(request, 'domain.html',locals())

def result_base(request):
    return render(request,'result.html',locals())


def yeast(request):
    return(render(request,'yeast_browse.html',locals()))
def yeast_associated_base(request):
    return(render(request,'yeast_associated.html',locals()))
def yeast_name_base(request):
    return(render(request, 'yeast_name.html',locals()))
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
            cds = data['fields']['protein_sequence']['data']['sequence']

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

    for i in range(len(spliced_feature)):
        if spliced_feature[i]['type'] == 'five_prime_UTR':
            spliced_feature.append(spliced_feature[i])
        elif spliced_feature[i]['type'] == 'three_prime_UTR':
            spliced_feature.append(spliced_feature[i])

    for i in range(len(unspliced_feature)):
        if unspliced_feature[i]['type'] == 'five_prime_UTR':
            unspliced_feature.append(unspliced_feature[i])
        elif unspliced_feature[i]['type'] == 'three_prime_UTR':
            unspliced_feature.append(unspliced_feature[i])

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
    # table_column = "SELECT "+ table_name+ "," + table_column
    # table_name = "FROM "+ table_name +"_all"

    sql = f"""
        SELECT `%s(Queried)`, %s, %s FROM %s_1_to_10;
    """%(table_name, table_name, table_column, table_name)
    # print(sql)
    # print(table_column)
    # print(table_name)
    try:
        connect = sqlite3.connect('db.sqlite3')
        table = pd.read_sql(sql, connect)
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
        select = f"""
            SELECT * FROM %s_1_to_10 WHERE `%s(Queried)` IN ('%s');
        """%(table_name, table_name, row_name)
        print(select)
        table = pd.read_sql('%s' %select, connect)
    finally:
        connect.close()
    '''---------------------刪除不必要的欄位------------------------'''
    associated_table = table.dropna(axis='columns')
    all_tables = associated_analysis(associated_table)
    network_data = network(associated_table)
    associated_table = associated_table.drop(['count','SystematicName'],axis=1)
    #拿出column name
    associated_table = associated_table.to_html(table_id='associated_table',index= None,classes="table table-striped table-bordered")
    response={'associated_table':associated_table , 'all_tables':all_tables, 'network_data':network_data}
    return JsonResponse(response)
'''------------------------------------------------------------------------------------------'''
def yeast_name(request):
    first_feature = request.POST.get('first_feature')
    second_feature = request.POST.get('second_feature')
    first_feature = first_feature.split('$')
    second_feature = second_feature.split('$')
    print(first_feature)
    print(second_feature)
    try:
        connect = sqlite3.connect('db.sqlite3')
        for  i in range(2):
            if i == 1:
                select = """
                    SELECT count,SystematicName FROM %s_1_to_10 WHERE `%s(Queried)` IN ('%s')
                """%(first_feature[0], first_feature[0], first_feature[1])
                first_table = pd.read_sql('%s' %select, connect)
                # print(select)
            else:
                select = """
                    SELECT count,SystematicName FROM %s_1_to_10 WHERE `%s(Queried)` IN ('%s')
                """%(second_feature[0], second_feature[0], second_feature[1])
                second_table = pd.read_sql('%s' %select, connect)
    finally:
        connect.close()

    print(first_table)
    first_names = eval(first_table.iat[0,1])
    second_names = eval(second_table.iat[0,1])
    print(type(len(second_names)))
    first_name_table = pd.DataFrame(list(zip(first_names,['true']*len(first_names))),columns=['all','%s'%first_feature[1]])
    second_name_table = pd.DataFrame(list(zip(second_names,['true']*len(second_names))),columns=['all','%s'%second_feature[1]])
    df_merge = pd.merge(first_name_table,second_name_table,how="outer")
    df_merge = df_merge.fillna('false').to_html(table_id='both_name_table',index=None,classes='table table-striped table-bordered')

    response = {'df_merge':df_merge}
    return JsonResponse(response)

def yeast_modal(request):
    evidence_table = modal(request)
    response ={'evidence_table':evidence_table}
    return JsonResponse(response)

# -----------------------------------------------pirscan---------------------------------------------------------
# def pirscan_output(request,pk):

#     return render(request,'pirscan_output.html',locals())


def result_pirscan(request):
    transcript = request.POST['gene_id']

    try:
        spliced_fin,sequence_fin,exon_intron,exon,protein = wormbase_crawler(transcript= transcript)
        #spliced = ''.join(c for c in spliced_fin if c.isupper())
        current_address = os.getcwd()
        os.chdir('/home/chunlin/Desktop/pirScan')
        with open ('inputSeq.fa','w') as f:
            f.write('>{}\n'.format(transcript)+spliced_fin)
        os.system('python3 piTarPrediction.py inputSeq.fa ce none [0,2,2,3,6]')
        os.chdir(current_address)

    except Exception as e:
        print(e)

    spliced_fin,sequence_fin,exon_intron,exon,protein = wormbase_crawler(transcript= transcript)
    exon = exon.sort_values(by='stop').reset_index(drop=True)
    exon_type = exon['type'].to_json(orient='records')
    exon_start = exon['start'].to_json(orient='records')
    exon_stop = exon['stop'].to_json(orient='records')
    #with open ('sequence.fa','w') as f:
    #    f.write('>\n{}'.format(sequence))
    #os.system('python3 piTarPrediction.py sequence.fa ce whole [0,2,2,3,6]')
    current_address = os.getcwd()
    os.chdir('/home/chunlin/Desktop/pirScan/output')
    '''for pirscan '''
    try:
        with open ('/home/chunlin/Desktop/pirScan/output/piRNA_targeting_sites.json','r') as jsondata:
            data = json.load(jsondata)
        with open('/home/chunlin/Desktop/pirScan/inputSeq.fa','r') as f:
            length = f.readlines()
        os.remove('piRNA_targeting_sites.json')
        os.chdir(current_address)
        newout = data['newout']
        total_json_list = []
        for item in newout:
            index = item[10].find("5'")
            start_end =item[1].split('-')
            modify_string_2 = item[10].replace('mark',"span class='y'")
            dict1 = {'piRNA name':item[0],
                    'piRNA target score':item[14],
                    'target region':item[1],
                    '# mismatches':item[2],
                    'position in piRNA':item[3],
                    '# non-GU mismatches in seed region':item[5],
                    '# GU mismatches in seed region':item[6],
                    '# non-GU mismatches in non seed region':item[7],
                    '# Gu mismatches in non seed region':item[8],
                    'pairing (top:Input sequence, bottom:piRNA)':item[9]+'<br>'+modify_string_2,
                    'start':int(start_end[0]),
                    'end':int(start_end[1]),
                    'y':0
                    }
            total_json_list.append(dict1)
        total_json_list = sorted(total_json_list, key=itemgetter('start')) #排序list
        '''
        for i in range(len(total_json_list)):
            print(total_json_list[i]['start'])
            print('==================================')
        '''
        cover  = 1
        count = 0
        y = 0
        y_list = [0]
        first = 1
        while cover != 0:
            cover = 0
            start = 0
            end = 0
            first = 1
            #繪製Y的高度這邊比對方式是，如果有與同一層的前一項重疊，則高度往上加，但這樣判斷會有錯誤，因為可能與前一層有重疊，但沒與更低層重疊
            for i in range(0,len(total_json_list)):
                if total_json_list[i]['y'] == y:
                    if first == 1:
                        start = total_json_list[i]['start']
                        end = total_json_list[i]['end']
                        first = 0
                    elif first != 1 :
                        #先判斷目前的開始點是否有被包在前一點的start以及end內，判斷完後再將start、end設定成現在判斷的start、end，讓下一個判斷使用
                        #若有判斷到，則y會加一層
                        if (total_json_list[i]['start'] > start) and (total_json_list[i]['start'] < end):
                            total_json_list[i]['y'] = y+2.1
                            cover = 1
                        elif (total_json_list[i]['start'] == start):
                            total_json_list[i]['y'] = y+2.1
                            cover = 1
                        elif (total_json_list[i]['start'] == end):
                            total_json_list[i]['y'] = y+2.1
                            cover = 1

                        else:
                            start = total_json_list[i]['start']
                            end = total_json_list[i]['end']
                            pass
            #print('========================================')
            y += 2.1
            y_list.append(y)
        y+=4.2
        y_list_inverse = y_list[::-1]

        #做y軸座標校正(讓排序在網頁上面看起來是由下往上排列，這邊做顛倒的動作，讓原本設定y為0的地方顛倒到y為序列中最大值,
        #原本為最大值的校正為0，這樣最大值就會在頁面的最上方，由上往下畫圖)
        for i in range(len(total_json_list)):
            index = y_list.index(total_json_list[i]['y'])
            total_json_list[i]['y'] = y_list_inverse[index]
        '''for 22G'''
        try:
            '''
            讀入22G的資料表，依造request得到的transcript搜尋相對應的資料(應該會有多筆資料，每筆的欄位會有開始點、結束點跟權重)
            回傳json檔案，單個元素裡面包含該22G的:開始點，結束點，權重，並將這份json檔案回傳，回傳後依造權重給予高度，開始結束點繪出結合位置，
            '''
            g22 = list(FinalResultWt1HrdeipWs285AllWithIdtype.objects.filter(ref_id=transcript).values())
            ls = sorted(g22, key=itemgetter('init_pos'))
            cover =1
            while cover !=0:
                count +=1
                start = 0
                end = 0
                first = 1
                cover = 0
                for i in range(0,len(ls)):
                    if first == 1:
                        start = ls[i]['init_pos']
                        end = ls[i]['end_pos']
                        height = ls[i]['evenly_rc']
                        index = i
                        first = 0
                    elif first != 1 :
                        if (ls[i]['init_pos'] > start) and (ls[i]['init_pos'] < end) and (ls[i]['end_pos']<end):
                            init_1 = start
                            end_1 = ls[i]['init_pos']-1
                            height_1 = height
                            init_2 = ls[i]['init_pos']
                            end_2 = ls[i]['end_pos']
                            height_2 = height+ls[i]['evenly_rc']
                            init_3 = ls[i]['end_pos']+1
                            end_3 = end
                            height_3 = height
                            remove_indices = [index,i]
                            ls = [k for o, k in enumerate(ls) if o not in remove_indices]
                            ls.append({'input_id':0,'ref_id':0,'wormbase_id':0,'type':0,'init_pos':init_1,'end_pos':end_1,'read_count':0,'field_ofanswers':0,'evenly_rc':height_1})
                            ls.append({'input_id':0,'ref_id':0,'wormbase_id':0,'type':0,'init_pos':init_2,'end_pos':end_2,'read_count':0,'field_ofanswers':0,'evenly_rc':height_2})
                            ls.append({'input_id':0,'ref_id':0,'wormbase_id':0,'type':0,'init_pos':init_3,'end_pos':end_3,'read_count':0,'field_ofanswers':0,'evenly_rc':height_3})
                            ls= sorted(ls, key=itemgetter('init_pos'),reverse=False)
                            cover = 1
                            break
                        elif (ls[i]['init_pos'] > start) and (ls[i]['init_pos'] < end) and (ls[i]['end_pos']>end):
                            init_1 = start
                            end_1 = ls[i]['init_pos']-1
                            height_1 = height
                            init_2 = ls[i]['init_pos']
                            end_2 = end
                            height_2 = height+ls[i]['evenly_rc']
                            init_3 = end+1
                            end_3 = ls[i]['end_pos']
                            height_3 = height
                            remove_indices = [index,i]
                            ls = [k for o, k in enumerate(ls) if o not in remove_indices]
                            ls.append({'input_id':0,'ref_id':0,'wormbase_id':0,'type':0,'init_pos':init_1,'end_pos':end_1,'read_count':0,'field_ofanswers':0,'evenly_rc':height_1})
                            ls.append({'input_id':0,'ref_id':0,'wormbase_id':0,'type':0,'init_pos':init_2,'end_pos':end_2,'read_count':0,'field_ofanswers':0,'evenly_rc':height_2})
                            ls.append({'input_id':0,'ref_id':0,'wormbase_id':0,'type':0,'init_pos':init_3,'end_pos':end_3,'read_count':0,'field_ofanswers':0,'evenly_rc':height_3})
                            ls= sorted(ls, key=itemgetter('init_pos'),reverse=False)
                            cover = 1
                            break
                        elif (ls[i]['init_pos'] == start) and (ls[i]['end_pos']<end) :
                            init_1 = start
                            end_1 = ls[i]['end_pos']
                            height_1 = ls[i]['evenly_rc']+height
                            init_2 = ls[i]['end_pos']+1
                            end_2 = end
                            height_2 = height
                            remove_indices = [index,i]
                            ls = [k for o, k in enumerate(ls) if o not in remove_indices]
                            ls.append({'input_id':0,'ref_id':0,'wormbase_id':0,'type':0,'init_pos':init_1,'end_pos':end_1,'read_count':0,'field_ofanswers':0,'evenly_rc':height_1})
                            ls.append({'input_id':0,'ref_id':0,'wormbase_id':0,'type':0,'init_pos':init_2,'end_pos':end_2,'read_count':0,'field_ofanswers':0,'evenly_rc':height_2})
                            ls= sorted(ls, key=itemgetter('init_pos'),reverse=False)
                            cover = 1
                            break
                        elif (ls[i]['init_pos'] > start) and (ls[i]['init_pos'] < end) and (ls[i]['end_pos'] == end):
                            init_1 = start
                            end_1 = ls[i]['init_pos'] -1
                            height_1 = height
                            init_2 = ls[i]['init_pos']
                            end_2 = end
                            height_2 = height+ls[i]['evenly_rc']
                            remove_indices = [index,i]
                            ls = [k for o, k in enumerate(ls) if o not in remove_indices]
                            ls.append({'input_id':0,'ref_id':0,'wormbase_id':0,'type':0,'init_pos':init_1,'end_pos':end_1,'read_count':0,'field_ofanswers':0,'evenly_rc':height_1})
                            ls.append({'input_id':0,'ref_id':0,'wormbase_id':0,'type':0,'init_pos':init_2,'end_pos':end_2,'read_count':0,'field_ofanswers':0,'evenly_rc':height_2})
                            ls= sorted(ls, key=itemgetter('init_pos'),reverse=False)
                            cover = 1
                            break

                        elif (ls[i]['init_pos'] == start)  and (ls[i]['end_pos'] == end):
                            init_1 = start
                            end_1 = end
                            height_1 = height +ls[i]['evenly_rc']
                            remove_indices = [index,i]
                            ls = [k for o, k in enumerate(ls) if o not in remove_indices]
                            ls.append({'input_id':0,'ref_id':0,'wormbase_id':0,'type':0,'init_pos':init_1,'end_pos':end_1,'read_count':0,'field_ofanswers':0,'evenly_rc':height_1})
                            ls= sorted(ls, key=itemgetter('init_pos'),reverse=False)
                            cover = 1
                            break

                        elif (ls[i]['init_pos'] == end)  and (ls[i]['end_pos'] == end):
                            init_1 = start
                            end_1 = end-1
                            height_1 = height
                            init_2 = end
                            end_2 = end
                            height_2 = height + ls[i]['evenly_rc']
                            remove_indices = [index,i]
                            ls = [k for o, k in enumerate(ls) if o not in remove_indices]
                            ls.append({'input_id':0,'ref_id':0,'wormbase_id':0,'type':0,'init_pos':init_1,'end_pos':end_1,'read_count':0,'field_ofanswers':0,'evenly_rc':height_1})
                            ls.append({'input_id':0,'ref_id':0,'wormbase_id':0,'type':0,'init_pos':init_2,'end_pos':end_2,'read_count':0,'field_ofanswers':0,'evenly_rc':height_2})
                            ls= sorted(ls, key=itemgetter('init_pos'),reverse=False)
                            cover = 1
                            break
                        elif (ls[i]['init_pos'] ==end+1) and (ls[i]['evenly_rc'] == height):
                            init_1 = start
                            end_1 =ls[i]['end_pos']
                            height_1 = height
                            remove_indices = [index,i]
                            ls = [k for o, k in enumerate(ls) if o not in remove_indices] #刪除在remove_indices內的元素（嚴格來說是如果在remove_indices內則不會加到新的創建的list內）
                            ls.append({'input_id':0,'ref_id':0,'wormbase_id':0,'type':0,'init_pos':init_1,'end_pos':end_1,'read_count':0,'field_ofanswers':0,'evenly_rc':height_1})
                            ls= sorted(ls, key=itemgetter('init_pos'),reverse=False)
                            cover = 1
                            break
                        else:
                            start = ls[i]['init_pos']
                            end = ls[i]['end_pos']
                            height = ls[i]['evenly_rc']
                            index = i
                            pass
            g22 = sorted(ls, key=itemgetter('evenly_rc'),reverse=True)
            max_evenly_rc = float(g22[0]['evenly_rc'])
        except:
            g22 = [{'input_id':0,'ref_id':0,'wormbase_id':0,'type':0,'init_pos':0,'end_pos':0,'read_count':0,'field_ofanswers':0,'evenly_rc':0}]
            max_evenly_rc = 0
        '''------------------for clash--------------------'''
        # clash = list(Clash.objects.filter(targetrnaname=transcript).values())
        # for i in range(len(clash)):
        #     clash_start_end = clash[i]['targetrnaregionfoundinclashread'].replace("'",'').split('-')
        #     clash[i].update({'y':float(0),'start':float(clash_start_end[0]),'end':float(clash_start_end[1])})#增加開始結束點，畫圖的y軸，以及要出表的pairing部份（跟教授確認是哪個部份）
        # clash = sorted(clash, key=itemgetter('start')) #排序list
        # #print(clash[len(clash)-1])
        # cover_2  = 1
        # count = 0
        # y_2 = 0
        # first_2 = 1
        # while cover_2 != 0:
        #     cover_2 = 0
        #     start = 0
        #     end = 0
        #     y_list_2 = [0]
        #     first_2 = 1

        #     for i in range(0,len(clash)):
        #         if clash[i]['y'] == y_2:
        #             if first_2 == 1:
        #                 start = clash[i]['start']
        #                 end = clash[i]['end']
        #                 first_2 = 0
        #             elif first_2 != 1 :
        #                 #先判斷目前的開始點是否有被包在前一點的start以及end內，判斷完後再將start、end設定成現在判斷的start、end，讓下一個判斷使用
        #                 #若有判斷到，則y會加一層
        #                 if (clash[i]['start'] > start) and (clash[i]['start'] < end):
        #                     clash[i]['y'] = y_2+2.1
        #                     cover_2 = 1
        #                 elif (clash[i]['start'] ==start):
        #                     clash[i]['y'] = y_2+2.1
        #                     cover_2 = 1
        #                 elif (clash[i]['start']==end):
        #                     clash[i]['y'] = y_2+2.1
        #                     cover_2 = 1
        #                 else:
        #                     start = clash[i]['start']
        #                     end = clash[i]['end']
        #                     pass
        #     #print('========================================')
        #     y_2 += 2.1
        #     y_list_2.append(y_2)
        #print(clash)

        response ={
            'total_json_list':total_json_list,
            'length':len(length[1]),
            'y':y,
            'g22':g22,
            'max_evenly_rc' : max_evenly_rc,
            'exon_start':exon_start,
            'exon_stop':exon_stop,
            'exon_type':exon_type,
            # 'clash':clash,
            # 'y_2':y_2
        }
    except Exception as e:
        print(e)
        response ={
            'total_json_list':'none',

        }
    return JsonResponse(response)