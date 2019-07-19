#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Specimen) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .duration import Duration
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity


@dataclass
class SpecimenProcessing(BackboneElement):
    """ Processing and processing step details.

    Details concerning processing and processing steps for the specimen.
    """
    resource_type: ClassVar[str] = "SpecimenProcessing"
    additive: Optional[List[FHIRReference]] = empty_list()
    description: Optional[str] = None
    procedure: Optional[CodeableConcept] = None
    timeDateTime: Optional[FHIRDate] = None
    timePeriod: Optional[Period] = None

    def elementProperties(self):
        js = super(SpecimenProcessing, self).elementProperties()
        js.extend([
            ("additive", "additive", FHIRReference, True, None, False),
            ("description", "description", str, False, None, False),
            ("procedure", "procedure", CodeableConcept, False, None, False),
            ("timeDateTime", "timeDateTime", FHIRDate, False, "time", False),
            ("timePeriod", "timePeriod", Period, False, "time", False),
        ])
        return js


@dataclass
class SpecimenContainer(BackboneElement):
    """ Direct container of specimen (tube/slide, etc.).

    The container holding the specimen.  The recursive nature of containers;
    i.e. blood in tube in tray in rack is not addressed here.
    """
    resource_type: ClassVar[str] = "SpecimenContainer"
    additiveCodeableConcept: Optional[CodeableConcept] = None
    additiveReference: Optional[FHIRReference] = None
    capacity: Optional[Quantity] = None
    description: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    specimenQuantity: Optional[Quantity] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SpecimenContainer, self).elementProperties()
        js.extend([
            ("additiveCodeableConcept", "additiveCodeableConcept", CodeableConcept, False, "additive", False),
            ("additiveReference", "additiveReference", FHIRReference, False, "additive", False),
            ("capacity", "capacity", Quantity, False, None, False),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("specimenQuantity", "specimenQuantity", Quantity, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SpecimenCollection(BackboneElement):
    """ Collection details.

    Details concerning the specimen collection.
    """
    resource_type: ClassVar[str] = "SpecimenCollection"
    bodySite: Optional[CodeableConcept] = None
    collectedDateTime: Optional[FHIRDate] = None
    collectedPeriod: Optional[Period] = None
    collector: Optional[FHIRReference] = None
    duration: Optional[Duration] = None
    fastingStatusCodeableConcept: Optional[CodeableConcept] = None
    fastingStatusDuration: Optional[Duration] = None
    method: Optional[CodeableConcept] = None
    quantity: Optional[Quantity] = None

    def elementProperties(self):
        js = super(SpecimenCollection, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", CodeableConcept, False, None, False),
            ("collectedDateTime", "collectedDateTime", FHIRDate, False, "collected", False),
            ("collectedPeriod", "collectedPeriod", Period, False, "collected", False),
            ("collector", "collector", FHIRReference, False, None, False),
            ("duration", "duration", Duration, False, None, False),
            ("fastingStatusCodeableConcept", "fastingStatusCodeableConcept", CodeableConcept, False, "fastingStatus", False),
            ("fastingStatusDuration", "fastingStatusDuration", Duration, False, "fastingStatus", False),
            ("method", "method", CodeableConcept, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
        ])
        return js


@dataclass
class Specimen(DomainResource):
    """ Sample for analysis.

    A sample to be used for analysis.
    """
    resource_type: ClassVar[str] = "Specimen"
    accessionIdentifier: Optional[Identifier] = None
    collection: Optional[SpecimenCollection] = None
    condition: Optional[List[CodeableConcept]] = empty_list()
    container: Optional[List[SpecimenContainer]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    parent: Optional[List[FHIRReference]] = empty_list()
    processing: Optional[List[SpecimenProcessing]] = empty_list()
    receivedTime: Optional[FHIRDate] = None
    request: Optional[List[FHIRReference]] = empty_list()
    status: Optional[str] = None
    subject: Optional[FHIRReference] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(Specimen, self).elementProperties()
        js.extend([
            ("accessionIdentifier", "accessionIdentifier", Identifier, False, None, False),
            ("collection", "collection", SpecimenCollection, False, None, False),
            ("condition", "condition", CodeableConcept, True, None, False),
            ("container", "container", SpecimenContainer, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("parent", "parent", FHIRReference, True, None, False),
            ("processing", "processing", SpecimenProcessing, True, None, False),
            ("receivedTime", "receivedTime", FHIRDate, False, None, False),
            ("request", "request", FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("subject", "subject", FHIRReference, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js