#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-07-15.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import explanationofbenefit
from .fhirdate import FHIRDate


class ExplanationOfBenefitTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ExplanationOfBenefit", js["resourceType"])
        return explanationofbenefit.ExplanationOfBenefit(js)
    
    def testExplanationOfBenefit1(self):
        inst = self.instantiate_from("explanationofbenefit-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ExplanationOfBenefit instance")
        self.implExplanationOfBenefit1(inst)
        
        js = inst.as_json()
        self.assertEqual("ExplanationOfBenefit", js["resourceType"])
        inst2 = explanationofbenefit.ExplanationOfBenefit(js)
        self.implExplanationOfBenefit1(inst2)
    
    def implExplanationOfBenefit1(self, inst):
        self.assertEqual(inst.careTeam[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Claim settled as per contract.")
        self.assertEqual(inst.id, "EB3500")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/explanationofbenefit")
        self.assertEqual(inst.identifier[0].value, "987654321")
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(inst.item[0].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.item[0].adjudication[0].amount.value, 120.0)
        self.assertEqual(inst.item[0].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.item[0].adjudication[1].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.item[0].adjudication[1].value, 0.8)
        self.assertEqual(inst.item[0].adjudication[2].amount.currency, "USD")
        self.assertEqual(inst.item[0].adjudication[2].amount.value, 96.0)
        self.assertEqual(inst.item[0].adjudication[2].category.coding[0].code, "benefit")
        self.assertEqual(inst.item[0].careTeamSequence[0], 1)
        self.assertEqual(inst.item[0].net.currency, "USD")
        self.assertEqual(inst.item[0].net.value, 135.57)
        self.assertEqual(inst.item[0].productOrService.coding[0].code, "1205")
        self.assertEqual(inst.item[0].productOrService.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-USCLS")
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(inst.item[0].unitPrice.currency, "USD")
        self.assertEqual(inst.item[0].unitPrice.value, 135.57)
        self.assertEqual(inst.item[1].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.item[1].adjudication[0].amount.value, 180.0)
        self.assertEqual(inst.item[1].adjudication[0].category.coding[0].code, "benefit")
        self.assertEqual(inst.item[1].careTeamSequence[0], 1)
        self.assertEqual(inst.item[1].detail[0].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.item[1].detail[0].adjudication[0].amount.value, 180.0)
        self.assertEqual(inst.item[1].detail[0].adjudication[0].category.coding[0].code, "benefit")
        self.assertEqual(inst.item[1].detail[0].net.currency, "USD")
        self.assertEqual(inst.item[1].detail[0].net.value, 200.0)
        self.assertEqual(inst.item[1].detail[0].productOrService.coding[0].code, "group")
        self.assertEqual(inst.item[1].detail[0].sequence, 1)
        self.assertEqual(inst.item[1].detail[0].subDetail[0].adjudication[0].amount.currency, "USD")
        self.assertEqual(inst.item[1].detail[0].subDetail[0].adjudication[0].amount.value, 200.0)
        self.assertEqual(inst.item[1].detail[0].subDetail[0].adjudication[0].category.coding[0].code, "eligible")
        self.assertEqual(inst.item[1].detail[0].subDetail[0].adjudication[1].category.coding[0].code, "eligpercent")
        self.assertEqual(inst.item[1].detail[0].subDetail[0].adjudication[1].value, 0.9)
        self.assertEqual(inst.item[1].detail[0].subDetail[0].adjudication[2].amount.currency, "USD")
        self.assertEqual(inst.item[1].detail[0].subDetail[0].adjudication[2].amount.value, 180.0)
        self.assertEqual(inst.item[1].detail[0].subDetail[0].adjudication[2].category.coding[0].code, "benefit")
        self.assertEqual(inst.item[1].detail[0].subDetail[0].net.currency, "USD")
        self.assertEqual(inst.item[1].detail[0].subDetail[0].net.value, 200.0)
        self.assertEqual(inst.item[1].detail[0].subDetail[0].productOrService.coding[0].code, "1205")
        self.assertEqual(inst.item[1].detail[0].subDetail[0].productOrService.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-USCLS")
        self.assertEqual(inst.item[1].detail[0].subDetail[0].sequence, 1)
        self.assertEqual(inst.item[1].detail[0].subDetail[0].unitPrice.currency, "USD")
        self.assertEqual(inst.item[1].detail[0].subDetail[0].unitPrice.value, 200.0)
        self.assertEqual(inst.item[1].net.currency, "USD")
        self.assertEqual(inst.item[1].net.value, 200.0)
        self.assertEqual(inst.item[1].productOrService.coding[0].code, "group")
        self.assertEqual(inst.item[1].sequence, 2)
        self.assertEqual(inst.item[1].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[1].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.payee.type.coding[0].code, "provider")
        self.assertEqual(inst.payee.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/payeetype")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the ExplanationOfBenefit</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.total[0].amount.currency, "USD")
        self.assertEqual(inst.total[0].amount.value, 135.57)
        self.assertEqual(inst.total[0].category.coding[0].code, "submitted")
        self.assertEqual(inst.total[1].amount.currency, "USD")
        self.assertEqual(inst.total[1].amount.value, 96.0)
        self.assertEqual(inst.total[1].category.coding[0].code, "benefit")
        self.assertEqual(inst.type.coding[0].code, "oral")
        self.assertEqual(inst.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/claim-type")
        self.assertEqual(inst.use, "claim")
    
    def testExplanationOfBenefit2(self):
        inst = self.instantiate_from("explanationofbenefit-example-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a ExplanationOfBenefit instance")
        self.implExplanationOfBenefit2(inst)
        
        js = inst.as_json()
        self.assertEqual("ExplanationOfBenefit", js["resourceType"])
        inst2 = explanationofbenefit.ExplanationOfBenefit(js)
        self.implExplanationOfBenefit2(inst2)
    
    def implExplanationOfBenefit2(self, inst):
        self.assertEqual(inst.accident.date.date, FHIRDate("2014-02-14").date)
        self.assertEqual(inst.accident.date.as_json(), "2014-02-14")
        self.assertEqual(inst.accident.type.coding[0].code, "SPT")
        self.assertEqual(inst.accident.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.billablePeriod.end.date, FHIRDate("2014-03-01").date)
        self.assertEqual(inst.billablePeriod.end.as_json(), "2014-03-01")
        self.assertEqual(inst.billablePeriod.start.date, FHIRDate("2014-02-01").date)
        self.assertEqual(inst.billablePeriod.start.as_json(), "2014-02-01")
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Could not process.")
        self.assertEqual(inst.formCode.coding[0].code, "2")
        self.assertEqual(inst.formCode.coding[0].system, "http://terminology.hl7.org/CodeSystem/forms-codes")
        self.assertEqual(inst.id, "EB3501")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/explanationofbenefit")
        self.assertEqual(inst.identifier[0].value, "error-1")
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "error")
        self.assertEqual(inst.precedence, 2)
        self.assertEqual(inst.procedure[0].date.date, FHIRDate("2014-02-14").date)
        self.assertEqual(inst.procedure[0].date.as_json(), "2014-02-14")
        self.assertEqual(inst.procedure[0].procedureCodeableConcept.coding[0].code, "123001")
        self.assertEqual(inst.procedure[0].procedureCodeableConcept.coding[0].system, "http://hl7.org/fhir/sid/ex-icd-10-procedures")
        self.assertEqual(inst.procedure[0].sequence, 1)
        self.assertEqual(inst.processNote[0].language.coding[0].code, "en-CA")
        self.assertEqual(inst.processNote[0].language.coding[0].system, "urn:ietf:bcp:47")
        self.assertEqual(inst.processNote[0].number, 1)
        self.assertEqual(inst.processNote[0].text, "Invalid claim")
        self.assertEqual(inst.processNote[0].type, "display")
        self.assertEqual(inst.related[0].reference.system, "http://www.BenefitsInc.com/case-number")
        self.assertEqual(inst.related[0].reference.value, "23-56Tu-XX-47-20150M14")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.subType.coding[0].code, "emergency")
        self.assertEqual(inst.subType.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-claimsubtype")
        self.assertEqual(inst.supportingInfo[0].category.coding[0].code, "employmentimpacted")
        self.assertEqual(inst.supportingInfo[0].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/claiminformationcategory")
        self.assertEqual(inst.supportingInfo[0].sequence, 1)
        self.assertEqual(inst.supportingInfo[0].timingPeriod.end.date, FHIRDate("2014-02-28").date)
        self.assertEqual(inst.supportingInfo[0].timingPeriod.end.as_json(), "2014-02-28")
        self.assertEqual(inst.supportingInfo[0].timingPeriod.start.date, FHIRDate("2014-02-14").date)
        self.assertEqual(inst.supportingInfo[0].timingPeriod.start.as_json(), "2014-02-14")
        self.assertEqual(inst.supportingInfo[1].category.coding[0].code, "hospitalized")
        self.assertEqual(inst.supportingInfo[1].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/claiminformationcategory")
        self.assertEqual(inst.supportingInfo[1].sequence, 2)
        self.assertEqual(inst.supportingInfo[1].timingPeriod.end.date, FHIRDate("2014-02-16").date)
        self.assertEqual(inst.supportingInfo[1].timingPeriod.end.as_json(), "2014-02-16")
        self.assertEqual(inst.supportingInfo[1].timingPeriod.start.date, FHIRDate("2014-02-14").date)
        self.assertEqual(inst.supportingInfo[1].timingPeriod.start.as_json(), "2014-02-14")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.total[0].amount.currency, "USD")
        self.assertEqual(inst.total[0].amount.value, 2478.57)
        self.assertEqual(inst.total[0].category.coding[0].code, "submitted")
        self.assertEqual(inst.total[1].amount.currency, "USD")
        self.assertEqual(inst.total[1].amount.value, 0.0)
        self.assertEqual(inst.total[1].category.coding[0].code, "benefit")
        self.assertEqual(inst.type.coding[0].code, "oral")
        self.assertEqual(inst.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/claim-type")
        self.assertEqual(inst.use, "claim")

