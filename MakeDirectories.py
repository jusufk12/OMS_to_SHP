import os

def makeDirectories(path):
    if not os.path.exists(path):
        os.makedirs(path)

    if not os.path.exists(path + 'data/'):
        os.makedirs(path + 'data')

    if not os.path.exists(path + 'merged_data_points/'):
        os.makedirs(path + 'merged_data_points/')

    if not os.path.exists(path + 'shp_points/'):
        os.makedirs(path + 'shp_points/')

    if not os.path.exists(path + 'shp_polygons/'):
        os.makedirs(path + 'shp_polygons/')

    if not os.path.exists(path + 'shp_relations/'):
        os.makedirs(path + 'shp_relations/')

    if not os.path.exists(path + 'csv_data/'):
        os.makedirs(path + 'csv_data/')

    if not os.path.exists(path + 'filtered_data/'):
        os.makedirs(path + 'filtered_data/')

    if not os.path.exists(path + 'tools/'):
        os.makedirs(path + 'tools/')

    if not os.path.exists(path + 'osm_data/'):
        os.makedirs(path + 'osm_data/')


    if not os.path.exists(path + 'filtered_polygon_data/'):
        os.makedirs(path + 'filtered_polygon_data/')

    if not os.path.exists(path + 'filtered_relation_data/'):
        os.makedirs(path + 'filtered_relation_data/')

    if not os.path.exists(path + 'merged_data_polygons/'):
        os.makedirs(path + 'merged_data_polygons/')

    if not os.path.exists(path + 'merged_data_relations/'):
        os.makedirs(path + 'merged_data_relations/')

    if not os.path.exists(path + 'osm_polygon_data/'):
        os.makedirs(path + 'osm_polygon_data/')

    if not os.path.exists(path + 'osm_relation_data/'):
        os.makedirs(path + 'osm_relation_data/')

    if not os.path.exists(path + 'merged_poi_poly/'):
        os.makedirs(path + 'merged_poi_poly/')

def makeSubDirectorides_for_shp_points(path, sub_dir):
    path1 = path+'shp_points/'
    if not os.path.exists(path1 + sub_dir):
        os.makedirs(path1 + sub_dir)

def makeSubDirectorides_for_shp_polygons(path, sub_dir):
    path1 = path+'shp_polygons/'
    if not os.path.exists(path1 + sub_dir):
        os.makedirs(path1 + sub_dir)

def makeSubDirectorides_for_shp_relations(path, sub_dir):
    path1 = path+'shp_relations/'
    if not os.path.exists(path1 + sub_dir):
        os.makedirs(path1 + sub_dir)

def make_subdir_for_filtered_data(path, sub_dir, tag):
    path1 = path+'filtered_data/'
    if not os.path.exists(path1 + sub_dir+'/'):
        os.makedirs(path1 + sub_dir+'/')

    if not os.path.exists(path1 + sub_dir+'/'+tag+'/'):
        os.makedirs(path1 + sub_dir+'/'+tag+'/')

def make_subdir_for_filtered_polygon_data(path, sub_dir, way):
    path1 = path+'filtered_polygon_data/'
    if not os.path.exists(path1 + sub_dir+'/'):
        os.makedirs(path1 + sub_dir+'/')

    if not os.path.exists(path1 + sub_dir+'/'+way+'/'):
        os.makedirs(path1 + sub_dir+'/'+way+'/')


def make_subdir_for_filrered_relations(path, sub_dir, relation):
    path1 = path+'filtered_relation_data/'
    if not os.path.exists(path1 + sub_dir+'/'):
        os.makedirs(path1 + sub_dir+'/')

    if not os.path.exists(path1 + sub_dir+'/'+relation+'/'):
        os.makedirs(path1 + sub_dir+'/'+relation+'/')