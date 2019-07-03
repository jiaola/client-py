#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier


from . import domainresource

@dataclass
class ImmunizationRecommendation(domainresource.DomainResource):
    """ Guidance or advice relating to an immunization.

    A patient's point-in-time set of recommendations (i.e. forecasting)
    according to a published schedule with optional supporting justification.
    """
    resource_type: ClassVar[str] = "ImmunizationRecommendation"
    authority: Optional[fhirreference.FHIRReference] = None
    date:fhirdate.FHIRDate = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    patient:fhirreference.FHIRReference = None
    recommendation: List[ ImmunizationRecommendationRecommendation] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.authority = None
#        """ Who is responsible for protocol.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.date = None
#        """ Date recommendation(s) created.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.identifier = None
#        """ Business identifier.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.patient = None
#        """ Who this profile is for.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.recommendation = None
#        """ Vaccine administration recommendations.
#        List of `ImmunizationRecommendationRecommendation` items
#
# (represented as `dict` in JSON). """
#

#        super(ImmunizationRecommendation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationRecommendation, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}True),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("patient", "patient", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("recommendation", "recommendation", ImmunizationRecommendationRecommendation, {  # #}True, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier


from . import backboneelement

@dataclass
class ImmunizationRecommendationRecommendation(backboneelement.BackboneElement):
    """ Vaccine administration recommendations.
    """
    resource_type: ClassVar[str] = "ImmunizationRecommendationRecommendation"
    contraindicatedVaccineCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    dateCriterion: Optional[List[ImmunizationRecommendationRecommendationDateCriterion]] = empty_list()
    description: Optional[str] = None
    doseNumberPositiveInt: Optional[int] = None
    doseNumberString: Optional[str] = None
    forecastReason: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    forecastStatus:codeableconcept.CodeableConcept = None
    series: Optional[str] = None
    seriesDosesPositiveInt: Optional[int] = None
    seriesDosesString: Optional[str] = None
    supportingImmunization: Optional[List[fhirreference.FHIRReference]] = empty_list()
    supportingPatientInformation: Optional[List[fhirreference.FHIRReference]] = empty_list()
    targetDisease: Optional[codeableconcept.CodeableConcept] = None
    vaccineCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.contraindicatedVaccineCode = None
#        """ Vaccine which is contraindicated to fulfill the recommendation.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.dateCriterion = None
#        """ Dates governing proposed immunization.
#        List of `ImmunizationRecommendationRecommendationDateCriterion` items
#
# (represented as `dict` in JSON). """
#
#
#        self.description = None
#        """ Protocol details.
#        Type `str`
#
#. """
#
#
#        self.doseNumberPositiveInt = None
#        """ Recommended dose number within series.
#        Type `int`
#
#. """
#
#
#        self.doseNumberString = None
#        """ Recommended dose number within series.
#        Type `str`
#
#. """
#
#
#        self.forecastReason = None
#        """ Vaccine administration status reason.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.forecastStatus = None
#        """ Vaccine recommendation status.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.series = None
#        """ Name of vaccination series.
#        Type `str`
#
#. """
#
#
#        self.seriesDosesPositiveInt = None
#        """ Recommended number of doses for immunity.
#        Type `int`
#
#. """
#
#
#        self.seriesDosesString = None
#        """ Recommended number of doses for immunity.
#        Type `str`
#
#. """
#
#
#        self.supportingImmunization = None
#        """ Past immunizations supporting recommendation.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.supportingPatientInformation = None
#        """ Patient observations supporting recommendation.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.targetDisease = None
#        """ Disease to be immunized against.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.vaccineCode = None
#        """ Vaccine  or vaccine group recommendation applies to.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#

#        super(ImmunizationRecommendationRecommendation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendation, self).elementProperties()
        js.extend([
            ("contraindicatedVaccineCode", "contraindicatedVaccineCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("dateCriterion", "dateCriterion", ImmunizationRecommendationRecommendationDateCriterion, {  # #}True, None, {  # #}False),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, {  # #}False, "doseNumber", {  # #}False),
            ("doseNumberString", "doseNumberString", str, {  # #}False, "doseNumber", {  # #}False),
            ("forecastReason", "forecastReason", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("forecastStatus", "forecastStatus", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("series", "series", str, {  # #}False, None, {  # #}False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, {  # #}False, "seriesDoses", {  # #}False),
            ("seriesDosesString", "seriesDosesString", str, {  # #}False, "seriesDoses", {  # #}False),
            ("supportingImmunization", "supportingImmunization", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("supportingPatientInformation", "supportingPatientInformation", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier


@dataclass
class ImmunizationRecommendationRecommendationDateCriterion(backboneelement.BackboneElement):
    """ Dates governing proposed immunization.

    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """
    resource_type: ClassVar[str] = "ImmunizationRecommendationRecommendationDateCriterion"
    code:codeableconcept.CodeableConcept = None
    value:fhirdate.FHIRDate = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.code = None
#        """ Type of date.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.value = None
#        """ Recommended date.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#

#        super(ImmunizationRecommendationRecommendationDateCriterion, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendationDateCriterion, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("value", "value", fhirdate.FHIRDate, {  # #}False, None, {  # #}True),
        ])
        return js