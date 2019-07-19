#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/EvidenceVariable) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .datarequirement import DataRequirement
from .domainresource import DomainResource
from .duration import Duration
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .relatedartifact import RelatedArtifact
from .timing import Timing
from .triggerdefinition import TriggerDefinition
from .usagecontext import UsageContext


@dataclass
class EvidenceVariableCharacteristic(BackboneElement):
    """ What defines the members of the evidence element.

    A characteristic that defines the members of the evidence element. Multiple
    characteristics are applied with "and" semantics.
    """
    resource_type: ClassVar[str] = "EvidenceVariableCharacteristic"
    definitionCanonical: str = None
    definitionCodeableConcept: CodeableConcept = None
    definitionDataRequirement: DataRequirement = None
    definitionExpression: Expression = None
    definitionReference: FHIRReference = None
    definitionTriggerDefinition: TriggerDefinition = None
    description: Optional[str] = None
    exclude: Optional[bool] = None
    groupMeasure: Optional[str] = None
    participantEffectiveDateTime: Optional[FHIRDate] = None
    participantEffectiveDuration: Optional[Duration] = None
    participantEffectivePeriod: Optional[Period] = None
    participantEffectiveTiming: Optional[Timing] = None
    timeFromStart: Optional[Duration] = None
    usageContext: Optional[List[UsageContext]] = empty_list()

    def elementProperties(self):
        js = super(EvidenceVariableCharacteristic, self).elementProperties()
        js.extend([
            ("definitionCanonical", "definitionCanonical", str, False, "definition", True),
            ("definitionCodeableConcept", "definitionCodeableConcept", CodeableConcept, False, "definition", True),
            ("definitionDataRequirement", "definitionDataRequirement", DataRequirement, False, "definition", True),
            ("definitionExpression", "definitionExpression", Expression, False, "definition", True),
            ("definitionReference", "definitionReference", FHIRReference, False, "definition", True),
            ("definitionTriggerDefinition", "definitionTriggerDefinition", TriggerDefinition, False, "definition", True),
            ("description", "description", str, False, None, False),
            ("exclude", "exclude", bool, False, None, False),
            ("groupMeasure", "groupMeasure", str, False, None, False),
            ("participantEffectiveDateTime", "participantEffectiveDateTime", FHIRDate, False, "participantEffective", False),
            ("participantEffectiveDuration", "participantEffectiveDuration", Duration, False, "participantEffective", False),
            ("participantEffectivePeriod", "participantEffectivePeriod", Period, False, "participantEffective", False),
            ("participantEffectiveTiming", "participantEffectiveTiming", Timing, False, "participantEffective", False),
            ("timeFromStart", "timeFromStart", Duration, False, None, False),
            ("usageContext", "usageContext", UsageContext, True, None, False),
        ])
        return js


@dataclass
class EvidenceVariable(DomainResource):
    """ A population, intervention, or exposure definition.

    The EvidenceVariable resource describes a "PICO" element that knowledge
    (evidence, assertion, recommendation) is about.
    """
    resource_type: ClassVar[str] = "EvidenceVariable"
    approvalDate: Optional[FHIRDate] = None
    author: Optional[List[ContactDetail]] = empty_list()
    characteristic: List[EvidenceVariableCharacteristic] = empty_list()
    contact: Optional[List[ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[FHIRDate] = None
    description: Optional[str] = None
    editor: Optional[List[ContactDetail]] = empty_list()
    effectivePeriod: Optional[Period] = None
    endorser: Optional[List[ContactDetail]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    lastReviewDate: Optional[FHIRDate] = None
    name: Optional[str] = None
    note: Optional[List[Annotation]] = empty_list()
    publisher: Optional[str] = None
    relatedArtifact: Optional[List[RelatedArtifact]] = empty_list()
    reviewer: Optional[List[ContactDetail]] = empty_list()
    shortTitle: Optional[str] = None
    status: str = None
    subtitle: Optional[str] = None
    title: Optional[str] = None
    topic: Optional[List[CodeableConcept]] = empty_list()
    type: Optional[str] = None
    url: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    version: Optional[str] = None

    def elementProperties(self):
        js = super(EvidenceVariable, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", FHIRDate, False, None, False),
            ("author", "author", ContactDetail, True, None, False),
            ("characteristic", "characteristic", EvidenceVariableCharacteristic, True, None, True),
            ("contact", "contact", ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", Period, False, None, False),
            ("endorser", "endorser", ContactDetail, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", ContactDetail, True, None, False),
            ("shortTitle", "shortTitle", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subtitle", "subtitle", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", CodeableConcept, True, None, False),
            ("type", "type", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js