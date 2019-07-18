#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicationAdministration) on 2019-07-18.
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
from . import quantity
from . import ratio

from . import backboneelement

@dataclass
class MedicationAdministrationPerformer(backboneelement.BackboneElement):
    """ Who performed the medication administration and what they did.

    Indicates who or what performed the medication administration and how they
    were involved.
    """
    resource_type: ClassVar[str] = "MedicationAdministrationPerformer"
    actor:fhirreference.FHIRReference = None
    function: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationAdministrationPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class MedicationAdministrationDosage(backboneelement.BackboneElement):
    """ Details of how medication was taken.

    Describes the medication dosage information details e.g. dose, rate, site,
    route, etc.
    """
    resource_type: ClassVar[str] = "MedicationAdministrationDosage"
    dose: Optional[quantity.Quantity] = None
    method: Optional[codeableconcept.CodeableConcept] = None
    rateQuantity: Optional[quantity.Quantity] = None
    rateRatio: Optional[ratio.Ratio] = None
    route: Optional[codeableconcept.CodeableConcept] = None
    site: Optional[codeableconcept.CodeableConcept] = None
    text: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationAdministrationDosage, self).elementProperties()
        js.extend([
            ("dose", "dose", quantity.Quantity, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("site", "site", codeableconcept.CodeableConcept, False, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js

from . import domainresource

@dataclass
class MedicationAdministration(domainresource.DomainResource):
    """ Administration of medication to a patient.

    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """
    resource_type: ClassVar[str] = "MedicationAdministration"
    category: Optional[codeableconcept.CodeableConcept] = None
    context: Optional[fhirreference.FHIRReference] = None
    device: Optional[List[fhirreference.FHIRReference]] = empty_list()
    dosage: Optional[MedicationAdministrationDosage] = None
    effectiveDateTime:fhirdate.FHIRDate = None
    effectivePeriod:period.Period = None
    eventHistory: Optional[List[fhirreference.FHIRReference]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    instantiates: Optional[List[str]] = empty_list()
    medicationCodeableConcept:codeableconcept.CodeableConcept = None
    medicationReference:fhirreference.FHIRReference = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    partOf: Optional[List[fhirreference.FHIRReference]] = empty_list()
    performer: Optional[List[MedicationAdministrationPerformer]] = empty_list()
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    request: Optional[fhirreference.FHIRReference] = None
    status: str = None
    statusReason: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    subject:fhirreference.FHIRReference = None
    supportingInformation: Optional[List[fhirreference.FHIRReference]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationAdministration, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("device", "device", fhirreference.FHIRReference, True, None, False),
            ("dosage", "dosage", MedicationAdministrationDosage, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdate.FHIRDate, False, "effective", True),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", True),
            ("eventHistory", "eventHistory", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiates", "instantiates", str, True, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performer", "performer", MedicationAdministrationPerformer, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']