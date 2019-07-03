#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/EnrollmentResponse) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier


from . import domainresource

@dataclass
class EnrollmentResponse(domainresource.DomainResource):
    """ EnrollmentResponse resource.

    This resource provides enrollment and plan details from the processing of
    an EnrollmentRequest resource.
    """
    resource_type: ClassVar[str] = "EnrollmentResponse"
    created: Optional[fhirdate.FHIRDate] = None
    disposition: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    organization: Optional[fhirreference.FHIRReference] = None
    outcome: Optional[str] = None
    request: Optional[fhirreference.FHIRReference] = None
    requestProvider: Optional[fhirreference.FHIRReference] = None
    status: Optional[str] = None

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
#        self.created = None
#        """ Creation date.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.disposition = None
#        """ Disposition Message.
#        Type `str`
#
#. """
#
#
#        self.identifier = None
#        """ Business Identifier.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.organization = None
#        """ Insurer.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.outcome = None
#        """ queued | complete | error | partial.
#        Type `str`
#
#. """
#
#
#        self.request = None
#        """ Claim reference.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.requestProvider = None
#        """ Responsible practitioner.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ active | cancelled | draft | entered-in-error.
#        Type `str`
#
#. """
#

#        super(EnrollmentResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EnrollmentResponse, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("disposition", "disposition", str, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("organization", "organization", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("outcome", "outcome", str, {  # #}False, None, {  # #}False),
            ("request", "request", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}False),
        ])
        return js