#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-07-15.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import auditevent
from .fhirdate import FHIRDate


class AuditEventTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("AuditEvent", js["resourceType"])
        return auditevent.AuditEvent(js)
    
    def testAuditEvent1(self):
        inst = self.instantiate_from("audit-event-example-search.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent1(inst)
        
        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent1(inst2)
    
    def implAuditEvent1(self, inst):
        self.assertEqual(inst.action, "E")
        self.assertEqual(inst.agent[0].altId, "601847123")
        self.assertEqual(inst.agent[0].name, "Grahame Grieve")
        self.assertTrue(inst.agent[0].requestor)
        self.assertEqual(inst.agent[0].type.coding[0].code, "humanuser")
        self.assertEqual(inst.agent[0].type.coding[0].display, "human user")
        self.assertEqual(inst.agent[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/extra-security-role-type")
        self.assertEqual(inst.agent[1].altId, "6580")
        self.assertEqual(inst.agent[1].network.address, "Workstation1.ehr.familyclinic.com")
        self.assertEqual(inst.agent[1].network.type, "1")
        self.assertFalse(inst.agent[1].requestor)
        self.assertEqual(inst.agent[1].type.coding[0].code, "110153")
        self.assertEqual(inst.agent[1].type.coding[0].display, "Source Role ID")
        self.assertEqual(inst.agent[1].type.coding[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.entity[0].query, "aHR0cDovL2ZoaXItZGV2LmhlYWx0aGludGVyc2VjdGlvbnMuY29tLmF1L29wZW4vRW5jb3VudGVyP3BhcnRpY2lwYW50PTEz")
        self.assertEqual(inst.entity[0].role.code, "24")
        self.assertEqual(inst.entity[0].role.display, "Query")
        self.assertEqual(inst.entity[0].role.system, "http://terminology.hl7.org/CodeSystem/object-role")
        self.assertEqual(inst.entity[0].type.code, "2")
        self.assertEqual(inst.entity[0].type.display, "System Object")
        self.assertEqual(inst.entity[0].type.system, "http://terminology.hl7.org/CodeSystem/audit-entity-type")
        self.assertEqual(inst.id, "example-search")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "0")
        self.assertEqual(inst.recorded.date, FHIRDate("2015-08-22T23:42:24Z").date)
        self.assertEqual(inst.recorded.as_json(), "2015-08-22T23:42:24Z")
        self.assertEqual(inst.source.site, "Cloud")
        self.assertEqual(inst.source.type[0].code, "3")
        self.assertEqual(inst.source.type[0].display, "Web Server")
        self.assertEqual(inst.source.type[0].system, "http://terminology.hl7.org/CodeSystem/security-source-type")
        self.assertEqual(inst.subtype[0].code, "search")
        self.assertEqual(inst.subtype[0].display, "search")
        self.assertEqual(inst.subtype[0].system, "http://hl7.org/fhir/restful-interaction")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.code, "rest")
        self.assertEqual(inst.type.display, "Restful Operation")
        self.assertEqual(inst.type.system, "http://terminology.hl7.org/CodeSystem/audit-event-type")
    
    def testAuditEvent2(self):
        inst = self.instantiate_from("audit-event-example-logout.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent2(inst)
        
        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent2(inst2)
    
    def implAuditEvent2(self, inst):
        self.assertEqual(inst.action, "E")
        self.assertEqual(inst.agent[0].altId, "601847123")
        self.assertEqual(inst.agent[0].name, "Grahame Grieve")
        self.assertEqual(inst.agent[0].network.address, "127.0.0.1")
        self.assertEqual(inst.agent[0].network.type, "2")
        self.assertTrue(inst.agent[0].requestor)
        self.assertEqual(inst.agent[0].type.coding[0].code, "humanuser")
        self.assertEqual(inst.agent[0].type.coding[0].display, "human user")
        self.assertEqual(inst.agent[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/extra-security-role-type")
        self.assertEqual(inst.agent[1].altId, "6580")
        self.assertEqual(inst.agent[1].network.address, "Workstation1.ehr.familyclinic.com")
        self.assertEqual(inst.agent[1].network.type, "1")
        self.assertFalse(inst.agent[1].requestor)
        self.assertEqual(inst.agent[1].type.coding[0].code, "110153")
        self.assertEqual(inst.agent[1].type.coding[0].display, "Source Role ID")
        self.assertEqual(inst.agent[1].type.coding[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.id, "example-logout")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "0")
        self.assertEqual(inst.recorded.date, FHIRDate("2013-06-20T23:46:41Z").date)
        self.assertEqual(inst.recorded.as_json(), "2013-06-20T23:46:41Z")
        self.assertEqual(inst.source.site, "Cloud")
        self.assertEqual(inst.source.type[0].code, "3")
        self.assertEqual(inst.source.type[0].display, "Web Server")
        self.assertEqual(inst.source.type[0].system, "http://terminology.hl7.org/CodeSystem/security-source-type")
        self.assertEqual(inst.subtype[0].code, "110123")
        self.assertEqual(inst.subtype[0].display, "Logout")
        self.assertEqual(inst.subtype[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.code, "110114")
        self.assertEqual(inst.type.display, "User Authentication")
        self.assertEqual(inst.type.system, "http://dicom.nema.org/resources/ontology/DCM")
    
    def testAuditEvent3(self):
        inst = self.instantiate_from("audit-event-example-vread.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent3(inst)
        
        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent3(inst2)
    
    def implAuditEvent3(self, inst):
        self.assertEqual(inst.action, "R")
        self.assertEqual(inst.agent[0].altId, "601847123")
        self.assertEqual(inst.agent[0].name, "Grahame Grieve")
        self.assertTrue(inst.agent[0].requestor)
        self.assertEqual(inst.agent[0].type.coding[0].code, "humanuser")
        self.assertEqual(inst.agent[0].type.coding[0].display, "human user")
        self.assertEqual(inst.agent[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/extra-security-role-type")
        self.assertEqual(inst.agent[1].altId, "6580")
        self.assertEqual(inst.agent[1].network.address, "Workstation1.ehr.familyclinic.com")
        self.assertEqual(inst.agent[1].network.type, "1")
        self.assertFalse(inst.agent[1].requestor)
        self.assertEqual(inst.agent[1].type.coding[0].code, "110153")
        self.assertEqual(inst.agent[1].type.coding[0].display, "Source Role ID")
        self.assertEqual(inst.agent[1].type.coding[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.entity[0].lifecycle.code, "6")
        self.assertEqual(inst.entity[0].lifecycle.display, "Access / Use")
        self.assertEqual(inst.entity[0].lifecycle.system, "http://terminology.hl7.org/CodeSystem/dicom-audit-lifecycle")
        self.assertEqual(inst.entity[0].type.code, "2")
        self.assertEqual(inst.entity[0].type.display, "System Object")
        self.assertEqual(inst.entity[0].type.system, "http://terminology.hl7.org/CodeSystem/audit-entity-type")
        self.assertEqual(inst.id, "example-rest")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "0")
        self.assertEqual(inst.recorded.date, FHIRDate("2013-06-20T23:42:24Z").date)
        self.assertEqual(inst.recorded.as_json(), "2013-06-20T23:42:24Z")
        self.assertEqual(inst.source.site, "Cloud")
        self.assertEqual(inst.source.type[0].code, "3")
        self.assertEqual(inst.source.type[0].display, "Web Server")
        self.assertEqual(inst.source.type[0].system, "http://terminology.hl7.org/CodeSystem/security-source-type")
        self.assertEqual(inst.subtype[0].code, "vread")
        self.assertEqual(inst.subtype[0].display, "vread")
        self.assertEqual(inst.subtype[0].system, "http://hl7.org/fhir/restful-interaction")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.code, "rest")
        self.assertEqual(inst.type.display, "Restful Operation")
        self.assertEqual(inst.type.system, "http://terminology.hl7.org/CodeSystem/audit-event-type")
    
    def testAuditEvent4(self):
        inst = self.instantiate_from("audit-event-example-media.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent4(inst)
        
        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent4(inst2)
    
    def implAuditEvent4(self, inst):
        self.assertEqual(inst.action, "R")
        self.assertFalse(inst.agent[0].requestor)
        self.assertEqual(inst.agent[0].type.coding[0].code, "110153")
        self.assertEqual(inst.agent[0].type.coding[0].display, "Source Role ID")
        self.assertEqual(inst.agent[0].type.coding[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.agent[1].altId, "601847123")
        self.assertEqual(inst.agent[1].name, "Grahame Grieve")
        self.assertTrue(inst.agent[1].requestor)
        self.assertEqual(inst.agent[1].type.coding[0].code, "humanuser")
        self.assertEqual(inst.agent[1].type.coding[0].display, "human user")
        self.assertEqual(inst.agent[1].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/extra-security-role-type")
        self.assertEqual(inst.agent[2].media.code, "110033")
        self.assertEqual(inst.agent[2].media.display, "DVD")
        self.assertEqual(inst.agent[2].media.system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.agent[2].name, "Media title: Hello World")
        self.assertFalse(inst.agent[2].requestor)
        self.assertEqual(inst.agent[2].type.coding[0].code, "110154")
        self.assertEqual(inst.agent[2].type.coding[0].display, "Destination Media")
        self.assertEqual(inst.agent[2].type.coding[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.entity[0].role.code, "1")
        self.assertEqual(inst.entity[0].role.display, "Patient")
        self.assertEqual(inst.entity[0].role.system, "http://terminology.hl7.org/CodeSystem/object-role")
        self.assertEqual(inst.entity[0].type.code, "1")
        self.assertEqual(inst.entity[0].type.display, "Person")
        self.assertEqual(inst.entity[0].type.system, "http://terminology.hl7.org/CodeSystem/audit-entity-type")
        self.assertEqual(inst.entity[1].role.code, "20")
        self.assertEqual(inst.entity[1].role.display, "Job")
        self.assertEqual(inst.entity[1].role.system, "http://terminology.hl7.org/CodeSystem/object-role")
        self.assertEqual(inst.entity[1].type.code, "2")
        self.assertEqual(inst.entity[1].type.display, "System Object")
        self.assertEqual(inst.entity[1].type.system, "http://terminology.hl7.org/CodeSystem/audit-entity-type")
        self.assertEqual(inst.entity[2].type.code, "2")
        self.assertEqual(inst.entity[2].type.display, "System Object")
        self.assertEqual(inst.entity[2].type.system, "http://terminology.hl7.org/CodeSystem/audit-entity-type")
        self.assertEqual(inst.id, "example-media")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "0")
        self.assertEqual(inst.recorded.date, FHIRDate("2015-08-27T23:42:24Z").date)
        self.assertEqual(inst.recorded.as_json(), "2015-08-27T23:42:24Z")
        self.assertEqual(inst.subtype[0].code, "ITI-32")
        self.assertEqual(inst.subtype[0].display, "Distribute Document Set on Media")
        self.assertEqual(inst.subtype[0].system, "urn:oid:1.3.6.1.4.1.19376.1.2")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.code, "110106")
        self.assertEqual(inst.type.display, "Export")
        self.assertEqual(inst.type.system, "http://dicom.nema.org/resources/ontology/DCM")
    
    def testAuditEvent5(self):
        inst = self.instantiate_from("audit-event-example-login.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent5(inst)
        
        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent5(inst2)
    
    def implAuditEvent5(self, inst):
        self.assertEqual(inst.action, "E")
        self.assertEqual(inst.agent[0].altId, "601847123")
        self.assertEqual(inst.agent[0].name, "Grahame Grieve")
        self.assertEqual(inst.agent[0].network.address, "127.0.0.1")
        self.assertEqual(inst.agent[0].network.type, "2")
        self.assertTrue(inst.agent[0].requestor)
        self.assertEqual(inst.agent[0].type.coding[0].code, "humanuser")
        self.assertEqual(inst.agent[0].type.coding[0].display, "human user")
        self.assertEqual(inst.agent[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/extra-security-role-type")
        self.assertEqual(inst.agent[1].altId, "6580")
        self.assertEqual(inst.agent[1].network.address, "Workstation1.ehr.familyclinic.com")
        self.assertEqual(inst.agent[1].network.type, "1")
        self.assertFalse(inst.agent[1].requestor)
        self.assertEqual(inst.agent[1].type.coding[0].code, "110153")
        self.assertEqual(inst.agent[1].type.coding[0].display, "Source Role ID")
        self.assertEqual(inst.agent[1].type.coding[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.id, "example-login")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "0")
        self.assertEqual(inst.recorded.date, FHIRDate("2013-06-20T23:41:23Z").date)
        self.assertEqual(inst.recorded.as_json(), "2013-06-20T23:41:23Z")
        self.assertEqual(inst.source.site, "Cloud")
        self.assertEqual(inst.source.type[0].code, "3")
        self.assertEqual(inst.source.type[0].display, "Web Server")
        self.assertEqual(inst.source.type[0].system, "http://terminology.hl7.org/CodeSystem/security-source-type")
        self.assertEqual(inst.subtype[0].code, "110122")
        self.assertEqual(inst.subtype[0].display, "Login")
        self.assertEqual(inst.subtype[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.code, "110114")
        self.assertEqual(inst.type.display, "User Authentication")
        self.assertEqual(inst.type.system, "http://dicom.nema.org/resources/ontology/DCM")
    
    def testAuditEvent6(self):
        inst = self.instantiate_from("audit-event-example-pixQuery.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent6(inst)
        
        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent6(inst2)
    
    def implAuditEvent6(self, inst):
        self.assertEqual(inst.action, "E")
        self.assertEqual(inst.agent[0].altId, "6580")
        self.assertEqual(inst.agent[0].network.address, "Workstation1.ehr.familyclinic.com")
        self.assertEqual(inst.agent[0].network.type, "1")
        self.assertFalse(inst.agent[0].requestor)
        self.assertEqual(inst.agent[0].type.coding[0].code, "110153")
        self.assertEqual(inst.agent[0].type.coding[0].display, "Source Role ID")
        self.assertEqual(inst.agent[0].type.coding[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.agent[1].altId, "601847123")
        self.assertEqual(inst.agent[1].name, "Grahame Grieve")
        self.assertTrue(inst.agent[1].requestor)
        self.assertEqual(inst.agent[1].type.coding[0].code, "humanuser")
        self.assertEqual(inst.agent[1].type.coding[0].display, "human user")
        self.assertEqual(inst.agent[1].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/extra-security-role-type")
        self.assertEqual(inst.entity[0].role.code, "1")
        self.assertEqual(inst.entity[0].role.display, "Patient")
        self.assertEqual(inst.entity[0].role.system, "http://terminology.hl7.org/CodeSystem/object-role")
        self.assertEqual(inst.entity[0].type.code, "1")
        self.assertEqual(inst.entity[0].type.display, "Person")
        self.assertEqual(inst.entity[0].type.system, "http://terminology.hl7.org/CodeSystem/audit-entity-type")
        self.assertEqual(inst.entity[1].detail[0].type, "MSH-10")
        self.assertEqual(inst.entity[1].detail[0].valueBase64Binary, "MS4yLjg0MC4xMTQzNTAuMS4xMy4wLjEuNy4xLjE=")
        self.assertEqual(inst.entity[1].role.code, "24")
        self.assertEqual(inst.entity[1].role.display, "Query")
        self.assertEqual(inst.entity[1].role.system, "http://terminology.hl7.org/CodeSystem/object-role")
        self.assertEqual(inst.entity[1].type.code, "2")
        self.assertEqual(inst.entity[1].type.display, "System Object")
        self.assertEqual(inst.entity[1].type.system, "http://terminology.hl7.org/CodeSystem/audit-entity-type")
        self.assertEqual(inst.id, "example-pixQuery")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "0")
        self.assertEqual(inst.recorded.date, FHIRDate("2015-08-26T23:42:24Z").date)
        self.assertEqual(inst.recorded.as_json(), "2015-08-26T23:42:24Z")
        self.assertEqual(inst.subtype[0].code, "ITI-9")
        self.assertEqual(inst.subtype[0].display, "PIX Query")
        self.assertEqual(inst.subtype[0].system, "urn:oid:1.3.6.1.4.1.19376.1.2")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.code, "110112")
        self.assertEqual(inst.type.display, "Query")
        self.assertEqual(inst.type.system, "http://dicom.nema.org/resources/ontology/DCM")
    
    def testAuditEvent7(self):
        inst = self.instantiate_from("auditevent-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent7(inst)
        
        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent7(inst2)
    
    def implAuditEvent7(self, inst):
        self.assertEqual(inst.action, "E")
        self.assertEqual(inst.agent[0].network.address, "127.0.0.1")
        self.assertEqual(inst.agent[0].network.type, "2")
        self.assertFalse(inst.agent[0].requestor)
        self.assertEqual(inst.agent[0].role[0].text, "Service User (Logon)")
        self.assertEqual(inst.agent[0].type.coding[0].code, "humanuser")
        self.assertEqual(inst.agent[0].type.coding[0].display, "human user")
        self.assertEqual(inst.agent[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/extra-security-role-type")
        self.assertEqual(inst.agent[1].altId, "6580")
        self.assertEqual(inst.agent[1].network.address, "Workstation1.ehr.familyclinic.com")
        self.assertEqual(inst.agent[1].network.type, "1")
        self.assertFalse(inst.agent[1].requestor)
        self.assertEqual(inst.agent[1].type.coding[0].code, "110153")
        self.assertEqual(inst.agent[1].type.coding[0].display, "Source Role ID")
        self.assertEqual(inst.agent[1].type.coding[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.entity[0].lifecycle.code, "6")
        self.assertEqual(inst.entity[0].lifecycle.display, "Access / Use")
        self.assertEqual(inst.entity[0].lifecycle.system, "http://terminology.hl7.org/CodeSystem/dicom-audit-lifecycle")
        self.assertEqual(inst.entity[0].name, "Grahame's Laptop")
        self.assertEqual(inst.entity[0].role.code, "4")
        self.assertEqual(inst.entity[0].role.display, "Domain Resource")
        self.assertEqual(inst.entity[0].role.system, "http://terminology.hl7.org/CodeSystem/object-role")
        self.assertEqual(inst.entity[0].type.code, "4")
        self.assertEqual(inst.entity[0].type.display, "Other")
        self.assertEqual(inst.entity[0].type.system, "http://terminology.hl7.org/CodeSystem/audit-entity-type")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "0")
        self.assertEqual(inst.recorded.date, FHIRDate("2012-10-25T22:04:27+11:00").date)
        self.assertEqual(inst.recorded.as_json(), "2012-10-25T22:04:27+11:00")
        self.assertEqual(inst.source.site, "Development")
        self.assertEqual(inst.source.type[0].code, "110122")
        self.assertEqual(inst.source.type[0].display, "Login")
        self.assertEqual(inst.source.type[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.subtype[0].code, "110120")
        self.assertEqual(inst.subtype[0].display, "Application Start")
        self.assertEqual(inst.subtype[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Application Start for under service login &quot;Grahame&quot; (id: Grahame's Test HL7Connect)</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.code, "110100")
        self.assertEqual(inst.type.display, "Application Activity")
        self.assertEqual(inst.type.system, "http://dicom.nema.org/resources/ontology/DCM")
    
    def testAuditEvent8(self):
        inst = self.instantiate_from("auditevent-example-disclosure.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent8(inst)
        
        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent8(inst2)
    
    def implAuditEvent8(self, inst):
        self.assertEqual(inst.action, "R")
        self.assertEqual(inst.agent[0].altId, "notMe")
        self.assertEqual(inst.agent[0].name, "That guy everyone wishes would be caught")
        self.assertEqual(inst.agent[0].network.address, "custodian.net")
        self.assertEqual(inst.agent[0].network.type, "1")
        self.assertEqual(inst.agent[0].policy[0], "http://consent.com/yes")
        self.assertTrue(inst.agent[0].requestor)
        self.assertEqual(inst.agent[0].type.coding[0].code, "110153")
        self.assertEqual(inst.agent[0].type.coding[0].display, "Source Role ID")
        self.assertEqual(inst.agent[0].type.coding[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.agent[1].network.address, "marketing.land")
        self.assertEqual(inst.agent[1].network.type, "1")
        self.assertEqual(inst.agent[1].purposeOfUse[0].coding[0].code, "HMARKT")
        self.assertEqual(inst.agent[1].purposeOfUse[0].coding[0].display, "healthcare marketing")
        self.assertEqual(inst.agent[1].purposeOfUse[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertFalse(inst.agent[1].requestor)
        self.assertEqual(inst.agent[1].type.coding[0].code, "110152")
        self.assertEqual(inst.agent[1].type.coding[0].display, "Destination Role ID")
        self.assertEqual(inst.agent[1].type.coding[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.entity[0].role.code, "1")
        self.assertEqual(inst.entity[0].role.display, "Patient")
        self.assertEqual(inst.entity[0].role.system, "http://terminology.hl7.org/CodeSystem/object-role")
        self.assertEqual(inst.entity[0].type.code, "1")
        self.assertEqual(inst.entity[0].type.display, "Person")
        self.assertEqual(inst.entity[0].type.system, "http://terminology.hl7.org/CodeSystem/audit-entity-type")
        self.assertEqual(inst.entity[1].description, "data about Everthing important")
        self.assertEqual(inst.entity[1].lifecycle.code, "11")
        self.assertEqual(inst.entity[1].lifecycle.display, "Disclosure")
        self.assertEqual(inst.entity[1].lifecycle.system, "http://terminology.hl7.org/CodeSystem/dicom-audit-lifecycle")
        self.assertEqual(inst.entity[1].name, "Namne of What")
        self.assertEqual(inst.entity[1].role.code, "4")
        self.assertEqual(inst.entity[1].role.display, "Domain Resource")
        self.assertEqual(inst.entity[1].role.system, "http://terminology.hl7.org/CodeSystem/object-role")
        self.assertEqual(inst.entity[1].securityLabel[0].code, "V")
        self.assertEqual(inst.entity[1].securityLabel[0].display, "very restricted")
        self.assertEqual(inst.entity[1].securityLabel[0].system, "http://terminology.hl7.org/CodeSystem/v3-Confidentiality")
        self.assertEqual(inst.entity[1].securityLabel[1].code, "STD")
        self.assertEqual(inst.entity[1].securityLabel[1].display, "sexually transmitted disease information sensitivity")
        self.assertEqual(inst.entity[1].securityLabel[1].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.entity[1].securityLabel[2].code, "DELAU")
        self.assertEqual(inst.entity[1].securityLabel[2].display, "delete after use")
        self.assertEqual(inst.entity[1].securityLabel[2].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.entity[1].type.code, "2")
        self.assertEqual(inst.entity[1].type.display, "System Object")
        self.assertEqual(inst.entity[1].type.system, "http://terminology.hl7.org/CodeSystem/audit-entity-type")
        self.assertEqual(inst.id, "example-disclosure")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "0")
        self.assertEqual(inst.outcomeDesc, "Successful  Disclosure")
        self.assertEqual(inst.purposeOfEvent[0].coding[0].code, "HMARKT")
        self.assertEqual(inst.purposeOfEvent[0].coding[0].display, "healthcare marketing")
        self.assertEqual(inst.purposeOfEvent[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.recorded.date, FHIRDate("2013-09-22T00:08:00Z").date)
        self.assertEqual(inst.recorded.as_json(), "2013-09-22T00:08:00Z")
        self.assertEqual(inst.source.site, "Watcher")
        self.assertEqual(inst.source.type[0].code, "4")
        self.assertEqual(inst.source.type[0].display, "Application Server")
        self.assertEqual(inst.source.type[0].system, "http://terminology.hl7.org/CodeSystem/security-source-type")
        self.assertEqual(inst.subtype[0].code, "Disclosure")
        self.assertEqual(inst.subtype[0].display, "HIPAA disclosure")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Disclosure by some idiot, for marketing reasons, to places unknown, of a Poor Sap, data about Everthing important.</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.code, "110106")
        self.assertEqual(inst.type.display, "Export")
        self.assertEqual(inst.type.system, "http://dicom.nema.org/resources/ontology/DCM")
    
    def testAuditEvent9(self):
        inst = self.instantiate_from("auditevent-example-error.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent9(inst)
        
        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent9(inst2)
    
    def implAuditEvent9(self, inst):
        self.assertEqual(inst.action, "C")
        self.assertEqual(inst.agent[0].altId, "601847123")
        self.assertEqual(inst.agent[0].name, "Grahame Grieve")
        self.assertTrue(inst.agent[0].requestor)
        self.assertEqual(inst.agent[0].type.coding[0].code, "humanuser")
        self.assertEqual(inst.agent[0].type.coding[0].display, "human user")
        self.assertEqual(inst.agent[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/extra-security-role-type")
        self.assertEqual(inst.agent[1].altId, "6580")
        self.assertEqual(inst.agent[1].network.address, "Workstation1.ehr.familyclinic.com")
        self.assertEqual(inst.agent[1].network.type, "1")
        self.assertFalse(inst.agent[1].requestor)
        self.assertEqual(inst.agent[1].type.coding[0].code, "110153")
        self.assertEqual(inst.agent[1].type.coding[0].display, "Source Role ID")
        self.assertEqual(inst.agent[1].type.coding[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.contained[0].id, "o1")
        self.assertEqual(inst.entity[0].detail[0].type, "requested transaction")
        self.assertEqual(inst.entity[0].detail[0].valueString, "http POST ..... ")
        self.assertEqual(inst.entity[0].type.code, "2")
        self.assertEqual(inst.entity[0].type.display, "System Object")
        self.assertEqual(inst.entity[0].type.system, "http://terminology.hl7.org/CodeSystem/audit-entity-type")
        self.assertEqual(inst.entity[1].description, "transaction failed")
        self.assertEqual(inst.entity[1].type.code, "OperationOutcome")
        self.assertEqual(inst.entity[1].type.display, "OperationOutcome")
        self.assertEqual(inst.entity[1].type.system, "http://hl7.org/fhir/resource-types")
        self.assertEqual(inst.id, "example-error")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "8")
        self.assertEqual(inst.outcomeDesc, "Invalid request to create an Operation resource on the Patient endpoint.")
        self.assertEqual(inst.recorded.date, FHIRDate("2017-09-07T23:42:24Z").date)
        self.assertEqual(inst.recorded.as_json(), "2017-09-07T23:42:24Z")
        self.assertEqual(inst.source.site, "Cloud")
        self.assertEqual(inst.source.type[0].code, "3")
        self.assertEqual(inst.source.type[0].display, "Web Server")
        self.assertEqual(inst.source.type[0].system, "http://terminology.hl7.org/CodeSystem/security-source-type")
        self.assertEqual(inst.subtype[0].code, "create")
        self.assertEqual(inst.subtype[0].display, "create")
        self.assertEqual(inst.subtype[0].system, "http://hl7.org/fhir/restful-interaction")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.code, "rest")
        self.assertEqual(inst.type.display, "Restful Operation")
        self.assertEqual(inst.type.system, "http://terminology.hl7.org/CodeSystem/audit-event-type")

