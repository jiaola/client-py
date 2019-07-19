#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Library) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .datarequirement import DataRequirement
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .parameterdefinition import ParameterDefinition
from .period import Period
from .relatedartifact import RelatedArtifact
from .usagecontext import UsageContext


@dataclass
class Library(DomainResource):
    """ Represents a library of quality improvement components.

    The Library resource is a general-purpose container for knowledge asset
    definitions. It can be used to describe and expose existing knowledge
    assets such as logic libraries and information model descriptions, as well
    as to describe a collection of knowledge assets.
    """
    resource_type: ClassVar[str] = "Library"
    approvalDate: Optional[FHIRDate] = None
    author: Optional[List[ContactDetail]] = empty_list()
    contact: Optional[List[ContactDetail]] = empty_list()
    content: Optional[List[Attachment]] = empty_list()
    copyright: Optional[str] = None
    dataRequirement: Optional[List[DataRequirement]] = empty_list()
    date: Optional[FHIRDate] = None
    description: Optional[str] = None
    editor: Optional[List[ContactDetail]] = empty_list()
    effectivePeriod: Optional[Period] = None
    endorser: Optional[List[ContactDetail]] = empty_list()
    experimental: Optional[bool] = None
    identifier: Optional[List[Identifier]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    lastReviewDate: Optional[FHIRDate] = None
    name: Optional[str] = None
    parameter: Optional[List[ParameterDefinition]] = empty_list()
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    relatedArtifact: Optional[List[RelatedArtifact]] = empty_list()
    reviewer: Optional[List[ContactDetail]] = empty_list()
    status: str = None
    subjectCodeableConcept: Optional[CodeableConcept] = None
    subjectReference: Optional[FHIRReference] = None
    subtitle: Optional[str] = None
    title: Optional[str] = None
    topic: Optional[List[CodeableConcept]] = empty_list()
    type: CodeableConcept = None
    url: Optional[str] = None
    usage: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    version: Optional[str] = None

    def elementProperties(self):
        js = super(Library, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", FHIRDate, False, None, False),
            ("author", "author", ContactDetail, True, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("content", "content", Attachment, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("dataRequirement", "dataRequirement", DataRequirement, True, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", Period, False, None, False),
            ("endorser", "endorser", ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("parameter", "parameter", ParameterDefinition, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", ContactDetail, True, None, False),
            ("status", "status", str, False, None, True),
            ("subjectCodeableConcept", "subjectCodeableConcept", CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", CodeableConcept, True, None, False),
            ("type", "type", CodeableConcept, False, None, True),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js