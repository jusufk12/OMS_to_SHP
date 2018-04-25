import subprocess
import os
from MakeDirectories import makeSubDirectorides_for_shp_points, makeSubDirectorides_for_shp_polygons
import zipfile
import shutil

def toShapeFile(path, name):
    makeSubDirectorides_for_shp_points(path, name)
    osm_data_path = path+'osm_data'
    shp_data_path = path+'shp_data'

    files = os.listdir(osm_data_path)
    print("Creating "+name+".osm file.")
    subprocess.call([['osmconvert '] +[path]+['merged_data/']+[name]+['.pbf -o=']+[osm_data_path]+['/']+[name]+['.osm']], shell=True, cwd=path+'/tools')

    print("Creating "+name+".shp file...")


    os.system('ogr2ogr --config OSM_USE_CUSTOM_INDEXING NO -skipfailures -f "ESRI Shapefile" '+path+'shp_data/'+name+' '+path+'clean_osm_files/'+name+'.    osm'+' -nlt "POINT" -overwrite ')
    os.remove(path+"shp_data/"+name+"/lines.shp")
    os.remove(path+"shp_data/"+name+"/lines.dbf")
    os.remove(path+'shp_data/'+name+'/lines.prj')
    os.remove(path+'shp_data/'+name+'/lines.shx')
    os.remove(path+'shp_data/'+name+'/multilinestrings.shp')
    os.remove(path+'shp_data/'+name+'/multilinestrings.dbf')
    os.remove(path+'shp_data/'+name+'/multilinestrings.prj')
    os.remove(path+'shp_data/'+name+'/multilinestrings.shx')
    os.remove(path+'shp_data/'+name+'/multipolygons.shp')
    os.remove(path+'shp_data/'+name+'/multipolygons.dbf')
    os.remove(path+'shp_data/'+name+'/multipolygons.prj')
    os.remove(path+'shp_data/'+name+'/multipolygons.shx')
    os.remove(path+'shp_data/'+name+'/other_relations.shp')
    os.remove(path+'shp_data/'+name+'/other_relations.dbf')
    os.remove(path+'shp_data/'+name+'/other_relations.prj')
    os.remove(path+'shp_data/'+name+'/other_relations.shx')

    shutil.move(path + "shp_data/" + name + "/points.dbf",
                path + "shp_data/" + name + "/" + name + ".dbf")
    shutil.move(path + "shp_data/" + name + "/points.shx",
                path + "shp_data/" + name + "/" + name + ".shx")
    shutil.move(path + "shp_data/" + name + "/points.shp",
                path + "shp_data/" + name + "/" + name + ".shp")
    shutil.move(path + "shp_data/" + name + "/points.prj",
                path + "shp_data/" + name + "/" + name + ".prj")

    z = zipfile.ZipFile(path+'shp_data/'+name+'/'+name+'.zip', 'w', zipfile.ZIP_DEFLATED)
    z.write(path + 'shp_data/' + name +"/"+name+'.prj')
    z.write(path + 'shp_data/' + name +"/"+name+'.shp')
    z.write(path + 'shp_data/' + name +"/"+name+'.shx')
    z.write(path + 'shp_data/' + name +"/"+name+'.dbf')
    z.close()



def points_to_osm(path, name):
    osm_data_points_path = path + 'osm_data'
    print("\tCreating " + name + " points.osm file.")
    print([['osmconvert "'] + [path] + ['merged_data_points/'] + [name] + ['.pbf" -o='] + [osm_data_points_path] + ['/'] + [
        name] + ['.osm']])
    subprocess.call([['osmconvert "'] + [path] + ['merged_data_points/'] + [name] + ['.pbf" -o='] + [osm_data_points_path] + ['/'] + [
        name] + ['.osm']], shell=True, cwd=path + '/tools')


def polygons_to_osm(path, name):
    print("Merged to osm data..")
    osm_data_polygon_path = path + 'osm_polygon_data'
    print("\tCreating " + name + ".osm polygon file.")
    print(['osmconvert '] + [path] + ['merged_data_polygons/'] + [name] + ['.pbf -o='] + [osm_data_polygon_path] + ['/'] + [
        name] + ['.osm'])
    subprocess.call([['osmconvert "'] + [path] + ['merged_data_polygons/'] + [name] + ['.pbf" -o="'] + [osm_data_polygon_path] + ['/'] + [
        name] + ['.osm"']], shell=True, cwd=path + '/tools')

