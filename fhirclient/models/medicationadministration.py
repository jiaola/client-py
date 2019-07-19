#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicationAdministration) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .ratio import Ratio


@dataclass
class MedicationAdministrationPerformer(BackboneElement):
    """ Who performed the medication administration and what they did.

    Indicates who or what performed the medication administration and how they
    were involved.
    """
    resource_type: ClassVar[str] = "MedicationAdministrationPerformer"
    actor: FHIRReference = None
    function: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(MedicationAdministrationPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", FHIRReference, False, None, True),
            ("function", "function", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class MedicationAdministrationDosage(BackboneElement):
    """ Details of how medication was taken.

    Describes the medication dosage information details e.g. dose, rate, site,
    route, etc.
    """
    resource_type: ClassVar[str] = "MedicationAdministrationDosage"
    dose: Optional[Quantity] = None
    method: Optional[CodeableConcept] = None
    rateQuantity: Optional[Quantity] = None
    rateRatio: Optional[Ratio] = None
    route: Optional[CodeableConcept] = None
    site: Optional[CodeableConcept] = None
    text: Optional[str] = None

    def elementProperties(self):
        js = super(MedicationAdministrationDosage, self).elementProperties()
        js.extend([
            ("dose", "dose", Quantity, False, None, False),
            ("method", "method", CodeableConcept, False, None, False),
            ("rateQuantity", "rateQuantity", Quantity, False, "rate", False),
            ("rateRatio", "rateRatio", Ratio, False, "rate", False),
            ("route", "route", CodeableConcept, False, None, False),
            ("site", "site", CodeableConcept, False, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js


@dataclass
class MedicationAdministration(DomainResource):
    """ Administration of medication to a patient.

    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """
    resource_type: ClassVar[str] = "MedicationAdministration"
    category: Optional[CodeableConcept] = None
    context: Optional[FHIRReference] = None
    device: Optional[List[FHIRReference]] = empty_list()
    dosage: Optional[MedicationAdministrationDosage] = None
    effectiveDateTime: FHIRDate = None
    effectivePeriod: Period = None
    eventHistory: Optional[List[FHIRReference]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    instantiates: Optional[List[str]] = empty_list()
    medicationCodeableConcept: CodeableConcept = None
    medicationReference: FHIRReference = None
    note: Optional[List[Annotation]] = empty_list()
    partOf: Optional[List[FHIRReference]] = empty_list()
    performer: Optional[List[MedicationAdministrationPerformer]] = empty_list()
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    request: Optional[FHIRReference] = None
    status: str = None
    statusReason: Optional[List[CodeableConcept]] = empty_list()
    subject: FHIRReference = None
    supportingInformation: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(MedicationAdministration, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, False),
            ("context", "context", FHIRReference, False, None, False),
            ("device", "device", FHIRReference, True, None, False),
            ("dosage", "dosage", MedicationAdministrationDosage, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", FHIRDate, False, "effective", True),
            ("effectivePeriod", "effectivePeriod", Period, False, "effective", True),
            ("eventHistory", "eventHistory", FHIRReference, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiates", "instantiates", str, True, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", FHIRReference, False, "medication", True),
            ("note", "note", Annotation, True, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("performer", "performer", MedicationAdministrationPerformer, True, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("request", "request", FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", CodeableConcept, True, None, False),
            ("subject", "subject", FHIRReference, False, None, True),
            ("supportingInformation", "supportingInformation", FHIRReference, True, None, False),
        ])
        return js