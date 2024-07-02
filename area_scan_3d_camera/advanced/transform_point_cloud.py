# With this sample, you can obtain point cloud in a specified coordinate system.

from mecheye.shared import *
from mecheye.area_scan_3d_camera import *
from mecheye.area_scan_3d_camera_utils import find_and_connect, confirm_capture_3d


class TransformPointCloud(object):
    def __init__(self):
        self.camera = Camera()
        self.frame_all_2d_3d = Frame2DAnd3D()

    def get_transformed_point_cloud(self):
        # obtain point cloud  in a specified coordinate system
        transformation = get_transformation_params(self.camera)
        frmae_3d = Frame3D(self.frame_all_2d_3d.frame_3d())
        transformed_point_cloud  =  transform_point_cloud(transformation,frmae_3d.get_untextured_point_cloud())
        point_cloud_file = "PointCloud.ply"
        show_error(Frame3D.save_point_cloud(transformed_point_cloud,FileFormat_PLY, point_cloud_file))
        print("Capture and save the point cloud: {}.".format(
            point_cloud_file))

    def get_transformed_textured_point_cloud(self):
        transformation = get_transformation_params(self.camera)
        # obtain textured point cloud  in a specified coordinate system
        transformed_textured_point_cloud  = transform_textured_point_cloud(transformation,self.frame_all_2d_3d.get_textured_point_cloud())
        textured_point_cloud_file = "TexturedPointCloud.ply"
        UntexturedPointCloud
        show_error(Frame2DAnd3D.save_point_cloud(transformed_textured_point_cloud,FileFormat_PLY,
                                                                  textured_point_cloud_file))
        print("Capture and save the textured point cloud: {}".format(
            textured_point_cloud_file))

    def get_transformed_point_cloud_with_normals(self):
        transformation = get_transformation_params(self.camera)
        # obtain point cloud with normals in a specified coordinate system
        frmae_3d = Frame3D(self.frame_all_2d_3d.frame_3d())
        transformed_point_cloud_with_normals  =  transform_point_cloud_with_normals(transformation,frmae_3d.get_untextured_point_cloud())
        point_cloud_with_normals_file = "PointCloudWithNormals.ply"
        show_error(
            Frame3D.save_point_cloud_with_normals(transformed_point_cloud_with_normals,FileFormat_PLY, point_cloud_with_normals_file,False))
        print("Capture and save the point cloud with normals: {}.".format(
            point_cloud_with_normals_file)) 

    def get_transformed_textured_point_cloud_with_normals(self):
        transformation = get_transformation_params(self.camera)
        # obtain textured point cloud with normals in a specified coordinate system
        cameraIntrinsics = CameraIntrinsics()
        self.camera.get_camera_intrinsics(cameraIntrinsics)
        transformed_textured_point_cloud_with_normals  =  transform_textured_point_cloud_with_normals( transformation,self.frame_all_2d_3d, cameraIntrinsics)
        textured_point_cloud_with_normals_file = "TexturedPointCloudWithNormals.ply"
        show_error(Frame2DAnd3D.save_point_cloud_with_normals(transformed_textured_point_cloud_with_normals,FileFormat_PLY,
                                                                  textured_point_cloud_with_normals_file,False))
        print("Capture and save the textured point cloud: {}".format(
            textured_point_cloud_with_normals_file))            

    def main(self):
        if find_and_connect(self.camera):
            if not confirm_capture_3d():
                return
            show_error(self.camera.capture_2d_and_3d(self.frame_all_2d_3d))
            self.get_transformed_point_cloud()
            self.get_transformed_textured_point_cloud()
            self.get_transformed_point_cloud_with_normals()
            self.get_transformed_textured_point_cloud_with_normals()
            self.camera.disconnect()
            print("Disconnected from the camera successfully.")

if __name__ == '__main__':
    a = TransformPointCloud()
    a.main()