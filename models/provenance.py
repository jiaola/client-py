#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Provenance) on 2019-07-03.
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
from . import period
from . import signature


from . import domainresource

@dataclass
class Provenance(domainresource.DomainResource):
    """ Who, What, When for a set of resources.

    Provenance of a resource is a record that describes entities and processes
    involved in producing and delivering or otherwise influencing that
    resource. Provenance provides a critical foundation for assessing
    authenticity, enabling trust, and allowing reproducibility. Provenance
    assertions are a form of contextual metadata and can themselves become
    important records with their own provenance. Provenance statement indicates
    clinical significance in terms of confidence in authenticity, reliability,
    and trustworthiness, integrity, and stage in lifecycle (e.g. Document
    Completion - has the artifact been legally authenticated), all of which may
    impact security, privacy, and trust policies.
    """
    resource_type: ClassVar[str] = "Provenance"
    activity: Optional[codeableconcept.CodeableConcept] = None
    agent: List[ ProvenanceAgent] = empty_list()
    entity: Optional[List[ProvenanceEntity]] = empty_list()
    location: Optional[fhirreference.FHIRReference] = None
    occurredDateTime: Optional[fhirdate.FHIRDate] = None
    occurredPeriod: Optional[period.Period] = None
    policy: Optional[List[str]] = empty_list()
    reason: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    recorded:fhirdate.FHIRDate = None
    signature: Optional[List[signature.Signature]] = empty_list()
    target: List[fhirreference.FHIRReference] = empty_list()

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
#        self.activity = None
#        """ Activity that occurred.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.agent = None
#        """ Actor involved.
#        List of `ProvenanceAgent` items
#
# (represented as `dict` in JSON). """
#
#
#        self.entity = None
#        """ An entity used in this activity.
#        List of `ProvenanceEntity` items
#
# (represented as `dict` in JSON). """
#
#
#        self.location = None
#        """ Where the activity occurred, if relevant.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.occurredDateTime = None
#        """ When the activity occurred.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.occurredPeriod = None
#        """ When the activity occurred.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.policy = None
#        """ Policy or plan the activity was defined by.
#        List of `str` items
#
#. """
#
#
#        self.reason = None
#        """ Reason the activity is occurring.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.recorded = None
#        """ When the activity was recorded / updated.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.signature = None
#        """ Signature on target.
#        List of `Signature` items
#
# (represented as `dict` in JSON). """
#
#
#        self.target = None
#        """ Target Reference(s) (usually version specific).
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#

#        super(Provenance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Provenance, self).elementProperties()
        js.extend([
            ("activity", "activity", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("agent", "agent", ProvenanceAgent, {  # #}True, None, {  # #}True),
            ("entity", "entity", ProvenanceEntity, {  # #}True, None, {  # #}False),
            ("location", "location", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("occurredDateTime", "occurredDateTime", fhirdate.FHIRDate, {  # #}False, "occurred", {  # #}False),
            ("occurredPeriod", "occurredPeriod", period.Period, {  # #}False, "occurred", {  # #}False),
            ("policy", "policy", str, {  # #}True, None, {  # #}False),
            ("reason", "reason", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("recorded", "recorded", fhirdate.FHIRDate, {  # #}False, None, {  # #}True),
            ("signature", "signature", signature.Signature, {  # #}True, None, {  # #}False),
            ("target", "target", fhirreference.FHIRReference, {  # #}True, None, {  # #}True),
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
from . import period
from . import signature


from . import backboneelement

@dataclass
class ProvenanceAgent(backboneelement.BackboneElement):
    """ Actor involved.

    An actor taking a role in an activity  for which it can be assigned some
    degree of responsibility for the activity taking place.
    """
    resource_type: ClassVar[str] = "ProvenanceAgent"
    onBehalfOf: Optional[fhirreference.FHIRReference] = None
    role: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None
    who:fhirreference.FHIRReference = None

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
#        self.onBehalfOf = None
#        """ Who the agent is representing.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.role = None
#        """ What the agents role was.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ How the agent participated.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.who = None
#        """ Who participated.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(ProvenanceAgent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ProvenanceAgent, self).elementProperties()
        js.extend([
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("role", "role", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("who", "who", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import period
from . import signature


@dataclass
class ProvenanceEntity(backboneelement.BackboneElement):
    """ An entity used in this activity.
    """
    resource_type: ClassVar[str] = "ProvenanceEntity"
    agent: Optional[List[ProvenanceAgent]] = empty_list()
    role: str = None
    what:fhirreference.FHIRReference = None

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
#        self.agent = None
#        """ Entity is attributed to this agent.
#        List of `ProvenanceAgent` items
#
# (represented as `dict` in JSON). """
#
#
#        self.role = None
#        """ derivation | revision | quotation | source | removal.
#        Type `str`
#
#. """
#
#
#        self.what = None
#        """ Identity of entity.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(ProvenanceEntity, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ProvenanceEntity, self).elementProperties()
        js.extend([
            ("agent", "agent", ProvenanceAgent, {  # #}True, None, {  # #}False),
            ("role", "role", str, {  # #}False, None, {  # #}True),
            ("what", "what", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
        ])
        return js