def relations_to_osm(path, name):
    print("Merged to osm data..")
    osm_data_polygon_path = path + 'osm_relation_data'
    print("\tCreating " + name + ".osm relation file.")
    print(['osmconvert '] + [path] + ['merged_data_relations/'] + [name] + ['.pbf -o='] + [osm_data_polygon_path] + ['/'] + [
        name] + ['.osm'])
    subprocess.call([['osmconvert "'] + [path] + ['merged_data_relations/'] + [name] + ['.pbf" -o="'] + [osm_data_polygon_path] + ['/'] + [
        name] + ['.osm"']], shell=True, cwd=path + '/tools')


def points_to_shapefile(path, attributes, osm_file, layers_points):
    f = open(path+"tools/osmconf.ini")
    lines = f.readlines()

    #last_item = tags[-1]
    #new_list_tags = [x + "," for x in tags[:-1]]
    #new_list_tags.extend(last_item)
    tags_to_show = "".join(attributes)

    lines[27] = "attributes="+tags_to_show+"\n"

    with open("C:/Program Files/GDAL/gdal-data/osmconf.ini", 'w') as file:
        file.writelines(lines)

    os.system(
        'ogr2ogr --config OSM_USE_CUSTOM_INDEXING NO -skipfailures -f "ESRI Shapefile" ' + path + 'shp_points/'\
            +layers_points+'/'+ osm_file + ' ' + path + 'clean_osm_points/' + osm_file+'.osm' +' -nlt "POINT" -overwrite ')

    os.remove(path+"shp_points/" +layers_points+'/'+osm_file+"/lines.shp")
    os.remove(path+"shp_points/" +layers_points+'/'+osm_file+"/lines.dbf")
    os.remove(path+'shp_points/' +layers_points+'/'+osm_file+'/lines.prj')
    os.remove(path+'shp_points/' +layers_points+'/'+osm_file+'/lines.shx')
    os.remove(path+'shp_points/' +layers_points+'/'+osm_file+'/multilinestrings.shp')
    os.remove(path+'shp_points/' +layers_points+'/'+osm_file+'/multilinestrings.dbf')
    os.remove(path+'shp_points/' +layers_points+'/'+osm_file+'/multilinestrings.prj')
    os.remove(path+'shp_points/' +layers_points+'/'+osm_file+'/multilinestrings.shx')
    os.remove(path+'shp_points/' +layers_points+'/'+osm_file+'/multipolygons.shp')
    os.remove(path+'shp_points/' +layers_points+'/'+osm_file+'/multipolygons.dbf')
    os.remove(path+'shp_points/' +layers_points+'/'+osm_file+'/multipolygons.prj')
    os.remove(path+'shp_points/' +layers_points+'/'+osm_file+'/multipolygons.shx')
    os.remove(path+'shp_points/' +layers_points+'/'+osm_file+'/other_relations.shp')
    os.remove(path+'shp_points/' +layers_points+'/'+osm_file+'/other_relations.dbf')
    os.remove(path+'shp_points/' +layers_points+'/'+osm_file+'/other_relations.prj')
    os.remove(path+'shp_points/' +layers_points+'/'+osm_file+'/other_relations.shx')

    temp_name = "".join(osm_file)
    osm_file1 = temp_name.replace("_", " ")
    shutil.move(path + "shp_points/" +layers_points+'/' + osm_file + "/points.dbf",
                path + "shp_points/" +layers_points+'/' + osm_file + "/" + osm_file1 + ".dbf")
    shutil.move(path + "shp_points/" +layers_points+'/' + osm_file + "/points.shx",
                path + "shp_points/" +layers_points+'/' + osm_file + "/" + osm_file1 + ".shx")
    shutil.move(path + "shp_points/" +layers_points+'/' + osm_file + "/points.shp",
                path + "shp_points/" +layers_points+'/' + osm_file + "/" + osm_file1 + ".shp")
    shutil.move(path + "shp_points/" +layers_points+'/' + osm_file + "/points.prj",
                path + "shp_points/" +layers_points+'/' + osm_file + "/" + osm_file1 + ".prj")

    z = zipfile.ZipFile(path+'shp_points/'+layers_points+'/'+osm_file+'/'+osm_file+'.zip', 'w', zipfile.ZIP_DEFLATED)
    z.write(path + 'shp_points/' +layers_points+'/'+ osm_file +"/"+osm_file1+'.prj')
    z.write(path + 'shp_points/' +layers_points+'/' + osm_file +"/"+osm_file1+'.shp')
    z.write(path + 'shp_points/' +layers_points+'/'+ osm_file +"/"+osm_file1+'.shx')
    z.write(path + 'shp_points/' +layers_points+'/'+ osm_file +"/"+osm_file1+'.dbf')
    z.close()

