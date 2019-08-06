#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 on 2019-08-06.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import capabilitystatement2
from .fhirdate import FHIRDate


class CapabilityStatement2Tests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CapabilityStatement2", js["resourceType"])
        return capabilitystatement2.CapabilityStatement2(js)
    
    def testCapabilityStatement21(self):
        inst = self.instantiate_from("capabilitystatement2-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CapabilityStatement2 instance")
        self.implCapabilityStatement21(inst)
        
        js = inst.as_json()
        self.assertEqual("CapabilityStatement2", js["resourceType"])
        inst2 = capabilitystatement2.CapabilityStatement2(js)
        self.implCapabilityStatement21(inst2)
    
    def implCapabilityStatement21(self, inst):
        self.assertEqual(inst.contact[0].name, "System Administrator")
        self.assertEqual(inst.contact[0].telecom[0].system, "email")
        self.assertEqual(inst.contact[0].telecom[0].value, "wile@acme.org")
        self.assertEqual(inst.copyright, "Copyright © Acme Healthcare and GoodCorp EHR Systems")
        self.assertEqual(inst.date.date, FHIRDate("2012-01-04").date)
        self.assertEqual(inst.date.as_json(), "2012-01-04")
        self.assertEqual(inst.description, "This is the FHIR capability statement for the main EHR at ACME for the private interface - it does not describe the public interface")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.fhirVersion, "4.1.0")
        self.assertEqual(inst.format[0], "xml")
        self.assertEqual(inst.format[1], "json")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.implementation.description, "main EHR at ACME")
        self.assertEqual(inst.implementation.url, "http://10.2.3.4/fhir")
        self.assertEqual(inst.implementationGuide[0], "http://hl7.org/fhir/us/lab")
        self.assertEqual(inst.instantiates[0], "http://ihe.org/fhir/CapabilityStatement2/pixm-client")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "US")
        self.assertEqual(inst.jurisdiction[0].coding[0].display, "United States of America (the)")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.kind, "instance")
        self.assertEqual(inst.name, "ACME-EHR")
        self.assertEqual(inst.patchFormat[0], "application/xml-patch+xml")
        self.assertEqual(inst.patchFormat[1], "application/json-patch+json")
        self.assertEqual(inst.publisher, "ACME Corporation")
        self.assertEqual(inst.purpose, "Main EHR capability statement, published for contracting and operational support")
        self.assertEqual(inst.rest[0].compartment[0], "http://hl7.org/fhir/CompartmentDefinition/patient")
        self.assertEqual(inst.rest[0].documentation, "Main FHIR endpoint for acem health")
        self.assertEqual(inst.rest[0].interaction[0].code, "transaction")
        self.assertEqual(inst.rest[0].interaction[1].code, "history-system")
        self.assertEqual(inst.rest[0].mode, "server")
        self.assertEqual(inst.rest[0].resource[0].documentation, "This server does not let the clients create identities.")
        self.assertEqual(inst.rest[0].resource[0].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[0].interaction[1].code, "vread")
        self.assertEqual(inst.rest[0].resource[0].interaction[1].documentation, "Only supported for patient records since 12-Dec 2012")
        self.assertEqual(inst.rest[0].resource[0].interaction[2].code, "update")
        self.assertEqual(inst.rest[0].resource[0].interaction[3].code, "history-instance")
        self.assertEqual(inst.rest[0].resource[0].interaction[4].code, "create")
        self.assertEqual(inst.rest[0].resource[0].interaction[5].code, "history-type")
        self.assertEqual(inst.rest[0].resource[0].profile, "http://registry.fhir.org/r4/StructureDefinition/7896271d-57f6-4231-89dc-dcc91eab2416")
        self.assertEqual(inst.rest[0].resource[0].searchParam[0].definition, "http://hl7.org/fhir/SearchParameter/Patient-identifier")
        self.assertEqual(inst.rest[0].resource[0].searchParam[0].documentation, "Only supports search by institution MRN")
        self.assertEqual(inst.rest[0].resource[0].searchParam[0].name, "identifier")
        self.assertEqual(inst.rest[0].resource[0].searchParam[0].type, "token")
        self.assertEqual(inst.rest[0].resource[0].searchParam[1].definition, "http://hl7.org/fhir/SearchParameter/Patient-general-practitioner")
        self.assertEqual(inst.rest[0].resource[0].searchParam[1].name, "general-practitioner")
        self.assertEqual(inst.rest[0].resource[0].searchParam[1].type, "reference")
        self.assertEqual(inst.rest[0].resource[0].supportedProfile[0], "http://registry.fhir.org/r4/StructureDefinition/00ab9e7a-06c7-4f77-9234-4154ca1e3347")
        self.assertEqual(inst.rest[0].resource[0].type, "Patient")
        self.assertEqual(inst.software.name, "EHR")
        self.assertEqual(inst.software.releaseDate.date, FHIRDate("2012-01-04").date)
        self.assertEqual(inst.software.releaseDate.as_json(), "2012-01-04")
        self.assertEqual(inst.software.version, "0.00.020.2134")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "ACME EHR capability statement")
        self.assertEqual(inst.url, "urn:uuid:68D043B5-9ECF-4559-A57A-396E0D452311")
        self.assertEqual(inst.useContext[0].code.code, "focus")
        self.assertEqual(inst.useContext[0].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].code, "positive")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].system, "http://terminology.hl7.org/CodeSystem/variant-state")
        self.assertEqual(inst.version, "20130510")
    
    def testCapabilityStatement22(self):
        inst = self.instantiate_from("capabilitystatement2-phr-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CapabilityStatement2 instance")
        self.implCapabilityStatement22(inst)
        
        js = inst.as_json()
        self.assertEqual("CapabilityStatement2", js["resourceType"])
        inst2 = capabilitystatement2.CapabilityStatement2(js)
        self.implCapabilityStatement22(inst2)
    
    def implCapabilityStatement22(self, inst):
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2013-06-18").date)
        self.assertEqual(inst.date.as_json(), "2013-06-18")
        self.assertEqual(inst.description, "Prototype Capability Statement for September 2013 Connectathon")
        self.assertEqual(inst.fhirVersion, "4.1.0")
        self.assertEqual(inst.format[0], "json")
        self.assertEqual(inst.format[1], "xml")
        self.assertEqual(inst.id, "phr")
        self.assertEqual(inst.kind, "capability")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "PHR Template")
        self.assertEqual(inst.publisher, "FHIR Project")
        self.assertEqual(inst.rest[0].documentation, "Protoype server Capability Statement for September 2013 Connectathon")
        self.assertEqual(inst.rest[0].mode, "server")
        self.assertEqual(inst.rest[0].resource[0].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[0].interaction[1].code, "search-type")
        self.assertEqual(inst.rest[0].resource[0].interaction[1].documentation, "When a client searches patients with no search criteria, they get a list of all patients they have access too. Servers may elect to offer additional search parameters, but this is not required")
        self.assertEqual(inst.rest[0].resource[0].type, "Patient")
        self.assertEqual(inst.rest[0].resource[1].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[1].interaction[1].code, "search-type")
        self.assertEqual(inst.rest[0].resource[1].searchParam[0].documentation, "_id parameter always supported. For the connectathon, servers may elect which search parameters are supported")
        self.assertEqual(inst.rest[0].resource[1].searchParam[0].name, "_id")
        self.assertEqual(inst.rest[0].resource[1].searchParam[0].type, "token")
        self.assertEqual(inst.rest[0].resource[1].type, "DocumentReference")
        self.assertEqual(inst.rest[0].resource[2].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[2].interaction[1].code, "search-type")
        self.assertEqual(inst.rest[0].resource[2].searchParam[0].documentation, "Standard _id parameter")
        self.assertEqual(inst.rest[0].resource[2].searchParam[0].name, "_id")
        self.assertEqual(inst.rest[0].resource[2].searchParam[0].type, "token")
        self.assertEqual(inst.rest[0].resource[2].type, "Condition")
        self.assertEqual(inst.rest[0].resource[3].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[3].interaction[1].code, "search-type")
        self.assertEqual(inst.rest[0].resource[3].searchParam[0].documentation, "Standard _id parameter")
        self.assertEqual(inst.rest[0].resource[3].searchParam[0].name, "_id")
        self.assertEqual(inst.rest[0].resource[3].searchParam[0].type, "token")
        self.assertEqual(inst.rest[0].resource[3].searchParam[1].documentation, "which diagnostic discipline/department created the report")
        self.assertEqual(inst.rest[0].resource[3].searchParam[1].name, "service")
        self.assertEqual(inst.rest[0].resource[3].searchParam[1].type, "token")
        self.assertEqual(inst.rest[0].resource[3].type, "DiagnosticReport")
        self.assertEqual(inst.software.name, "ACME PHR Server")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")

