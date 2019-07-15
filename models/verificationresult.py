#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/VerificationResult) on 2019-07-15.
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
from . import signature
from . import timing

from . import domainresource

@dataclass
class VerificationResult(domainresource.DomainResource):
    """ Describes validation requirements, source(s), status and dates for one or
    more elements.
    """
    resource_type: ClassVar[str] = "VerificationResult"
    attestation: Optional[VerificationResultAttestation] = None
    failureAction: Optional[codeableconcept.CodeableConcept] = None
    frequency: Optional[timing.Timing] = None
    lastPerformed: Optional[fhirdate.FHIRDate] = None
    need: Optional[codeableconcept.CodeableConcept] = None
    nextScheduled: Optional[fhirdate.FHIRDate] = None
    primarySource: Optional[List[VerificationResultPrimarySource]] = empty_list()
    status: str = None
    statusDate: Optional[fhirdate.FHIRDate] = None
    target: Optional[List[fhirreference.FHIRReference]] = empty_list()
    targetLocation: Optional[List[str]] = empty_list()
    validationProcess: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    validationType: Optional[codeableconcept.CodeableConcept] = None
    validator: Optional[List[VerificationResultValidator]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(VerificationResult, self).elementProperties()
        js.extend([
            ("attestation", "attestation", VerificationResultAttestation, False, None, False),
            ("failureAction", "failureAction", codeableconcept.CodeableConcept, False, None, False),
            ("frequency", "frequency", timing.Timing, False, None, False),
            ("lastPerformed", "lastPerformed", fhirdate.FHIRDate, False, None, False),
            ("need", "need", codeableconcept.CodeableConcept, False, None, False),
            ("nextScheduled", "nextScheduled", fhirdate.FHIRDate, False, None, False),
            ("primarySource", "primarySource", VerificationResultPrimarySource, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
            ("target", "target", fhirreference.FHIRReference, True, None, False),
            ("targetLocation", "targetLocation", str, True, None, False),
            ("validationProcess", "validationProcess", codeableconcept.CodeableConcept, True, None, False),
            ("validationType", "validationType", codeableconcept.CodeableConcept, False, None, False),
            ("validator", "validator", VerificationResultValidator, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class VerificationResultAttestation(backboneelement.BackboneElement):
    """ Information about the entity attesting to information.
    """
    resource_type: ClassVar[str] = "VerificationResultAttestation"
    communicationMethod: Optional[codeableconcept.CodeableConcept] = None
    date: Optional[fhirdate.FHIRDate] = None
    onBehalfOf: Optional[fhirreference.FHIRReference] = None
    proxyIdentityCertificate: Optional[str] = None
    proxySignature: Optional[signature.Signature] = None
    sourceIdentityCertificate: Optional[str] = None
    sourceSignature: Optional[signature.Signature] = None
    who: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(VerificationResultAttestation, self).elementProperties()
        js.extend([
            ("communicationMethod", "communicationMethod", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
            ("proxyIdentityCertificate", "proxyIdentityCertificate", str, False, None, False),
            ("proxySignature", "proxySignature", signature.Signature, False, None, False),
            ("sourceIdentityCertificate", "sourceIdentityCertificate", str, False, None, False),
            ("sourceSignature", "sourceSignature", signature.Signature, False, None, False),
            ("who", "who", fhirreference.FHIRReference, False, None, False),
        ])
        return js

@dataclass
class VerificationResultPrimarySource(backboneelement.BackboneElement):
    """ Information about the primary source(s) involved in validation.
    """
    resource_type: ClassVar[str] = "VerificationResultPrimarySource"
    canPushUpdates: Optional[codeableconcept.CodeableConcept] = None
    communicationMethod: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    pushTypeAvailable: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    type: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    validationDate: Optional[fhirdate.FHIRDate] = None
    validationStatus: Optional[codeableconcept.CodeableConcept] = None
    who: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(VerificationResultPrimarySource, self).elementProperties()
        js.extend([
            ("canPushUpdates", "canPushUpdates", codeableconcept.CodeableConcept, False, None, False),
            ("communicationMethod", "communicationMethod", codeableconcept.CodeableConcept, True, None, False),
            ("pushTypeAvailable", "pushTypeAvailable", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("validationDate", "validationDate", fhirdate.FHIRDate, False, None, False),
            ("validationStatus", "validationStatus", codeableconcept.CodeableConcept, False, None, False),
            ("who", "who", fhirreference.FHIRReference, False, None, False),
        ])
        return js

@dataclass
class VerificationResultValidator(backboneelement.BackboneElement):
    """ Information about the entity validating information.
    """
    resource_type: ClassVar[str] = "VerificationResultValidator"
    attestationSignature: Optional[signature.Signature] = None
    identityCertificate: Optional[str] = None
    organization:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(VerificationResultValidator, self).elementProperties()
        js.extend([
            ("attestationSignature", "attestationSignature", signature.Signature, False, None, False),
            ("identityCertificate", "identityCertificate", str, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, True),
        ])
        return js


import sys
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
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + '.signature']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']