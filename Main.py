from Merge import Merge_pbf_data_points, Merge_pbf_data_polygons, Merge_pbf_data_polygons_2, Merge_pbf_data_relations_2
from Filter_data import read_tags_for_points, read_tags_for_relation, read_tags_for_ways, filter_polygons, filer_POI_data, filter_relations
from MakeDirectories import makeDirectories, make_subdir_for_filtered_data, make_subdir_for_filtered_polygon_data, make_subdir_for_filrered_relations,makeSubDirectorides_for_shp_points, makeSubDirectorides_for_shp_polygons, makeSubDirectorides_for_shp_relations
from CreateShapeFile import polygons_to_shapefile
import os

path = 'D:/SE Data Projects/USData/'
tags_name_file = 'tags5.csv'

makeDirectories(path)


layers_relations, relations, names_relations, relation_attributes = read_tags_for_relation(path, tags_name_file)
layers_points, points, names_points, attributes = read_tags_for_points(path, tags_name_file)
layers_way, ways, names_way = read_tags_for_ways(path, tags_name_file)


set_tags = set(points)
set_layers = set(layers_points)
set_names = set(names_points)


for i in range(len(layers_points)):
    make_subdir_for_filtered_data(path, layers_points[i], str(names_points[i]))

for i in range(len(layers_way)):
    make_subdir_for_filtered_polygon_data(path, layers_way[i], str(names_way[i]))

for i in range(len(layers_relations)):
    make_subdir_for_filrered_relations(path, layers_relations[i], str(names_relations[i]))


#filer_POI_data(path, points, layers_points, names_points)
filter_polygons(path, ways, layers_way, names_way)
filter_relations(path, relations, layers_relations, names_relations)


'''
for i in range(len(points)):
    Merge_pbf_data_points(path, layers_points[i], str(names_points[i]))
    print("\t", str(i), "Merginig of", names_points[i], " finished.")





for i in range(len(ways)):
    print("\t", str(i), "Merginig of", names_way[i], " finished.")
    Merge_pbf_data_polygons_2(path, layers_way[i], str(names_way[i]))


for i in range(len(relations)):
    print("\t", str(i), "Merginig of", names_relations[i], " finished.")
    Merge_pbf_data_relations_2(path, layers_relations[i], str(names_relations[i]))


print("Creating subdirectories for polygon shp files..")
for i in range(len(layers_points)):
    #makeSubDirectorides_for_shp_points(path, layers_points[i])
    makeSubDirectorides_for_shp_polygons(path, layers_way[i])

for i in range(len(layers_relations)):
    makeSubDirectorides_for_shp_relations(path, layers_relations[i])

print("Preprocessing polygons")
'''

files = os.listdir(path+'merged_data_polygons')
for n in range(len(names_way)):
    for i in range(len(files)):
        if (names_way[n] in files[i]):
            polygons_to_shapefile(path, attributes[n], "polygon", files[i])



files = os.listdir(path+'merged_data_relations')
for n in range(len(names_relations)):
    for i in range(len(names_relations)):
        if (names_relations[n] in files[i]):
            polygons_to_shapefile(path, relation_attributes[n], "relation", files[i])

