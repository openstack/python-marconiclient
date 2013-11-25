# Copyright (c) 2013 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from marconiclient.transport import api


class FakeApi(api.Api):
    schema = {
        'test_operation': {
            'ref': 'test/{name}',
            'method': 'GET',
            'properties': {
                'name': {'type': 'string'},
                'address': {'type': 'string'}
            },

            'additionalProperties': False,
            'required': ['name']
        }
    }