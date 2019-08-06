#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 on 2019-08-06.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import claimresponse
from .fhirdate import FHIRDate


class ClaimResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ClaimResponse", js["resourceType"])
        return claimresponse.ClaimResponse(js)
    
    def testClaimResponse1(self):
        inst = self.instantiate_from("claimresponse-example-unsolicited-preauth.json")
        self.assertIsNotNone(inst, "Must have instantiated a ClaimResponse instance")
        self.implClaimResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("ClaimResponse", js["resourceType"])
        inst2 = claimresponse.ClaimResponse(js)
        self.implClaimResponse1(inst2)
    
    def implClaimResponse1(self, inst):
        self.assertEqual(inst.addItem[0].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.addItem[0].adjudication[0].amount.value, 250.0)
        self.assertEqual(inst.addItem[0].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.addItem[0].adjudication[1].amount.currency, "USD")
        self.assertEqual(inst.addItem[0].adjudication[1].amount.value, 10.0)
        self.assertEqual(inst.addItem[0].adjudication[1].category.coding[0].code, "copay")
        self.assertEqual(inst.addItem[0].adjudication[2].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.addItem[0].adjudication[2].value, 100.0)
        self.assertEqual(inst.addItem[0].adjudication[3].amount.currency, "USD")
        self.assertEqual(inst.addItem[0].adjudication[3].amount.value, 240.0)
        self.assertEqual(inst.addItem[0].adjudication[3].category.coding[0].code, "benefit")
        self.assertEqual(inst.addItem[0].itemSequence[0], 1)
        self.assertEqual(inst.addItem[0].modifier[0].coding[0].code, "x")
        self.assertEqual(inst.addItem[0].modifier[0].coding[0].display, "None")
        self.assertEqual(inst.addItem[0].modifier[0].coding[0].system, "http://example.org/fhir/modifiers")
        self.assertEqual(inst.addItem[0].net.currency, "USD")
        self.assertEqual(inst.addItem[0].net.value, 250.0)
        self.assertEqual(inst.addItem[0].noteNumber[0], 101)
        self.assertEqual(inst.addItem[0].productOrService.coding[0].code, "1101")
        self.assertEqual(inst.addItem[0].productOrService.coding[0].system, "http://example.org/fhir/oralservicecodes")
        self.assertEqual(inst.addItem[1].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.addItem[1].adjudication[0].amount.value, 800.0)
        self.assertEqual(inst.addItem[1].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.addItem[1].adjudication[1].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.addItem[1].adjudication[1].value, 100.0)
        self.assertEqual(inst.addItem[1].adjudication[2].amount.currency, "USD")
        self.assertEqual(inst.addItem[1].adjudication[2].amount.value, 800.0)
        self.assertEqual(inst.addItem[1].adjudication[2].category.coding[0].code, "benefit")
        self.assertEqual(inst.addItem[1].itemSequence[0], 1)
        self.assertEqual(inst.addItem[1].net.currency, "USD")
        self.assertEqual(inst.addItem[1].net.value, 800.0)
        self.assertEqual(inst.addItem[1].productOrService.coding[0].code, "2101")
        self.assertEqual(inst.addItem[1].productOrService.coding[0].display, "Radiograph, series (12)")
        self.assertEqual(inst.addItem[1].productOrService.coding[0].system, "http://example.org/fhir/oralservicecodes")
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "The enclosed services are authorized for your provision within 30 days of this notice.")
        self.assertEqual(inst.id, "UR3503")
        self.assertEqual(inst.identifier[0].system, "http://www.SocialBenefitsInc.com/fhir/ClaimResponse")
        self.assertEqual(inst.identifier[0].value, "UR3503")
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(inst.insurance[0].sequence, 1)
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.payeeType.coding[0].code, "provider")
        self.assertEqual(inst.payeeType.coding[0].system, "http://terminology.hl7.org/CodeSystem/payeetype")
        self.assertEqual(inst.preAuthRef, "18SS12345")
        self.assertEqual(inst.processNote[0].language.coding[0].code, "en-CA")
        self.assertEqual(inst.processNote[0].language.coding[0].system, "urn:ietf:bcp:47")
        self.assertEqual(inst.processNote[0].number, 101)
        self.assertEqual(inst.processNote[0].text, "Please submit a Pre-Authorization request if a more extensive examination or urgent services are required.")
        self.assertEqual(inst.processNote[0].type, "print")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A sample unsolicited pre-authorization response which authorizes basic dental services to be performed for a patient.</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.total[0].amount.currency, "USD")
        self.assertEqual(inst.total[0].amount.value, 1050.0)
        self.assertEqual(inst.total[0].category.coding[0].code, "submitted")
        self.assertEqual(inst.total[1].amount.currency, "USD")
        self.assertEqual(inst.total[1].amount.value, 1040.0)
        self.assertEqual(inst.total[1].category.coding[0].code, "benefit")
        self.assertEqual(inst.type.coding[0].code, "oral")
        self.assertEqual(inst.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/claim-type")
        self.assertEqual(inst.use, "preauthorization")
    
    def testClaimResponse2(self):
        inst = self.instantiate_from("claimresponse-example-additem.json")
        self.assertIsNotNone(inst, "Must have instantiated a ClaimResponse instance")
        self.implClaimResponse2(inst)
        
        js = inst.as_json()
        self.assertEqual("ClaimResponse", js["resourceType"])
        inst2 = claimresponse.ClaimResponse(js)
        self.implClaimResponse2(inst2)
    
    def implClaimResponse2(self, inst):
        self.assertEqual(inst.addItem[0].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.addItem[0].adjudication[0].amount.value, 100.0)
        self.assertEqual(inst.addItem[0].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.addItem[0].adjudication[1].amount.currency, "USD")
        self.assertEqual(inst.addItem[0].adjudication[1].amount.value, 10.0)
        self.assertEqual(inst.addItem[0].adjudication[1].category.coding[0].code, "copay")
        self.assertEqual(inst.addItem[0].adjudication[2].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.addItem[0].adjudication[2].value, 80.0)
        self.assertEqual(inst.addItem[0].adjudication[3].amount.currency, "USD")
        self.assertEqual(inst.addItem[0].adjudication[3].amount.value, 72.0)
        self.assertEqual(inst.addItem[0].adjudication[3].category.coding[0].code, "benefit")
        self.assertEqual(inst.addItem[0].adjudication[3].reason.coding[0].code, "ar002")
        self.assertEqual(inst.addItem[0].adjudication[3].reason.coding[0].display, "Plan Limit Reached")
        self.assertEqual(inst.addItem[0].adjudication[3].reason.coding[0].system, "http://terminology.hl7.org/CodeSystem/adjudication-reason")
        self.assertEqual(inst.addItem[0].itemSequence[0], 1)
        self.assertEqual(inst.addItem[0].modifier[0].coding[0].code, "x")
        self.assertEqual(inst.addItem[0].modifier[0].coding[0].display, "None")
        self.assertEqual(inst.addItem[0].modifier[0].coding[0].system, "http://example.org/fhir/modifiers")
        self.assertEqual(inst.addItem[0].net.currency, "USD")
        self.assertEqual(inst.addItem[0].net.value, 135.57)
        self.assertEqual(inst.addItem[0].noteNumber[0], 101)
        self.assertEqual(inst.addItem[0].productOrService.coding[0].code, "1101")
        self.assertEqual(inst.addItem[0].productOrService.coding[0].system, "http://example.org/fhir/oralservicecodes")
        self.assertEqual(inst.addItem[1].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.addItem[1].adjudication[0].amount.value, 35.57)
        self.assertEqual(inst.addItem[1].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.addItem[1].adjudication[1].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.addItem[1].adjudication[1].value, 80.0)
        self.assertEqual(inst.addItem[1].adjudication[2].amount.currency, "USD")
        self.assertEqual(inst.addItem[1].adjudication[2].amount.value, 28.47)
        self.assertEqual(inst.addItem[1].adjudication[2].category.coding[0].code, "benefit")
        self.assertEqual(inst.addItem[1].itemSequence[0], 1)
        self.assertEqual(inst.addItem[1].net.currency, "USD")
        self.assertEqual(inst.addItem[1].net.value, 35.57)
        self.assertEqual(inst.addItem[1].productOrService.coding[0].code, "2141")
        self.assertEqual(inst.addItem[1].productOrService.coding[0].display, "Radiograph, bytewing")
        self.assertEqual(inst.addItem[1].productOrService.coding[0].system, "http://example.org/fhir/oralservicecodes")
        self.assertEqual(inst.addItem[2].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.addItem[2].adjudication[0].amount.value, 350.0)
        self.assertEqual(inst.addItem[2].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.addItem[2].adjudication[1].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.addItem[2].adjudication[1].value, 80.0)
        self.assertEqual(inst.addItem[2].adjudication[2].amount.currency, "USD")
        self.assertEqual(inst.addItem[2].adjudication[2].amount.value, 270.0)
        self.assertEqual(inst.addItem[2].adjudication[2].category.coding[0].code, "benefit")
        self.assertEqual(inst.addItem[2].detailSequence[0], 2)
        self.assertEqual(inst.addItem[2].itemSequence[0], 3)
        self.assertEqual(inst.addItem[2].modifier[0].coding[0].code, "x")
        self.assertEqual(inst.addItem[2].modifier[0].coding[0].display, "None")
        self.assertEqual(inst.addItem[2].modifier[0].coding[0].system, "http://example.org/fhir/modifiers")
        self.assertEqual(inst.addItem[2].net.currency, "USD")
        self.assertEqual(inst.addItem[2].net.value, 350.0)
        self.assertEqual(inst.addItem[2].noteNumber[0], 101)
        self.assertEqual(inst.addItem[2].productOrService.coding[0].code, "expense")
        self.assertEqual(inst.addItem[2].productOrService.coding[0].system, "http://example.org/fhir/oralservicecodes")
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Claim settled as per contract.")
        self.assertEqual(inst.id, "R3503")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/remittance")
        self.assertEqual(inst.identifier[0].value, "R3503")
        self.assertEqual(inst.item[0].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.item[0].adjudication[0].amount.value, 0.0)
        self.assertEqual(inst.item[0].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.item[0].adjudication[1].amount.currency, "USD")
        self.assertEqual(inst.item[0].adjudication[1].amount.value, 0.0)
        self.assertEqual(inst.item[0].adjudication[1].category.coding[0].code, "benefit")
        self.assertEqual(inst.item[0].itemSequence, 1)
        self.assertEqual(inst.item[1].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.item[1].adjudication[0].amount.value, 105.0)
        self.assertEqual(inst.item[1].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.item[1].adjudication[1].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.item[1].adjudication[1].value, 80.0)
        self.assertEqual(inst.item[1].adjudication[2].amount.currency, "USD")
        self.assertEqual(inst.item[1].adjudication[2].amount.value, 84.0)
        self.assertEqual(inst.item[1].adjudication[2].category.coding[0].code, "benefit")
        self.assertEqual(inst.item[1].itemSequence, 2)
        self.assertEqual(inst.item[2].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.item[2].adjudication[0].amount.value, 750.0)
        self.assertEqual(inst.item[2].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.item[2].adjudication[1].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.item[2].adjudication[1].value, 80.0)
        self.assertEqual(inst.item[2].adjudication[2].amount.currency, "USD")
        self.assertEqual(inst.item[2].adjudication[2].amount.value, 600.0)
        self.assertEqual(inst.item[2].adjudication[2].category.coding[0].code, "benefit")
        self.assertEqual(inst.item[2].detail[0].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.item[2].detail[0].adjudication[0].amount.value, 750.0)
        self.assertEqual(inst.item[2].detail[0].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.item[2].detail[0].adjudication[1].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.item[2].detail[0].adjudication[1].value, 80.0)
        self.assertEqual(inst.item[2].detail[0].adjudication[2].amount.currency, "USD")
        self.assertEqual(inst.item[2].detail[0].adjudication[2].amount.value, 600.0)
        self.assertEqual(inst.item[2].detail[0].adjudication[2].category.coding[0].code, "benefit")
        self.assertEqual(inst.item[2].detail[0].detailSequence, 1)
        self.assertEqual(inst.item[2].detail[1].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.item[2].detail[1].adjudication[0].amount.value, 0.0)
        self.assertEqual(inst.item[2].detail[1].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.item[2].detail[1].adjudication[1].amount.currency, "USD")
        self.assertEqual(inst.item[2].detail[1].adjudication[1].amount.value, 0.0)
        self.assertEqual(inst.item[2].detail[1].adjudication[1].category.coding[0].code, "benefit")
        self.assertEqual(inst.item[2].detail[1].detailSequence, 2)
        self.assertEqual(inst.item[2].itemSequence, 3)
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.payeeType.coding[0].code, "provider")
        self.assertEqual(inst.payeeType.coding[0].system, "http://terminology.hl7.org/CodeSystem/payeetype")
        self.assertEqual(inst.payment.amount.currency, "USD")
        self.assertEqual(inst.payment.amount.value, 100.47)
        self.assertEqual(inst.payment.date.date, FHIRDate("2014-08-31").date)
        self.assertEqual(inst.payment.date.as_json(), "2014-08-31")
        self.assertEqual(inst.payment.identifier.system, "http://www.BenefitsInc.com/fhir/paymentidentifier")
        self.assertEqual(inst.payment.identifier.value, "201408-2-15507")
        self.assertEqual(inst.payment.type.coding[0].code, "complete")
        self.assertEqual(inst.payment.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-paymenttype")
        self.assertEqual(inst.processNote[0].language.coding[0].code, "en-CA")
        self.assertEqual(inst.processNote[0].language.coding[0].system, "urn:ietf:bcp:47")
        self.assertEqual(inst.processNote[0].number, 101)
        self.assertEqual(inst.processNote[0].text, "Package codes are not permitted. Codes replaced by Insurer.")
        self.assertEqual(inst.processNote[0].type, "print")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the ClaimResponse to Claim Oral Average with additional items</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.total[0].amount.currency, "USD")
        self.assertEqual(inst.total[0].amount.value, 1340.57)
        self.assertEqual(inst.total[0].category.coding[0].code, "submitted")
        self.assertEqual(inst.total[1].amount.currency, "USD")
        self.assertEqual(inst.total[1].amount.value, 1054.47)
        self.assertEqual(inst.total[1].category.coding[0].code, "benefit")
        self.assertEqual(inst.type.coding[0].code, "oral")
        self.assertEqual(inst.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/claim-type")
        self.assertEqual(inst.use, "claim")
    
    def testClaimResponse3(self):
        inst = self.instantiate_from("claimresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ClaimResponse instance")
        self.implClaimResponse3(inst)
        
        js = inst.as_json()
        self.assertEqual("ClaimResponse", js["resourceType"])
        inst2 = claimresponse.ClaimResponse(js)
        self.implClaimResponse3(inst2)
    
    def implClaimResponse3(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Claim settled as per contract.")
        self.assertEqual(inst.id, "R3500")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/remittance")
        self.assertEqual(inst.identifier[0].value, "R3500")
        self.assertEqual(inst.item[0].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.item[0].adjudication[0].amount.value, 135.57)
        self.assertEqual(inst.item[0].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.item[0].adjudication[1].amount.currency, "USD")
        self.assertEqual(inst.item[0].adjudication[1].amount.value, 10.0)
        self.assertEqual(inst.item[0].adjudication[1].category.coding[0].code, "copay")
        self.assertEqual(inst.item[0].adjudication[2].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.item[0].adjudication[2].value, 80.0)
        self.assertEqual(inst.item[0].adjudication[3].amount.currency, "USD")
        self.assertEqual(inst.item[0].adjudication[3].amount.value, 90.47)
        self.assertEqual(inst.item[0].adjudication[3].category.coding[0].code, "benefit")
        self.assertEqual(inst.item[0].adjudication[3].reason.coding[0].code, "ar002")
        self.assertEqual(inst.item[0].adjudication[3].reason.coding[0].display, "Plan Limit Reached")
        self.assertEqual(inst.item[0].adjudication[3].reason.coding[0].system, "http://terminology.hl7.org/CodeSystem/adjudication-reason")
        self.assertEqual(inst.item[0].itemSequence, 1)
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.payeeType.coding[0].code, "provider")
        self.assertEqual(inst.payeeType.coding[0].system, "http://terminology.hl7.org/CodeSystem/payeetype")
        self.assertEqual(inst.payment.amount.currency, "USD")
        self.assertEqual(inst.payment.amount.value, 100.47)
        self.assertEqual(inst.payment.date.date, FHIRDate("2014-08-31").date)
        self.assertEqual(inst.payment.date.as_json(), "2014-08-31")
        self.assertEqual(inst.payment.identifier.system, "http://www.BenefitsInc.com/fhir/paymentidentifier")
        self.assertEqual(inst.payment.identifier.value, "201408-2-1569478")
        self.assertEqual(inst.payment.type.coding[0].code, "complete")
        self.assertEqual(inst.payment.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-paymenttype")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.subType.coding[0].code, "emergency")
        self.assertEqual(inst.subType.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-claimsubtype")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the ClaimResponse</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.total[0].amount.currency, "USD")
        self.assertEqual(inst.total[0].amount.value, 135.57)
        self.assertEqual(inst.total[0].category.coding[0].code, "submitted")
        self.assertEqual(inst.total[1].amount.currency, "USD")
        self.assertEqual(inst.total[1].amount.value, 90.47)
        self.assertEqual(inst.total[1].category.coding[0].code, "benefit")
        self.assertEqual(inst.type.coding[0].code, "oral")
        self.assertEqual(inst.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/claim-type")
        self.assertEqual(inst.use, "claim")
    
    def testClaimResponse4(self):
        inst = self.instantiate_from("claimresponse-example-vision-3tier.json")
        self.assertIsNotNone(inst, "Must have instantiated a ClaimResponse instance")
        self.implClaimResponse4(inst)
        
        js = inst.as_json()
        self.assertEqual("ClaimResponse", js["resourceType"])
        inst2 = claimresponse.ClaimResponse(js)
        self.implClaimResponse4(inst2)
    
    def implClaimResponse4(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Claim settled as per contract.")
        self.assertEqual(inst.id, "R3502")
        self.assertEqual(inst.identifier[0].system, "http://thebenefitcompany.com/claimresponse")
        self.assertEqual(inst.identifier[0].value, "CR6532875367")
        self.assertEqual(inst.item[0].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.item[0].adjudication[0].amount.value, 235.4)
        self.assertEqual(inst.item[0].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.item[0].adjudication[1].amount.currency, "USD")
        self.assertEqual(inst.item[0].adjudication[1].amount.value, 20.0)
        self.assertEqual(inst.item[0].adjudication[1].category.coding[0].code, "copay")
        self.assertEqual(inst.item[0].adjudication[2].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.item[0].adjudication[2].value, 80.0)
        self.assertEqual(inst.item[0].adjudication[3].amount.currency, "USD")
        self.assertEqual(inst.item[0].adjudication[3].amount.value, 172.32)
        self.assertEqual(inst.item[0].adjudication[3].category.coding[0].code, "benefit")
        self.assertEqual(inst.item[0].detail[0].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.item[0].detail[0].adjudication[0].amount.value, 100.0)
        self.assertEqual(inst.item[0].detail[0].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.item[0].detail[0].adjudication[1].amount.currency, "USD")
        self.assertEqual(inst.item[0].detail[0].adjudication[1].amount.value, 20.0)
        self.assertEqual(inst.item[0].detail[0].adjudication[1].category.coding[0].code, "copay")
        self.assertEqual(inst.item[0].detail[0].adjudication[2].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.item[0].detail[0].adjudication[2].value, 80.0)
        self.assertEqual(inst.item[0].detail[0].adjudication[3].amount.currency, "USD")
        self.assertEqual(inst.item[0].detail[0].adjudication[3].amount.value, 80.0)
        self.assertEqual(inst.item[0].detail[0].adjudication[3].category.coding[0].code, "benefit")
        self.assertEqual(inst.item[0].detail[0].detailSequence, 1)
        self.assertEqual(inst.item[0].detail[0].noteNumber[0], 1)
        self.assertEqual(inst.item[0].detail[1].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.item[0].detail[1].adjudication[0].amount.value, 110.0)
        self.assertEqual(inst.item[0].detail[1].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.item[0].detail[1].adjudication[1].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.item[0].detail[1].adjudication[1].value, 80.0)
        self.assertEqual(inst.item[0].detail[1].adjudication[2].amount.currency, "USD")
        self.assertEqual(inst.item[0].detail[1].adjudication[2].amount.value, 88.0)
        self.assertEqual(inst.item[0].detail[1].adjudication[2].category.coding[0].code, "benefit")
        self.assertEqual(inst.item[0].detail[1].detailSequence, 2)
        self.assertEqual(inst.item[0].detail[1].noteNumber[0], 1)
        self.assertEqual(inst.item[0].detail[1].subDetail[0].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.item[0].detail[1].subDetail[0].adjudication[0].amount.value, 60.0)
        self.assertEqual(inst.item[0].detail[1].subDetail[0].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.item[0].detail[1].subDetail[0].adjudication[1].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.item[0].detail[1].subDetail[0].adjudication[1].value, 80.0)
        self.assertEqual(inst.item[0].detail[1].subDetail[0].adjudication[2].amount.currency, "USD")
        self.assertEqual(inst.item[0].detail[1].subDetail[0].adjudication[2].amount.value, 48.0)
        self.assertEqual(inst.item[0].detail[1].subDetail[0].adjudication[2].category.coding[0].code, "benefit")
        self.assertEqual(inst.item[0].detail[1].subDetail[0].noteNumber[0], 1)
        self.assertEqual(inst.item[0].detail[1].subDetail[0].subDetailSequence, 1)
        self.assertEqual(inst.item[0].detail[1].subDetail[1].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.item[0].detail[1].subDetail[1].adjudication[0].amount.value, 30.0)
        self.assertEqual(inst.item[0].detail[1].subDetail[1].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.item[0].detail[1].subDetail[1].adjudication[1].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.item[0].detail[1].subDetail[1].adjudication[1].value, 80.0)
        self.assertEqual(inst.item[0].detail[1].subDetail[1].adjudication[2].amount.currency, "USD")
        self.assertEqual(inst.item[0].detail[1].subDetail[1].adjudication[2].amount.value, 24.0)
        self.assertEqual(inst.item[0].detail[1].subDetail[1].adjudication[2].category.coding[0].code, "benefit")
        self.assertEqual(inst.item[0].detail[1].subDetail[1].subDetailSequence, 2)
        self.assertEqual(inst.item[0].detail[1].subDetail[2].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.item[0].detail[1].subDetail[2].adjudication[0].amount.value, 10.0)
        self.assertEqual(inst.item[0].detail[1].subDetail[2].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.item[0].detail[1].subDetail[2].adjudication[1].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.item[0].detail[1].subDetail[2].adjudication[1].value, 80.0)
        self.assertEqual(inst.item[0].detail[1].subDetail[2].adjudication[2].amount.currency, "USD")
        self.assertEqual(inst.item[0].detail[1].subDetail[2].adjudication[2].amount.value, 8.0)
        self.assertEqual(inst.item[0].detail[1].subDetail[2].adjudication[2].category.coding[0].code, "benefit")
        self.assertEqual(inst.item[0].detail[1].subDetail[2].noteNumber[0], 1)
        self.assertEqual(inst.item[0].detail[1].subDetail[2].subDetailSequence, 3)
        self.assertEqual(inst.item[0].detail[2].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.item[0].detail[2].adjudication[0].amount.value, 200.0)
        self.assertEqual(inst.item[0].detail[2].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.item[0].detail[2].adjudication[1].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.item[0].detail[2].adjudication[1].value, 80.0)
        self.assertEqual(inst.item[0].detail[2].adjudication[2].amount.currency, "USD")
        self.assertEqual(inst.item[0].detail[2].adjudication[2].amount.value, 14.0)
        self.assertEqual(inst.item[0].detail[2].adjudication[2].category.coding[0].code, "benefit")
        self.assertEqual(inst.item[0].detail[2].detailSequence, 3)
        self.assertEqual(inst.item[0].detail[2].noteNumber[0], 1)
        self.assertEqual(inst.item[0].itemSequence, 1)
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.payeeType.coding[0].code, "provider")
        self.assertEqual(inst.payeeType.coding[0].system, "http://terminology.hl7.org/CodeSystem/payeetype")
        self.assertEqual(inst.payment.adjustment.currency, "USD")
        self.assertEqual(inst.payment.adjustment.value, 75.0)
        self.assertEqual(inst.payment.adjustmentReason.coding[0].code, "a002")
        self.assertEqual(inst.payment.adjustmentReason.coding[0].display, "Prior Overpayment")
        self.assertEqual(inst.payment.adjustmentReason.coding[0].system, "http://terminology.hl7.org/CodeSystem/payment-adjustment-reason")
        self.assertEqual(inst.payment.amount.currency, "USD")
        self.assertEqual(inst.payment.amount.value, 107.0)
        self.assertEqual(inst.payment.date.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.payment.date.as_json(), "2014-08-16")
        self.assertEqual(inst.payment.identifier.system, "http://thebenefitcompany.com/paymentidentifier")
        self.assertEqual(inst.payment.identifier.value, "201416-123456")
        self.assertEqual(inst.payment.type.coding[0].code, "complete")
        self.assertEqual(inst.payment.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-paymenttype")
        self.assertEqual(inst.processNote[0].language.coding[0].code, "en-CA")
        self.assertEqual(inst.processNote[0].language.coding[0].system, "urn:ietf:bcp:47")
        self.assertEqual(inst.processNote[0].number, 1)
        self.assertEqual(inst.processNote[0].text, "After hours surcharge declined")
        self.assertEqual(inst.processNote[0].type, "display")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the ClaimResponse</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.total[0].amount.currency, "USD")
        self.assertEqual(inst.total[0].amount.value, 235.4)
        self.assertEqual(inst.total[0].category.coding[0].code, "submitted")
        self.assertEqual(inst.total[1].amount.currency, "USD")
        self.assertEqual(inst.total[1].amount.value, 182.0)
        self.assertEqual(inst.total[1].category.coding[0].code, "benefit")
        self.assertEqual(inst.type.coding[0].code, "vision")
        self.assertEqual(inst.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/claim-type")
        self.assertEqual(inst.use, "claim")
    
    def testClaimResponse5(self):
        inst = self.instantiate_from("claimresponse-example-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a ClaimResponse instance")
        self.implClaimResponse5(inst)
        
        js = inst.as_json()
        self.assertEqual("ClaimResponse", js["resourceType"])
        inst2 = claimresponse.ClaimResponse(js)
        self.implClaimResponse5(inst2)
    
    def implClaimResponse5(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Claim could not be processed")
        self.assertEqual(inst.error[0].code.coding[0].code, "a002")
        self.assertEqual(inst.error[0].code.coding[0].system, "http://terminology.hl7.org/CodeSystem/adjudication-error")
        self.assertEqual(inst.error[0].detailSequence, 2)
        self.assertEqual(inst.error[0].itemSequence, 3)
        self.assertEqual(inst.formCode.coding[0].code, "2")
        self.assertEqual(inst.formCode.coding[0].system, "http://terminology.hl7.org/CodeSystem/forms-codes")
        self.assertEqual(inst.id, "R3501")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/remittance")
        self.assertEqual(inst.identifier[0].value, "R3501")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "error")
        self.assertEqual(inst.processNote[0].language.coding[0].code, "en-CA")
        self.assertEqual(inst.processNote[0].language.coding[0].system, "urn:ietf:bcp:47")
        self.assertEqual(inst.processNote[0].number, 1)
        self.assertEqual(inst.processNote[0].text, "Invalid claim")
        self.assertEqual(inst.processNote[0].type, "display")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the ClaimResponse that demonstrates returning errors</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "oral")
        self.assertEqual(inst.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/claim-type")
        self.assertEqual(inst.use, "claim")

