import subprocess
import os
from CreateShapeFile import points_to_osm, polygons_to_osm, relations_to_osm


def Merge_pbf_data_points(path, subdirectory, name):
    try:
        path2 = (path+"filtered_data/"+subdirectory+"/"+name)
        files = os.listdir(path2)
        if (len(files) == 51):
            subprocess.call(
                [['osmosis -q --rbf '] + [files[0]] + [' --rbf '] + [files[1]] + [' --rbf '] + [files[2]] + [
                    ' --rbf '] + [files[3]] + [' --rbf '] + [files[4]] + [' --rbf '] + [files[5]] + [' --rbf '] + [
                     files[6]]
                 + [' --rbf '] + [files[7]] + [' --rbf '] + [files[8]] + [' --rbf '] + [files[9]] + [
                     ' --rbf '] + [files[10]] + [' --rbf '] + [files[11]] + [' --rbf '] + [files[12]] + [
                     ' --rbf '] + [files[13]]
                 + [' --rbf '] + [files[14]] + [' --rbf '] + [files[15]] + [' --rbf '] + [files[16]] + [
                     ' --rbf '] + [files[17]] + [' --rbf '] + [files[18]] + [' --rbf '] + [files[19]] + [
                     ' --rbf '] + [files[20]]
                 + [' --rbf '] + [files[21]] + [' --rbf '] + [files[22]] + [' --rbf '] + [files[23]] + [
                     ' --rbf '] + [files[24]] + [' --rbf '] + [files[25]] + [' --rbf '] + [files[26]] + [
                     ' --rbf '] + [files[27]]
                 + [' --rbf '] + [files[28]] + [' --rbf '] + [files[29]] + [' --rbf '] + [files[30]] + [
                     ' --rbf '] + [files[31]] + [' --rbf '] + [files[32]] + [' --rbf '] + [files[33]] + [
                     ' --rbf '] + [files[34]]
                 + [' --rbf '] + [files[35]] + [' --rbf '] + [files[36]] + [' --rbf '] + [files[37]] + [
                     ' --rbf '] + [files[38]] + [' --rbf '] + [files[39]] + [' --rbf '] + [files[40]] + [
                     ' --rbf '] + [files[41]]
                 + [' --rbf '] + [files[42]] + [' --rbf '] + [files[43]] + [' --rbf '] + [files[44]] + [
                     ' --rbf '] + [files[45]] + [' --rbf '] + [files[46]] + [' --rbf '] + [files[47]] + [
                     ' --rbf '] + [files[48]]
                 + [' --rbf '] + [files[49]] + [' --rbf '] + [files[50]] + [' --merge --merge --merge --merge --merge --merge --merge  \
                        --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge \
                        --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge \
                        --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge \
                        --merge --write-pbf "'] + [path] + ['merged_data_points/'] + [name] + ['.pbf"']],
                shell=True, cwd=path2)
        #####################################################
            points_to_osm(path, name)
        ####################################################


            subprocess.call([['osmosis -q --rbf '] + [files[0]]])

    except:
        pass
        print("Merging failed for "+str(name))


def Merge_pbf_data_polygons(path, subdirectory, name):
    try:
        path2 = (path+"filtered_polygon_data/"+subdirectory+"/"+name)
        files = os.listdir(path2)
        subprocess.call(
            [['osmosis -q --rbf '] + [files[0]] + [' --rbf '] + [files[1]] + [' --rbf '] + [files[2]] + [
                ' --rbf '] + [files[3]] + [' --rbf '] + [files[4]] + [' --rbf '] + [files[5]] + [' --rbf '] + [
                 files[6]]
             + [' --rbf '] + [files[7]] + [' --rbf '] + [files[8]] + [' --rbf '] + [files[9]] + [
                 ' --rbf '] + [files[10]] + [' --rbf '] + [files[11]] + [' --rbf '] + [files[12]] + [
                 ' --rbf '] + [files[13]]
             + [' --rbf '] + [files[14]] + [' --rbf '] + [files[15]] + [' --rbf '] + [files[16]] + [
                 ' --rbf '] + [files[17]] + [' --rbf '] + [files[18]] + [' --rbf '] + [files[19]] + [
                 ' --rbf '] + [files[20]]
             + [' --rbf '] + [files[21]] + [' --rbf '] + [files[22]] + [' --rbf '] + [files[23]] + [
                 ' --rbf '] + [files[24]] + [' --rbf '] + [files[25]] + [' --rbf '] + [files[26]] + [
                 ' --rbf '] + [files[27]]
             + [' --rbf '] + [files[28]] + [' --rbf '] + [files[29]] + [' --rbf '] + [files[30]] + [
                 ' --rbf '] + [files[31]] + [' --rbf '] + [files[32]] + [' --rbf '] + [files[33]] + [
                 ' --rbf '] + [files[34]]
             + [' --rbf '] + [files[35]] + [' --rbf '] + [files[36]] + [' --rbf '] + [files[37]] + [
                 ' --rbf '] + [files[38]] + [' --rbf '] + [files[39]] + [' --rbf '] + [files[40]] + [
                 ' --rbf '] + [files[41]]
             + [' --rbf '] + [files[42]] + [' --rbf '] + [files[43]] + [' --rbf '] + [files[44]] + [
                 ' --rbf '] + [files[45]] + [' --rbf '] + [files[46]] + [' --rbf '] + [files[47]] + [
                  ' --rbf '] + [files[48]]
             + [' --rbf '] + [files[49]] + [' --rbf '] + [files[50]] + [' --merge --merge --merge --merge --merge --merge --merge  \
                    --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge \
                    --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge \
                    --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge --merge \
                    --merge --write-pbf "'] + [path] + ['merged_data_polygons/'] + [name] + ['.pbf"']],
            shell=True, cwd=path2)
    #####################################################
        polygons_to_osm(path, name)
        ####################################################

    except:
        pass
        print("Merging failed for "+str(name))



def Merge_pbf_data_polygons_2(path, subdirectory, name):
    try:
        path2 = (path+"filtered_polygon_data/"+subdirectory+"/"+name)
        files = os.listdir(path2)
        subprocess.call(
            [['osmosis -q --rbf '] + [files[0]] + [' --rbf '] + [files[1]] + [' --rbf '] + [files[2]] + [' --merge \
                    --merge --write-pbf "'] + [path] + ['merged_data_polygons/'] + [name] + ['.pbf"']],
            shell=True, cwd=path2)
    #####################################################

        polygons_to_osm(path, name)
        ####################################################

    except:
        pass
        print("Merging failed for "+str(name))




def Merge_pbf_data_relations_2(path, subdirectory, name):
    try:
        path2 = (path+"filtered_relation_data/"+subdirectory+"/"+name)
        files = os.listdir(path2)
        subprocess.call(
            [['osmosis -q --rbf '] + [files[0]] + [' --rbf '] + [files[1]] + [' --rbf '] + [files[2]] + [' --merge \
                    --merge --write-pbf "'] + [path] + ['merged_data_relations/'] + [name] + ['.pbf"']],
            shell=True, cwd=path2)
    #####################################################

        relations_to_osm(path, name)
        ####################################################

    except:
        pass
        print("Merging failed for "+str(name))