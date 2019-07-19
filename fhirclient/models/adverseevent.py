#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/AdverseEvent) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class AdverseEventSuspectEntityCausality(BackboneElement):
    """ Information on the possible cause of the event.
    """
    resource_type: ClassVar[str] = "AdverseEventSuspectEntityCausality"
    assessment: Optional[CodeableConcept] = None
    author: Optional[FHIRReference] = None
    method: Optional[CodeableConcept] = None
    productRelatedness: Optional[str] = None

    def elementProperties(self):
        js = super(AdverseEventSuspectEntityCausality, self).elementProperties()
        js.extend([
            ("assessment", "assessment", CodeableConcept, False, None, False),
            ("author", "author", FHIRReference, False, None, False),
            ("method", "method", CodeableConcept, False, None, False),
            ("productRelatedness", "productRelatedness", str, False, None, False),
        ])
        return js


@dataclass
class AdverseEventSuspectEntity(BackboneElement):
    """ The suspected agent causing the adverse event.

    Describes the entity that is suspected to have caused the adverse event.
    """
    resource_type: ClassVar[str] = "AdverseEventSuspectEntity"
    causality: Optional[List[AdverseEventSuspectEntityCausality]] = empty_list()
    instance: FHIRReference = None

    def elementProperties(self):
        js = super(AdverseEventSuspectEntity, self).elementProperties()
        js.extend([
            ("causality", "causality", AdverseEventSuspectEntityCausality, True, None, False),
            ("instance", "instance", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class AdverseEvent(DomainResource):
    """ Medical care, research study or other healthcare event causing physical
    injury.

    Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or other
    healthcare setting factors that requires additional monitoring, treatment,
    or hospitalization, or that results in death.
    """
    resource_type: ClassVar[str] = "AdverseEvent"
    actuality: str = None
    category: Optional[List[CodeableConcept]] = empty_list()
    contributor: Optional[List[FHIRReference]] = empty_list()
    date: Optional[FHIRDate] = None
    detected: Optional[FHIRDate] = None
    encounter: Optional[FHIRReference] = None
    event: Optional[CodeableConcept] = None
    identifier: Optional[Identifier] = None
    location: Optional[FHIRReference] = None
    outcome: Optional[CodeableConcept] = None
    recordedDate: Optional[FHIRDate] = None
    recorder: Optional[FHIRReference] = None
    referenceDocument: Optional[List[FHIRReference]] = empty_list()
    resultingCondition: Optional[List[FHIRReference]] = empty_list()
    seriousness: Optional[CodeableConcept] = None
    severity: Optional[CodeableConcept] = None
    study: Optional[List[FHIRReference]] = empty_list()
    subject: FHIRReference = None
    subjectMedicalHistory: Optional[List[FHIRReference]] = empty_list()
    suspectEntity: Optional[List[AdverseEventSuspectEntity]] = empty_list()

    def elementProperties(self):
        js = super(AdverseEvent, self).elementProperties()
        js.extend([
            ("actuality", "actuality", str, False, None, True),
            ("category", "category", CodeableConcept, True, None, False),
            ("contributor", "contributor", FHIRReference, True, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("detected", "detected", FHIRDate, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("event", "event", CodeableConcept, False, None, False),
            ("identifier", "identifier", Identifier, False, None, False),
            ("location", "location", FHIRReference, False, None, False),
            ("outcome", "outcome", CodeableConcept, False, None, False),
            ("recordedDate", "recordedDate", FHIRDate, False, None, False),
            ("recorder", "recorder", FHIRReference, False, None, False),
            ("referenceDocument", "referenceDocument", FHIRReference, True, None, False),
            ("resultingCondition", "resultingCondition", FHIRReference, True, None, False),
            ("seriousness", "seriousness", CodeableConcept, False, None, False),
            ("severity", "severity", CodeableConcept, False, None, False),
            ("study", "study", FHIRReference, True, None, False),
            ("subject", "subject", FHIRReference, False, None, True),
            ("subjectMedicalHistory", "subjectMedicalHistory", FHIRReference, True, None, False),
            ("suspectEntity", "suspectEntity", AdverseEventSuspectEntity, True, None, False),
        ])
        return js