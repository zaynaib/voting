import geopandas

file_dict = {'congressional_districts':'Congressional Plan.shp', 'house_districts':'House Plan.shp','senate_districts':'Senate Plan.shp'}

for folder,file in file_dict.items():
    #print(f'{folder} is in this {file}')
    shp_file = geopandas.read_file(f'./{folder}/{file}')
    shp_file.to_file(f'./{folder}/{folder}.geojson',driver='GeoJSON')


#shp_file = geopandas.read_file('./congressional_map/Congressional Plan.shp')
#shp_file.to_file('./congressional_map/congressional_plan.geojson',driver='GeoJSON')