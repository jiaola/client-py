#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class ImmunizationRecommendationRecommendationDateCriterion(BackboneElement):
    """ Dates governing proposed immunization.

    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """
    resource_type: ClassVar[str] = "ImmunizationRecommendationRecommendationDateCriterion"
    code: CodeableConcept = None
    value: FHIRDate = None

    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendationDateCriterion, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("value", "value", FHIRDate, False, None, True),
        ])
        return js


@dataclass
class ImmunizationRecommendationRecommendation(BackboneElement):
    """ Vaccine administration recommendations.
    """
    resource_type: ClassVar[str] = "ImmunizationRecommendationRecommendation"
    contraindicatedVaccineCode: Optional[List[CodeableConcept]] = empty_list()
    dateCriterion: Optional[List[ImmunizationRecommendationRecommendationDateCriterion]] = empty_list()
    description: Optional[str] = None
    doseNumberPositiveInt: Optional[int] = None
    doseNumberString: Optional[str] = None
    forecastReason: Optional[List[CodeableConcept]] = empty_list()
    forecastStatus: CodeableConcept = None
    series: Optional[str] = None
    seriesDosesPositiveInt: Optional[int] = None
    seriesDosesString: Optional[str] = None
    supportingImmunization: Optional[List[FHIRReference]] = empty_list()
    supportingPatientInformation: Optional[List[FHIRReference]] = empty_list()
    targetDisease: Optional[CodeableConcept] = None
    vaccineCode: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendation, self).elementProperties()
        js.extend([
            ("contraindicatedVaccineCode", "contraindicatedVaccineCode", CodeableConcept, True, None, False),
            ("dateCriterion", "dateCriterion", ImmunizationRecommendationRecommendationDateCriterion, True, None, False),
            ("description", "description", str, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", False),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", False),
            ("forecastReason", "forecastReason", CodeableConcept, True, None, False),
            ("forecastStatus", "forecastStatus", CodeableConcept, False, None, True),
            ("series", "series", str, False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("supportingImmunization", "supportingImmunization", FHIRReference, True, None, False),
            ("supportingPatientInformation", "supportingPatientInformation", FHIRReference, True, None, False),
            ("targetDisease", "targetDisease", CodeableConcept, False, None, False),
            ("vaccineCode", "vaccineCode", CodeableConcept, True, None, False),
        ])
        return js


@dataclass
class ImmunizationRecommendation(DomainResource):
    """ Guidance or advice relating to an immunization.

    A patient's point-in-time set of recommendations (i.e. forecasting)
    according to a published schedule with optional supporting justification.
    """
    resource_type: ClassVar[str] = "ImmunizationRecommendation"
    authority: Optional[FHIRReference] = None
    date: FHIRDate = None
    identifier: Optional[List[Identifier]] = empty_list()
    patient: FHIRReference = None
    recommendation: List[ImmunizationRecommendationRecommendation] = empty_list()

    def elementProperties(self):
        js = super(ImmunizationRecommendation, self).elementProperties()
        js.extend([
            ("authority", "authority", FHIRReference, False, None, False),
            ("date", "date", FHIRDate, False, None, True),
            ("identifier", "identifier", Identifier, True, None, False),
            ("patient", "patient", FHIRReference, False, None, True),
            ("recommendation", "recommendation", ImmunizationRecommendationRecommendation, True, None, True),
        ])
        return js