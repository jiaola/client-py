#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/RiskAssessment) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import range


from . import domainresource

@dataclass
class RiskAssessment(domainresource.DomainResource):
    """ Potential outcomes for a subject with likelihood.

    An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """
    resource_type: ClassVar[str] = "RiskAssessment"
    basedOn: Optional[fhirreference.FHIRReference] = None
    basis: Optional[List[fhirreference.FHIRReference]] = empty_list()
    code: Optional[codeableconcept.CodeableConcept] = None
    condition: Optional[fhirreference.FHIRReference] = None
    encounter: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    method: Optional[codeableconcept.CodeableConcept] = None
    mitigation: Optional[str] = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    occurrenceDateTime: Optional[fhirdate.FHIRDate] = None
    occurrencePeriod: Optional[period.Period] = None
    parent: Optional[fhirreference.FHIRReference] = None
    performer: Optional[fhirreference.FHIRReference] = None
    prediction: Optional[List[RiskAssessmentPrediction]] = empty_list()
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: str = None
    subject:fhirreference.FHIRReference = None

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
#        self.basedOn = None
#        """ Request fulfilled by this assessment.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.basis = None
#        """ Information used in assessment.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.code = None
#        """ Type of assessment.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.condition = None
#        """ Condition assessed.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.encounter = None
#        """ Where was assessment performed?.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Unique identifier for the assessment.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.method = None
#        """ Evaluation mechanism.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.mitigation = None
#        """ How to reduce risk.
#        Type `str`
#
#. """
#
#
#        self.note = None
#        """ Comments on the risk assessment.
#        List of `Annotation` items
#
# (represented as `dict` in JSON). """
#
#
#        self.occurrenceDateTime = None
#        """ When was assessment made?.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.occurrencePeriod = None
#        """ When was assessment made?.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.parent = None
#        """ Part of this occurrence.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.performer = None
#        """ Who did assessment?.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.prediction = None
#        """ Outcome predicted.
#        List of `RiskAssessmentPrediction` items
#
# (represented as `dict` in JSON). """
#
#
#        self.reasonCode = None
#        """ Why the assessment was necessary?.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.reasonReference = None
#        """ Why the assessment was necessary?.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ registered | preliminary | final | amended +.
#        Type `str`
#
#. """
#
#
#        self.subject = None
#        """ Who/what does assessment apply to?.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(RiskAssessment, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RiskAssessment, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("basis", "basis", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("condition", "condition", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("encounter", "encounter", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("method", "method", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("mitigation", "mitigation", str, {  # #}False, None, {  # #}False),
            ("note", "note", annotation.Annotation, {  # #}True, None, {  # #}False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, {  # #}False, "occurrence", {  # #}False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, {  # #}False, "occurrence", {  # #}False),
            ("parent", "parent", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("performer", "performer", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("prediction", "prediction", RiskAssessmentPrediction, {  # #}True, None, {  # #}False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("subject", "subject", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import range


from . import backboneelement

@dataclass
class RiskAssessmentPrediction(backboneelement.BackboneElement):
    """ Outcome predicted.

    Describes the expected outcome for the subject.
    """
    resource_type: ClassVar[str] = "RiskAssessmentPrediction"
    outcome: Optional[codeableconcept.CodeableConcept] = None
    probabilityDecimal: Optional[float] = None
    probabilityRange: Optional[range.Range] = None
    qualitativeRisk: Optional[codeableconcept.CodeableConcept] = None
    rationale: Optional[str] = None
    relativeRisk: Optional[float] = None
    whenPeriod: Optional[period.Period] = None
    whenRange: Optional[range.Range] = None

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
#        self.outcome = None
#        """ Possible outcome for the subject.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.probabilityDecimal = None
#        """ Likelihood of specified outcome.
#        Type `float`
#
#. """
#
#
#        self.probabilityRange = None
#        """ Likelihood of specified outcome.
#        Type `Range`
#
# (represented as `dict` in JSON). """
#
#
#        self.qualitativeRisk = None
#        """ Likelihood of specified outcome as a qualitative value.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.rationale = None
#        """ Explanation of prediction.
#        Type `str`
#
#. """
#
#
#        self.relativeRisk = None
#        """ Relative likelihood.
#        Type `float`
#
#. """
#
#
#        self.whenPeriod = None
#        """ Timeframe or age range.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.whenRange = None
#        """ Timeframe or age range.
#        Type `Range`
#
# (represented as `dict` in JSON). """
#

#        super(RiskAssessmentPrediction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RiskAssessmentPrediction, self).elementProperties()
        js.extend([
            ("outcome", "outcome", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("probabilityDecimal", "probabilityDecimal", float, {  # #}False, "probability", {  # #}False),
            ("probabilityRange", "probabilityRange", range.Range, {  # #}False, "probability", {  # #}False),
            ("qualitativeRisk", "qualitativeRisk", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("rationale", "rationale", str, {  # #}False, None, {  # #}False),
            ("relativeRisk", "relativeRisk", float, {  # #}False, None, {  # #}False),
            ("whenPeriod", "whenPeriod", period.Period, {  # #}False, "when", {  # #}False),
            ("whenRange", "whenRange", range.Range, {  # #}False, "when", {  # #}False),
        ])
        return js