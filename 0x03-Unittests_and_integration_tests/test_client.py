#!/usr/bin/env python3
import unittest
from unittest.mock import Mock
from parameterized import parameterized
from client import GithubOrgClient
'''
Testing client file methods
'''


class TestGithubOrgClient(unittest.TestCase):
    '''
    tests client.GithubOrgClient
    '''

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @unittest.mock.patch('client.get_json')
    def test_org(self, org: str, mock_get):
        '''
        test that GithubOrgClient.org returns the correct value.
        '''
        client_test = GithubOrgClient(org)
        resp = client_test.org
        mock_get.assert_called_once_with(
            "https://api.github.com/orgs/{org}".format(org=org)
        )
