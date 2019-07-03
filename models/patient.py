#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Patient) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import backboneelement
from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import period


from . import domainresource

@dataclass
class Patient(domainresource.DomainResource):
    """ Information about an individual or animal receiving health care services.

    Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """
    resource_type: ClassVar[str] = "Patient"
    active: Optional[bool] = None
    address: Optional[List[address.Address]] = empty_list()
    birthDate: Optional[fhirdate.FHIRDate] = None
    communication: Optional[List[PatientCommunication]] = empty_list()
    contact: Optional[List[PatientContact]] = empty_list()
    deceasedBoolean: Optional[bool] = None
    deceasedDateTime: Optional[fhirdate.FHIRDate] = None
    gender: Optional[str] = None
    generalPractitioner: Optional[List[fhirreference.FHIRReference]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    link: Optional[List[PatientLink]] = empty_list()
    managingOrganization: Optional[fhirreference.FHIRReference] = None
    maritalStatus: Optional[codeableconcept.CodeableConcept] = None
    multipleBirthBoolean: Optional[bool] = None
    multipleBirthInteger: Optional[int] = None
    name: Optional[List[humanname.HumanName]] = empty_list()
    photo: Optional[List[attachment.Attachment]] = empty_list()
    telecom: Optional[List[contactpoint.ContactPoint]] = empty_list()

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
#        """ Whether this patient's record is in active use.
#        Type `bool`
#
#. """
#
#
#        self.address = None
#        """ An address for the individual.
#        List of `Address` items
#
# (represented as `dict` in JSON). """
#
#
#        self.birthDate = None
#        """ The date of birth for the individual.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.communication = None
#        """ A language which may be used to communicate with the patient about
        his or her health.
#        List of `PatientCommunication` items
#
# (represented as `dict` in JSON). """
#
#
#        self.contact = None
#        """ A contact party (e.g. guardian, partner, friend) for the patient.
#        List of `PatientContact` items
#
# (represented as `dict` in JSON). """
#
#
#        self.deceasedBoolean = None
#        """ Indicates if the individual is deceased or not.
#        Type `bool`
#
#. """
#
#
#        self.deceasedDateTime = None
#        """ Indicates if the individual is deceased or not.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.gender = None
#        """ male | female | other | unknown.
#        Type `str`
#
#. """
#
#
#        self.generalPractitioner = None
#        """ Patient's nominated primary care provider.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ An identifier for this patient.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.link = None
#        """ Link to another patient resource that concerns the same actual
        person.
#        List of `PatientLink` items
#
# (represented as `dict` in JSON). """
#
#
#        self.managingOrganization = None
#        """ Organization that is the custodian of the patient record.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.maritalStatus = None
#        """ Marital (civil) status of a patient.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.multipleBirthBoolean = None
#        """ Whether patient is part of a multiple birth.
#        Type `bool`
#
#. """
#
#
#        self.multipleBirthInteger = None
#        """ Whether patient is part of a multiple birth.
#        Type `int`
#
#. """
#
#
#        self.name = None
#        """ A name associated with the patient.
#        List of `HumanName` items
#
# (represented as `dict` in JSON). """
#
#
#        self.photo = None
#        """ Image of the patient.
#        List of `Attachment` items
#
# (represented as `dict` in JSON). """
#
#
#        self.telecom = None
#        """ A contact detail for the individual.
#        List of `ContactPoint` items
#
# (represented as `dict` in JSON). """
#

#        super(Patient, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Patient, self).elementProperties()
        js.extend([
            ("active", "active", bool, {  # #}False, None, {  # #}False),
            ("address", "address", address.Address, {  # #}True, None, {  # #}False),
            ("birthDate", "birthDate", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("communication", "communication", PatientCommunication, {  # #}True, None, {  # #}False),
            ("contact", "contact", PatientContact, {  # #}True, None, {  # #}False),
            ("deceasedBoolean", "deceasedBoolean", bool, {  # #}False, "deceased", {  # #}False),
            ("deceasedDateTime", "deceasedDateTime", fhirdate.FHIRDate, {  # #}False, "deceased", {  # #}False),
            ("gender", "gender", str, {  # #}False, None, {  # #}False),
            ("generalPractitioner", "generalPractitioner", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("link", "link", PatientLink, {  # #}True, None, {  # #}False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("maritalStatus", "maritalStatus", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("multipleBirthBoolean", "multipleBirthBoolean", bool, {  # #}False, "multipleBirth", {  # #}False),
            ("multipleBirthInteger", "multipleBirthInteger", int, {  # #}False, "multipleBirth", {  # #}False),
            ("name", "name", humanname.HumanName, {  # #}True, None, {  # #}False),
            ("photo", "photo", attachment.Attachment, {  # #}True, None, {  # #}False),
            ("telecom", "telecom", contactpoint.ContactPoint, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import backboneelement
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import period


from . import backboneelement

@dataclass
class PatientCommunication(backboneelement.BackboneElement):
    """ A language which may be used to communicate with the patient about his or
    her health.
    """
    resource_type: ClassVar[str] = "PatientCommunication"
    language:codeableconcept.CodeableConcept = None
    preferred: Optional[bool] = None

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
#        self.language = None
#        """ The language which can be used to communicate with the patient
        about his or her health.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.preferred = None
#        """ Language preference indicator.
#        Type `bool`
#
#. """
#

#        super(PatientCommunication, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PatientCommunication, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("preferred", "preferred", bool, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import period


@dataclass
class PatientContact(backboneelement.BackboneElement):
    """ A contact party (e.g. guardian, partner, friend) for the patient.
    """
    resource_type: ClassVar[str] = "PatientContact"
    address: Optional[address.Address] = None
    gender: Optional[str] = None
    name: Optional[humanname.HumanName] = None
    organization: Optional[fhirreference.FHIRReference] = None
    period: Optional[period.Period] = None
    relationship: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    telecom: Optional[List[contactpoint.ContactPoint]] = empty_list()

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
#        self.address = None
#        """ Address for the contact person.
#        Type `Address`
#
# (represented as `dict` in JSON). """
#
#
#        self.gender = None
#        """ male | female | other | unknown.
#        Type `str`
#
#. """
#
#
#        self.name = None
#        """ A name associated with the contact person.
#        Type `HumanName`
#
# (represented as `dict` in JSON). """
#
#
#        self.organization = None
#        """ Organization that is associated with the contact.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.period = None
#        """ The period during which this contact person or organization is
        valid to be contacted relating to this patient.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.relationship = None
#        """ The kind of relationship.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.telecom = None
#        """ A contact detail for the person.
#        List of `ContactPoint` items
#
# (represented as `dict` in JSON). """
#

#        super(PatientContact, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PatientContact, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, {  # #}False, None, {  # #}False),
            ("gender", "gender", str, {  # #}False, None, {  # #}False),
            ("name", "name", humanname.HumanName, {  # #}False, None, {  # #}False),
            ("organization", "organization", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("period", "period", period.Period, {  # #}False, None, {  # #}False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("telecom", "telecom", contactpoint.ContactPoint, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import period


@dataclass
class PatientLink(backboneelement.BackboneElement):
    """ Link to another patient resource that concerns the same actual person.

    Link to another patient resource that concerns the same actual patient.
    """
    resource_type: ClassVar[str] = "PatientLink"
    other:fhirreference.FHIRReference = None
    type: str = None

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
#        self.other = None
#        """ The other patient or related person resource that the link refers
        to.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ replaced-by | replaces | refer | seealso.
#        Type `str`
#
#. """
#

#        super(PatientLink, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PatientLink, self).elementProperties()
        js.extend([
            ("other", "other", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("type", "type", str, {  # #}False, None, {  # #}True),
        ])
        return js