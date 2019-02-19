# -*- coding: utf-8 -*-
"""
author: Ashish Singh

class TestRestAPI includes test cases for call_api() function imported from HW04a.py file


"""

import unittest
import urllib.request

from HW04a import call_api

# This code implements the unit test functionality


class TestRestAPI(unittest.TestCase):
    
    def test_rest_api(self):
        #includes a repository with zero commits
        self.assertTrue(call_api("ashish-python"),{'567': 2, 'dragon_fighter': 1, 'practice': 10, 'Student-Database-810': 29, 'Triangle567': 4,'empty':'Data not available'})

        #All repositories have at least one commit
        self.assertTrue(call_api("raymondyin"),{'2d-shooting-game': 5, 'cs-foundation': 5, 'csc309a3': 26, 'daily-life-organizing': 4, 'FoodHero': 1, 'FoodHeroProject': 29, 'google-interview-university': 30, 'heroku-node': 4, 'IBM-Frontend-Exercise': 15, 'Jandgeo_Project': 22, 'Pumpkin': 30, 'raymondyin.github.io': 1, 'sit-ssw567-homework': 4, 'sit-ssw690-group-work': 4, 'sit-ssw810-homework': 10, 'startbootstrap':
30})


        #Repository does not exist
        with self.assertRaises(urllib.error.URLError):
            call_api(call_api("this_repository_does_not_exist"))


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

