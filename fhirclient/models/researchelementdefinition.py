#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ResearchElementDefinition) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

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
from .usagecontext import UsageContext


@dataclass
class ResearchElementDefinitionCharacteristic(BackboneElement):
    """ What defines the members of the research element.

    A characteristic that defines the members of the research element. Multiple
    characteristics are applied with "and" semantics.
    """
    resource_type: ClassVar[str] = "ResearchElementDefinitionCharacteristic"
    definitionCanonical: str = None
    definitionCodeableConcept: CodeableConcept = None
    definitionDataRequirement: DataRequirement = None
    definitionExpression: Expression = None
    exclude: Optional[bool] = None
    participantEffectiveDateTime: Optional[FHIRDate] = None
    participantEffectiveDescription: Optional[str] = None
    participantEffectiveDuration: Optional[Duration] = None
    participantEffectiveGroupMeasure: Optional[str] = None
    participantEffectivePeriod: Optional[Period] = None
    participantEffectiveTimeFromStart: Optional[Duration] = None
    participantEffectiveTiming: Optional[Timing] = None
    studyEffectiveDateTime: Optional[FHIRDate] = None
    studyEffectiveDescription: Optional[str] = None
    studyEffectiveDuration: Optional[Duration] = None
    studyEffectiveGroupMeasure: Optional[str] = None
    studyEffectivePeriod: Optional[Period] = None
    studyEffectiveTimeFromStart: Optional[Duration] = None
    studyEffectiveTiming: Optional[Timing] = None
    unitOfMeasure: Optional[CodeableConcept] = None
    usageContext: Optional[List[UsageContext]] = empty_list()

    def elementProperties(self):
        js = super(ResearchElementDefinitionCharacteristic, self).elementProperties()
        js.extend([
            ("definitionCanonical", "definitionCanonical", str, False, "definition", True),
            ("definitionCodeableConcept", "definitionCodeableConcept", CodeableConcept, False, "definition", True),
            ("definitionDataRequirement", "definitionDataRequirement", DataRequirement, False, "definition", True),
            ("definitionExpression", "definitionExpression", Expression, False, "definition", True),
            ("exclude", "exclude", bool, False, None, False),
            ("participantEffectiveDateTime", "participantEffectiveDateTime", FHIRDate, False, "participantEffective", False),
            ("participantEffectiveDescription", "participantEffectiveDescription", str, False, None, False),
            ("participantEffectiveDuration", "participantEffectiveDuration", Duration, False, "participantEffective", False),
            ("participantEffectiveGroupMeasure", "participantEffectiveGroupMeasure", str, False, None, False),
            ("participantEffectivePeriod", "participantEffectivePeriod", Period, False, "participantEffective", False),
            ("participantEffectiveTimeFromStart", "participantEffectiveTimeFromStart", Duration, False, None, False),
            ("participantEffectiveTiming", "participantEffectiveTiming", Timing, False, "participantEffective", False),
            ("studyEffectiveDateTime", "studyEffectiveDateTime", FHIRDate, False, "studyEffective", False),
            ("studyEffectiveDescription", "studyEffectiveDescription", str, False, None, False),
            ("studyEffectiveDuration", "studyEffectiveDuration", Duration, False, "studyEffective", False),
            ("studyEffectiveGroupMeasure", "studyEffectiveGroupMeasure", str, False, None, False),
            ("studyEffectivePeriod", "studyEffectivePeriod", Period, False, "studyEffective", False),
            ("studyEffectiveTimeFromStart", "studyEffectiveTimeFromStart", Duration, False, None, False),
            ("studyEffectiveTiming", "studyEffectiveTiming", Timing, False, "studyEffective", False),
            ("unitOfMeasure", "unitOfMeasure", CodeableConcept, False, None, False),
            ("usageContext", "usageContext", UsageContext, True, None, False),
        ])
        return js


@dataclass
class ResearchElementDefinition(DomainResource):
    """ A population, intervention, or exposure definition.

    The ResearchElementDefinition resource describes a "PICO" element that
    knowledge (evidence, assertion, recommendation) is about.
    """
    resource_type: ClassVar[str] = "ResearchElementDefinition"
    approvalDate: Optional[FHIRDate] = None
    author: Optional[List[ContactDetail]] = empty_list()
    characteristic: List[ResearchElementDefinitionCharacteristic] = empty_list()
    comment: Optional[List[str]] = empty_list()
    contact: Optional[List[ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[FHIRDate] = None
    description: Optional[str] = None
    editor: Optional[List[ContactDetail]] = empty_list()
    effectivePeriod: Optional[Period] = None
    endorser: Optional[List[ContactDetail]] = empty_list()
    experimental: Optional[bool] = None
    identifier: Optional[List[Identifier]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    lastReviewDate: Optional[FHIRDate] = None
    library: Optional[List[str]] = empty_list()
    name: Optional[str] = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    relatedArtifact: Optional[List[RelatedArtifact]] = empty_list()
    reviewer: Optional[List[ContactDetail]] = empty_list()
    shortTitle: Optional[str] = None
    status: str = None
    subjectCodeableConcept: Optional[CodeableConcept] = None
    subjectReference: Optional[FHIRReference] = None
    subtitle: Optional[str] = None
    title: Optional[str] = None
    topic: Optional[List[CodeableConcept]] = empty_list()
    type: str = None
    url: Optional[str] = None
    usage: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    variableType: Optional[str] = None
    version: Optional[str] = None

    def elementProperties(self):
        js = super(ResearchElementDefinition, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", FHIRDate, False, None, False),
            ("author", "author", ContactDetail, True, None, False),
            ("characteristic", "characteristic", ResearchElementDefinitionCharacteristic, True, None, True),
            ("comment", "comment", str, True, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", Period, False, None, False),
            ("endorser", "endorser", ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", FHIRDate, False, None, False),
            ("library", "library", str, True, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", ContactDetail, True, None, False),
            ("shortTitle", "shortTitle", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subjectCodeableConcept", "subjectCodeableConcept", CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", CodeableConcept, True, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("variableType", "variableType", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js