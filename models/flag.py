#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Flag) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import domainresource
from . import fhirreference
from . import identifier
from . import period


from . import domainresource

@dataclass
class Flag(domainresource.DomainResource):
    """ Key information to flag to healthcare providers.

    Prospective warnings of potential issues when providing care to the
    patient.
    """
    resource_type: ClassVar[str] = "Flag"
    author: Optional[fhirreference.FHIRReference] = None
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    code:codeableconcept.CodeableConcept = None
    encounter: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    period: Optional[period.Period] = None
    status: str = None
    subject:fhirreference.FHIRReference = None

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
#        self.author = None
#        """ Flag creator.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.category = None
#        """ Clinical, administrative, etc..
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.code = None
#        """ Coded or textual message to display to user.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.encounter = None
#        """ Alert relevant during encounter.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Business identifier.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.period = None
#        """ Time period when flag is active.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ active | inactive | entered-in-error.
#        Type `str`
#
#. """
#
#
#        self.subject = None
#        """ Who/What is flag about?.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(Flag, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Flag, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("category", "category", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("encounter", "encounter", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("period", "period", period.Period, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("subject", "subject", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
        ])
        return js