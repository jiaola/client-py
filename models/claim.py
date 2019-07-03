#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Claim) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


from . import domainresource

@dataclass
class Claim(domainresource.DomainResource):
    """ Claim, Pre-determination or Pre-authorization.

    A provider issued list of professional services and products which have
    been provided, or are to be provided, to a patient which is sent to an
    insurer for reimbursement.
    """
    resource_type: ClassVar[str] = "Claim"
    accident: Optional[ClaimAccident] = None
    billablePeriod: Optional[period.Period] = None
    careTeam: Optional[List[ClaimCareTeam]] = empty_list()
    created:fhirdate.FHIRDate = None
    diagnosis: Optional[List[ClaimDiagnosis]] = empty_list()
    enterer: Optional[fhirreference.FHIRReference] = None
    facility: Optional[fhirreference.FHIRReference] = None
    fundsReserve: Optional[codeableconcept.CodeableConcept] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    insurance: List[ ClaimInsurance] = empty_list()
    insurer: Optional[fhirreference.FHIRReference] = None
    item: Optional[List[ClaimItem]] = empty_list()
    originalPrescription: Optional[fhirreference.FHIRReference] = None
    patient:fhirreference.FHIRReference = None
    payee: Optional[ClaimPayee] = None
    prescription: Optional[fhirreference.FHIRReference] = None
    priority:codeableconcept.CodeableConcept = None
    procedure: Optional[List[ClaimProcedure]] = empty_list()
    provider:fhirreference.FHIRReference = None
    referral: Optional[fhirreference.FHIRReference] = None
    related: Optional[List[ClaimRelated]] = empty_list()
    status: str = None
    subType: Optional[codeableconcept.CodeableConcept] = None
    supportingInfo: Optional[List[ClaimSupportingInfo]] = empty_list()
    total: Optional[money.Money] = None
    type:codeableconcept.CodeableConcept = None
    use: str = None

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
#        self.accident = None
#        """ Details of the event.
#        Type `ClaimAccident`
#
# (represented as `dict` in JSON). """
#
#
#        self.billablePeriod = None
#        """ Relevant time frame for the claim.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.careTeam = None
#        """ Members of the care team.
#        List of `ClaimCareTeam` items
#
# (represented as `dict` in JSON). """
#
#
#        self.created = None
#        """ Resource creation date.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.diagnosis = None
#        """ Pertinent diagnosis information.
#        List of `ClaimDiagnosis` items
#
# (represented as `dict` in JSON). """
#
#
#        self.enterer = None
#        """ Author of the claim.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.facility = None
#        """ Servicing facility.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.fundsReserve = None
#        """ For whom to reserve funds.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Business Identifier for claim.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.insurance = None
#        """ Patient insurance information.
#        List of `ClaimInsurance` items
#
# (represented as `dict` in JSON). """
#
#
#        self.insurer = None
#        """ Target.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.item = None
#        """ Product or service provided.
#        List of `ClaimItem` items
#
# (represented as `dict` in JSON). """
#
#
#        self.originalPrescription = None
#        """ Original prescription if superseded by fulfiller.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.patient = None
#        """ The recipient of the products and services.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.payee = None
#        """ Recipient of benefits payable.
#        Type `ClaimPayee`
#
# (represented as `dict` in JSON). """
#
#
#        self.prescription = None
#        """ Prescription authorizing services and products.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.priority = None
#        """ Desired processing ugency.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.procedure = None
#        """ Clinical procedures performed.
#        List of `ClaimProcedure` items
#
# (represented as `dict` in JSON). """
#
#
#        self.provider = None
#        """ Party responsible for the claim.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.referral = None
#        """ Treatment referral.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.related = None
#        """ Prior or corollary claims.
#        List of `ClaimRelated` items
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
#
#        self.subType = None
#        """ More granular claim type.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.supportingInfo = None
#        """ Supporting information.
#        List of `ClaimSupportingInfo` items
#
# (represented as `dict` in JSON). """
#
#
#        self.total = None
#        """ Total claim cost.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ Category or discipline.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.use = None
#        """ claim | preauthorization | predetermination.
#        Type `str`
#
#. """
#

