#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/VerificationResult) on 2019-07-03.
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
#        self.attestation = None
#        """ Information about the entity attesting to information.
#        Type `VerificationResultAttestation`
#
# (represented as `dict` in JSON). """
#
#
#        self.failureAction = None
#        """ fatal | warn | rec-only | none.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.frequency = None
#        """ Frequency of revalidation.
#        Type `Timing`
#
# (represented as `dict` in JSON). """
#
#
#        self.lastPerformed = None
#        """ The date/time validation was last completed (including failed
        validations).
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.need = None
#        """ none | initial | periodic.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.nextScheduled = None
#        """ The date when target is next validated, if appropriate.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.primarySource = None
#        """ Information about the primary source(s) involved in validation.
#        List of `VerificationResultPrimarySource` items
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ attested | validated | in-process | req-revalid | val-fail | reval-
        fail.
#        Type `str`
#
#. """
#
#
#        self.statusDate = None
#        """ When the validation status was updated.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.target = None
#        """ A resource that was validated.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.targetLocation = None
#        """ The fhirpath location(s) within the resource that was validated.
#        List of `str` items
#
#. """
#
#
#        self.validationProcess = None
#        """ The primary process by which the target is validated (edit check;
        value set; primary source; multiple sources; standalone; in
        context).
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.validationType = None
#        """ nothing | primary | multiple.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.validator = None
#        """ Information about the entity validating information.
#        List of `VerificationResultValidator` items
#
# (represented as `dict` in JSON). """
#

#        super(VerificationResult, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(VerificationResult, self).elementProperties()
        js.extend([
            ("attestation", "attestation", VerificationResultAttestation, {  # #}False, None, {  # #}False),
            ("failureAction", "failureAction", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("frequency", "frequency", timing.Timing, {  # #}False, None, {  # #}False),
            ("lastPerformed", "lastPerformed", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("need", "need", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("nextScheduled", "nextScheduled", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("primarySource", "primarySource", VerificationResultPrimarySource, {  # #}True, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("statusDate", "statusDate", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("target", "target", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("targetLocation", "targetLocation", str, {  # #}True, None, {  # #}False),
            ("validationProcess", "validationProcess", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("validationType", "validationType", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("validator", "validator", VerificationResultValidator, {  # #}True, None, {  # #}False),
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
from . import signature
from . import timing


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
#        self.communicationMethod = None
#        """ The method by which attested information was submitted/retrieved.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.date = None
#        """ The date the information was attested to.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.onBehalfOf = None
#        """ When the who is asserting on behalf of another (organization or
        individual).
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.proxyIdentityCertificate = None
#        """ A digital identity certificate associated with the proxy entity
        submitting attested information on behalf of the attestation source.
#        Type `str`
#
#. """
#
#
#        self.proxySignature = None
#        """ Proxy signature.
#        Type `Signature`
#
# (represented as `dict` in JSON). """
#
#
#        self.sourceIdentityCertificate = None
#        """ A digital identity certificate associated with the attestation
        source.
#        Type `str`
#
#. """
#
#
#        self.sourceSignature = None
#        """ Attester signature.
#        Type `Signature`
#
# (represented as `dict` in JSON). """
#
#
#        self.who = None
#        """ The individual or organization attesting to information.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(VerificationResultAttestation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(VerificationResultAttestation, self).elementProperties()
        js.extend([
            ("communicationMethod", "communicationMethod", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("proxyIdentityCertificate", "proxyIdentityCertificate", str, {  # #}False, None, {  # #}False),
            ("proxySignature", "proxySignature", signature.Signature, {  # #}False, None, {  # #}False),
            ("sourceIdentityCertificate", "sourceIdentityCertificate", str, {  # #}False, None, {  # #}False),
            ("sourceSignature", "sourceSignature", signature.Signature, {  # #}False, None, {  # #}False),
            ("who", "who", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import signature
from . import timing


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
#        self.canPushUpdates = None
#        """ yes | no | undetermined.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.communicationMethod = None
#        """ Method for exchanging information with the primary source.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.pushTypeAvailable = None
#        """ specific | any | source.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ Type of primary source (License Board; Primary Education;
        Continuing Education; Postal Service; Relationship owner;
        Registration Authority; legal source; issuing source; authoritative
        source).
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.validationDate = None
#        """ When the target was validated against the primary source.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.validationStatus = None
#        """ successful | failed | unknown.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.who = None
#        """ Reference to the primary source.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(VerificationResultPrimarySource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(VerificationResultPrimarySource, self).elementProperties()
        js.extend([
            ("canPushUpdates", "canPushUpdates", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("communicationMethod", "communicationMethod", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("pushTypeAvailable", "pushTypeAvailable", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("validationDate", "validationDate", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("validationStatus", "validationStatus", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("who", "who", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import signature
from . import timing


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
#        self.attestationSignature = None
#        """ Validator signature.
#        Type `Signature`
#
# (represented as `dict` in JSON). """
#
#
#        self.identityCertificate = None
#        """ A digital identity certificate associated with the validator.
#        Type `str`
#
#. """
#
#
#        self.organization = None
#        """ Reference to the organization validating information.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(VerificationResultValidator, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(VerificationResultValidator, self).elementProperties()
        js.extend([
            ("attestationSignature", "attestationSignature", signature.Signature, {  # #}False, None, {  # #}False),
            ("identityCertificate", "identityCertificate", str, {  # #}False, None, {  # #}False),
            ("organization", "organization", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
        ])
        return js