#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Immunization) on 2019-07-18.
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
from .quantity import Quantity


@dataclass
class ImmunizationReaction(BackboneElement):
    """ Details of a reaction that follows immunization.

    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """
    resource_type: ClassVar[str] = "ImmunizationReaction"
    date: Optional[FHIRDate] = None
    detail: Optional[FHIRReference] = None
    reported: Optional[bool] = None

    def elementProperties(self):
        js = super(ImmunizationReaction, self).elementProperties()
        js.extend([
            ("date", "date", FHIRDate, False, None, False),
            ("detail", "detail", FHIRReference, False, None, False),
            ("reported", "reported", bool, False, None, False),
        ])
        return js


@dataclass
class ImmunizationProtocolApplied(BackboneElement):
    """ Protocol followed by the provider.

    The protocol (set of recommendations) being followed by the provider who
    administered the dose.
    """
    resource_type: ClassVar[str] = "ImmunizationProtocolApplied"
    authority: Optional[FHIRReference] = None
    doseNumberPositiveInt: int = None
    doseNumberString: str = None
    series: Optional[str] = None
    seriesDosesPositiveInt: Optional[int] = None
    seriesDosesString: Optional[str] = None
    targetDisease: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(ImmunizationProtocolApplied, self).elementProperties()
        js.extend([
            ("authority", "authority", FHIRReference, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", True),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", True),
            ("series", "series", str, False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("targetDisease", "targetDisease", CodeableConcept, True, None, False),
        ])
        return js


@dataclass
class ImmunizationPerformer(BackboneElement):
    """ Who performed event.

    Indicates who performed the immunization event.
    """
    resource_type: ClassVar[str] = "ImmunizationPerformer"
    actor: FHIRReference = None
    function: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ImmunizationPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", FHIRReference, False, None, True),
            ("function", "function", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ImmunizationEducation(BackboneElement):
    """ Educational material presented to patient.

    Educational material presented to the patient (or guardian) at the time of
    vaccine administration.
    """
    resource_type: ClassVar[str] = "ImmunizationEducation"
    documentType: Optional[str] = None
    presentationDate: Optional[FHIRDate] = None
    publicationDate: Optional[FHIRDate] = None
    reference: Optional[str] = None

    def elementProperties(self):
        js = super(ImmunizationEducation, self).elementProperties()
        js.extend([
            ("documentType", "documentType", str, False, None, False),
            ("presentationDate", "presentationDate", FHIRDate, False, None, False),
            ("publicationDate", "publicationDate", FHIRDate, False, None, False),
            ("reference", "reference", str, False, None, False),
        ])
        return js


@dataclass
class Immunization(DomainResource):
    """ Immunization event information.

    Describes the event of a patient being administered a vaccine or a record
    of an immunization as reported by a patient, a clinician or another party.
    """
    resource_type: ClassVar[str] = "Immunization"
    doseQuantity: Optional[Quantity] = None
    education: Optional[List[ImmunizationEducation]] = empty_list()
    encounter: Optional[FHIRReference] = None
    expirationDate: Optional[FHIRDate] = None
    fundingSource: Optional[CodeableConcept] = None
    identifier: Optional[List[Identifier]] = empty_list()
    isSubpotent: Optional[bool] = None
    location: Optional[FHIRReference] = None
    lotNumber: Optional[str] = None
    manufacturer: Optional[FHIRReference] = None
    note: Optional[List[Annotation]] = empty_list()
    occurrenceDateTime: FHIRDate = None
    occurrenceString: str = None
    patient: FHIRReference = None
    performer: Optional[List[ImmunizationPerformer]] = empty_list()
    primarySource: Optional[bool] = None
    programEligibility: Optional[List[CodeableConcept]] = empty_list()
    protocolApplied: Optional[List[ImmunizationProtocolApplied]] = empty_list()
    reaction: Optional[List[ImmunizationReaction]] = empty_list()
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    recorded: Optional[FHIRDate] = None
    reportOrigin: Optional[CodeableConcept] = None
    route: Optional[CodeableConcept] = None
    site: Optional[CodeableConcept] = None
    status: str = None
    statusReason: Optional[CodeableConcept] = None
    subpotentReason: Optional[List[CodeableConcept]] = empty_list()
    vaccineCode: CodeableConcept = None

    def elementProperties(self):
        js = super(Immunization, self).elementProperties()
        js.extend([
            ("doseQuantity", "doseQuantity", Quantity, False, None, False),
            ("education", "education", ImmunizationEducation, True, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("expirationDate", "expirationDate", FHIRDate, False, None, False),
            ("fundingSource", "fundingSource", CodeableConcept, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("isSubpotent", "isSubpotent", bool, False, None, False),
            ("location", "location", FHIRReference, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("manufacturer", "manufacturer", FHIRReference, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", FHIRDate, False, "occurrence", True),
            ("occurrenceString", "occurrenceString", str, False, "occurrence", True),
            ("patient", "patient", FHIRReference, False, None, True),
            ("performer", "performer", ImmunizationPerformer, True, None, False),
            ("primarySource", "primarySource", bool, False, None, False),
            ("programEligibility", "programEligibility", CodeableConcept, True, None, False),
            ("protocolApplied", "protocolApplied", ImmunizationProtocolApplied, True, None, False),
            ("reaction", "reaction", ImmunizationReaction, True, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("recorded", "recorded", FHIRDate, False, None, False),
            ("reportOrigin", "reportOrigin", CodeableConcept, False, None, False),
            ("route", "route", CodeableConcept, False, None, False),
            ("site", "site", CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", CodeableConcept, False, None, False),
            ("subpotentReason", "subpotentReason", CodeableConcept, True, None, False),
            ("vaccineCode", "vaccineCode", CodeableConcept, False, None, True),
        ])
        return js