#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Consent) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import backboneelement
from . import codeableconcept
from . import coding
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period

from . import domainresource

@dataclass
class Consent(domainresource.DomainResource):
    """ A healthcare consumer's  choices to permit or deny recipients or roles to
    perform actions for specific purposes and periods of time.

    A record of a healthcare consumer’s  choices, which permits or denies
    identified recipient(s) or recipient role(s) to perform one or more actions
    within a given policy context, for specific purposes and periods of time.
    """
    resource_type: ClassVar[str] = "Consent"
    category: List[codeableconcept.CodeableConcept] = empty_list()
    dateTime: Optional[fhirdate.FHIRDate] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    organization: Optional[List[fhirreference.FHIRReference]] = empty_list()
    patient: Optional[fhirreference.FHIRReference] = None
    performer: Optional[List[fhirreference.FHIRReference]] = empty_list()
    policy: Optional[List[ConsentPolicy]] = empty_list()
    policyRule: Optional[codeableconcept.CodeableConcept] = None
    provision: Optional[ConsentProvision] = None
    scope:codeableconcept.CodeableConcept = None
    sourceAttachment: Optional[attachment.Attachment] = None
    sourceReference: Optional[fhirreference.FHIRReference] = None
    status: str = None
    verification: Optional[List[ConsentVerification]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Consent, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, True, None, True),
            ("dateTime", "dateTime", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("policy", "policy", ConsentPolicy, True, None, False),
            ("policyRule", "policyRule", codeableconcept.CodeableConcept, False, None, False),
            ("provision", "provision", ConsentProvision, False, None, False),
            ("scope", "scope", codeableconcept.CodeableConcept, False, None, True),
            ("sourceAttachment", "sourceAttachment", attachment.Attachment, False, "source", False),
            ("sourceReference", "sourceReference", fhirreference.FHIRReference, False, "source", False),
            ("status", "status", str, False, None, True),
            ("verification", "verification", ConsentVerification, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class ConsentPolicy(backboneelement.BackboneElement):
    """ Policies covered by this consent.

    The references to the policies that are included in this consent scope.
    Policies may be organizational, but are often defined jurisdictionally, or
    in law.
    """
    resource_type: ClassVar[str] = "ConsentPolicy"
    authority: Optional[str] = None
    uri: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ConsentPolicy, self).elementProperties()
        js.extend([
            ("authority", "authority", str, False, None, False),
            ("uri", "uri", str, False, None, False),
        ])
        return js

@dataclass
class ConsentProvision(backboneelement.BackboneElement):
    """ Constraints to the base Consent.policyRule.

    An exception to the base policy of this consent. An exception can be an
    addition or removal of access permissions.
    """
    resource_type: ClassVar[str] = "ConsentProvision"
    action: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    actor: Optional[List[ConsentProvisionActor]] = empty_list()
    class_fhir: Optional[List[coding.Coding]] = empty_list()
    code: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    data: Optional[List[ConsentProvisionData]] = empty_list()
    dataPeriod: Optional[period.Period] = None
    period: Optional[period.Period] = None
    provision: Optional[List[ConsentProvision]] = empty_list()
    purpose: Optional[List[coding.Coding]] = empty_list()
    securityLabel: Optional[List[coding.Coding]] = empty_list()
    type: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ConsentProvision, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, True, None, False),
            ("actor", "actor", ConsentProvisionActor, True, None, False),
            ("class_fhir", "class", coding.Coding, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("data", "data", ConsentProvisionData, True, None, False),
            ("dataPeriod", "dataPeriod", period.Period, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("provision", "provision", ConsentProvision, True, None, False),
            ("purpose", "purpose", coding.Coding, True, None, False),
            ("securityLabel", "securityLabel", coding.Coding, True, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js

@dataclass
class ConsentProvisionActor(backboneelement.BackboneElement):
    """ Who|what controlled by this rule (or group, by role).

    Who or what is controlled by this rule. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """
    resource_type: ClassVar[str] = "ConsentProvisionActor"
    reference:fhirreference.FHIRReference = None
    role:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ConsentProvisionActor, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class ConsentProvisionData(backboneelement.BackboneElement):
    """ Data controlled by this rule.

    The resources controlled by this rule if specific resources are referenced.
    """
    resource_type: ClassVar[str] = "ConsentProvisionData"
    meaning: str = None
    reference:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ConsentProvisionData, self).elementProperties()
        js.extend([
            ("meaning", "meaning", str, False, None, True),
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
        ])
        return js

@dataclass
class ConsentVerification(backboneelement.BackboneElement):
    """ Consent Verified by patient or family.

    Whether a treatment instruction (e.g. artificial respiration yes or no) was
    verified with the patient, his/her family or another authorized person.
    """
    resource_type: ClassVar[str] = "ConsentVerification"
    verificationDate: Optional[fhirdate.FHIRDate] = None
    verified: bool = None
    verifiedWith: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ConsentVerification, self).elementProperties()
        js.extend([
            ("verificationDate", "verificationDate", fhirdate.FHIRDate, False, None, False),
            ("verified", "verified", bool, False, None, True),
            ("verifiedWith", "verifiedWith", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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