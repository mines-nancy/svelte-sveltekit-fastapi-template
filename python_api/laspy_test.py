import numpy as np
import pygltflib

# https://medium.com/spatial-data-science/an-easy-way-to-work-and-visualize-lidar-data-in-python-eed0e028996c


import laspy
import open3d as o3d
import numpy as np
import trimesh
from pyntcloud import PyntCloud
import pandas as pd

las = laspy.read("plane.laz")

point_data = np.stack([las.X, las.Y, las.Z], axis=0).transpose((1, 0))
color_data = np.stack([las.red, las.green, las.blue], axis=0).transpose((1, 0))
for point in point_data:
    print("[x:{}, y:{}, z:{}],".format(point[0], point[1], point[2]).replace("[","{").replace("]","}"))

geom = o3d.geometry.PointCloud()
geom.points = o3d.utility.Vector3dVector(point_data)
geom.estimate_normals()

cloud = PyntCloud(pd.DataFrame(
    # same arguments that you are passing to visualize_pcl
    data=np.hstack((point_data, color_data)),
    columns=["x", "y", "z", "red", "green", "blue"]))

cloud.to_file("output.ply")
pcd = o3d.io.read_point_cloud("output.ply")
o3d.visualization.draw_geometries([pcd])
#o3d.visualization.draw_geometries([geom])

# # estimate radius for rolling ball
# distances = geom.compute_nearest_neighbor_distance()
# avg_dist = np.mean(distances)
# radius = 1.5 * avg_dist
#
# mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
#            geom,
#            o3d.utility.DoubleVector([radius, radius * 2]))
#
# mesh.compute_vertex_normals()
#
# # create the triangular mesh with the vertices and faces from open3d
# tri_mesh = trimesh.Trimesh(np.asarray(mesh.vertices), np.asarray(mesh.triangles), vertex_normals=np.asarray(mesh.vertex_normals))
#
# trimesh.convex.is_convex(tri_mesh)
# arr = tri_mesh.triangles
# triangles = []
# for a in arr:
#     for b in a:
#         triangles.append(b)
#
# #
# points = point_data
# triangles = np.array(triangles)
# # points = np.array(
# #     [
# #         [-0.5, -0.5, 0.5],
# #         [0.5, -0.5, 0.5],
# #         [-0.5, 0.5, 0.5],
# #         [0.5, 0.5, 0.5],
# #         [0.5, -0.5, -0.5],
# #         [-0.5, -0.5, -0.5],
# #         [0.5, 0.5, -0.5],
# #         [-0.5, 0.5, -0.5],
# #     ],
# #     dtype="float32",
# # )
# # triangles = np.array(
# #     [
# #         [0, 1, 2],
# #         [3, 2, 1],
# #         [1, 0, 4],
# #         [5, 4, 0],
# #         [3, 1, 6],
# #         [4, 6, 1],
# #         [2, 3, 7],
# #         [6, 7, 3],
# #         [0, 2, 5],
# #         [7, 5, 2],
# #         [5, 7, 4],
# #         [6, 4, 7],
# #     ],
# #     dtype="uint8",
# # )
# triangles_binary_blob = triangles.flatten().tobytes()
# points_binary_blob = points.tobytes()
# gltf = pygltflib.GLTF2(
#     scene=0,
#     scenes=[pygltflib.Scene(nodes=[0])],
#     nodes=[pygltflib.Node(mesh=0)],
#     meshes=[
#         pygltflib.Mesh(
#             primitives=[
#                 pygltflib.Primitive(
#                     attributes=pygltflib.Attributes(POSITION=1), indices=0
#                 )
#             ]
#         )
#     ],
#     accessors=[
#         pygltflib.Accessor(
#             bufferView=0,
#             componentType=pygltflib.UNSIGNED_BYTE,
#             count=triangles.size,
#             type=pygltflib.SCALAR,
#             max=[int(triangles.max())],
#             min=[int(triangles.min())],
#         ),
#         pygltflib.Accessor(
#             bufferView=1,
#             componentType=pygltflib.FLOAT,
#             count=len(points),
#             type=pygltflib.VEC3,
#             max=points.max(axis=0).tolist(),
#             min=points.min(axis=0).tolist(),
#         ),
#     ],
#     bufferViews=[
#         pygltflib.BufferView(
#             buffer=0,
#             byteLength=len(triangles_binary_blob),
#             target=pygltflib.ELEMENT_ARRAY_BUFFER,
#         ),
#         pygltflib.BufferView(
#             buffer=0,
#             byteOffset=len(triangles_binary_blob),
#             byteLength=len(points_binary_blob),
#             target=pygltflib.ARRAY_BUFFER,
#         ),
#     ],
#     buffers=[
#         pygltflib.Buffer(
#             byteLength=len(triangles_binary_blob) + len(points_binary_blob)
#         )
#     ],
# )
# gltf.set_binary_blob(triangles_binary_blob + points_binary_blob)
# gltf.save("test.glb")
#
# mesh = o3d.io.read_triangle_mesh("test.glb")
# print(mesh)
# mesh.compute_vertex_normals()
# mesh.paint_uniform_color([0.5,0,0])
# print("Try to render a mesh with normals (exist: " +
#       str(mesh.has_vertex_normals()) + ") and colors (exist: " +
#       str(mesh.has_vertex_colors()) + ")")
# o3d.visualization.draw_geometries([mesh])
# print("A mesh with no normals and no colors does not look good.")