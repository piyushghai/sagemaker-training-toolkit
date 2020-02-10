# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License'). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the 'license' file accompanying this file. This file is
# distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from __future__ import absolute_import

import time

import pytest

import sagemaker_training
from sagemaker_training import _timeout


def test_timeout():
    sec = 2
    with pytest.raises(sagemaker_training._timeout.TimeoutError):
        with _timeout.timeout(seconds=sec):
            print("Waiting and testing timeout, it should happen in {} seconds.".format(sec))
            time.sleep(sec + 1)
