#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory) on 2019-07-18.
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
class FamilyMemberHistoryCondition(BackboneElement):
    """ Condition that the related person had.

    The significant Conditions (or condition) that the family member had. This
    is a repeating section to allow a system to represent more than one
    condition per resource, though there is nothing stopping multiple resources
    - one per condition.
    """
    resource_type: ClassVar[str] = "FamilyMemberHistoryCondition"
    code: CodeableConcept = None
    contributedToDeath: Optional[bool] = None
    note: Optional[List[Annotation]] = empty_list()
    onsetAge: Optional[Age] = None
    onsetPeriod: Optional[Period] = None
    onsetRange: Optional[Range] = None
    onsetString: Optional[str] = None
    outcome: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(FamilyMemberHistoryCondition, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("contributedToDeath", "contributedToDeath", bool, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("onsetAge", "onsetAge", Age, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", Period, False, "onset", False),
            ("onsetRange", "onsetRange", Range, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("outcome", "outcome", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class FamilyMemberHistory(DomainResource):
    """ Information about patient's relatives, relevant for patient.

    Significant health conditions for a person related to the patient relevant
    in the context of care for the patient.
    """
    resource_type: ClassVar[str] = "FamilyMemberHistory"
    ageAge: Optional[Age] = None
    ageRange: Optional[Range] = None
    ageString: Optional[str] = None
    bornDate: Optional[FHIRDate] = None
    bornPeriod: Optional[Period] = None
    bornString: Optional[str] = None
    condition: Optional[List[FamilyMemberHistoryCondition]] = empty_list()
    dataAbsentReason: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None
    deceasedAge: Optional[Age] = None
    deceasedBoolean: Optional[bool] = None
    deceasedDate: Optional[FHIRDate] = None
    deceasedRange: Optional[Range] = None
    deceasedString: Optional[str] = None
    estimatedAge: Optional[bool] = None
    identifier: Optional[List[Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    name: Optional[str] = None
    note: Optional[List[Annotation]] = empty_list()
    patient: FHIRReference = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    relationship: CodeableConcept = None
    sex: Optional[CodeableConcept] = None
    status: str = None

    def elementProperties(self):
        js = super(FamilyMemberHistory, self).elementProperties()
        js.extend([
            ("ageAge", "ageAge", Age, False, "age", False),
            ("ageRange", "ageRange", Range, False, "age", False),
            ("ageString", "ageString", str, False, "age", False),
            ("bornDate", "bornDate", FHIRDate, False, "born", False),
            ("bornPeriod", "bornPeriod", Period, False, "born", False),
            ("bornString", "bornString", str, False, "born", False),
            ("condition", "condition", FamilyMemberHistoryCondition, True, None, False),
            ("dataAbsentReason", "dataAbsentReason", CodeableConcept, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("deceasedAge", "deceasedAge", Age, False, "deceased", False),
            ("deceasedBoolean", "deceasedBoolean", bool, False, "deceased", False),
            ("deceasedDate", "deceasedDate", FHIRDate, False, "deceased", False),
            ("deceasedRange", "deceasedRange", Range, False, "deceased", False),
            ("deceasedString", "deceasedString", str, False, "deceased", False),
            ("estimatedAge", "estimatedAge", bool, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("name", "name", str, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("patient", "patient", FHIRReference, False, None, True),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("relationship", "relationship", CodeableConcept, False, None, True),
            ("sex", "sex", CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js