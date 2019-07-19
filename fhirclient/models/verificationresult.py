#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/VerificationResult) on 2019-07-18.
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
from .signature import Signature
from .timing import Timing


@dataclass
class VerificationResultValidator(BackboneElement):
    """ Information about the entity validating information.
    """
    resource_type: ClassVar[str] = "VerificationResultValidator"
    attestationSignature: Optional[Signature] = None
    identityCertificate: Optional[str] = None
    organization: FHIRReference = None

    def elementProperties(self):
        js = super(VerificationResultValidator, self).elementProperties()
        js.extend([
            ("attestationSignature", "attestationSignature", Signature, False, None, False),
            ("identityCertificate", "identityCertificate", str, False, None, False),
            ("organization", "organization", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class VerificationResultPrimarySource(BackboneElement):
    """ Information about the primary source(s) involved in validation.
    """
    resource_type: ClassVar[str] = "VerificationResultPrimarySource"
    canPushUpdates: Optional[CodeableConcept] = None
    communicationMethod: Optional[List[CodeableConcept]] = empty_list()
    pushTypeAvailable: Optional[List[CodeableConcept]] = empty_list()
    type: Optional[List[CodeableConcept]] = empty_list()
    validationDate: Optional[FHIRDate] = None
    validationStatus: Optional[CodeableConcept] = None
    who: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(VerificationResultPrimarySource, self).elementProperties()
        js.extend([
            ("canPushUpdates", "canPushUpdates", CodeableConcept, False, None, False),
            ("communicationMethod", "communicationMethod", CodeableConcept, True, None, False),
            ("pushTypeAvailable", "pushTypeAvailable", CodeableConcept, True, None, False),
            ("type", "type", CodeableConcept, True, None, False),
            ("validationDate", "validationDate", FHIRDate, False, None, False),
            ("validationStatus", "validationStatus", CodeableConcept, False, None, False),
            ("who", "who", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class VerificationResultAttestation(BackboneElement):
    """ Information about the entity attesting to information.
    """
    resource_type: ClassVar[str] = "VerificationResultAttestation"
    communicationMethod: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None
    onBehalfOf: Optional[FHIRReference] = None
    proxyIdentityCertificate: Optional[str] = None
    proxySignature: Optional[Signature] = None
    sourceIdentityCertificate: Optional[str] = None
    sourceSignature: Optional[Signature] = None
    who: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(VerificationResultAttestation, self).elementProperties()
        js.extend([
            ("communicationMethod", "communicationMethod", CodeableConcept, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("onBehalfOf", "onBehalfOf", FHIRReference, False, None, False),
            ("proxyIdentityCertificate", "proxyIdentityCertificate", str, False, None, False),
            ("proxySignature", "proxySignature", Signature, False, None, False),
            ("sourceIdentityCertificate", "sourceIdentityCertificate", str, False, None, False),
            ("sourceSignature", "sourceSignature", Signature, False, None, False),
            ("who", "who", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class VerificationResult(DomainResource):
    """ Describes validation requirements, source(s), status and dates for one or
    more elements.
    """
    resource_type: ClassVar[str] = "VerificationResult"
    attestation: Optional[VerificationResultAttestation] = None
    failureAction: Optional[CodeableConcept] = None
    frequency: Optional[Timing] = None
    lastPerformed: Optional[FHIRDate] = None
    need: Optional[CodeableConcept] = None
    nextScheduled: Optional[FHIRDate] = None
    primarySource: Optional[List[VerificationResultPrimarySource]] = empty_list()
    status: str = None
    statusDate: Optional[FHIRDate] = None
    target: Optional[List[FHIRReference]] = empty_list()
    targetLocation: Optional[List[str]] = empty_list()
    validationProcess: Optional[List[CodeableConcept]] = empty_list()
    validationType: Optional[CodeableConcept] = None
    validator: Optional[List[VerificationResultValidator]] = empty_list()

    def elementProperties(self):
        js = super(VerificationResult, self).elementProperties()
        js.extend([
            ("attestation", "attestation", VerificationResultAttestation, False, None, False),
            ("failureAction", "failureAction", CodeableConcept, False, None, False),
            ("frequency", "frequency", Timing, False, None, False),
            ("lastPerformed", "lastPerformed", FHIRDate, False, None, False),
            ("need", "need", CodeableConcept, False, None, False),
            ("nextScheduled", "nextScheduled", FHIRDate, False, None, False),
            ("primarySource", "primarySource", VerificationResultPrimarySource, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusDate", "statusDate", FHIRDate, False, None, False),
            ("target", "target", FHIRReference, True, None, False),
            ("targetLocation", "targetLocation", str, True, None, False),
            ("validationProcess", "validationProcess", CodeableConcept, True, None, False),
            ("validationType", "validationType", CodeableConcept, False, None, False),
            ("validator", "validator", VerificationResultValidator, True, None, False),
        ])
        return js