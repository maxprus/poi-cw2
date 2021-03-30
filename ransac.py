#import pyransac3d as pyrsc
import csv

def csv_points():
    with open(file="Lidar.csv", newline='') as csvfile:
        read = csv.reader(csvfile, delimiter=',')
        for x, y, z in read:
            yield float(x), float(y), float(z)


