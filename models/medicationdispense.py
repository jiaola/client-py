#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicationDispense) on 2019-07-15.
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
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity

from . import domainresource

@dataclass
class MedicationDispense(domainresource.DomainResource):
    """ Dispensing a medication to a named patient.

    Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """
    resource_type: ClassVar[str] = "MedicationDispense"
    authorizingPrescription: Optional[List[fhirreference.FHIRReference]] = empty_list()
    category: Optional[codeableconcept.CodeableConcept] = None
    context: Optional[fhirreference.FHIRReference] = None
    daysSupply: Optional[quantity.Quantity] = None
    destination: Optional[fhirreference.FHIRReference] = None
    detectedIssue: Optional[List[fhirreference.FHIRReference]] = empty_list()
    dosageInstruction: Optional[List[dosage.Dosage]] = empty_list()
    eventHistory: Optional[List[fhirreference.FHIRReference]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    location: Optional[fhirreference.FHIRReference] = None
    medicationCodeableConcept:codeableconcept.CodeableConcept = None
    medicationReference:fhirreference.FHIRReference = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    partOf: Optional[List[fhirreference.FHIRReference]] = empty_list()
    performer: Optional[List[MedicationDispensePerformer]] = empty_list()
    quantity: Optional[quantity.Quantity] = None
    receiver: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: str = None
    statusReasonCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    statusReasonReference: Optional[fhirreference.FHIRReference] = None
    subject: Optional[fhirreference.FHIRReference] = None
    substitution: Optional[MedicationDispenseSubstitution] = None
    supportingInformation: Optional[List[fhirreference.FHIRReference]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None
    whenHandedOver: Optional[fhirdate.FHIRDate] = None
    whenPrepared: Optional[fhirdate.FHIRDate] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationDispense, self).elementProperties()
        js.extend([
            ("authorizingPrescription", "authorizingPrescription", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("daysSupply", "daysSupply", quantity.Quantity, False, None, False),
            ("destination", "destination", fhirreference.FHIRReference, False, None, False),
            ("detectedIssue", "detectedIssue", fhirreference.FHIRReference, True, None, False),
            ("dosageInstruction", "dosageInstruction", dosage.Dosage, True, None, False),
            ("eventHistory", "eventHistory", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performer", "performer", MedicationDispensePerformer, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("receiver", "receiver", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReasonCodeableConcept", "statusReasonCodeableConcept", codeableconcept.CodeableConcept, False, "statusReason", False),
            ("statusReasonReference", "statusReasonReference", fhirreference.FHIRReference, False, "statusReason", False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("substitution", "substitution", MedicationDispenseSubstitution, False, None, False),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("whenHandedOver", "whenHandedOver", fhirdate.FHIRDate, False, None, False),
            ("whenPrepared", "whenPrepared", fhirdate.FHIRDate, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class MedicationDispensePerformer(backboneelement.BackboneElement):
    """ Who performed event.

    Indicates who or what performed the event.
    """
    resource_type: ClassVar[str] = "MedicationDispensePerformer"
    actor:fhirreference.FHIRReference = None
    function: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationDispensePerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class MedicationDispenseSubstitution(backboneelement.BackboneElement):
    """ Whether a substitution was performed on the dispense.

    Indicates whether or not substitution was made as part of the dispense.  In
    some cases, substitution will be expected but does not happen, in other
    cases substitution is not expected but does happen.  This block explains
    what substitution did or did not happen and why.  If nothing is specified,
    substitution was not done.
    """
    resource_type: ClassVar[str] = "MedicationDispenseSubstitution"
    reason: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    responsibleParty: Optional[List[fhirreference.FHIRReference]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None
    wasSubstituted: bool = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicationDispenseSubstitution, self).elementProperties()
        js.extend([
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("responsibleParty", "responsibleParty", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("wasSubstituted", "wasSubstituted", bool, False, None, True),
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']