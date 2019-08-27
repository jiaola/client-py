#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/AdverseEvent) on 2019-08-26.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class AdverseEventSuspectEntityCausality(BackboneElement):
    """ Information on the possible cause of the event.
    """
    resource_type: ClassVar[str] = "AdverseEventSuspectEntityCausality"

    assessmentMethod: Optional[CodeableConcept] = None
    entityRelatedness: Optional[CodeableConcept] = None
    author: Optional[FHIRReference] = None


@dataclass
class AdverseEventSuspectEntity(BackboneElement):
    """ The suspected agent causing the adverse event.

    Describes the entity that is suspected to have caused the adverse event.
    """
    resource_type: ClassVar[str] = "AdverseEventSuspectEntity"

    instanceCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='instance',))
    instanceReference: FHIRReference = field(default=None, metadata=dict(one_of_many='instance',))
    causality: Optional[List[AdverseEventSuspectEntityCausality]] = None


@dataclass
class AdverseEventSupportingInfo(BackboneElement):
    """ Supporting information relevant to the event.
    """
    resource_type: ClassVar[str] = "AdverseEventSupportingInfo"

    item: FHIRReference = None
    contributingFactor: Optional[bool] = None


@dataclass
class AdverseEvent(DomainResource):
    """ Medical care, research study or other healthcare event causing physical
    injury.

    An event (i.e. any change to current patient status) that may be related to
    unintended effects on a patient or research subject.  The unintended
    effects may require additional monitoring, treatment or hospitalization or
    may result in death.  The AdverseEvent resource also extends to potential
    or avoided events that could have had such effects.
    """
    resource_type: ClassVar[str] = "AdverseEvent"

    identifier: Optional[List[Identifier]] = None
    actuality: str = None
    category: Optional[List[CodeableConcept]] = None
    code: Optional[CodeableConcept] = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    detected: Optional[FHIRDate] = None
    recordedDate: Optional[FHIRDate] = None
    resultingCondition: Optional[List[FHIRReference]] = None
    location: Optional[FHIRReference] = None
    seriousness: Optional[CodeableConcept] = None
    severity: Optional[CodeableConcept] = None
    outcome: Optional[CodeableConcept] = None
    recorder: Optional[FHIRReference] = None
    contributor: Optional[List[FHIRReference]] = None
    detector: Optional[List[FHIRReference]] = None
    suspectEntity: Optional[List[AdverseEventSuspectEntity]] = None
    supportingInfo: Optional[List[AdverseEventSupportingInfo]] = None
    study: Optional[List[FHIRReference]] = None