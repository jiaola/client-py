#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicationRequest) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import dosage
from . import duration
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity

from . import backboneelement

@dataclass
class MedicationRequestSubstitution(backboneelement.BackboneElement):
    """ Any restrictions on medication substitution.

    Indicates whether or not substitution can or should be part of the
    dispense. In some cases, substitution must happen, in other cases
    substitution must not happen. This block explains the prescriber's intent.
    If nothing is specified substitution may be done.
    """
    resource_type: ClassVar[str] = "MedicationRequestSubstitution"
    allowedBoolean: bool = None
    allowedCodeableConcept:codeableconcept.CodeableConcept = None
    reason: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationRequestSubstitution, self).elementProperties()
        js.extend([
            ("allowedBoolean", "allowedBoolean", bool, False, "allowed", True),
            ("allowedCodeableConcept", "allowedCodeableConcept", codeableconcept.CodeableConcept, False, "allowed", True),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class MedicationRequestDispenseRequestInitialFill(backboneelement.BackboneElement):
    """ First fill details.

    Indicates the quantity or duration for the first dispense of the
    medication.
    """
    resource_type: ClassVar[str] = "MedicationRequestDispenseRequestInitialFill"
    duration: Optional[duration.Duration] = None
    quantity: Optional[quantity.Quantity] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationRequestDispenseRequestInitialFill, self).elementProperties()
        js.extend([
            ("duration", "duration", duration.Duration, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
        ])
        return js

@dataclass
class MedicationRequestDispenseRequest(backboneelement.BackboneElement):
    """ Medication supply authorization.

    Indicates the specific details for the dispense or medication supply part
    of a medication request (also known as a Medication Prescription or
    Medication Order).  Note that this information is not always sent with the
    order.  There may be in some settings (e.g. hospitals) institutional or
    system support for completing the dispense details in the pharmacy
    department.
    """
    resource_type: ClassVar[str] = "MedicationRequestDispenseRequest"
    dispenseInterval: Optional[duration.Duration] = None
    expectedSupplyDuration: Optional[duration.Duration] = None
    initialFill: Optional[MedicationRequestDispenseRequestInitialFill] = None
    numberOfRepeatsAllowed: Optional[int] = None
    performer: Optional[fhirreference.FHIRReference] = None
    quantity: Optional[quantity.Quantity] = None
    validityPeriod: Optional[period.Period] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationRequestDispenseRequest, self).elementProperties()
        js.extend([
            ("dispenseInterval", "dispenseInterval", duration.Duration, False, None, False),
            ("expectedSupplyDuration", "expectedSupplyDuration", duration.Duration, False, None, False),
            ("initialFill", "initialFill", MedicationRequestDispenseRequestInitialFill, False, None, False),
            ("numberOfRepeatsAllowed", "numberOfRepeatsAllowed", int, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
        ])
        return js

from . import domainresource

@dataclass
class MedicationRequest(domainresource.DomainResource):
    """ Ordering of medication for patient or group.

    An order or request for both supply of the medication and the instructions
    for administration of the medication to a patient. The resource is called
    "MedicationRequest" rather than "MedicationPrescription" or
    "MedicationOrder" to generalize the use across inpatient and outpatient
    settings, including care plans, etc., and to harmonize with workflow
    patterns.
    """
    resource_type: ClassVar[str] = "MedicationRequest"
    authoredOn: Optional[fhirdate.FHIRDate] = None
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    courseOfTherapyType: Optional[codeableconcept.CodeableConcept] = None
    detectedIssue: Optional[List[fhirreference.FHIRReference]] = empty_list()
    dispenseRequest: Optional[MedicationRequestDispenseRequest] = None
    doNotPerform: Optional[bool] = None
    dosageInstruction: Optional[List[dosage.Dosage]] = empty_list()
    encounter: Optional[fhirreference.FHIRReference] = None
    eventHistory: Optional[List[fhirreference.FHIRReference]] = empty_list()
    groupIdentifier: Optional[identifier.Identifier] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    insurance: Optional[List[fhirreference.FHIRReference]] = empty_list()
    intent: str = None
    medicationCodeableConcept:codeableconcept.CodeableConcept = None
    medicationReference:fhirreference.FHIRReference = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    performer: Optional[fhirreference.FHIRReference] = None
    performerType: Optional[codeableconcept.CodeableConcept] = None
    priorPrescription: Optional[fhirreference.FHIRReference] = None
    priority: Optional[str] = None
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    recorder: Optional[fhirreference.FHIRReference] = None
    reportedBoolean: Optional[bool] = None
    reportedReference: Optional[fhirreference.FHIRReference] = None
    requester: Optional[fhirreference.FHIRReference] = None
    status: str = None
    statusReason: Optional[codeableconcept.CodeableConcept] = None
    subject:fhirreference.FHIRReference = None
    substitution: Optional[MedicationRequestSubstitution] = None
    supportingInformation: Optional[List[fhirreference.FHIRReference]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationRequest, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("courseOfTherapyType", "courseOfTherapyType", codeableconcept.CodeableConcept, False, None, False),
            ("detectedIssue", "detectedIssue", fhirreference.FHIRReference, True, None, False),
            ("dispenseRequest", "dispenseRequest", MedicationRequestDispenseRequest, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("dosageInstruction", "dosageInstruction", dosage.Dosage, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("eventHistory", "eventHistory", fhirreference.FHIRReference, True, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, False, None, False),
            ("priorPrescription", "priorPrescription", fhirreference.FHIRReference, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("reportedBoolean", "reportedBoolean", bool, False, "reported", False),
            ("reportedReference", "reportedReference", fhirreference.FHIRReference, False, "reported", False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("substitution", "substitution", MedicationRequestSubstitution, False, None, False),
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
    from . import dosage
except ImportError:
    dosage = sys.modules[__package__ + '.dosage']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
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