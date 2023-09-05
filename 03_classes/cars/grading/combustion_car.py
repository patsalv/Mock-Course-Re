#!/usr/bin/env python3

# Scaffolding necessary to set up ACCESS test
import sys
try: from universal.harness import *
except: sys.path.append("../../universal/"); from harness import *

# Grading test suite starts here
CombustionCar = grading_import("task.combustion_car", "CombustionCar")

class TestCombustionCar(AccessTestCase):

    #@marks(1) # optional, because marks(1) is the default
    def test00_gas_init(self):
        try:
            sut = CombustionCar(123.4, 3.45)
            actual_cur, actual_max = sut.get_gas_tank_status()
        except:
            m = "Unexpected error when checking the gas tank of a CombustionCar directly after initialization."
            self.fail(m)
        m = "Incorrect result when checking the gas tank of a CombustionCar directly after initialization."
        self.assertAlmostEqual(123.4, actual_cur, delta=0.001, msg=m)
        self.assertAlmostEqual(123.4, actual_max, delta=0.001, msg=m)

    def test01_remaining_range(self):
        try:
            sut = CombustionCar(12.0, 2.5)
            actual = sut.get_remaining_range()
            expected = 100 * 12.0/2.5
        except:
            m = "Unexpected error when checking the remaining range of a CombustionCar with a full tank."
            self.fail(m)
        m = "Incorrect result when checking the remaining range of a CombustionCar with a full tank."
        self.assertAlmostEqual(expected, actual, delta=0.001, msg=m)

    def test02_drive(self):
        try:
            sut = CombustionCar(12.0, 2.5)
            sut.drive(100.0)
            actual_cur, actual_max = sut.get_gas_tank_status()
        except:
            m = "Unexpected error when checking the gas tank of a CombustionCar after a short drive."
            self.fail(m)
        m = "Incorrect result when checking the gas tank of a CombustionCar after a short drive."
        self.assertAlmostEqual(9.5, actual_cur, delta=0.001, msg=m)
        self.assertAlmostEqual(12.0, actual_max, delta=0.001, msg=m)

    def test03_error_drive_wrong_type(self):
        try:
            sut = CombustionCar(10.0, 2.5)
            sut.drive("")
        except Warning:
            return
        except:
            m = "Unexpected error when passing a non-float to 'CombustionCar.drive'."
            self.fail(m)
        else:
            m = "Passing a non-float to 'CombustionCar.drive' should raise a Warning."
            self.fail(m)

    def test04_error_drive_too_small(self):
        try:
            sut = CombustionCar(10.0, 2.5)
            sut.drive(-1.0)
        except Warning:
            return
        except:
            m = "Unexpected error when passing a negative distance to 'CombustionCar.drive'."
            self.fail(m)
        else:
            m = "Passing a negative distance to 'CombustionCar.drive' should raise a Warning."
            self.fail(m)

    def test05_error_drive_too_far(self):
        try:
            sut = CombustionCar(10.0, 2.5)
            sut.drive(401.0)
        except Warning:
            return
        except:
            m = "Unexpected error when driving a CombustionCar until the gas tank is depleted."
            self.fail(m)
        else:
            m = "Driving a CombustionCar until the gas tank is depleted should raise a Warning."
            self.fail(m)

    def test06_error_drive_too_far_depletes_gas_tank(self):
        try:
            sut = CombustionCar(10.0, 2.5)
            sut.drive(401.0)
        except:
            pass
        else:
            self.fail("Depleting the gas tank in a CombustionCar does not raise an exception.")
        try:
            actual = sut.get_gas_tank_status()
        except:
            self.fail("Failed to get gas tank status of a CombustionCar after fully depleting the gas.")
        m = "Driving a CombustionCar until the gas tank is depleted should remove all gas from the tank."
        self.assertEqual((0, 10), actual, m)

    def test07_fuel(self):
        try:
            sut = CombustionCar(12.0, 2.5)
            sut.drive(100.0)
            sut.fuel(1.0)
            actual_cur, actual_max = sut.get_gas_tank_status()
        except:
            m = "Unexpected error when checking the gas tank of a CombustionCar after driving and refueling."
            self.fail(m)
        m = "Incorrect result when checking the gas tank of a CombustionCar after driving and refueling."
        self.assertAlmostEqual(10.5, actual_cur, delta=0.001, msg=m)
        self.assertAlmostEqual(12.0, actual_max, delta=0.001, msg=m)

    def test08_error_fuel_overfill(self):
        try:
            sut = CombustionCar(10.0, 2.5)
            sut.drive(100.0)
            sut.fuel(2.6)
        except Warning:
            return
        except:
            m = "Unexpected error when overfilling the gas tank of a CombustionCar after a drive."
            self.fail(m)
        else:
            m = "Overfilling the gas tank of a CombustionCar after a drive should raise a Warning."
            self.fail(m)

    def test09_error_init_capacity_type(self):
        try:
            CombustionCar("", 3.45)
        except Warning:
            return
        except:
            m = "Unexpected error initializing a CombustionCar with a non-float tank capacity."
            self.fail(m)
        else:
            m = "Initializing a CombustionCar with a non-float tank capacity should raise a Warning."
            self.fail(m)

    def test10_error_init_capacity_value(self):
        try:
            CombustionCar(-1.0, 3.45)
        except Warning:
            return
        except:
            m = "Unexpected error initializing a CombustionCar with a non-positive tank capacity."
            self.fail(m)
        else:
            m = "Initializing a CombustionCar with a non-positive tank capacity should raise a Warning."
            self.fail(m)

    def test11_error_init_mileage_type(self):
        try:
            CombustionCar(123.4, "")
        except Warning:
            return
        except:
            m = "Unexpected error initializing a CombustionCar with a non-float mileage."
            self.fail(m)
        else:
            m = "Initializing a CombustionCar with a non-float mileage should raise a Warning."
            self.fail(m)

    def test12_error_init_mileage_value(self):
        try:
            CombustionCar(123.4, -1.0)
        except Warning:
            return
        except:
            m = "Unexpected error initializing a CombustionCar with a non-positive mileage."
            self.fail(m)
        else:
            m = "Initializing a CombustionCar with a non-positive mileage should raise a Warning."
            self.fail(m)