def polygons_to_shapefile(path, attributes, type, state):

    if (type == "polygon"):
        shape_type = "merged_data_polygons"
        to_shp_folder = "shp_polygons"

    elif (type == "relation"):
        shape_type = "merged_data_relations"
        to_shp_folder = "shp_relations"

    f = open(path+"tools/osmconf.ini")
    lines = f.readlines()

    #last_item = tags[-1]
    #new_list_tags = [x + "," for x in tags[:-1]]
    #new_list_tags.extend(last_item)
    tags_to_show = "".join(attributes)

    lines[78] = "attributes=" + tags_to_show + "\n"
    print(tags_to_show)

    with open("C:/Program Files/GDAL/gdal-data/osmconf.ini", 'w') as file:
        file.writelines(lines)
    os.system(
        'ogr2ogr --config OSM_USE_CUSTOM_INDEXING NO -skipfailures -f "ESRI Shapefile" "' + path + to_shp_folder+'/'+state[:-4] + '"'+' "' + path + shape_type+'/' +state+'" -nlt "MULTIPOLYGON" -overwrite ')

    os.remove(path + to_shp_folder+"/"+'/' + state[:-4]  + "/lines.shp")
    os.remove(path + to_shp_folder+"/"+'/' + state[:-4]  + "/lines.dbf")
    os.remove(path + to_shp_folder+'/'+'/' + state[:-4] + '/lines.prj')
    os.remove(path + to_shp_folder+'/'+'/' + state[:-4]  + '/lines.shx')
    os.remove(path + to_shp_folder+'/'+'/' + state[:-4] + '/multilinestrings.shp')
    os.remove(path + to_shp_folder+'/'+'/' + state[:-4]  + '/multilinestrings.dbf')
    os.remove(path + to_shp_folder+'/'+'/' + state[:-4]  + '/multilinestrings.prj')
    os.remove(path + to_shp_folder+'/'+'/' + state[:-4]  + '/multilinestrings.shx')
    os.remove(path + to_shp_folder+'/'+'/' + state[:-4]  + '/points.shp')
    os.remove(path + to_shp_folder+'/'+'/' + state[:-4]  + '/points.dbf')
    os.remove(path + to_shp_folder+'/'+'/' + state[:-4]  + '/points.prj')
    os.remove(path + to_shp_folder+'/'+'/' + state[:-4]  + '/points.shx')
    os.remove(path + to_shp_folder+'/'+'/' + state[:-4]  + '/other_relations.shp')
    os.remove(path + to_shp_folder+'/'+'/' + state[:-4]  + '/other_relations.dbf')
    os.remove(path + to_shp_folder+'/'+'/' + state[:-4]  + '/other_relations.prj')
    os.remove(path + to_shp_folder+'/'+'/' + state[:-4]  + '/other_relations.shx')

    temp_name = "".join(state[:-4] )
    osm_file1 = temp_name.replace("_", " ")

    shutil.move(path + to_shp_folder+"/"+'/' + state[:-4]  + "/multipolygons.dbf",
                path + to_shp_folder+"/"+'/'+ state[:-4]  + "/" + osm_file1 + ".dbf")
    shutil.move(path + to_shp_folder+"/"+'/' + state[:-4]  + "/multipolygons.shx",
                path + to_shp_folder+"/"+'/' + state[:-4]  + "/" + osm_file1 + ".shx")
    shutil.move(path + to_shp_folder+"/"+'/' + state[:-4]  + "/multipolygons.shp",
                path + to_shp_folder+"/"+'/' + state[:-4]  + "/" + osm_file1 + ".shp")
    shutil.move(path + to_shp_folder+"/"+'/' + state[:-4]  + "/multipolygons.prj",
                path + to_shp_folder+"/"+'/' + state[:-4]  + "/" + osm_file1 + ".prj")

    z = zipfile.ZipFile(path + to_shp_folder+'/' +'/'+ state[:-4]  + '/' + state[:-4]  + '.zip', 'w', zipfile.ZIP_DEFLATED)
    z.write(path + to_shp_folder+'/' +'/'+ state[:-4]  + "/" + osm_file1 + '.prj')
    z.write(path + to_shp_folder+'/' +'/'+ state[:-4]  + "/" + osm_file1 + '.shp')
    z.write(path + to_shp_folder+'/' +'/'+ state[:-4]  + "/" + osm_file1 + '.shx')
    z.write(path + to_shp_folder+'/' +'/'+ state[:-4]  + "/" + osm_file1 + '.dbf')
    z.close()