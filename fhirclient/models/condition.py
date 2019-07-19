#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Condition) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .age import Age
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .range import Range


@dataclass
class ConditionStage(BackboneElement):
    """ Stage/grade, usually assessed formally.

    Clinical stage or grade of a condition. May include formal severity
    assessments.
    """
    resource_type: ClassVar[str] = "ConditionStage"
    assessment: Optional[List[FHIRReference]] = empty_list()
    summary: Optional[CodeableConcept] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ConditionStage, self).elementProperties()
        js.extend([
            ("assessment", "assessment", FHIRReference, True, None, False),
            ("summary", "summary", CodeableConcept, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ConditionEvidence(BackboneElement):
    """ Supporting evidence.

    Supporting evidence / manifestations that are the basis of the Condition's
    verification status, such as evidence that confirmed or refuted the
    condition.
    """
    resource_type: ClassVar[str] = "ConditionEvidence"
    code: Optional[List[CodeableConcept]] = empty_list()
    detail: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(ConditionEvidence, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, True, None, False),
            ("detail", "detail", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class Condition(DomainResource):
    """ Detailed information about conditions, problems or diagnoses.

    A clinical condition, problem, diagnosis, or other event, situation, issue,
    or clinical concept that has risen to a level of concern.
    """
    resource_type: ClassVar[str] = "Condition"
    abatementAge: Optional[Age] = None
    abatementDateTime: Optional[FHIRDate] = None
    abatementPeriod: Optional[Period] = None
    abatementRange: Optional[Range] = None
    abatementString: Optional[str] = None
    asserter: Optional[FHIRReference] = None
    bodySite: Optional[List[CodeableConcept]] = empty_list()
    category: Optional[List[CodeableConcept]] = empty_list()
    clinicalStatus: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None
    encounter: Optional[FHIRReference] = None
    evidence: Optional[List[ConditionEvidence]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    onsetAge: Optional[Age] = None
    onsetDateTime: Optional[FHIRDate] = None
    onsetPeriod: Optional[Period] = None
    onsetRange: Optional[Range] = None
    onsetString: Optional[str] = None
    recordedDate: Optional[FHIRDate] = None
    recorder: Optional[FHIRReference] = None
    severity: Optional[CodeableConcept] = None
    stage: Optional[List[ConditionStage]] = empty_list()
    subject: FHIRReference = None
    verificationStatus: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(Condition, self).elementProperties()
        js.extend([
            ("abatementAge", "abatementAge", Age, False, "abatement", False),
            ("abatementDateTime", "abatementDateTime", FHIRDate, False, "abatement", False),
            ("abatementPeriod", "abatementPeriod", Period, False, "abatement", False),
            ("abatementRange", "abatementRange", Range, False, "abatement", False),
            ("abatementString", "abatementString", str, False, "abatement", False),
            ("asserter", "asserter", FHIRReference, False, None, False),
            ("bodySite", "bodySite", CodeableConcept, True, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("clinicalStatus", "clinicalStatus", CodeableConcept, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("evidence", "evidence", ConditionEvidence, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("onsetAge", "onsetAge", Age, False, "onset", False),
            ("onsetDateTime", "onsetDateTime", FHIRDate, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", Period, False, "onset", False),
            ("onsetRange", "onsetRange", Range, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("recordedDate", "recordedDate", FHIRDate, False, None, False),
            ("recorder", "recorder", FHIRReference, False, None, False),
            ("severity", "severity", CodeableConcept, False, None, False),
            ("stage", "stage", ConditionStage, True, None, False),
            ("subject", "subject", FHIRReference, False, None, True),
            ("verificationStatus", "verificationStatus", CodeableConcept, False, None, False),
        ])
        return js