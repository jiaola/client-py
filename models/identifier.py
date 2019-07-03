#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Identifier) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import element
from . import fhirreference
from . import period


from . import element

@dataclass
class Identifier(element.Element):
    """ An identifier intended for computation.

    An identifier - identifies some entity uniquely and unambiguously.
    Typically this is used for business identifiers.
    """
    resource_type: ClassVar[str] = "Identifier"
    assigner: Optional[fhirreference.FHIRReference] = None
    period: Optional[period.Period] = None
    system: Optional[str] = None
    type: Optional[codeableconcept.CodeableConcept] = None
    use: Optional[str] = None
    value: Optional[str] = None

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
#        self.assigner = None
#        """ Organization that issued id (may be just text).
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.period = None
#        """ Time period when id is/was valid for use.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.system = None
#        """ The namespace for the identifier value.
#        Type `str`
#
#. """
#
#
#        self.type = None
#        """ Description of identifier.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.use = None
#        """ usual | official | temp | secondary | old (If known).
#        Type `str`
#
#. """
#
#
#        self.value = None
#        """ The value that is unique.
#        Type `str`
#
#. """
#

#        super(Identifier, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Identifier, self).elementProperties()
        js.extend([
            ("assigner", "assigner", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("period", "period", period.Period, {  # #}False, None, {  # #}False),
            ("system", "system", str, {  # #}False, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("use", "use", str, {  # #}False, None, {  # #}False),
            ("value", "value", str, {  # #}False, None, {  # #}False),
        ])
        return js