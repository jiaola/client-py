#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CapabilityStatement) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import coding
from . import contactdetail
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import usagecontext


from . import domainresource

@dataclass
class CapabilityStatement(domainresource.DomainResource):
    """ A statement of system capabilities.

    A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server for a particular version of FHIR that may be used as a
    statement of actual server functionality or a statement of required or
    desired server implementation.
    """
    resource_type: ClassVar[str] = "CapabilityStatement"
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date:fhirdate.FHIRDate = None
    description: Optional[str] = None
    document: Optional[List[CapabilityStatementDocument]] = empty_list()
    experimental: Optional[bool] = None
    fhirVersion: str = None
    format: List[ str] = empty_list()
    implementation: Optional[CapabilityStatementImplementation] = None
    implementationGuide: Optional[List[str]] = empty_list()
    imports: Optional[List[str]] = empty_list()
    instantiates: Optional[List[str]] = empty_list()
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    kind: str = None
    messaging: Optional[List[CapabilityStatementMessaging]] = empty_list()
    name: Optional[str] = None
    patchFormat: Optional[List[str]] = empty_list()
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    rest: Optional[List[CapabilityStatementRest]] = empty_list()
    software: Optional[CapabilityStatementSoftware] = None
    status: str = None
    title: Optional[str] = None
    url: Optional[str] = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    version: Optional[str] = None

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
#        self.contact = None
#        """ Contact details for the publisher.
#        List of `ContactDetail` items
#
# (represented as `dict` in JSON). """
#
#
#        self.copyright = None
#        """ Use and/or publishing restrictions.
#        Type `str`
#
#. """
#
#
#        self.date = None
#        """ Date last changed.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.description = None
#        """ Natural language description of the capability statement.
#        Type `str`
#
#. """
#
#
#        self.document = None
#        """ Document definition.
#        List of `CapabilityStatementDocument` items
#
# (represented as `dict` in JSON). """
#
#
#        self.experimental = None
#        """ For testing purposes, not real usage.
#        Type `bool`
#
#. """
#
#
#        self.fhirVersion = None
#        """ FHIR Version the system supports.
#        Type `str`
#
#. """
#
#
#        self.format = None
#        """ formats supported (xml | json | ttl | mime type).
#        List of `str` items
#
#. """
#
#
#        self.implementation = None
#        """ If this describes a specific instance.
#        Type `CapabilityStatementImplementation`
#
# (represented as `dict` in JSON). """
#
#
#        self.implementationGuide = None
#        """ Implementation guides supported.
#        List of `str` items
#
#. """
#
#
#        self.imports = None
#        """ Canonical URL of another capability statement this adds to.
#        List of `str` items
#
#. """
#
#
#        self.instantiates = None
#        """ Canonical URL of another capability statement this implements.
#        List of `str` items
#
#. """
#
#
#        self.jurisdiction = None
#        """ Intended jurisdiction for capability statement (if applicable).
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.kind = None
#        """ instance | capability | requirements.
#        Type `str`
#
#. """
#
#
#        self.messaging = None
#        """ If messaging is supported.
#        List of `CapabilityStatementMessaging` items
#
# (represented as `dict` in JSON). """
#
#
#        self.name = None
#        """ Name for this capability statement (computer friendly).
#        Type `str`
#
#. """
#
#
#        self.patchFormat = None
#        """ Patch formats supported.
#        List of `str` items
#
#. """
#
#
#        self.publisher = None
#        """ Name of the publisher (organization or individual).
#        Type `str`
#
#. """
#
#
#        self.purpose = None
#        """ Why this capability statement is defined.
#        Type `str`
#
#. """
#
#
#        self.rest = None
#        """ If the endpoint is a RESTful one.
#        List of `CapabilityStatementRest` items
#
# (represented as `dict` in JSON). """
#
#
#        self.software = None
#        """ Software that is covered by this capability statement.
#        Type `CapabilityStatementSoftware`
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ draft | active | retired | unknown.
#        Type `str`
#
#. """
#
#
#        self.title = None
#        """ Name for this capability statement (human friendly).
#        Type `str`
#
#. """
#
#
#        self.url = None
#        """ Canonical identifier for this capability statement, represented as
        a URI (globally unique).