#        super(Claim, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Claim, self).elementProperties()
        js.extend([
            ("accident", "accident", ClaimAccident, {  # #}False, None, {  # #}False),
            ("billablePeriod", "billablePeriod", period.Period, {  # #}False, None, {  # #}False),
            ("careTeam", "careTeam", ClaimCareTeam, {  # #}True, None, {  # #}False),
            ("created", "created", fhirdate.FHIRDate, {  # #}False, None, {  # #}True),
            ("diagnosis", "diagnosis", ClaimDiagnosis, {  # #}True, None, {  # #}False),
            ("enterer", "enterer", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("facility", "facility", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("fundsReserve", "fundsReserve", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("insurance", "insurance", ClaimInsurance, {  # #}True, None, {  # #}True),
            ("insurer", "insurer", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("item", "item", ClaimItem, {  # #}True, None, {  # #}False),
            ("originalPrescription", "originalPrescription", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("patient", "patient", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("payee", "payee", ClaimPayee, {  # #}False, None, {  # #}False),
            ("prescription", "prescription", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("priority", "priority", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("procedure", "procedure", ClaimProcedure, {  # #}True, None, {  # #}False),
            ("provider", "provider", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("referral", "referral", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("related", "related", ClaimRelated, {  # #}True, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("subType", "subType", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("supportingInfo", "supportingInfo", ClaimSupportingInfo, {  # #}True, None, {  # #}False),
            ("total", "total", money.Money, {  # #}False, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("use", "use", str, {  # #}False, None, {  # #}True),
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
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


from . import backboneelement

@dataclass
class ClaimAccident(backboneelement.BackboneElement):
    """ Details of the event.

    Details of an accident which resulted in injuries which required the
    products and services listed in the claim.
    """
    resource_type: ClassVar[str] = "ClaimAccident"
    date:fhirdate.FHIRDate = None
    locationAddress: Optional[address.Address] = None
    locationReference: Optional[fhirreference.FHIRReference] = None
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
#        self.date = None
#        """ When the incident occurred.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.locationAddress = None
#        """ Where the event occurred.
#        Type `Address`
#
# (represented as `dict` in JSON). """
#
#
#        self.locationReference = None
#        """ Where the event occurred.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ The nature of the accident.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(ClaimAccident, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimAccident, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}True),
            ("locationAddress", "locationAddress", address.Address, {  # #}False, "location", {  # #}False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, {  # #}False, "location", {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


@dataclass
class ClaimCareTeam(backboneelement.BackboneElement):
    """ Members of the care team.

    The members of the team who provided the products and services.
    """
    resource_type: ClassVar[str] = "ClaimCareTeam"
    provider:fhirreference.FHIRReference = None
    qualification: Optional[codeableconcept.CodeableConcept] = None
    responsible: Optional[bool] = None
    role: Optional[codeableconcept.CodeableConcept] = None
    sequence: int = None

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
#        self.provider = None
#        """ Practitioner or organization.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.qualification = None
#        """ Practitioner credential or specialization.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.responsible = None
#        """ Indicator of the lead practitioner.
#        Type `bool`
#
#. """
#
#
#        self.role = None
#        """ Function within the team.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.sequence = None
#        """ Order of care team.
#        Type `int`
#
#. """
#

#        super(ClaimCareTeam, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimCareTeam, self).elementProperties()
        js.extend([
            ("provider", "provider", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("qualification", "qualification", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("responsible", "responsible", bool, {  # #}False, None, {  # #}False),
            ("role", "role", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("sequence", "sequence", int, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


@dataclass
class ClaimDiagnosis(backboneelement.BackboneElement):
    """ Pertinent diagnosis information.

    Information about diagnoses relevant to the claim items.
    """
    resource_type: ClassVar[str] = "ClaimDiagnosis"
    diagnosisCodeableConcept:codeableconcept.CodeableConcept = None
    diagnosisReference:fhirreference.FHIRReference = None
    onAdmission: Optional[codeableconcept.CodeableConcept] = None
    packageCode: Optional[codeableconcept.CodeableConcept] = None
    sequence: int = None
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
#        self.diagnosisCodeableConcept = None
#        """ Nature of illness or problem.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.diagnosisReference = None
#        """ Nature of illness or problem.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.onAdmission = None
#        """ Present on admission.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.packageCode = None
#        """ Package billing code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.sequence = None
#        """ Diagnosis instance identifier.
#        Type `int`
#
#. """
#
#
#        self.type = None
#        """ Timing or nature of the diagnosis.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#

#        super(ClaimDiagnosis, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "diagnosis", {  # #}True),
            ("diagnosisReference", "diagnosisReference", fhirreference.FHIRReference, {  # #}False, "diagnosis", {  # #}True),
            ("onAdmission", "onAdmission", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("packageCode", "packageCode", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("sequence", "sequence", int, {  # #}False, None, {  # #}True),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


@dataclass
class ClaimInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    resource_type: ClassVar[str] = "ClaimInsurance"
    businessArrangement: Optional[str] = None
    claimResponse: Optional[fhirreference.FHIRReference] = None
    coverage:fhirreference.FHIRReference = None
    focal: bool = None
    identifier: Optional[identifier.Identifier] = None
    preAuthRef: Optional[List[str]] = empty_list()
    sequence: int = None

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
#        self.businessArrangement = None
#        """ Additional provider contract number.
#        Type `str`
#
#. """
#
#
#        self.claimResponse = None
#        """ Adjudication results.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.coverage = None
#        """ Insurance information.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.focal = None
#        """ Coverage to be used for adjudication.
#        Type `bool`
#
#. """
#
#
#        self.identifier = None
#        """ Pre-assigned Claim number.
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#
#
#        self.preAuthRef = None
#        """ Prior authorization reference number.
#        List of `str` items
#
#. """
#
#
#        self.sequence = None
#        """ Insurance instance identifier.
#        Type `int`
#
#. """
#

#        super(ClaimInsurance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, {  # #}False, None, {  # #}False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("coverage", "coverage", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("focal", "focal", bool, {  # #}False, None, {  # #}True),
            ("identifier", "identifier", identifier.Identifier, {  # #}False, None, {  # #}False),
            ("preAuthRef", "preAuthRef", str, {  # #}True, None, {  # #}False),
            ("sequence", "sequence", int, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


@dataclass
class ClaimItem(backboneelement.BackboneElement):
    """ Product or service provided.

    A claim line. Either a simple  product or service or a 'group' of details
    which can each be a simple items or groups of sub-details.
    """
    resource_type: ClassVar[str] = "ClaimItem"
    bodySite: Optional[codeableconcept.CodeableConcept] = None
    careTeamSequence: Optional[List[int]] = empty_list()
    category: Optional[codeableconcept.CodeableConcept] = None
    detail: Optional[List[ClaimItemDetail]] = empty_list()
    diagnosisSequence: Optional[List[int]] = empty_list()
    encounter: Optional[List[fhirreference.FHIRReference]] = empty_list()
    factor: Optional[float] = None
    informationSequence: Optional[List[int]] = empty_list()
    locationAddress: Optional[address.Address] = None
    locationCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    locationReference: Optional[fhirreference.FHIRReference] = None
    modifier: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    net: Optional[money.Money] = None
    procedureSequence: Optional[List[int]] = empty_list()
    productOrService:codeableconcept.CodeableConcept = None
    programCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    quantity: Optional[quantity.Quantity] = None
    revenue: Optional[codeableconcept.CodeableConcept] = None
    sequence: int = None
    servicedDate: Optional[fhirdate.FHIRDate] = None
    servicedPeriod: Optional[period.Period] = None
    subSite: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    udi: Optional[List[fhirreference.FHIRReference]] = empty_list()
    unitPrice: Optional[money.Money] = None

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
#        self.bodySite = None
#        """ Anatomical location.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.careTeamSequence = None
#        """ Applicable careTeam members.
#        List of `int` items
#
#. """
#
#
#        self.category = None
#        """ Benefit classification.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.detail = None
#        """ Product or service provided.
#        List of `ClaimItemDetail` items
#
# (represented as `dict` in JSON). """
#
#
#        self.diagnosisSequence = None
#        """ Applicable diagnoses.
#        List of `int` items
#
#. """
#
#
#        self.encounter = None
#        """ Encounters related to this billed item.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.factor = None
#        """ Price scaling factor.
#        Type `float`
#
#. """
#
#
#        self.informationSequence = None
#        """ Applicable exception and supporting information.
#        List of `int` items
#
#. """
#
#
#        self.locationAddress = None
#        """ Place of service or where product was supplied.
#        Type `Address`
#
# (represented as `dict` in JSON). """
#
#
#        self.locationCodeableConcept = None
#        """ Place of service or where product was supplied.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.locationReference = None
#        """ Place of service or where product was supplied.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.modifier = None
#        """ Product or service billing modifiers.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.net = None
#        """ Total item cost.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#
#
#        self.procedureSequence = None
#        """ Applicable procedures.
#        List of `int` items
#
#. """
#
#
#        self.productOrService = None
#        """ Billing, service, product, or drug code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.programCode = None
#        """ Program the product or service is provided under.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.quantity = None
#        """ Count of products or services.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.revenue = None
#        """ Revenue or cost center code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.sequence = None
#        """ Item instance identifier.
#        Type `int`
#
#. """
#
#
#        self.servicedDate = None
#        """ Date or dates of service or product delivery.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.servicedPeriod = None
#        """ Date or dates of service or product delivery.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.subSite = None
#        """ Anatomical sub-location.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.udi = None
#        """ Unique device identifier.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.unitPrice = None
#        """ Fee, charge or cost per item.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#

#        super(ClaimItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimItem, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("careTeamSequence", "careTeamSequence", int, {  # #}True, None, {  # #}False),
            ("category", "category", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("detail", "detail", ClaimItemDetail, {  # #}True, None, {  # #}False),
            ("diagnosisSequence", "diagnosisSequence", int, {  # #}True, None, {  # #}False),
            ("encounter", "encounter", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("factor", "factor", float, {  # #}False, None, {  # #}False),
            ("informationSequence", "informationSequence", int, {  # #}True, None, {  # #}False),
            ("locationAddress", "locationAddress", address.Address, {  # #}False, "location", {  # #}False),
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "location", {  # #}False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, {  # #}False, "location", {  # #}False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("net", "net", money.Money, {  # #}False, None, {  # #}False),
            ("procedureSequence", "procedureSequence", int, {  # #}True, None, {  # #}False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("quantity", "quantity", quantity.Quantity, {  # #}False, None, {  # #}False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("sequence", "sequence", int, {  # #}False, None, {  # #}True),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, {  # #}False, "serviced", {  # #}False),
            ("servicedPeriod", "servicedPeriod", period.Period, {  # #}False, "serviced", {  # #}False),
            ("subSite", "subSite", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("udi", "udi", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("unitPrice", "unitPrice", money.Money, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


@dataclass
class ClaimItemDetail(backboneelement.BackboneElement):
    """ Product or service provided.

    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """
    resource_type: ClassVar[str] = "ClaimItemDetail"
    category: Optional[codeableconcept.CodeableConcept] = None
    factor: Optional[float] = None
    modifier: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    net: Optional[money.Money] = None
    productOrService:codeableconcept.CodeableConcept = None
    programCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    quantity: Optional[quantity.Quantity] = None
    revenue: Optional[codeableconcept.CodeableConcept] = None
    sequence: int = None
    subDetail: Optional[List[ClaimItemDetailSubDetail]] = empty_list()
    udi: Optional[List[fhirreference.FHIRReference]] = empty_list()
    unitPrice: Optional[money.Money] = None

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
#        self.category = None
#        """ Benefit classification.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.factor = None
#        """ Price scaling factor.
#        Type `float`
#
#. """
#
#
#        self.modifier = None
#        """ Service/Product billing modifiers.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.net = None
#        """ Total item cost.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#
#
#        self.productOrService = None
#        """ Billing, service, product, or drug code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.programCode = None
#        """ Program the product or service is provided under.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.quantity = None
#        """ Count of products or services.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.revenue = None
#        """ Revenue or cost center code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.sequence = None
#        """ Item instance identifier.
#        Type `int`
#
#. """
#
#
#        self.subDetail = None
#        """ Product or service provided.
#        List of `ClaimItemDetailSubDetail` items
#
# (represented as `dict` in JSON). """
#
#
#        self.udi = None
#        """ Unique device identifier.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.unitPrice = None
#        """ Fee, charge or cost per item.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#

#        super(ClaimItemDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimItemDetail, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("factor", "factor", float, {  # #}False, None, {  # #}False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("net", "net", money.Money, {  # #}False, None, {  # #}False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("quantity", "quantity", quantity.Quantity, {  # #}False, None, {  # #}False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("sequence", "sequence", int, {  # #}False, None, {  # #}True),
            ("subDetail", "subDetail", ClaimItemDetailSubDetail, {  # #}True, None, {  # #}False),
            ("udi", "udi", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("unitPrice", "unitPrice", money.Money, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


@dataclass
class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
    """ Product or service provided.

    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """
    resource_type: ClassVar[str] = "ClaimItemDetailSubDetail"
    category: Optional[codeableconcept.CodeableConcept] = None
    factor: Optional[float] = None
    modifier: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    net: Optional[money.Money] = None
    productOrService:codeableconcept.CodeableConcept = None
    programCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    quantity: Optional[quantity.Quantity] = None
    revenue: Optional[codeableconcept.CodeableConcept] = None
    sequence: int = None
    udi: Optional[List[fhirreference.FHIRReference]] = empty_list()
    unitPrice: Optional[money.Money] = None

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
#        self.category = None
#        """ Benefit classification.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.factor = None
#        """ Price scaling factor.
#        Type `float`
#
#. """
#
#
#        self.modifier = None
#        """ Service/Product billing modifiers.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.net = None
#        """ Total item cost.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#
#
#        self.productOrService = None
#        """ Billing, service, product, or drug code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.programCode = None
#        """ Program the product or service is provided under.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.quantity = None
#        """ Count of products or services.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.revenue = None
#        """ Revenue or cost center code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.sequence = None
#        """ Item instance identifier.
#        Type `int`
#
#. """
#
#
#        self.udi = None
#        """ Unique device identifier.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.unitPrice = None
#        """ Fee, charge or cost per item.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#

#        super(ClaimItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("factor", "factor", float, {  # #}False, None, {  # #}False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("net", "net", money.Money, {  # #}False, None, {  # #}False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("quantity", "quantity", quantity.Quantity, {  # #}False, None, {  # #}False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("sequence", "sequence", int, {  # #}False, None, {  # #}True),
            ("udi", "udi", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("unitPrice", "unitPrice", money.Money, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


@dataclass
class ClaimPayee(backboneelement.BackboneElement):
    """ Recipient of benefits payable.

    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """
    resource_type: ClassVar[str] = "ClaimPayee"
    party: Optional[fhirreference.FHIRReference] = None
    type:codeableconcept.CodeableConcept = None

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
#        self.party = None
#        """ Recipient reference.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ Category of recipient.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(ClaimPayee, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimPayee, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


@dataclass
class ClaimProcedure(backboneelement.BackboneElement):
    """ Clinical procedures performed.

    Procedures performed on the patient relevant to the billing items with the
    claim.
    """
    resource_type: ClassVar[str] = "ClaimProcedure"
    date: Optional[fhirdate.FHIRDate] = None
    procedureCodeableConcept:codeableconcept.CodeableConcept = None
    procedureReference:fhirreference.FHIRReference = None
    sequence: int = None
    type: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    udi: Optional[List[fhirreference.FHIRReference]] = empty_list()

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
#        self.date = None
#        """ When the procedure was performed.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.procedureCodeableConcept = None
#        """ Specific clinical procedure.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.procedureReference = None
#        """ Specific clinical procedure.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.sequence = None
#        """ Procedure instance identifier.
#        Type `int`
#
#. """
#
#
#        self.type = None
#        """ Category of Procedure.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.udi = None
#        """ Unique device identifier.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#

#        super(ClaimProcedure, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimProcedure, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("procedureCodeableConcept", "procedureCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "procedure", {  # #}True),
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, {  # #}False, "procedure", {  # #}True),
            ("sequence", "sequence", int, {  # #}False, None, {  # #}True),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("udi", "udi", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


@dataclass
class ClaimRelated(backboneelement.BackboneElement):
    """ Prior or corollary claims.

    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
    """
    resource_type: ClassVar[str] = "ClaimRelated"
    claim: Optional[fhirreference.FHIRReference] = None
    reference: Optional[identifier.Identifier] = None
    relationship: Optional[codeableconcept.CodeableConcept] = None

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
#        self.claim = None
#        """ Reference to the related claim.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.reference = None
#        """ File or case reference.
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#
#
#        self.relationship = None
#        """ How the reference claim is related.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(ClaimRelated, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimRelated, self).elementProperties()
        js.extend([
            ("claim", "claim", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("reference", "reference", identifier.Identifier, {  # #}False, None, {  # #}False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


@dataclass
class ClaimSupportingInfo(backboneelement.BackboneElement):
    """ Supporting information.

    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    resource_type: ClassVar[str] = "ClaimSupportingInfo"
    category:codeableconcept.CodeableConcept = None
    code: Optional[codeableconcept.CodeableConcept] = None
    reason: Optional[codeableconcept.CodeableConcept] = None
    sequence: int = None
    timingDate: Optional[fhirdate.FHIRDate] = None
    timingPeriod: Optional[period.Period] = None
    valueAttachment: Optional[attachment.Attachment] = None
    valueBoolean: Optional[bool] = None
    valueQuantity: Optional[quantity.Quantity] = None
    valueReference: Optional[fhirreference.FHIRReference] = None
    valueString: Optional[str] = None

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
#        self.category = None
#        """ Classification of the supplied information.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.code = None
#        """ Type of information.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.reason = None
#        """ Explanation for the information.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.sequence = None
#        """ Information instance identifier.
#        Type `int`
#
#. """
#
#
#        self.timingDate = None
#        """ When it occurred.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.timingPeriod = None
#        """ When it occurred.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.valueAttachment = None
#        """ Data to be provided.
#        Type `Attachment`
#
# (represented as `dict` in JSON). """
#
#
#        self.valueBoolean = None
#        """ Data to be provided.
#        Type `bool`
#
#. """
#
#
#        self.valueQuantity = None
#        """ Data to be provided.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.valueReference = None
#        """ Data to be provided.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.valueString = None
#        """ Data to be provided.
#        Type `str`
#
#. """
#

#        super(ClaimSupportingInfo, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimSupportingInfo, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("reason", "reason", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("sequence", "sequence", int, {  # #}False, None, {  # #}True),
            ("timingDate", "timingDate", fhirdate.FHIRDate, {  # #}False, "timing", {  # #}False),
            ("timingPeriod", "timingPeriod", period.Period, {  # #}False, "timing", {  # #}False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, {  # #}False, "value", {  # #}False),
            ("valueBoolean", "valueBoolean", bool, {  # #}False, "value", {  # #}False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, {  # #}False, "value", {  # #}False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, {  # #}False, "value", {  # #}False),
            ("valueString", "valueString", str, {  # #}False, "value", {  # #}False),
        ])
        return js