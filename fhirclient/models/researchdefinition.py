#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ResearchDefinition) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .relatedartifact import RelatedArtifact
from .usagecontext import UsageContext


@dataclass
class ResearchDefinition(DomainResource):
    """ A research context or question.

    The ResearchDefinition resource describes the conditional state (population
    and any exposures being compared within the population) and outcome (if
    specified) that the knowledge (evidence, assertion, recommendation) is
    about.
    """
    resource_type: ClassVar[str] = "ResearchDefinition"
    approvalDate: Optional[FHIRDate] = None
    author: Optional[List[ContactDetail]] = empty_list()
    comment: Optional[List[str]] = empty_list()
    contact: Optional[List[ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[FHIRDate] = None
    description: Optional[str] = None
    editor: Optional[List[ContactDetail]] = empty_list()
    effectivePeriod: Optional[Period] = None
    endorser: Optional[List[ContactDetail]] = empty_list()
    experimental: Optional[bool] = None
    exposure: Optional[FHIRReference] = None
    exposureAlternative: Optional[FHIRReference] = None
    identifier: Optional[List[Identifier]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    lastReviewDate: Optional[FHIRDate] = None
    library: Optional[List[str]] = empty_list()
    name: Optional[str] = None
    outcome: Optional[FHIRReference] = None
    population: FHIRReference = None
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
    url: Optional[str] = None
    usage: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    version: Optional[str] = None

    def elementProperties(self):
        js = super(ResearchDefinition, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", FHIRDate, False, None, False),
            ("author", "author", ContactDetail, True, None, False),
            ("comment", "comment", str, True, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", Period, False, None, False),
            ("endorser", "endorser", ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("exposure", "exposure", FHIRReference, False, None, False),
            ("exposureAlternative", "exposureAlternative", FHIRReference, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", FHIRDate, False, None, False),
            ("library", "library", str, True, None, False),
            ("name", "name", str, False, None, False),
            ("outcome", "outcome", FHIRReference, False, None, False),
            ("population", "population", FHIRReference, False, None, True),
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
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js