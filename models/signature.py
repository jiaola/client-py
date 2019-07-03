#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Signature) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import coding
from . import element
from . import fhirdate
from . import fhirreference


from . import element

@dataclass
class Signature(element.Element):
    """ A Signature - XML DigSig, JWS, Graphical image of signature, etc..

    A signature along with supporting context. The signature may be a digital
    signature that is cryptographic in nature, or some other signature
    acceptable to the domain. This other signature may be as simple as a
    graphical image representing a hand-written signature, or a signature
    ceremony Different signature approaches have different utilities.
    """
    resource_type: ClassVar[str] = "Signature"
    data: Optional[str] = None
    onBehalfOf: Optional[fhirreference.FHIRReference] = None
    sigFormat: Optional[str] = None
    targetFormat: Optional[str] = None
    type: List[coding.Coding] = empty_list()
    when:fhirdate.FHIRDate = None
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
#        self.data = None
#        """ The actual signature content (XML DigSig. JWS, picture, etc.).
#        Type `str`
#
#. """
#
#
#        self.onBehalfOf = None
#        """ The party represented.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.sigFormat = None
#        """ The technical format of the signature.
#        Type `str`
#
#. """
#
#
#        self.targetFormat = None
#        """ The technical format of the signed resources.
#        Type `str`
#
#. """
#
#
#        self.type = None
#        """ Indication of the reason the entity signed the object(s).
#        List of `Coding` items
#
# (represented as `dict` in JSON). """
#
#
#        self.when = None
#        """ When the signature was created.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.who = None
#        """ Who signed.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(Signature, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Signature, self).elementProperties()
        js.extend([
            ("data", "data", str, {  # #}False, None, {  # #}False),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("sigFormat", "sigFormat", str, {  # #}False, None, {  # #}False),
            ("targetFormat", "targetFormat", str, {  # #}False, None, {  # #}False),
            ("type", "type", coding.Coding, {  # #}True, None, {  # #}True),
            ("when", "when", fhirdate.FHIRDate, {  # #}False, None, {  # #}True),
            ("who", "who", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
        ])
        return js