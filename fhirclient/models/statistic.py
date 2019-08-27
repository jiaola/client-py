#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Statistic) on 2019-08-26.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .contributor import Contributor
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .range import Range
from .relatedartifact import RelatedArtifact
from .usagecontext import UsageContext


@dataclass
class StatisticCertaintyCertaintySubcomponent(BackboneElement):
    """ A component that contributes to the overall certainty.

    A description of a component of the overall certainty.
    """
    resource_type: ClassVar[str] = "StatisticCertaintyCertaintySubcomponent"

    description: Optional[str] = None
    note: Optional[List[Annotation]] = None
    type: Optional[List[CodeableConcept]] = None
    rating: Optional[List[CodeableConcept]] = None


@dataclass
class StatisticStatisticPublisher(BackboneElement):
    """ The individual or organization that produced this statistic.
    """
    resource_type: ClassVar[str] = "StatisticStatisticPublisher"

    name: str = None
    contact: Optional[List[ContactDetail]] = None


@dataclass
class StatisticSampleSize(BackboneElement):
    """ Population sample size.
    """
    resource_type: ClassVar[str] = "StatisticSampleSize"

    description: Optional[str] = None
    note: Optional[List[Annotation]] = None
    numberOfStudies: Optional[int] = None
    numberOfParticipants: Optional[int] = None
    knownDataCount: Optional[int] = None
    numeratorCount: Optional[int] = None


@dataclass
class StatisticPrecisionEstimate(BackboneElement):
    """ An estimate of the precision of the statistic.
    """
    resource_type: ClassVar[str] = "StatisticPrecisionEstimate"

    description: Optional[str] = None
    note: Optional[List[Annotation]] = None
    type: Optional[CodeableConcept] = None
    level: Optional[float] = None
    from_fhir: Optional[float] = field(default=None, metadata=dict(orig_name='from'))
    to: Optional[float] = None


@dataclass
class StatisticPValue(BackboneElement):
    """ The probability that this statistic would be the same given the null
    hypothesis.
    """
    resource_type: ClassVar[str] = "StatisticPValue"

    description: Optional[str] = None
    note: Optional[List[Annotation]] = None
    type: Optional[CodeableConcept] = None
    quantity: Optional[Quantity] = None
    range: Optional[Range] = None


@dataclass
class StatisticCertainty(BackboneElement):
    """ How certain is the effect.

    A description of the certainty of the effect estimate.
    """
    resource_type: ClassVar[str] = "StatisticCertainty"

    description: Optional[str] = None
    note: Optional[List[Annotation]] = None
    rating: Optional[List[CodeableConcept]] = None
    certaintySubcomponent: Optional[List[StatisticCertaintyCertaintySubcomponent]] = None


@dataclass
class Statistic(DomainResource):
    """ A statistic.

    The Statistic resource codifies a statistical measure and corresponding
    certainty.
    """
    resource_type: ClassVar[str] = "Statistic"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    title: Optional[str] = None
    status: str = None
    date: Optional[FHIRDate] = None
    useContext: Optional[List[UsageContext]] = None
    approvalDate: Optional[FHIRDate] = None
    lastReviewDate: Optional[FHIRDate] = None
    statisticPublisher: Optional[List[StatisticStatisticPublisher]] = None
    contributor: Optional[List[Contributor]] = None
    relatedArtifact: Optional[List[RelatedArtifact]] = None
    description: Optional[str] = None
    note: Optional[List[Annotation]] = None
    synthesisType: Optional[CodeableConcept] = None
    studyType: Optional[CodeableConcept] = None
    exposureBackground: FHIRReference = None
    exposure: Optional[FHIRReference] = None
    exposureVariant: Optional[List[FHIRReference]] = None
    measuredVariable: Optional[List[FHIRReference]] = None
    statisticType: Optional[CodeableConcept] = None
    quantity: Optional[Quantity] = None
    sampleSize: Optional[StatisticSampleSize] = None
    precisionEstimate: Optional[List[StatisticPrecisionEstimate]] = None
    pValue: Optional[List[StatisticPValue]] = None
    certainty: Optional[List[StatisticCertainty]] = None