#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ResearchSubject) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import domainresource
from . import fhirreference
from . import identifier
from . import period


from . import domainresource

@dataclass
class ResearchSubject(domainresource.DomainResource):
    """ Physical entity which is the primary unit of interest in the study.

    A physical entity which is the primary unit of operational and/or
    administrative interest in a study.
    """
    resource_type: ClassVar[str] = "ResearchSubject"
    actualArm: Optional[str] = None
    assignedArm: Optional[str] = None
    consent: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    individual:fhirreference.FHIRReference = None
    period: Optional[period.Period] = None
    status: str = None
    study:fhirreference.FHIRReference = None

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
#        self.actualArm = None
#        """ What path was followed.
#        Type `str`
#
#. """
#
#
#        self.assignedArm = None
#        """ What path should be followed.
#        Type `str`
#
#. """
#
#
#        self.consent = None
#        """ Agreement to participate in study.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Business Identifier for research subject in a study.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.individual = None
#        """ Who is part of study.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.period = None
#        """ Start and end of participation.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ candidate | eligible | follow-up | ineligible | not-registered |
        off-study | on-study | on-study-intervention | on-study-observation
        | pending-on-study | potential-candidate | screening | withdrawn.
#        Type `str`
#
#. """
#
#
#        self.study = None
#        """ Study subject is part of.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(ResearchSubject, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ResearchSubject, self).elementProperties()
        js.extend([
            ("actualArm", "actualArm", str, {  # #}False, None, {  # #}False),
            ("assignedArm", "assignedArm", str, {  # #}False, None, {  # #}False),
            ("consent", "consent", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("individual", "individual", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("period", "period", period.Period, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("study", "study", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
        ])
        return js