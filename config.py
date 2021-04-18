#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("13ec83fe-eafc-4c6d-af38-ebecc88d6dab", "")
    APP_PASSWORD = os.environ.get("~IDRY5x3Hn2b--l_bP9Lldk_6eS6PmI6P~", "")
