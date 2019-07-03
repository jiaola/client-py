#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Basic) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier


from . import domainresource

@dataclass
class Basic(domainresource.DomainResource):
    """ Resource for non-supported content.

    Basic is used for handling concepts not yet defined in FHIR, narrative-only
    resources that don't map to an existing resource, and custom resources not
    appropriate for inclusion in the FHIR specification.
    """
    resource_type: ClassVar[str] = "Basic"
    author: Optional[fhirreference.FHIRReference] = None
    code:codeableconcept.CodeableConcept = None
    created: Optional[fhirdate.FHIRDate] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    subject: Optional[fhirreference.FHIRReference] = None

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
#        """ Who created.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.code = None
#        """ Kind of Resource.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.created = None
#        """ When created.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.identifier = None
#        """ Business identifier.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.subject = None
#        """ Identifies the focus of this resource.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(Basic, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Basic, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("created", "created", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("subject", "subject", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
        ])
        return js