#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/AllergyIntolerance) on 2019-07-18.
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
class AllergyIntoleranceReaction(BackboneElement):
    """ Adverse Reaction Events linked to exposure to substance.

    Details about each adverse reaction event linked to exposure to the
    identified substance.
    """
    resource_type: ClassVar[str] = "AllergyIntoleranceReaction"
    description: Optional[str] = None
    exposureRoute: Optional[CodeableConcept] = None
    manifestation: List[CodeableConcept] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    onset: Optional[FHIRDate] = None
    severity: Optional[str] = None
    substance: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(AllergyIntoleranceReaction, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("exposureRoute", "exposureRoute", CodeableConcept, False, None, False),
            ("manifestation", "manifestation", CodeableConcept, True, None, True),
            ("note", "note", Annotation, True, None, False),
            ("onset", "onset", FHIRDate, False, None, False),
            ("severity", "severity", str, False, None, False),
            ("substance", "substance", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class AllergyIntolerance(DomainResource):
    """ Allergy or Intolerance (generally: Risk of adverse reaction to a substance).

    Risk of harmful or undesirable, physiological response which is unique to
    an individual and associated with exposure to a substance.
    """
    resource_type: ClassVar[str] = "AllergyIntolerance"
    asserter: Optional[FHIRReference] = None
    category: Optional[List[str]] = empty_list()
    clinicalStatus: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None
    criticality: Optional[str] = None
    encounter: Optional[FHIRReference] = None
    identifier: Optional[List[Identifier]] = empty_list()
    lastOccurrence: Optional[FHIRDate] = None
    note: Optional[List[Annotation]] = empty_list()
    onsetAge: Optional[Age] = None
    onsetDateTime: Optional[FHIRDate] = None
    onsetPeriod: Optional[Period] = None
    onsetRange: Optional[Range] = None
    onsetString: Optional[str] = None
    patient: FHIRReference = None
    reaction: Optional[List[AllergyIntoleranceReaction]] = empty_list()
    recordedDate: Optional[FHIRDate] = None
    recorder: Optional[FHIRReference] = None
    type: Optional[str] = None
    verificationStatus: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(AllergyIntolerance, self).elementProperties()
        js.extend([
            ("asserter", "asserter", FHIRReference, False, None, False),
            ("category", "category", str, True, None, False),
            ("clinicalStatus", "clinicalStatus", CodeableConcept, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("criticality", "criticality", str, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("lastOccurrence", "lastOccurrence", FHIRDate, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("onsetAge", "onsetAge", Age, False, "onset", False),
            ("onsetDateTime", "onsetDateTime", FHIRDate, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", Period, False, "onset", False),
            ("onsetRange", "onsetRange", Range, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("patient", "patient", FHIRReference, False, None, True),
            ("reaction", "reaction", AllergyIntoleranceReaction, True, None, False),
            ("recordedDate", "recordedDate", FHIRDate, False, None, False),
            ("recorder", "recorder", FHIRReference, False, None, False),
            ("type", "type", str, False, None, False),
            ("verificationStatus", "verificationStatus", CodeableConcept, False, None, False),
        ])
        return js