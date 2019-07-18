#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Measure) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import contactdetail
from . import domainresource
from . import expression
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import relatedartifact
from . import usagecontext

from . import backboneelement

@dataclass
class MeasureSupplementalData(backboneelement.BackboneElement):
    """ What other data should be reported with the measure.

    The supplemental data criteria for the measure report, specified as either
    the name of a valid CQL expression within a referenced library, or a valid
    FHIR Resource Path.
    """
    resource_type: ClassVar[str] = "MeasureSupplementalData"
    code: Optional[codeableconcept.CodeableConcept] = None
    criteria:expression.Expression = None
    description: Optional[str] = None
    usage: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MeasureSupplementalData, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("criteria", "criteria", expression.Expression, False, None, True),
            ("description", "description", str, False, None, False),
            ("usage", "usage", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js

@dataclass
class MeasureGroupStratifierComponent(backboneelement.BackboneElement):
    """ Stratifier criteria component for the measure.

    A component of the stratifier criteria for the measure report, specified as
    either the name of a valid CQL expression defined within a referenced
    library or a valid FHIR Resource Path.
    """
    resource_type: ClassVar[str] = "MeasureGroupStratifierComponent"
    code: Optional[codeableconcept.CodeableConcept] = None
    criteria:expression.Expression = None
    description: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MeasureGroupStratifierComponent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("criteria", "criteria", expression.Expression, False, None, True),
            ("description", "description", str, False, None, False),
        ])
        return js

@dataclass
class MeasureGroupStratifier(backboneelement.BackboneElement):
    """ Stratifier criteria for the measure.

    The stratifier criteria for the measure report, specified as either the
    name of a valid CQL expression defined within a referenced library or a
    valid FHIR Resource Path.
    """
    resource_type: ClassVar[str] = "MeasureGroupStratifier"
    code: Optional[codeableconcept.CodeableConcept] = None
    component: Optional[List[MeasureGroupStratifierComponent]] = empty_list()
    criteria: Optional[expression.Expression] = None
    description: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MeasureGroupStratifier, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("component", "component", MeasureGroupStratifierComponent, True, None, False),
            ("criteria", "criteria", expression.Expression, False, None, False),
            ("description", "description", str, False, None, False),
        ])
        return js

@dataclass
class MeasureGroupPopulation(backboneelement.BackboneElement):
    """ Population criteria.

    A population criteria for the measure.
    """
    resource_type: ClassVar[str] = "MeasureGroupPopulation"
    code: Optional[codeableconcept.CodeableConcept] = None
    criteria:expression.Expression = None
    description: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MeasureGroupPopulation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("criteria", "criteria", expression.Expression, False, None, True),
            ("description", "description", str, False, None, False),
        ])
        return js

@dataclass
class MeasureGroup(backboneelement.BackboneElement):
    """ Population criteria group.

    A group of population criteria for the measure.
    """
    resource_type: ClassVar[str] = "MeasureGroup"
    code: Optional[codeableconcept.CodeableConcept] = None
    description: Optional[str] = None
    population: Optional[List[MeasureGroupPopulation]] = empty_list()
    stratifier: Optional[List[MeasureGroupStratifier]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MeasureGroup, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("population", "population", MeasureGroupPopulation, True, None, False),
            ("stratifier", "stratifier", MeasureGroupStratifier, True, None, False),
        ])
        return js

from . import domainresource

@dataclass
class Measure(domainresource.DomainResource):
    """ A quality measure definition.

    The Measure resource provides the definition of a quality measure.
    """
    resource_type: ClassVar[str] = "Measure"
    approvalDate: Optional[fhirdate.FHIRDate] = None
    author: Optional[List[contactdetail.ContactDetail]] = empty_list()
    clinicalRecommendationStatement: Optional[str] = None
    compositeScoring: Optional[codeableconcept.CodeableConcept] = None
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[fhirdate.FHIRDate] = None
    definition: Optional[List[str]] = empty_list()
    description: Optional[str] = None
    disclaimer: Optional[str] = None
    editor: Optional[List[contactdetail.ContactDetail]] = empty_list()
    effectivePeriod: Optional[period.Period] = None
    endorser: Optional[List[contactdetail.ContactDetail]] = empty_list()
    experimental: Optional[bool] = None
    group: Optional[List[MeasureGroup]] = empty_list()
    guidance: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    improvementNotation: Optional[codeableconcept.CodeableConcept] = None
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    lastReviewDate: Optional[fhirdate.FHIRDate] = None
    library: Optional[List[str]] = empty_list()
    name: Optional[str] = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    rateAggregation: Optional[str] = None
    rationale: Optional[str] = None
    relatedArtifact: Optional[List[relatedartifact.RelatedArtifact]] = empty_list()
    reviewer: Optional[List[contactdetail.ContactDetail]] = empty_list()
    riskAdjustment: Optional[str] = None
    scoring: Optional[codeableconcept.CodeableConcept] = None
    status: str = None
    subjectCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    subjectReference: Optional[fhirreference.FHIRReference] = None
    subtitle: Optional[str] = None
    supplementalData: Optional[List[MeasureSupplementalData]] = empty_list()
    title: Optional[str] = None
    topic: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    type: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    url: Optional[str] = None
    usage: Optional[str] = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Measure, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("clinicalRecommendationStatement", "clinicalRecommendationStatement", str, False, None, False),
            ("compositeScoring", "compositeScoring", codeableconcept.CodeableConcept, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("definition", "definition", str, True, None, False),
            ("description", "description", str, False, None, False),
            ("disclaimer", "disclaimer", str, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("group", "group", MeasureGroup, True, None, False),
            ("guidance", "guidance", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("improvementNotation", "improvementNotation", codeableconcept.CodeableConcept, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("library", "library", str, True, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("rateAggregation", "rateAggregation", str, False, None, False),
            ("rationale", "rationale", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("riskAdjustment", "riskAdjustment", str, False, None, False),
            ("scoring", "scoring", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("supplementalData", "supplementalData", MeasureSupplementalData, True, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
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
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']