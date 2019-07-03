#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Account) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirreference
from . import identifier
from . import period


from . import domainresource

@dataclass
class Account(domainresource.DomainResource):
    """ Tracks balance, charges, for patient or cost center.

    A financial tool for tracking value accrued for a particular purpose.  In
    the healthcare field, used to track charges for a patient, cost centers,
    etc.
    """
    resource_type: ClassVar[str] = "Account"
    coverage: Optional[List[AccountCoverage]] = empty_list()
    description: Optional[str] = None
    guarantor: Optional[List[AccountGuarantor]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    name: Optional[str] = None
    owner: Optional[fhirreference.FHIRReference] = None
    partOf: Optional[fhirreference.FHIRReference] = None
    servicePeriod: Optional[period.Period] = None
    status: str = None
    subject: Optional[List[fhirreference.FHIRReference]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None

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
#        self.coverage = None
#        """ The party(s) that are responsible for covering the payment of this
        account, and what order should they be applied to the account.
#        List of `AccountCoverage` items
#
# (represented as `dict` in JSON). """
#
#
#        self.description = None
#        """ Explanation of purpose/use.
#        Type `str`
#
#. """
#
#
#        self.guarantor = None
#        """ The parties ultimately responsible for balancing the Account.
#        List of `AccountGuarantor` items
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Account number.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.name = None
#        """ Human-readable label.
#        Type `str`
#
#. """
#
#
#        self.owner = None
#        """ Entity managing the Account.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.partOf = None
#        """ Reference to a parent Account.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.servicePeriod = None
#        """ Transaction window.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ active | inactive | entered-in-error | on-hold | unknown.
#        Type `str`
#
#. """
#
#
#        self.subject = None
#        """ The entity that caused the expenses.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ E.g. patient, expense, depreciation.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(Account, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Account, self).elementProperties()
        js.extend([
            ("coverage", "coverage", AccountCoverage, {  # #}True, None, {  # #}False),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("guarantor", "guarantor", AccountGuarantor, {  # #}True, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("name", "name", str, {  # #}False, None, {  # #}False),
            ("owner", "owner", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("partOf", "partOf", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("servicePeriod", "servicePeriod", period.Period, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("subject", "subject", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import fhirreference
from . import identifier
from . import period


from . import backboneelement

@dataclass
class AccountCoverage(backboneelement.BackboneElement):
    """ The party(s) that are responsible for covering the payment of this account,
    and what order should they be applied to the account.
    """
    resource_type: ClassVar[str] = "AccountCoverage"
    coverage:fhirreference.FHIRReference = None
    priority: Optional[int] = None

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
#        self.coverage = None
#        """ The party(s), such as insurances, that may contribute to the
        payment of this account.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.priority = None
#        """ The priority of the coverage in the context of this account.
#        Type `int`
#
#. """
#

#        super(AccountCoverage, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AccountCoverage, self).elementProperties()
        js.extend([
            ("coverage", "coverage", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("priority", "priority", int, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import period


@dataclass
class AccountGuarantor(backboneelement.BackboneElement):
    """ The parties ultimately responsible for balancing the Account.

    The parties responsible for balancing the account if other payment options
    fall short.
    """
    resource_type: ClassVar[str] = "AccountGuarantor"
    onHold: Optional[bool] = None
    party:fhirreference.FHIRReference = None
    period: Optional[period.Period] = None

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
#        self.onHold = None
#        """ Credit or other hold applied.
#        Type `bool`
#
#. """
#
#
#        self.party = None
#        """ Responsible entity.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.period = None
#        """ Guarantee account during.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#

#        super(AccountGuarantor, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AccountGuarantor, self).elementProperties()
        js.extend([
            ("onHold", "onHold", bool, {  # #}False, None, {  # #}False),
            ("party", "party", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("period", "period", period.Period, {  # #}False, None, {  # #}False),
        ])
        return js