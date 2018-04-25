import subprocess
import os
import pandas as pd



def filer_POI_data(path, key_values_list, subdirectory, names):
    print("Filtering points")
    files = os.listdir(path+'data')
    if(len(files) == 51):
        for i in range(len(files)):
            print("\t",str(i+1)," Filtering ",files[i]," finished.")
            for n in range(len(key_values_list)):
                print(key_values_list[n])
                subprocess.call([['osmosis -q --rbf '] + [files[i]] + [' --nkv keyValueList='+key_values_list[n]+''] + \
                                [' --write-xml "']+[path]+['merged_data_points/']++[names[n]]+['_']+[files[i][:-4]+'"']], shell=True, cwd=path+'data')


def filter_polygons(path, key_values_list, subdirectory, names):
    print("Filtering polygons")
    files = os.listdir(path+'data')
    for i in range(len(files)):
        print("\t",str(i+1)," Filtering ", files[i]," finished.")
        for n in range(len(key_values_list)):
            print("\t\t"+key_values_list[n])
            subprocess.call([['osmosis -q --rbf '] + [files[i]] + [' --tf accept-ways '+key_values_list[n]+''] + \
                            [' --tf reject-relation --used-node --write-xml ']+['"'+path]+['merged_data_polygons/']+[names[n]]+['_']+[files[i][:-4]+'"']], shell=True, cwd=path+'data')


def filter_relations(path, key_values_list, subdirectory, names):
    print("Filtering relations")
    files = os.listdir(path+'data')
    for i in range(len(files)):
        print("\t",str(i+1)," Filtering ",files[i]," finished.")
        for n in range(len(key_values_list)):
            print("\t\t"+key_values_list[n])
            subprocess.call([['osmosis -q --rbf '] + [files[i]] + [' --tf accept-relations '+key_values_list[n]+''] + \
                            [' --used-way --used-node --write-xml "']+[path]+['merged_data_relations/']+[names[n]]+['_']+[files[i][:-4]+'"']], shell=True, cwd=path+'data')



def read_tags_for_points(path, file_name):

    tags_data = pd.read_csv(path+'tools/'+file_name, encoding='Windows 1252')
    tags_data.Points = tags_data.Points.str.replace("   ", ",")
    tags_data.Points = tags_data.Points.str.replace("  ", ",")
    tags_data.Points = tags_data.Points.str.replace(" ", ",")
    tags = tags_data['Points'].values.tolist()
    layers = tags_data['Layer'].values.tolist()
    attributes = tags_data['Attributes'].values.tolist()
    names = tags_data['Name'].values.tolist()
    return layers, tags, names, attributes

def read_tags_for_ways(path, file_name):
    tags_data = pd.read_csv(path+'tools/'+file_name, encoding='Windows 1252')
    tags_data = tags_data.dropna(subset=['Polygons'])

    tags_data['Polygons'] = tags_data.Polygons.str.replace(".", "=")
    layers = tags_data['Layer'].values.tolist()
    names = tags_data['Name'].values.tolist()
    ways = tags_data['Polygons'].values.tolist()
    return layers, ways, names

def read_tags_for_relation(path, file_name):
    tags_data = pd.read_csv(path+'tools/'+file_name, encoding='Windows 1252')
    tags_data = tags_data.dropna(subset=['Relations'])

    tags_data['Relations'] = tags_data.Polygons.str.replace(".", "=")
    layers = tags_data['Layer'].values.tolist()
    names = tags_data['Name'].values.tolist()
    relations = tags_data['Relations'].values.tolist()
    attributes = tags_data['Attributes'].values.tolist()
    return layers, relations, names, attributes
