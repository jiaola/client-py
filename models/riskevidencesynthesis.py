#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/RiskEvidenceSynthesis) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import contactdetail
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import relatedartifact
from . import usagecontext

from . import backboneelement

@dataclass
class RiskEvidenceSynthesisSampleSize(backboneelement.BackboneElement):
    """ What sample size was involved?.

    A description of the size of the sample involved in the synthesis.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesisSampleSize"
    description: Optional[str] = None
    numberOfParticipants: Optional[int] = None
    numberOfStudies: Optional[int] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisSampleSize, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("numberOfParticipants", "numberOfParticipants", int, False, None, False),
            ("numberOfStudies", "numberOfStudies", int, False, None, False),
        ])
        return js

@dataclass
class RiskEvidenceSynthesisRiskEstimatePrecisionEstimate(backboneelement.BackboneElement):
    """ How precise the estimate is.

    A description of the precision of the estimate for the effect.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesisRiskEstimatePrecisionEstimate"
    from_fhir: Optional[float] = None
    level: Optional[float] = None
    to: Optional[float] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, self).elementProperties()
        js.extend([
            ("from_fhir", "from", float, False, None, False),
            ("level", "level", float, False, None, False),
            ("to", "to", float, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class RiskEvidenceSynthesisRiskEstimate(backboneelement.BackboneElement):
    """ What was the estimated risk.

    The estimated risk of the outcome.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesisRiskEstimate"
    denominatorCount: Optional[int] = None
    description: Optional[str] = None
    numeratorCount: Optional[int] = None
    precisionEstimate: Optional[List[RiskEvidenceSynthesisRiskEstimatePrecisionEstimate]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None
    unitOfMeasure: Optional[codeableconcept.CodeableConcept] = None
    value: Optional[float] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisRiskEstimate, self).elementProperties()
        js.extend([
            ("denominatorCount", "denominatorCount", int, False, None, False),
            ("description", "description", str, False, None, False),
            ("numeratorCount", "numeratorCount", int, False, None, False),
            ("precisionEstimate", "precisionEstimate", RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("unitOfMeasure", "unitOfMeasure", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js

@dataclass
class RiskEvidenceSynthesisCertaintyCertaintySubcomponent(backboneelement.BackboneElement):
    """ A component that contributes to the overall certainty.

    A description of a component of the overall certainty.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesisCertaintyCertaintySubcomponent"
    note: Optional[List[annotation.Annotation]] = empty_list()
    rating: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisCertaintyCertaintySubcomponent, self).elementProperties()
        js.extend([
            ("note", "note", annotation.Annotation, True, None, False),
            ("rating", "rating", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class RiskEvidenceSynthesisCertainty(backboneelement.BackboneElement):
    """ How certain is the risk.

    A description of the certainty of the risk estimate.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesisCertainty"
    certaintySubcomponent: Optional[List[RiskEvidenceSynthesisCertaintyCertaintySubcomponent]] = empty_list()
    note: Optional[List[annotation.Annotation]] = empty_list()
    rating: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisCertainty, self).elementProperties()
        js.extend([
            ("certaintySubcomponent", "certaintySubcomponent", RiskEvidenceSynthesisCertaintyCertaintySubcomponent, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("rating", "rating", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js

from . import domainresource

@dataclass
class RiskEvidenceSynthesis(domainresource.DomainResource):
    """ A quantified estimate of risk based on a body of evidence.

    The RiskEvidenceSynthesis resource describes the likelihood of an outcome
    in a population plus exposure state where the risk estimate is derived from
    a combination of research studies.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesis"
    approvalDate: Optional[fhirdate.FHIRDate] = None
    author: Optional[List[contactdetail.ContactDetail]] = empty_list()
    certainty: Optional[List[RiskEvidenceSynthesisCertainty]] = empty_list()
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[fhirdate.FHIRDate] = None
    description: Optional[str] = None
    editor: Optional[List[contactdetail.ContactDetail]] = empty_list()
    effectivePeriod: Optional[period.Period] = None
    endorser: Optional[List[contactdetail.ContactDetail]] = empty_list()
    exposure: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    lastReviewDate: Optional[fhirdate.FHIRDate] = None
    name: Optional[str] = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    outcome:fhirreference.FHIRReference = None
    population:fhirreference.FHIRReference = None
    publisher: Optional[str] = None
    relatedArtifact: Optional[List[relatedartifact.RelatedArtifact]] = empty_list()
    reviewer: Optional[List[contactdetail.ContactDetail]] = empty_list()
    riskEstimate: Optional[RiskEvidenceSynthesisRiskEstimate] = None
    sampleSize: Optional[RiskEvidenceSynthesisSampleSize] = None
    status: str = None
    studyType: Optional[codeableconcept.CodeableConcept] = None
    synthesisType: Optional[codeableconcept.CodeableConcept] = None
    title: Optional[str] = None
    topic: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    url: Optional[str] = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesis, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("certainty", "certainty", RiskEvidenceSynthesisCertainty, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("exposure", "exposure", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("outcome", "outcome", fhirreference.FHIRReference, False, None, True),
            ("population", "population", fhirreference.FHIRReference, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("riskEstimate", "riskEstimate", RiskEvidenceSynthesisRiskEstimate, False, None, False),
            ("sampleSize", "sampleSize", RiskEvidenceSynthesisSampleSize, False, None, False),
            ("status", "status", str, False, None, True),
            ("studyType", "studyType", codeableconcept.CodeableConcept, False, None, False),
            ("synthesisType", "synthesisType", codeableconcept.CodeableConcept, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
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