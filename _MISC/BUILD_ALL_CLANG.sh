#!/bin/sh
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
# Created by Devyn Collier Johnson
# <DevynCJohnson@Gmail.com>

cd ..

gnome-terminal --hide-menubar --title=Build_Pybooster_Clang -e './_MISC/build_clang.sh'
exit 0