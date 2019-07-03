#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier


from . import domainresource

@dataclass
class ImmunizationEvaluation(domainresource.DomainResource):
    """ Immunization evaluation information.

    Describes a comparison of an immunization event against published
    recommendations to determine if the administration is "valid" in relation
    to those  recommendations.
    """
    resource_type: ClassVar[str] = "ImmunizationEvaluation"
    authority: Optional[fhirreference.FHIRReference] = None
    date: Optional[fhirdate.FHIRDate] = None
    description: Optional[str] = None
    doseNumberPositiveInt: Optional[int] = None
    doseNumberString: Optional[str] = None
    doseStatus:codeableconcept.CodeableConcept = None
    doseStatusReason: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    immunizationEvent:fhirreference.FHIRReference = None
    patient:fhirreference.FHIRReference = None
    series: Optional[str] = None
    seriesDosesPositiveInt: Optional[int] = None
    seriesDosesString: Optional[str] = None
    status: str = None
    targetDisease:codeableconcept.CodeableConcept = None

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
#        """ Who is responsible for publishing the recommendations.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.date = None
#        """ Date evaluation was performed.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.description = None
#        """ Evaluation notes.
#        Type `str`
#
#. """
#
#
#        self.doseNumberPositiveInt = None
#        """ Dose number within series.
#        Type `int`
#
#. """
#
#
#        self.doseNumberString = None
#        """ Dose number within series.
#        Type `str`
#
#. """
#
#
#        self.doseStatus = None
#        """ Status of the dose relative to published recommendations.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.doseStatusReason = None
#        """ Reason for the dose status.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Business identifier.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.immunizationEvent = None
#        """ Immunization being evaluated.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.patient = None
#        """ Who this evaluation is for.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.series = None
#        """ Name of vaccine series.
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
#        self.status = None
#        """ completed | entered-in-error.
#        Type `str`
#
#. """
#
#
#        self.targetDisease = None
#        """ Evaluation target disease.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(ImmunizationEvaluation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationEvaluation, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, {  # #}False, "doseNumber", {  # #}False),
            ("doseNumberString", "doseNumberString", str, {  # #}False, "doseNumber", {  # #}False),
            ("doseStatus", "doseStatus", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("doseStatusReason", "doseStatusReason", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("immunizationEvent", "immunizationEvent", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("patient", "patient", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("series", "series", str, {  # #}False, None, {  # #}False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, {  # #}False, "seriesDoses", {  # #}False),
            ("seriesDosesString", "seriesDosesString", str, {  # #}False, "seriesDoses", {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
        ])
        return js