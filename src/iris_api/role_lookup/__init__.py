# Copyright (c) LinkedIn Corporation. All rights reserved. Licensed under the BSD-2 Clause license.
# See LICENSE in the project root for license information.

from iris_api.custom_import import import_custom_module


def get_role_lookup(config):
    return import_custom_module('iris_api.role_lookup', config['role_lookup'])(config)
