# -*- coding: utf-8 -*-


import os
import io
import json
import shutil
from fhirclient import server
import unittest
import fhirclient.models.fhirabstractbase as fabst
from tests.test_client import datadir, serverdir, outputdir


class TestServer(unittest.TestCase):
    
    def testValidCapabilityStatement(self):
        shutil.copyfile(os.path.join(datadir, 'metadata_valid.json'), os.path.join(serverdir, 'metadata'))
        mock = MockServer()
        mock.get_capability()
        
        self.assertIsNotNone(mock.auth._registration_uri)
        self.assertIsNotNone(mock.auth._authorize_uri)
        self.assertIsNotNone(mock.auth._token_uri)
    
    def testStateConservation(self):
        shutil.copyfile(os.path.join(datadir, 'metadata_valid.json'), os.path.join(serverdir, 'metadata'))
        mock = MockServer()
        self.assertIsNotNone(mock.capabilityStatement)
        
        fhir = server.FHIRServer(None, state=mock.state)
        self.assertIsNotNone(fhir.auth._registration_uri)
        self.assertIsNotNone(fhir.auth._authorize_uri)
        self.assertIsNotNone(fhir.auth._token_uri)
    
    def testInvalidCapabilityStatement(self):
        shutil.copyfile(os.path.join(datadir, 'metadata_invalid.json'), os.path.join(serverdir, 'metadata'))
        mock = MockServer()
        expected_data_fname = os.path.join(outputdir, 'metadata_errors.txt')
        try:
            mock.get_capability()
            self.assertTrue(False, "Must have thrown exception")
        except fabst.FHIRValidationError as e:
            if not os.path.exists(expected_data_fname):
                with open(expected_data_fname, 'w') as f:
                    f.write(str(e))
                self.fail(f"Writing a new copy of {expected_data_fname} - rerun test")
            with open(expected_data_fname) as f:
                expected = f.read()
            self.assertEqual(expected, str(e))


class MockServer(server.FHIRServer):
    """ Reads local files.
    """
    
    def __init__(self):
        super().__init__(None, base_uri='https://fhir.smarthealthit.org')
    
    def request_json(self, path, nosign=False):
        assert path
        with io.open(os.path.join(serverdir, path), encoding='utf-8') as handle:
            return json.load(handle)
        
        return None
    
