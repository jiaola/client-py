#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/AdverseEvent) on 2019-07-29.
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
    productRelatedness: Optional[str] = None
    author: Optional[FHIRReference] = None
    method: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(AdverseEventSuspectEntityCausality, self).elementProperties()
        js.extend([
            ("assessment", "assessment", CodeableConcept, False, None, False),
            ("productRelatedness", "productRelatedness", str, False, None, False),
            ("author", "author", FHIRReference, False, None, False),
            ("method", "method", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class AdverseEventSuspectEntity(BackboneElement):
    """ The suspected agent causing the adverse event.

    Describes the entity that is suspected to have caused the adverse event.
    """
    resource_type: ClassVar[str] = "AdverseEventSuspectEntity"
    instance: FHIRReference = None
    causality: Optional[List[AdverseEventSuspectEntityCausality]] = empty_list()

    def elementProperties(self):
        js = super(AdverseEventSuspectEntity, self).elementProperties()
        js.extend([
            ("instance", "instance", FHIRReference, False, None, True),
            ("causality", "causality", AdverseEventSuspectEntityCausality, True, None, False),
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
    identifier: Optional[Identifier] = None
    actuality: str = None
    category: Optional[List[CodeableConcept]] = empty_list()
    event: Optional[CodeableConcept] = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    detected: Optional[FHIRDate] = None
    recordedDate: Optional[FHIRDate] = None
    resultingCondition: Optional[List[FHIRReference]] = empty_list()
    location: Optional[FHIRReference] = None
    seriousness: Optional[CodeableConcept] = None
    severity: Optional[CodeableConcept] = None
    outcome: Optional[CodeableConcept] = None
    recorder: Optional[FHIRReference] = None
    contributor: Optional[List[FHIRReference]] = empty_list()
    suspectEntity: Optional[List[AdverseEventSuspectEntity]] = empty_list()
    subjectMedicalHistory: Optional[List[FHIRReference]] = empty_list()
    referenceDocument: Optional[List[FHIRReference]] = empty_list()
    study: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(AdverseEvent, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, False, None, False),
            ("actuality", "actuality", str, False, None, True),
            ("category", "category", CodeableConcept, True, None, False),
            ("event", "event", CodeableConcept, False, None, False),
            ("subject", "subject", FHIRReference, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("detected", "detected", FHIRDate, False, None, False),
            ("recordedDate", "recordedDate", FHIRDate, False, None, False),
            ("resultingCondition", "resultingCondition", FHIRReference, True, None, False),
            ("location", "location", FHIRReference, False, None, False),
            ("seriousness", "seriousness", CodeableConcept, False, None, False),
            ("severity", "severity", CodeableConcept, False, None, False),
            ("outcome", "outcome", CodeableConcept, False, None, False),
            ("recorder", "recorder", FHIRReference, False, None, False),
            ("contributor", "contributor", FHIRReference, True, None, False),
            ("suspectEntity", "suspectEntity", AdverseEventSuspectEntity, True, None, False),
            ("subjectMedicalHistory", "subjectMedicalHistory", FHIRReference, True, None, False),
            ("referenceDocument", "referenceDocument", FHIRReference, True, None, False),
            ("study", "study", FHIRReference, True, None, False),
        ])
        return js