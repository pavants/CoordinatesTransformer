from pyproj import Proj, Transformer

# Step 1: Convert DMS to Decimal Degrees
def dms_to_dd(degrees, minutes, seconds, direction):
    dd = degrees + minutes / 60 + seconds / 3600
    if direction in ['S', 'W']:
        dd *= -1
    return dd

def dd_to_dms(degrees):
    dd = int(degrees) 
    minutes = (degrees-dd) * 60 
    seconds = float(minutes-int(minutes)) * 3600
    return f"{dd:d} {minutes:.0f} {seconds:.2f}"
    


def WGS84_to_GaussBoaga():
  lat_s= input("insert latitude 00:00:00.000->")
  lon_s= input("insert longitude 00:00:00.000->")

  lat_deg    =int(lat_s[0:2])
  lat_minute =int(lat_s[3:5])
  lat_seconds=float(lat_s[6:])
  lon_deg    =int(lon_s[0:2])
  lon_minute =int(lon_s[3:5])
  lon_seconds=float(lon_s[6:])

  # Input: DMS
  lat_dd = dms_to_dd(lat_deg, lat_minute, lat_seconds, 'N')  # Latitude: 45°37'20"N
  lon_dd = dms_to_dd(lon_deg, lon_minute, lon_seconds, 'E')  # Longitude: 13°46'38"E

  transformer = Transformer.from_crs("epsg:4326", "epsg:3004", always_xy=True)
  easting, northing = transformer.transform(lon_dd, lat_dd)

  print(f"Gauss-Boaga (EPSG:3004) Coordinates:\nEasting: {easting:.2f} m\nNorthing: {northing:.2f} m")


def GaussBoaga_to_WGS84():
  N_coord= input("insert North 0000000.000->")
  E_coord= input("insert East 0000000.000->")

  transformer = Transformer.from_crs("epsg:3004", "epsg:4326", always_xy=True)
  easting, northing = transformer.transform(E_coord, N_coord)
  dd = dd_to_dms(easting)
  print(f"here the Longitude {dd} ")
  dd = dd_to_dms(northing)
  print(f"here the Latitude {dd} ")
  return   


response = input("how do you want to convert ? Gauss-Boaga to WGS84 type: G or vice versa type W ->")

response=response.upper()


if response not in "WG":
  quit()
elif response in "W":
  WGS84_to_GaussBoaga()
elif response in "G":
  GaussBoaga_to_WGS84()
  
  


