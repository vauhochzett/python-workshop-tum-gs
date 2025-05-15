#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pytest


def raise_exercise_not_yet_started():
    pytest.xfail('Exercise not yet started')
