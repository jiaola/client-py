#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/EffectEvidenceSynthesis) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
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
class EffectEvidenceSynthesisSampleSize(BackboneElement):
    """ What sample size was involved?.

    A description of the size of the sample involved in the synthesis.
    """
    resource_type: ClassVar[str] = "EffectEvidenceSynthesisSampleSize"
    description: Optional[str] = None
    numberOfParticipants: Optional[int] = None
    numberOfStudies: Optional[int] = None

    def elementProperties(self):
        js = super(EffectEvidenceSynthesisSampleSize, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("numberOfParticipants", "numberOfParticipants", int, False, None, False),
            ("numberOfStudies", "numberOfStudies", int, False, None, False),
        ])
        return js


@dataclass
class EffectEvidenceSynthesisResultsByExposure(BackboneElement):
    """ What was the result per exposure?.

    A description of the results for each exposure considered in the effect
    estimate.
    """
    resource_type: ClassVar[str] = "EffectEvidenceSynthesisResultsByExposure"
    description: Optional[str] = None
    exposureState: Optional[str] = None
    riskEvidenceSynthesis: FHIRReference = None
    variantState: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(EffectEvidenceSynthesisResultsByExposure, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("exposureState", "exposureState", str, False, None, False),
            ("riskEvidenceSynthesis", "riskEvidenceSynthesis", FHIRReference, False, None, True),
            ("variantState", "variantState", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class EffectEvidenceSynthesisEffectEstimatePrecisionEstimate(BackboneElement):
    """ How precise the estimate is.

    A description of the precision of the estimate for the effect.
    """
    resource_type: ClassVar[str] = "EffectEvidenceSynthesisEffectEstimatePrecisionEstimate"
    from_fhir: Optional[float] = None
    level: Optional[float] = None
    to: Optional[float] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(EffectEvidenceSynthesisEffectEstimatePrecisionEstimate, self).elementProperties()
        js.extend([
            ("from_fhir", "from", float, False, None, False),
            ("level", "level", float, False, None, False),
            ("to", "to", float, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class EffectEvidenceSynthesisEffectEstimate(BackboneElement):
    """ What was the estimated effect.

    The estimated effect of the exposure variant.
    """
    resource_type: ClassVar[str] = "EffectEvidenceSynthesisEffectEstimate"
    description: Optional[str] = None
    precisionEstimate: Optional[List[EffectEvidenceSynthesisEffectEstimatePrecisionEstimate]] = empty_list()
    type: Optional[CodeableConcept] = None
    unitOfMeasure: Optional[CodeableConcept] = None
    value: Optional[float] = None
    variantState: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(EffectEvidenceSynthesisEffectEstimate, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("precisionEstimate", "precisionEstimate", EffectEvidenceSynthesisEffectEstimatePrecisionEstimate, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("unitOfMeasure", "unitOfMeasure", CodeableConcept, False, None, False),
            ("value", "value", float, False, None, False),
            ("variantState", "variantState", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class EffectEvidenceSynthesisCertaintyCertaintySubcomponent(BackboneElement):
    """ A component that contributes to the overall certainty.

    A description of a component of the overall certainty.
    """
    resource_type: ClassVar[str] = "EffectEvidenceSynthesisCertaintyCertaintySubcomponent"
    note: Optional[List[Annotation]] = empty_list()
    rating: Optional[List[CodeableConcept]] = empty_list()
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(EffectEvidenceSynthesisCertaintyCertaintySubcomponent, self).elementProperties()
        js.extend([
            ("note", "note", Annotation, True, None, False),
            ("rating", "rating", CodeableConcept, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class EffectEvidenceSynthesisCertainty(BackboneElement):
    """ How certain is the effect.

    A description of the certainty of the effect estimate.
    """
    resource_type: ClassVar[str] = "EffectEvidenceSynthesisCertainty"
    certaintySubcomponent: Optional[List[EffectEvidenceSynthesisCertaintyCertaintySubcomponent]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    rating: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(EffectEvidenceSynthesisCertainty, self).elementProperties()
        js.extend([
            ("certaintySubcomponent", "certaintySubcomponent", EffectEvidenceSynthesisCertaintyCertaintySubcomponent, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("rating", "rating", CodeableConcept, True, None, False),
        ])
        return js


@dataclass
class EffectEvidenceSynthesis(DomainResource):
    """ A quantified estimate of effect based on a body of evidence.

    The EffectEvidenceSynthesis resource describes the difference in an outcome
    between exposures states in a population where the effect estimate is
    derived from a combination of research studies.
    """
    resource_type: ClassVar[str] = "EffectEvidenceSynthesis"
    approvalDate: Optional[FHIRDate] = None
    author: Optional[List[ContactDetail]] = empty_list()
    certainty: Optional[List[EffectEvidenceSynthesisCertainty]] = empty_list()
    contact: Optional[List[ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[FHIRDate] = None
    description: Optional[str] = None
    editor: Optional[List[ContactDetail]] = empty_list()
    effectEstimate: Optional[List[EffectEvidenceSynthesisEffectEstimate]] = empty_list()
    effectivePeriod: Optional[Period] = None
    endorser: Optional[List[ContactDetail]] = empty_list()
    exposure: FHIRReference = None
    exposureAlternative: FHIRReference = None
    identifier: Optional[List[Identifier]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    lastReviewDate: Optional[FHIRDate] = None
    name: Optional[str] = None
    note: Optional[List[Annotation]] = empty_list()
    outcome: FHIRReference = None
    population: FHIRReference = None
    publisher: Optional[str] = None
    relatedArtifact: Optional[List[RelatedArtifact]] = empty_list()
    resultsByExposure: Optional[List[EffectEvidenceSynthesisResultsByExposure]] = empty_list()
    reviewer: Optional[List[ContactDetail]] = empty_list()
    sampleSize: Optional[EffectEvidenceSynthesisSampleSize] = None
    status: str = None
    studyType: Optional[CodeableConcept] = None
    synthesisType: Optional[CodeableConcept] = None
    title: Optional[str] = None
    topic: Optional[List[CodeableConcept]] = empty_list()
    url: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    version: Optional[str] = None

    def elementProperties(self):
        js = super(EffectEvidenceSynthesis, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", FHIRDate, False, None, False),
            ("author", "author", ContactDetail, True, None, False),
            ("certainty", "certainty", EffectEvidenceSynthesisCertainty, True, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", ContactDetail, True, None, False),
            ("effectEstimate", "effectEstimate", EffectEvidenceSynthesisEffectEstimate, True, None, False),
            ("effectivePeriod", "effectivePeriod", Period, False, None, False),
            ("endorser", "endorser", ContactDetail, True, None, False),
            ("exposure", "exposure", FHIRReference, False, None, True),
            ("exposureAlternative", "exposureAlternative", FHIRReference, False, None, True),
            ("identifier", "identifier", Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("outcome", "outcome", FHIRReference, False, None, True),
            ("population", "population", FHIRReference, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", RelatedArtifact, True, None, False),
            ("resultsByExposure", "resultsByExposure", EffectEvidenceSynthesisResultsByExposure, True, None, False),
            ("reviewer", "reviewer", ContactDetail, True, None, False),
            ("sampleSize", "sampleSize", EffectEvidenceSynthesisSampleSize, False, None, False),
            ("status", "status", str, False, None, True),
            ("studyType", "studyType", CodeableConcept, False, None, False),
            ("synthesisType", "synthesisType", CodeableConcept, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", CodeableConcept, True, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js