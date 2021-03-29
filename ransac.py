#import pyransac3d as pyrsc
import csv

#Wczytywanie chmury
def cloud_reader():
    with open('LidarData.xyz', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for x, y, z in reader:
            yield (float(x), float(y), float(z))




points = []
for p in cloud_reader():
    points.append(p)


#points = load_points(.) # Load your point cloud as a numpy array (N, 3)
#plane1 = pyrsc.Plane()
#best_eq, best_inliers = plane1.fit(points, 0.01)