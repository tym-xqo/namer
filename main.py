#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

import wordlists

word_lists = {
    "namer": wordlists.namer,
    "encabulator": wordlists.encabulator,
}


def namer(request, input_list="namer"):

    if request:
        request_json = request.get_json(silent=True)
        request_args = request.args

        if request_json and "list" in request_json:
            list = request_json["list"]
        elif request_args and "list" in request_args:
            list = request_args["list"]
        else:
            list = input_list
    else:
        list = input_list

    if list not in word_lists.keys():
        list = "namer"

    source = word_lists[list]
    adj = random.choice(source["adjectives"])
    nom = random.choice(source["nouns"])

    digits = "".join(["%s" % random.randint(0, 9) for num in range(0, 2)])

    name = "-".join((adj, nom, digits))
    return name


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--list", "-l", action="store", default="namer")
    args = parser.parse_args()
    input_list = args.list
    name = namer(request=None, input_list=input_list)
    print(name)
