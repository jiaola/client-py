#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CareTeam) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirreference
from . import identifier
from . import period

from . import domainresource

@dataclass
class CareTeam(domainresource.DomainResource):
    """ Planned participants in the coordination and delivery of care for a patient
    or group.

    The Care Team includes all the people and organizations who plan to
    participate in the coordination and delivery of care for a patient.
    """
    resource_type: ClassVar[str] = "CareTeam"
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    encounter: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    managingOrganization: Optional[List[fhirreference.FHIRReference]] = empty_list()
    name: Optional[str] = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    participant: Optional[List[CareTeamParticipant]] = empty_list()
    period: Optional[period.Period] = None
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: Optional[str] = None
    subject: Optional[fhirreference.FHIRReference] = None
    telecom: Optional[List[contactpoint.ContactPoint]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CareTeam, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, True, None, False),
            ("name", "name", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("participant", "participant", CareTeamParticipant, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class CareTeamParticipant(backboneelement.BackboneElement):
    """ Members of the team.

    Identifies all people and organizations who are expected to be involved in
    the care team.
    """
    resource_type: ClassVar[str] = "CareTeamParticipant"
    member: Optional[fhirreference.FHIRReference] = None
    onBehalfOf: Optional[fhirreference.FHIRReference] = None
    period: Optional[period.Period] = None
    role: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CareTeamParticipant, self).elementProperties()
        js.extend([
            ("member", "member", fhirreference.FHIRReference, False, None, False),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, True, None, False),
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
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
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