#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/HealthcareService) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import backboneelement
from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period


from . import domainresource

@dataclass
class HealthcareService(domainresource.DomainResource):
    """ The details of a healthcare service available at a location.
    """
    resource_type: ClassVar[str] = "HealthcareService"
    active: Optional[bool] = None
    appointmentRequired: Optional[bool] = None
    availabilityExceptions: Optional[str] = None
    availableTime: Optional[List[HealthcareServiceAvailableTime]] = empty_list()
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    characteristic: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    comment: Optional[str] = None
    communication: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    coverageArea: Optional[List[fhirreference.FHIRReference]] = empty_list()
    eligibility: Optional[List[HealthcareServiceEligibility]] = empty_list()
    endpoint: Optional[List[fhirreference.FHIRReference]] = empty_list()
    extraDetails: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    location: Optional[List[fhirreference.FHIRReference]] = empty_list()
    name: Optional[str] = None
    notAvailable: Optional[List[HealthcareServiceNotAvailable]] = empty_list()
    photo: Optional[attachment.Attachment] = None
    program: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    providedBy: Optional[fhirreference.FHIRReference] = None
    referralMethod: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    serviceProvisionCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    specialty: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    telecom: Optional[List[contactpoint.ContactPoint]] = empty_list()
    type: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

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
#        self.active = None
#        """ Whether this HealthcareService record is in active use.
#        Type `bool`
#
#. """
#
#
#        self.appointmentRequired = None
#        """ If an appointment is required for access to this service.
#        Type `bool`
#
#. """
#
#
#        self.availabilityExceptions = None
#        """ Description of availability exceptions.
#        Type `str`
#
#. """
#
#
#        self.availableTime = None
#        """ Times the Service Site is available.
#        List of `HealthcareServiceAvailableTime` items
#
# (represented as `dict` in JSON). """
#
#
#        self.category = None
#        """ Broad category of service being performed or delivered.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.characteristic = None
#        """ Collection of characteristics (attributes).
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.comment = None
#        """ Additional description and/or any specific issues not covered
        elsewhere.
#        Type `str`
#
#. """
#
#
#        self.communication = None
#        """ The language that this service is offered in.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.coverageArea = None
#        """ Location(s) service is intended for/available to.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.eligibility = None
#        """ Specific eligibility requirements required to use the service.
#        List of `HealthcareServiceEligibility` items
#
# (represented as `dict` in JSON). """
#
#
#        self.endpoint = None
#        """ Technical endpoints providing access to electronic services
        operated for the healthcare service.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.extraDetails = None
#        """ Extra details about the service that can't be placed in the other
        fields.
#        Type `str`
#
#. """
#
#
#        self.identifier = None
#        """ External identifiers for this item.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.location = None
#        """ Location(s) where service may be provided.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.name = None
#        """ Description of service as presented to a consumer while searching.
#        Type `str`
#
#. """
#
#
#        self.notAvailable = None
#        """ Not available during this time due to provided reason.
#        List of `HealthcareServiceNotAvailable` items
#
# (represented as `dict` in JSON). """
#
#
#        self.photo = None
#        """ Facilitates quick identification of the service.
#        Type `Attachment`
#
# (represented as `dict` in JSON). """
#
#
#        self.program = None
#        """ Programs that this service is applicable to.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.providedBy = None
#        """ Organization that provides this service.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.referralMethod = None
#        """ Ways that the service accepts referrals.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.serviceProvisionCode = None
#        """ Conditions under which service is available/offered.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.specialty = None
#        """ Specialties handled by the HealthcareService.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.telecom = None
#        """ Contacts related to the healthcare service.
#        List of `ContactPoint` items
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ Type of service that may be delivered or performed.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#

#        super(HealthcareService, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(HealthcareService, self).elementProperties()
        js.extend([
            ("active", "active", bool, {  # #}False, None, {  # #}False),
            ("appointmentRequired", "appointmentRequired", bool, {  # #}False, None, {  # #}False),
            ("availabilityExceptions", "availabilityExceptions", str, {  # #}False, None, {  # #}False),
            ("availableTime", "availableTime", HealthcareServiceAvailableTime, {  # #}True, None, {  # #}False),
            ("category", "category", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("characteristic", "characteristic", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("comment", "comment", str, {  # #}False, None, {  # #}False),
            ("communication", "communication", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("eligibility", "eligibility", HealthcareServiceEligibility, {  # #}True, None, {  # #}False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("extraDetails", "extraDetails", str, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("location", "location", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("name", "name", str, {  # #}False, None, {  # #}False),
            ("notAvailable", "notAvailable", HealthcareServiceNotAvailable, {  # #}True, None, {  # #}False),
            ("photo", "photo", attachment.Attachment, {  # #}False, None, {  # #}False),
            ("program", "program", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("providedBy", "providedBy", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("referralMethod", "referralMethod", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("serviceProvisionCode", "serviceProvisionCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("telecom", "telecom", contactpoint.ContactPoint, {  # #}True, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import backboneelement
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period


from . import backboneelement

@dataclass
class HealthcareServiceAvailableTime(backboneelement.BackboneElement):
    """ Times the Service Site is available.

    A collection of times that the Service Site is available.
    """
    resource_type: ClassVar[str] = "HealthcareServiceAvailableTime"
    allDay: Optional[bool] = None
    availableEndTime: Optional[fhirdate.FHIRDate] = None
    availableStartTime: Optional[fhirdate.FHIRDate] = None
    daysOfWeek: Optional[List[str]] = empty_list()

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
#        self.allDay = None
#        """ Always available? e.g. 24 hour service.
#        Type `bool`
#
#. """
#
#
#        self.availableEndTime = None
#        """ Closing time of day (ignored if allDay = true).
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.availableStartTime = None
#        """ Opening time of day (ignored if allDay = true).
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.daysOfWeek = None
#        """ mon | tue | wed | thu | fri | sat | sun.
#        List of `str` items
#
#. """
#

#        super(HealthcareServiceAvailableTime, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(HealthcareServiceAvailableTime, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, {  # #}False, None, {  # #}False),
            ("availableEndTime", "availableEndTime", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("availableStartTime", "availableStartTime", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("daysOfWeek", "daysOfWeek", str, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period


@dataclass
class HealthcareServiceEligibility(backboneelement.BackboneElement):
    """ Specific eligibility requirements required to use the service.

    Does this service have specific eligibility requirements that need to be
    met in order to use the service?
    """
    resource_type: ClassVar[str] = "HealthcareServiceEligibility"
    code: Optional[codeableconcept.CodeableConcept] = None
    comment: Optional[str] = None

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
#        self.code = None
#        """ Coded value for the eligibility.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.comment = None
#        """ Describes the eligibility conditions for the service.
#        Type `str`
#
#. """
#

#        super(HealthcareServiceEligibility, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(HealthcareServiceEligibility, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("comment", "comment", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period


@dataclass
class HealthcareServiceNotAvailable(backboneelement.BackboneElement):
    """ Not available during this time due to provided reason.

    The HealthcareService is not available during this period of time due to
    the provided reason.
    """
    resource_type: ClassVar[str] = "HealthcareServiceNotAvailable"
    description: str = None
    during: Optional[period.Period] = None

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
#        self.description = None
#        """ Reason presented to the user explaining why time not available.
#        Type `str`
#
#. """
#
#
#        self.during = None
#        """ Service not available from this date.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#

#        super(HealthcareServiceNotAvailable, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(HealthcareServiceNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, {  # #}False, None, {  # #}True),
            ("during", "during", period.Period, {  # #}False, None, {  # #}False),
        ])
        return js