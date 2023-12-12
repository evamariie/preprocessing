import os
import shutil
import unittest

from auxiliary.turbopath import turbopath

from brainles_preprocessing.registration.niftyreg import NiftyRegRegistrator


class TestNiftyRegRegistrator(unittest.TestCase):
    def setUp(self):
        test_data_dir = turbopath(__file__).parent + "/test_data"
        input_dir = test_data_dir + "/input"
        self.output_dir = test_data_dir + "/temp_output_niftyreg"
        os.makedirs(self.output_dir, exist_ok=True)

        self.registrator = NiftyRegRegistrator()

        self.fixed_image = input_dir + "/tcia_example_t1c.nii.gz"
        self.moving_image = input_dir + "/bet_tcia_example_t1c_mask.nii.gz"

        self.transformed_image = self.output_dir + "/transformed_image.nii.gz"
        self.matrix = self.output_dir + "/matrix.txt"
        self.log_file = self.output_dir + "/registration.log"

    def tearDown(self):
        # Clean up created files if they exist
        shutil.rmtree(self.output_dir)

    def test_register_creates_output_files(self):
        # we try to run the fastest possible skullstripping on GPU
        self.registrator.register(
            fixed_image_path=self.fixed_image,
            moving_image_path=self.moving_image,
            transformed_image_path=self.transformed_image,
            matrix_path=self.matrix,
            log_file_path=self.log_file,
        )

        self.assertTrue(
            os.path.exists(self.transformed_image),
            "transformed file was not created.",
        )

        self.assertTrue(
            os.path.exists(self.matrix),
            "matrix file was not created.",
        )

        self.assertTrue(
            os.path.exists(self.log_file),
            "log file was not created.",
        )


# TODO also test transform