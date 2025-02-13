# ----------------------------------------------------------------------------
# Copyright 2019-2021 Pelion
#
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------
# Auto-generated by asn1ate v.0.6.0 from manifest_v3.asn
# (last modified on 2021-06-22 12:17:55.466130)

from pyasn1.type import univ, char, namedtype, namedval, tag, constraint, useful


class PayloadMetadata(univ.Sequence):
    pass


PayloadMetadata.componentType = namedtype.NamedTypes(
    namedtype.NamedType('installed-size', univ.Integer()),
    namedtype.NamedType('installed-digest', univ.OctetString()),
    namedtype.OptionalNamedType('precursor-digest', univ.OctetString())
)


class Manifest(univ.Sequence):
    pass


Manifest.componentType = namedtype.NamedTypes(
    namedtype.NamedType('vendor-id', univ.OctetString()),
    namedtype.NamedType('class-id', univ.OctetString()),
    namedtype.NamedType('update-priority', univ.Integer()),
    namedtype.NamedType('component-name', char.UTF8String()),
    namedtype.NamedType('payload-version', char.UTF8String()),
    namedtype.NamedType('payload-digest', univ.OctetString()),
    namedtype.NamedType('payload-size', univ.Integer()),
    namedtype.NamedType('payload-uri', char.UTF8String()),
    namedtype.NamedType('payload-format', univ.Enumerated(namedValues=namedval.NamedValues(('raw-binary', 1), ('arm-patch-stream', 5), ('combined', 6), ('encrypted-raw', 257), ('encrypted-combined', 262)))),
    namedtype.NamedType('installed-signature', univ.OctetString()),
    namedtype.OptionalNamedType('payload-metadata', PayloadMetadata()),
    namedtype.OptionalNamedType('vendor-data', univ.OctetString())
)


class SignedResource(univ.Sequence):
    pass


SignedResource.componentType = namedtype.NamedTypes(
    namedtype.NamedType('manifest-version', univ.Enumerated(namedValues=namedval.NamedValues(('v3', 3)))),
    namedtype.NamedType('manifest', Manifest()),
    namedtype.NamedType('signature', univ.OctetString())
)