#        Type `str`
#
#. """
#
#
#        self.useContext = None
#        """ The context that the content is intended to support.
#        List of `UsageContext` items
#
# (represented as `dict` in JSON). """
#
#
#        self.version = None
#        """ Business version of the capability statement.
#        Type `str`
#
#. """
#

#        super(CapabilityStatement, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatement, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, {  # #}True, None, {  # #}False),
            ("copyright", "copyright", str, {  # #}False, None, {  # #}False),
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}True),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("document", "document", CapabilityStatementDocument, {  # #}True, None, {  # #}False),
            ("experimental", "experimental", bool, {  # #}False, None, {  # #}False),
            ("fhirVersion", "fhirVersion", str, {  # #}False, None, {  # #}True),
            ("format", "format", str, {  # #}True, None, {  # #}True),
            ("implementation", "implementation", CapabilityStatementImplementation, {  # #}False, None, {  # #}False),
            ("implementationGuide", "implementationGuide", str, {  # #}True, None, {  # #}False),
            ("imports", "imports", str, {  # #}True, None, {  # #}False),
            ("instantiates", "instantiates", str, {  # #}True, None, {  # #}False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("kind", "kind", str, {  # #}False, None, {  # #}True),
            ("messaging", "messaging", CapabilityStatementMessaging, {  # #}True, None, {  # #}False),
            ("name", "name", str, {  # #}False, None, {  # #}False),
            ("patchFormat", "patchFormat", str, {  # #}True, None, {  # #}False),
            ("publisher", "publisher", str, {  # #}False, None, {  # #}False),
            ("purpose", "purpose", str, {  # #}False, None, {  # #}False),
            ("rest", "rest", CapabilityStatementRest, {  # #}True, None, {  # #}False),
            ("software", "software", CapabilityStatementSoftware, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("title", "title", str, {  # #}False, None, {  # #}False),
            ("url", "url", str, {  # #}False, None, {  # #}False),
            ("useContext", "useContext", usagecontext.UsageContext, {  # #}True, None, {  # #}False),
            ("version", "version", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import usagecontext


from . import backboneelement

@dataclass
class CapabilityStatementDocument(backboneelement.BackboneElement):
    """ Document definition.

    A document definition.
    """
    resource_type: ClassVar[str] = "CapabilityStatementDocument"
    documentation: Optional[str] = None
    mode: str = None
    profile: str = None

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
#        self.documentation = None
#        """ Description of document support.
#        Type `str`
#
#. """
#
#
#        self.mode = None
#        """ producer | consumer.
#        Type `str`
#
#. """
#
#
#        self.profile = None
#        """ Constraint on the resources used in the document.
#        Type `str`
#
#. """
#

#        super(CapabilityStatementDocument, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementDocument, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, {  # #}False, None, {  # #}False),
            ("mode", "mode", str, {  # #}False, None, {  # #}True),
            ("profile", "profile", str, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import usagecontext


@dataclass
class CapabilityStatementImplementation(backboneelement.BackboneElement):
    """ If this describes a specific instance.

    Identifies a specific implementation instance that is described by the
    capability statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """
    resource_type: ClassVar[str] = "CapabilityStatementImplementation"
    custodian: Optional[fhirreference.FHIRReference] = None
    description: str = None
    url: Optional[str] = None

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
#        self.custodian = None
#        """ Organization that manages the data.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.description = None
#        """ Describes this specific instance.
#        Type `str`
#
#. """
#
#
#        self.url = None
#        """ Base URL for the installation.
#        Type `str`
#
#. """
#

#        super(CapabilityStatementImplementation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementImplementation, self).elementProperties()
        js.extend([
            ("custodian", "custodian", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("description", "description", str, {  # #}False, None, {  # #}True),
            ("url", "url", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import usagecontext


@dataclass
class CapabilityStatementMessaging(backboneelement.BackboneElement):
    """ If messaging is supported.

    A description of the messaging capabilities of the solution.
    """
    resource_type: ClassVar[str] = "CapabilityStatementMessaging"
    documentation: Optional[str] = None
    endpoint: Optional[List[CapabilityStatementMessagingEndpoint]] = empty_list()
    reliableCache: Optional[int] = None
    supportedMessage: Optional[List[CapabilityStatementMessagingSupportedMessage]] = empty_list()

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
#        self.documentation = None
#        """ Messaging interface behavior details.
#        Type `str`
#
#. """
#
#
#        self.endpoint = None
#        """ Where messages should be sent.
#        List of `CapabilityStatementMessagingEndpoint` items
#
# (represented as `dict` in JSON). """
#
#
#        self.reliableCache = None
#        """ Reliable Message Cache Length (min).
#        Type `int`
#
#. """
#
#
#        self.supportedMessage = None
#        """ Messages supported by this system.
#        List of `CapabilityStatementMessagingSupportedMessage` items
#
# (represented as `dict` in JSON). """
#

#        super(CapabilityStatementMessaging, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementMessaging, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, {  # #}False, None, {  # #}False),
            ("endpoint", "endpoint", CapabilityStatementMessagingEndpoint, {  # #}True, None, {  # #}False),
            ("reliableCache", "reliableCache", int, {  # #}False, None, {  # #}False),
            ("supportedMessage", "supportedMessage", CapabilityStatementMessagingSupportedMessage, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import usagecontext


@dataclass
class CapabilityStatementMessagingEndpoint(backboneelement.BackboneElement):
    """ Where messages should be sent.

    An endpoint (network accessible address) to which messages and/or replies
    are to be sent.
    """
    resource_type: ClassVar[str] = "CapabilityStatementMessagingEndpoint"
    address: str = None
    protocol:coding.Coding = None

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
#        """ Network address or identifier of the end-point.
#        Type `str`
#
#. """
#
#
#        self.protocol = None
#        """ http | ftp | mllp +.
#        Type `Coding`
#
# (represented as `dict` in JSON). """
#

#        super(CapabilityStatementMessagingEndpoint, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementMessagingEndpoint, self).elementProperties()
        js.extend([
            ("address", "address", str, {  # #}False, None, {  # #}True),
            ("protocol", "protocol", coding.Coding, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import usagecontext


@dataclass
class CapabilityStatementMessagingSupportedMessage(backboneelement.BackboneElement):
    """ Messages supported by this system.

    References to message definitions for messages this system can send or
    receive.
    """
    resource_type: ClassVar[str] = "CapabilityStatementMessagingSupportedMessage"
    definition: str = None
    mode: str = None

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
#        self.definition = None
#        """ Message supported by this system.
#        Type `str`
#
#. """
#
#
#        self.mode = None
#        """ sender | receiver.
#        Type `str`
#
#. """
#

#        super(CapabilityStatementMessagingSupportedMessage, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementMessagingSupportedMessage, self).elementProperties()
        js.extend([
            ("definition", "definition", str, {  # #}False, None, {  # #}True),
            ("mode", "mode", str, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import usagecontext


@dataclass
class CapabilityStatementRest(backboneelement.BackboneElement):
    """ If the endpoint is a RESTful one.

    A definition of the restful capabilities of the solution, if any.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRest"
    compartment: Optional[List[str]] = empty_list()
    documentation: Optional[str] = None
    interaction: Optional[List[CapabilityStatementRestInteraction]] = empty_list()
    mode: str = None
    operation: Optional[List[CapabilityStatementRestResourceOperation]] = empty_list()
    resource: Optional[List[CapabilityStatementRestResource]] = empty_list()
    searchParam: Optional[List[CapabilityStatementRestResourceSearchParam]] = empty_list()
    security: Optional[CapabilityStatementRestSecurity] = None

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
#        self.compartment = None
#        """ Compartments served/used by system.
#        List of `str` items
#
#. """
#
#
#        self.documentation = None
#        """ General description of implementation.
#        Type `str`
#
#. """
#
#
#        self.interaction = None
#        """ What operations are supported?.
#        List of `CapabilityStatementRestInteraction` items
#
# (represented as `dict` in JSON). """
#
#
#        self.mode = None
#        """ client | server.
#        Type `str`
#
#. """
#
#
#        self.operation = None
#        """ Definition of a system level operation.
#        List of `CapabilityStatementRestResourceOperation` items
#
# (represented as `dict` in JSON). """
#
#
#        self.resource = None
#        """ Resource served on the REST interface.
#        List of `CapabilityStatementRestResource` items
#
# (represented as `dict` in JSON). """
#
#
#        self.searchParam = None
#        """ Search parameters for searching all resources.
#        List of `CapabilityStatementRestResourceSearchParam` items
#
# (represented as `dict` in JSON). """
#
#
#        self.security = None
#        """ Information about security of implementation.
#        Type `CapabilityStatementRestSecurity`
#
# (represented as `dict` in JSON). """
#

#        super(CapabilityStatementRest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementRest, self).elementProperties()
        js.extend([
            ("compartment", "compartment", str, {  # #}True, None, {  # #}False),
            ("documentation", "documentation", str, {  # #}False, None, {  # #}False),
            ("interaction", "interaction", CapabilityStatementRestInteraction, {  # #}True, None, {  # #}False),
            ("mode", "mode", str, {  # #}False, None, {  # #}True),
            ("operation", "operation", CapabilityStatementRestResourceOperation, {  # #}True, None, {  # #}False),
            ("resource", "resource", CapabilityStatementRestResource, {  # #}True, None, {  # #}False),
            ("searchParam", "searchParam", CapabilityStatementRestResourceSearchParam, {  # #}True, None, {  # #}False),
            ("security", "security", CapabilityStatementRestSecurity, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import usagecontext


@dataclass
class CapabilityStatementRestInteraction(backboneelement.BackboneElement):
    """ What operations are supported?.

    A specification of restful operations supported by the system.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestInteraction"
    code: str = None
    documentation: Optional[str] = None

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
#        """ transaction | batch | search-system | history-system.
#        Type `str`
#
#. """
#
#
#        self.documentation = None
#        """ Anything special about operation behavior.
#        Type `str`
#
#. """
#

#        super(CapabilityStatementRestInteraction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementRestInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, {  # #}False, None, {  # #}True),
            ("documentation", "documentation", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import usagecontext


@dataclass
class CapabilityStatementRestResource(backboneelement.BackboneElement):
    """ Resource served on the REST interface.

    A specification of the restful capabilities of the solution for a specific
    resource type.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestResource"
    conditionalCreate: Optional[bool] = None
    conditionalDelete: Optional[str] = None
    conditionalRead: Optional[str] = None
    conditionalUpdate: Optional[bool] = None
    documentation: Optional[str] = None
    interaction: Optional[List[CapabilityStatementRestResourceInteraction]] = empty_list()
    operation: Optional[List[CapabilityStatementRestResourceOperation]] = empty_list()
    profile: Optional[str] = None
    readHistory: Optional[bool] = None
    referencePolicy: Optional[List[str]] = empty_list()
    searchInclude: Optional[List[str]] = empty_list()
    searchParam: Optional[List[CapabilityStatementRestResourceSearchParam]] = empty_list()
    searchRevInclude: Optional[List[str]] = empty_list()
    supportedProfile: Optional[List[str]] = empty_list()
    type: str = None
    updateCreate: Optional[bool] = None
    versioning: Optional[str] = None

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
#        self.conditionalCreate = None
#        """ If allows/uses conditional create.
#        Type `bool`
#
#. """
#
#
#        self.conditionalDelete = None
#        """ not-supported | single | multiple - how conditional delete is
        supported.
#        Type `str`
#
#. """
#
#
#        self.conditionalRead = None
#        """ not-supported | modified-since | not-match | full-support.
#        Type `str`
#
#. """
#
#
#        self.conditionalUpdate = None
#        """ If allows/uses conditional update.
#        Type `bool`
#
#. """
#
#
#        self.documentation = None
#        """ Additional information about the use of the resource type.
#        Type `str`
#
#. """
#
#
#        self.interaction = None
#        """ What operations are supported?.
#        List of `CapabilityStatementRestResourceInteraction` items
#
# (represented as `dict` in JSON). """
#
#
#        self.operation = None
#        """ Definition of a resource operation.
#        List of `CapabilityStatementRestResourceOperation` items
#
# (represented as `dict` in JSON). """
#
#
#        self.profile = None
#        """ Base System profile for all uses of resource.
#        Type `str`
#
#. """
#
#
#        self.readHistory = None
#        """ Whether vRead can return past versions.
#        Type `bool`
#
#. """
#
#
#        self.referencePolicy = None
#        """ literal | logical | resolves | enforced | local.
#        List of `str` items
#
#. """
#
#
#        self.searchInclude = None
#        """ _include values supported by the server.
#        List of `str` items
#
#. """
#
#
#        self.searchParam = None
#        """ Search parameters supported by implementation.
#        List of `CapabilityStatementRestResourceSearchParam` items
#
# (represented as `dict` in JSON). """
#
#
#        self.searchRevInclude = None
#        """ _revinclude values supported by the server.
#        List of `str` items
#
#. """
#
#
#        self.supportedProfile = None
#        """ Profiles for use cases supported.
#        List of `str` items
#
#. """
#
#
#        self.type = None
#        """ A resource type that is supported.
#        Type `str`
#
#. """
#
#
#        self.updateCreate = None
#        """ If update can commit to a new identity.
#        Type `bool`
#
#. """
#
#
#        self.versioning = None
#        """ no-version | versioned | versioned-update.
#        Type `str`
#
#. """
#

#        super(CapabilityStatementRestResource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementRestResource, self).elementProperties()
        js.extend([
            ("conditionalCreate", "conditionalCreate", bool, {  # #}False, None, {  # #}False),
            ("conditionalDelete", "conditionalDelete", str, {  # #}False, None, {  # #}False),
            ("conditionalRead", "conditionalRead", str, {  # #}False, None, {  # #}False),
            ("conditionalUpdate", "conditionalUpdate", bool, {  # #}False, None, {  # #}False),
            ("documentation", "documentation", str, {  # #}False, None, {  # #}False),
            ("interaction", "interaction", CapabilityStatementRestResourceInteraction, {  # #}True, None, {  # #}False),
            ("operation", "operation", CapabilityStatementRestResourceOperation, {  # #}True, None, {  # #}False),
            ("profile", "profile", str, {  # #}False, None, {  # #}False),
            ("readHistory", "readHistory", bool, {  # #}False, None, {  # #}False),
            ("referencePolicy", "referencePolicy", str, {  # #}True, None, {  # #}False),
            ("searchInclude", "searchInclude", str, {  # #}True, None, {  # #}False),
            ("searchParam", "searchParam", CapabilityStatementRestResourceSearchParam, {  # #}True, None, {  # #}False),
            ("searchRevInclude", "searchRevInclude", str, {  # #}True, None, {  # #}False),
            ("supportedProfile", "supportedProfile", str, {  # #}True, None, {  # #}False),
            ("type", "type", str, {  # #}False, None, {  # #}True),
            ("updateCreate", "updateCreate", bool, {  # #}False, None, {  # #}False),
            ("versioning", "versioning", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import usagecontext


@dataclass
class CapabilityStatementRestResourceInteraction(backboneelement.BackboneElement):
    """ What operations are supported?.

    Identifies a restful operation supported by the solution.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestResourceInteraction"
    code: str = None
    documentation: Optional[str] = None

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
#        """ read | vread | update | patch | delete | history-instance |
        history-type | create | search-type.
#        Type `str`
#
#. """
#
#
#        self.documentation = None
#        """ Anything special about operation behavior.
#        Type `str`
#
#. """
#

#        super(CapabilityStatementRestResourceInteraction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementRestResourceInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, {  # #}False, None, {  # #}True),
            ("documentation", "documentation", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import usagecontext


@dataclass
class CapabilityStatementRestResourceOperation(backboneelement.BackboneElement):
    """ Definition of a resource operation.

    Definition of an operation or a named query together with its parameters
    and their meaning and type. Consult the definition of the operation for
    details about how to invoke the operation, and the parameters.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestResourceOperation"
    definition: str = None
    documentation: Optional[str] = None
    name: str = None

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
#        self.definition = None
#        """ The defined operation/query.
#        Type `str`
#
#. """
#
#
#        self.documentation = None
#        """ Specific details about operation behavior.
#        Type `str`
#
#. """
#
#
#        self.name = None
#        """ Name by which the operation/query is invoked.
#        Type `str`
#
#. """
#

#        super(CapabilityStatementRestResourceOperation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementRestResourceOperation, self).elementProperties()
        js.extend([
            ("definition", "definition", str, {  # #}False, None, {  # #}True),
            ("documentation", "documentation", str, {  # #}False, None, {  # #}False),
            ("name", "name", str, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import usagecontext


@dataclass
class CapabilityStatementRestResourceSearchParam(backboneelement.BackboneElement):
    """ Search parameters supported by implementation.

    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestResourceSearchParam"
    definition: Optional[str] = None
    documentation: Optional[str] = None
    name: str = None
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
#        self.definition = None
#        """ Source of definition for parameter.
#        Type `str`
#
#. """
#
#
#        self.documentation = None
#        """ Server-specific usage.
#        Type `str`
#
#. """
#
#
#        self.name = None
#        """ Name of search parameter.
#        Type `str`
#
#. """
#
#
#        self.type = None
#        """ number | date | string | token | reference | composite | quantity |
        uri | special.
#        Type `str`
#
#. """
#

#        super(CapabilityStatementRestResourceSearchParam, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementRestResourceSearchParam, self).elementProperties()
        js.extend([
            ("definition", "definition", str, {  # #}False, None, {  # #}False),
            ("documentation", "documentation", str, {  # #}False, None, {  # #}False),
            ("name", "name", str, {  # #}False, None, {  # #}True),
            ("type", "type", str, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import usagecontext


@dataclass
class CapabilityStatementRestSecurity(backboneelement.BackboneElement):
    """ Information about security of implementation.

    Information about security implementation from an interface perspective -
    what a client needs to know.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestSecurity"
    cors: Optional[bool] = None
    description: Optional[str] = None
    service: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

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
#        self.cors = None
#        """ Adds CORS Headers (http://enable-cors.org/).
#        Type `bool`
#
#. """
#
#
#        self.description = None
#        """ General description of how security works.
#        Type `str`
#
#. """
#
#
#        self.service = None
#        """ OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#

#        super(CapabilityStatementRestSecurity, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementRestSecurity, self).elementProperties()
        js.extend([
            ("cors", "cors", bool, {  # #}False, None, {  # #}False),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("service", "service", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import usagecontext


@dataclass
class CapabilityStatementSoftware(backboneelement.BackboneElement):
    """ Software that is covered by this capability statement.

    Software that is covered by this capability statement.  It is used when the
    capability statement describes the capabilities of a particular software
    version, independent of an installation.
    """
    resource_type: ClassVar[str] = "CapabilityStatementSoftware"
    name: str = None
    releaseDate: Optional[fhirdate.FHIRDate] = None
    version: Optional[str] = None

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
#        self.name = None
#        """ A name the software is known by.
#        Type `str`
#
#. """
#
#
#        self.releaseDate = None
#        """ Date this version was released.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.version = None
#        """ Version covered by this statement.
#        Type `str`
#
#. """
#

#        super(CapabilityStatementSoftware, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementSoftware, self).elementProperties()
        js.extend([
            ("name", "name", str, {  # #}False, None, {  # #}True),
            ("releaseDate", "releaseDate", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("version", "version", str, {  # #}False, None, {  # #}False),
        ])
        return js