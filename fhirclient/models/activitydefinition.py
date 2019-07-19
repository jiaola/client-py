#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ActivityDefinition) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .age import Age
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .dosage import Dosage
from .duration import Duration
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range
from .relatedartifact import RelatedArtifact
from .timing import Timing
from .usagecontext import UsageContext


@dataclass
class ActivityDefinitionParticipant(BackboneElement):
    """ Who should participate in the action.

    Indicates who should participate in performing the action described.
    """
    resource_type: ClassVar[str] = "ActivityDefinitionParticipant"
    role: Optional[CodeableConcept] = None
    type: str = None

    def elementProperties(self):
        js = super(ActivityDefinitionParticipant, self).elementProperties()
        js.extend([
            ("role", "role", CodeableConcept, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


@dataclass
class ActivityDefinitionDynamicValue(BackboneElement):
    """ Dynamic aspects of the definition.

    Dynamic values that will be evaluated to produce values for elements of the
    resulting resource. For example, if the dosage of a medication must be
    computed based on the patient's weight, a dynamic value would be used to
    specify an expression that calculated the weight, and the path on the
    request resource that would contain the result.
    """
    resource_type: ClassVar[str] = "ActivityDefinitionDynamicValue"
    expression: Expression = None
    path: str = None

    def elementProperties(self):
        js = super(ActivityDefinitionDynamicValue, self).elementProperties()
        js.extend([
            ("expression", "expression", Expression, False, None, True),
            ("path", "path", str, False, None, True),
        ])
        return js


@dataclass
class ActivityDefinition(DomainResource):
    """ The definition of a specific activity to be taken, independent of any
    particular patient or context.

    This resource allows for the definition of some activity to be performed,
    independent of a particular patient, practitioner, or other performance
    context.
    """
    resource_type: ClassVar[str] = "ActivityDefinition"
    approvalDate: Optional[FHIRDate] = None
    author: Optional[List[ContactDetail]] = empty_list()
    bodySite: Optional[List[CodeableConcept]] = empty_list()
    code: Optional[CodeableConcept] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[FHIRDate] = None
    description: Optional[str] = None
    doNotPerform: Optional[bool] = None
    dosage: Optional[List[Dosage]] = empty_list()
    dynamicValue: Optional[List[ActivityDefinitionDynamicValue]] = empty_list()
    editor: Optional[List[ContactDetail]] = empty_list()
    effectivePeriod: Optional[Period] = None
    endorser: Optional[List[ContactDetail]] = empty_list()
    experimental: Optional[bool] = None
    identifier: Optional[List[Identifier]] = empty_list()
    intent: Optional[str] = None
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    kind: Optional[str] = None
    lastReviewDate: Optional[FHIRDate] = None
    library: Optional[List[str]] = empty_list()
    location: Optional[FHIRReference] = None
    name: Optional[str] = None
    observationRequirement: Optional[List[FHIRReference]] = empty_list()
    observationResultRequirement: Optional[List[FHIRReference]] = empty_list()
    participant: Optional[List[ActivityDefinitionParticipant]] = empty_list()
    priority: Optional[str] = None
    productCodeableConcept: Optional[CodeableConcept] = None
    productReference: Optional[FHIRReference] = None
    profile: Optional[str] = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    quantity: Optional[Quantity] = None
    relatedArtifact: Optional[List[RelatedArtifact]] = empty_list()
    reviewer: Optional[List[ContactDetail]] = empty_list()
    specimenRequirement: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    subjectCodeableConcept: Optional[CodeableConcept] = None
    subjectReference: Optional[FHIRReference] = None
    subtitle: Optional[str] = None
    timingAge: Optional[Age] = None
    timingDateTime: Optional[FHIRDate] = None
    timingDuration: Optional[Duration] = None
    timingPeriod: Optional[Period] = None
    timingRange: Optional[Range] = None
    timingTiming: Optional[Timing] = None
    title: Optional[str] = None
    topic: Optional[List[CodeableConcept]] = empty_list()
    transform: Optional[str] = None
    url: Optional[str] = None
    usage: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    version: Optional[str] = None

    def elementProperties(self):
        js = super(ActivityDefinition, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", FHIRDate, False, None, False),
            ("author", "author", ContactDetail, True, None, False),
            ("bodySite", "bodySite", CodeableConcept, True, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("dosage", "dosage", Dosage, True, None, False),
            ("dynamicValue", "dynamicValue", ActivityDefinitionDynamicValue, True, None, False),
            ("editor", "editor", ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", Period, False, None, False),
            ("endorser", "endorser", ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("intent", "intent", str, False, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("kind", "kind", str, False, None, False),
            ("lastReviewDate", "lastReviewDate", FHIRDate, False, None, False),
            ("library", "library", str, True, None, False),
            ("location", "location", FHIRReference, False, None, False),
            ("name", "name", str, False, None, False),
            ("observationRequirement", "observationRequirement", FHIRReference, True, None, False),
            ("observationResultRequirement", "observationResultRequirement", FHIRReference, True, None, False),
            ("participant", "participant", ActivityDefinitionParticipant, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("productCodeableConcept", "productCodeableConcept", CodeableConcept, False, "product", False),
            ("productReference", "productReference", FHIRReference, False, "product", False),
            ("profile", "profile", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("relatedArtifact", "relatedArtifact", RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", ContactDetail, True, None, False),
            ("specimenRequirement", "specimenRequirement", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subjectCodeableConcept", "subjectCodeableConcept", CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("timingAge", "timingAge", Age, False, "timing", False),
            ("timingDateTime", "timingDateTime", FHIRDate, False, "timing", False),
            ("timingDuration", "timingDuration", Duration, False, "timing", False),
            ("timingPeriod", "timingPeriod", Period, False, "timing", False),
            ("timingRange", "timingRange", Range, False, "timing", False),
            ("timingTiming", "timingTiming", Timing, False, "timing", False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", CodeableConcept, True, None, False),
            ("transform", "transform", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js