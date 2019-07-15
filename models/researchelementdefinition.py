#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ResearchElementDefinition) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import contactdetail
from . import datarequirement
from . import domainresource
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import relatedartifact
from . import timing
from . import usagecontext

from . import domainresource

@dataclass
class ResearchElementDefinition(domainresource.DomainResource):
    """ A population, intervention, or exposure definition.

    The ResearchElementDefinition resource describes a "PICO" element that
    knowledge (evidence, assertion, recommendation) is about.
    """
    resource_type: ClassVar[str] = "ResearchElementDefinition"
    approvalDate: Optional[fhirdate.FHIRDate] = None
    author: Optional[List[contactdetail.ContactDetail]] = empty_list()
    characteristic: List[ ResearchElementDefinitionCharacteristic] = empty_list()
    comment: Optional[List[str]] = empty_list()
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[fhirdate.FHIRDate] = None
    description: Optional[str] = None
    editor: Optional[List[contactdetail.ContactDetail]] = empty_list()
    effectivePeriod: Optional[period.Period] = None
    endorser: Optional[List[contactdetail.ContactDetail]] = empty_list()
    experimental: Optional[bool] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    lastReviewDate: Optional[fhirdate.FHIRDate] = None
    library: Optional[List[str]] = empty_list()
    name: Optional[str] = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    relatedArtifact: Optional[List[relatedartifact.RelatedArtifact]] = empty_list()
    reviewer: Optional[List[contactdetail.ContactDetail]] = empty_list()
    shortTitle: Optional[str] = None
    status: str = None
    subjectCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    subjectReference: Optional[fhirreference.FHIRReference] = None
    subtitle: Optional[str] = None
    title: Optional[str] = None
    topic: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    type: str = None
    url: Optional[str] = None
    usage: Optional[str] = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    variableType: Optional[str] = None
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ResearchElementDefinition, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("characteristic", "characteristic", ResearchElementDefinitionCharacteristic, True, None, True),
            ("comment", "comment", str, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("library", "library", str, True, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("shortTitle", "shortTitle", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("variableType", "variableType", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class ResearchElementDefinitionCharacteristic(backboneelement.BackboneElement):
    """ What defines the members of the research element.

    A characteristic that defines the members of the research element. Multiple
    characteristics are applied with "and" semantics.
    """
    resource_type: ClassVar[str] = "ResearchElementDefinitionCharacteristic"
    definitionCanonical: str = None
    definitionCodeableConcept:codeableconcept.CodeableConcept = None
    definitionDataRequirement:datarequirement.DataRequirement = None
    definitionExpression:expression.Expression = None
    exclude: Optional[bool] = None
    participantEffectiveDateTime: Optional[fhirdate.FHIRDate] = None
    participantEffectiveDescription: Optional[str] = None
    participantEffectiveDuration: Optional[duration.Duration] = None
    participantEffectiveGroupMeasure: Optional[str] = None
    participantEffectivePeriod: Optional[period.Period] = None
    participantEffectiveTimeFromStart: Optional[duration.Duration] = None
    participantEffectiveTiming: Optional[timing.Timing] = None
    studyEffectiveDateTime: Optional[fhirdate.FHIRDate] = None
    studyEffectiveDescription: Optional[str] = None
    studyEffectiveDuration: Optional[duration.Duration] = None
    studyEffectiveGroupMeasure: Optional[str] = None
    studyEffectivePeriod: Optional[period.Period] = None
    studyEffectiveTimeFromStart: Optional[duration.Duration] = None
    studyEffectiveTiming: Optional[timing.Timing] = None
    unitOfMeasure: Optional[codeableconcept.CodeableConcept] = None
    usageContext: Optional[List[usagecontext.UsageContext]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ResearchElementDefinitionCharacteristic, self).elementProperties()
        js.extend([
            ("definitionCanonical", "definitionCanonical", str, False, "definition", True),
            ("definitionCodeableConcept", "definitionCodeableConcept", codeableconcept.CodeableConcept, False, "definition", True),
            ("definitionDataRequirement", "definitionDataRequirement", datarequirement.DataRequirement, False, "definition", True),
            ("definitionExpression", "definitionExpression", expression.Expression, False, "definition", True),
            ("exclude", "exclude", bool, False, None, False),
            ("participantEffectiveDateTime", "participantEffectiveDateTime", fhirdate.FHIRDate, False, "participantEffective", False),
            ("participantEffectiveDescription", "participantEffectiveDescription", str, False, None, False),
            ("participantEffectiveDuration", "participantEffectiveDuration", duration.Duration, False, "participantEffective", False),
            ("participantEffectiveGroupMeasure", "participantEffectiveGroupMeasure", str, False, None, False),
            ("participantEffectivePeriod", "participantEffectivePeriod", period.Period, False, "participantEffective", False),
            ("participantEffectiveTimeFromStart", "participantEffectiveTimeFromStart", duration.Duration, False, None, False),
            ("participantEffectiveTiming", "participantEffectiveTiming", timing.Timing, False, "participantEffective", False),
            ("studyEffectiveDateTime", "studyEffectiveDateTime", fhirdate.FHIRDate, False, "studyEffective", False),
            ("studyEffectiveDescription", "studyEffectiveDescription", str, False, None, False),
            ("studyEffectiveDuration", "studyEffectiveDuration", duration.Duration, False, "studyEffective", False),
            ("studyEffectiveGroupMeasure", "studyEffectiveGroupMeasure", str, False, None, False),
            ("studyEffectivePeriod", "studyEffectivePeriod", period.Period, False, "studyEffective", False),
            ("studyEffectiveTimeFromStart", "studyEffectiveTimeFromStart", duration.Duration, False, None, False),
            ("studyEffectiveTiming", "studyEffectiveTiming", timing.Timing, False, "studyEffective", False),
            ("unitOfMeasure", "unitOfMeasure", codeableconcept.CodeableConcept, False, None, False),
            ("usageContext", "usageContext", usagecontext.UsageContext, True, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import expression
except ImportError:
    expression = sys.modules[__package__ + '.expression']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']